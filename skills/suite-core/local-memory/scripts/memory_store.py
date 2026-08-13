#!/usr/bin/env python3
"""Lightweight durable memory store for local AI agents."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_DB = Path("~/.local/share/agent-skill-suite/memory.sqlite3").expanduser()
VALID_KINDS = {"preference", "fact", "decision", "procedure", "failure", "handoff"}
VALID_SENSITIVITY = {"public", "internal", "confidential", "restricted"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def db_path(value: str | None) -> Path:
    raw = value or os.getenv("AGENT_SKILL_MEMORY_DB")
    return Path(raw).expanduser() if raw else DEFAULT_DB


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db(conn: sqlite3.Connection) -> bool:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS memories (
            id TEXT PRIMARY KEY,
            scope TEXT NOT NULL,
            kind TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT NOT NULL DEFAULT '',
            source TEXT NOT NULL DEFAULT '',
            confidence REAL NOT NULL DEFAULT 1.0 CHECK(confidence >= 0 AND confidence <= 1),
            sensitivity TEXT NOT NULL DEFAULT 'internal',
            pinned INTEGER NOT NULL DEFAULT 0 CHECK(pinned IN (0, 1)),
            status TEXT NOT NULL DEFAULT 'active' CHECK(status IN ('active', 'forgotten')),
            content_hash TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            last_accessed_at TEXT,
            access_count INTEGER NOT NULL DEFAULT 0,
            UNIQUE(scope, content_hash)
        );
        CREATE INDEX IF NOT EXISTS idx_memories_scope_status ON memories(scope, status);
        CREATE INDEX IF NOT EXISTS idx_memories_kind_status ON memories(kind, status);
        CREATE INDEX IF NOT EXISTS idx_memories_updated ON memories(updated_at DESC);
        """
    )
    fts = True
    try:
        conn.execute(
            "CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts "
            "USING fts5(id UNINDEXED, content, tags, scope UNINDEXED, kind UNINDEXED, tokenize='unicode61')"
        )
    except sqlite3.OperationalError:
        fts = False
    conn.commit()
    return fts


def has_fts(conn: sqlite3.Connection) -> bool:
    row = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='memories_fts'"
    ).fetchone()
    return row is not None


def normalize(content: str) -> str:
    return " ".join(content.strip().split())


def content_hash(content: str) -> str:
    return hashlib.sha256(normalize(content).casefold().encode("utf-8")).hexdigest()


def tags_value(raw: str) -> str:
    tags = sorted({item.strip().casefold() for item in raw.split(",") if item.strip()})
    return ",".join(tags)


def row_dict(row: sqlite3.Row) -> dict[str, Any]:
    result = dict(row)
    result["pinned"] = bool(result["pinned"])
    result["tags"] = [item for item in result["tags"].split(",") if item]
    result.pop("content_hash", None)
    return result


def emit(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


def fts_upsert(conn: sqlite3.Connection, record: dict[str, Any]) -> None:
    if not has_fts(conn):
        return
    conn.execute("DELETE FROM memories_fts WHERE id = ?", (record["id"],))
    if record.get("status", "active") == "active":
        conn.execute(
            "INSERT INTO memories_fts(id, content, tags, scope, kind) VALUES (?, ?, ?, ?, ?)",
            (record["id"], record["content"], record["tags"], record["scope"], record["kind"]),
        )


def get_active(conn: sqlite3.Connection, memory_id: str) -> sqlite3.Row:
    row = conn.execute(
        "SELECT * FROM memories WHERE id = ? AND status = 'active'", (memory_id,)
    ).fetchone()
    if row is None:
        raise ValueError(f"Active memory not found: {memory_id}")
    return row


def cmd_init(args: argparse.Namespace) -> None:
    path = db_path(args.db)
    with connect(path) as conn:
        fts = init_db(conn)
    emit({"database": str(path), "fts5": fts, "status": "initialized"})


def cmd_add(args: argparse.Namespace) -> None:
    if args.kind not in VALID_KINDS:
        raise ValueError(f"Invalid kind: {args.kind}")
    if args.sensitivity not in VALID_SENSITIVITY:
        raise ValueError(f"Invalid sensitivity: {args.sensitivity}")
    content = normalize(args.content)
    if not content:
        raise ValueError("Content cannot be empty")
    if not 0 <= args.confidence <= 1:
        raise ValueError("Confidence must be between 0 and 1")
    path = db_path(args.db)
    with connect(path) as conn:
        init_db(conn)
        digest = content_hash(content)
        duplicate = conn.execute(
            "SELECT * FROM memories WHERE scope = ? AND content_hash = ? AND status = 'active'",
            (args.scope, digest),
        ).fetchone()
        if duplicate:
            emit({"duplicate": True, "memory": row_dict(duplicate)})
            return
        record = {
            "id": uuid.uuid4().hex,
            "scope": args.scope,
            "kind": args.kind,
            "content": content,
            "tags": tags_value(args.tags),
            "source": args.source,
            "confidence": args.confidence,
            "sensitivity": args.sensitivity,
            "pinned": int(args.pin),
            "status": "active",
            "content_hash": digest,
            "created_at": now(),
            "updated_at": now(),
            "last_accessed_at": None,
            "access_count": 0,
        }
        conn.execute(
            """INSERT INTO memories
            (id, scope, kind, content, tags, source, confidence, sensitivity, pinned, status,
             content_hash, created_at, updated_at, last_accessed_at, access_count)
            VALUES (:id, :scope, :kind, :content, :tags, :source, :confidence, :sensitivity,
                    :pinned, :status, :content_hash, :created_at, :updated_at, :last_accessed_at,
                    :access_count)""",
            record,
        )
        fts_upsert(conn, record)
        conn.commit()
        row = conn.execute("SELECT * FROM memories WHERE id = ?", (record["id"],)).fetchone()
    emit({"duplicate": False, "memory": row_dict(row)})


def make_fts_query(query: str) -> str:
    tokens = re.findall(r"[\w.-]+", query, flags=re.UNICODE)
    return " AND ".join(f'"{token.replace(chr(34), chr(34) * 2)}"' for token in tokens)


def cmd_search(args: argparse.Namespace) -> None:
    path = db_path(args.db)
    with connect(path) as conn:
        init_db(conn)
        params: list[Any] = []
        filters = ["m.status = 'active'"]
        if args.scope:
            filters.append("m.scope = ?")
            params.append(args.scope)
        if args.kind:
            filters.append("m.kind = ?")
            params.append(args.kind)
        fts_query = make_fts_query(args.query)
        if has_fts(conn) and fts_query:
            sql = (
                "SELECT m.* FROM memories_fts JOIN memories m ON m.id = memories_fts.id "
                "WHERE memories_fts MATCH ? AND " + " AND ".join(filters) +
                " ORDER BY m.pinned DESC, bm25(memories_fts), m.updated_at DESC LIMIT ?"
            )
            rows = conn.execute(sql, [fts_query, *params, args.limit]).fetchall()
            mode = "fts5"
        else:
            filters.append("(m.content LIKE ? OR m.tags LIKE ?)")
            like = f"%{args.query}%"
            sql = (
                "SELECT m.* FROM memories m WHERE " + " AND ".join(filters) +
                " ORDER BY m.pinned DESC, m.updated_at DESC LIMIT ?"
            )
            rows = conn.execute(sql, [*params, like, like, args.limit]).fetchall()
            mode = "like"
        if rows:
            ids = [row["id"] for row in rows]
            placeholders = ",".join("?" for _ in ids)
            conn.execute(
                f"UPDATE memories SET last_accessed_at = ?, access_count = access_count + 1 "
                f"WHERE id IN ({placeholders})",
                [now(), *ids],
            )
            conn.commit()
    emit({"count": len(rows), "mode": mode, "results": [row_dict(row) for row in rows]})


def cmd_get(args: argparse.Namespace) -> None:
    path = db_path(args.db)
    with connect(path) as conn:
        init_db(conn)
        row = get_active(conn, args.id)
        conn.execute(
            "UPDATE memories SET last_accessed_at = ?, access_count = access_count + 1 WHERE id = ?",
            (now(), args.id),
        )
        conn.commit()
    emit({"memory": row_dict(row)})


def cmd_update(args: argparse.Namespace) -> None:
    path = db_path(args.db)
    with connect(path) as conn:
        init_db(conn)
        current = dict(get_active(conn, args.id))
        updates: dict[str, Any] = {}
        if args.content is not None:
            content = normalize(args.content)
            if not content:
                raise ValueError("Content cannot be empty")
            updates["content"] = content
            updates["content_hash"] = content_hash(content)
        if args.tags is not None:
            updates["tags"] = tags_value(args.tags)
        if args.source is not None:
            updates["source"] = args.source
        if args.confidence is not None:
            if not 0 <= args.confidence <= 1:
                raise ValueError("Confidence must be between 0 and 1")
            updates["confidence"] = args.confidence
        if args.sensitivity is not None:
            if args.sensitivity not in VALID_SENSITIVITY:
                raise ValueError(f"Invalid sensitivity: {args.sensitivity}")
            updates["sensitivity"] = args.sensitivity
        if not updates:
            raise ValueError("No update fields supplied")
        updates["updated_at"] = now()
        assignments = ", ".join(f"{key} = ?" for key in updates)
        conn.execute(
            f"UPDATE memories SET {assignments} WHERE id = ?",
            [*updates.values(), args.id],
        )
        current.update(updates)
        fts_upsert(conn, current)
        conn.commit()
        row = conn.execute("SELECT * FROM memories WHERE id = ?", (args.id,)).fetchone()
    emit({"memory": row_dict(row), "updated": sorted(updates)})


def cmd_pin(args: argparse.Namespace) -> None:
    path = db_path(args.db)
    with connect(path) as conn:
        init_db(conn)
        get_active(conn, args.id)
        value = 0 if args.unpin else 1
        conn.execute(
            "UPDATE memories SET pinned = ?, updated_at = ? WHERE id = ?",
            (value, now(), args.id),
        )
        conn.commit()
        row = conn.execute("SELECT * FROM memories WHERE id = ?", (args.id,)).fetchone()
    emit({"memory": row_dict(row)})


def cmd_forget(args: argparse.Namespace) -> None:
    path = db_path(args.db)
    with connect(path) as conn:
        init_db(conn)
        current = dict(get_active(conn, args.id))
        conn.execute(
            "UPDATE memories SET status = 'forgotten', pinned = 0, updated_at = ? WHERE id = ?",
            (now(), args.id),
        )
        current["status"] = "forgotten"
        fts_upsert(conn, current)
        conn.commit()
    emit({"forgotten": args.id})


def cmd_status(args: argparse.Namespace) -> None:
    path = db_path(args.db)
    with connect(path) as conn:
        init_db(conn)
        fts_enabled = has_fts(conn)
        status_rows = conn.execute(
            "SELECT status, COUNT(*) AS count FROM memories GROUP BY status"
        ).fetchall()
        scope_rows = conn.execute(
            "SELECT scope, COUNT(*) AS count FROM memories WHERE status = 'active' "
            "GROUP BY scope ORDER BY count DESC, scope"
        ).fetchall()
        pinned = conn.execute(
            "SELECT COUNT(*) FROM memories WHERE status = 'active' AND pinned = 1"
        ).fetchone()[0]
    emit({
        "database": str(path),
        "fts5": fts_enabled,
        "pinned": pinned,
        "scopes": {row["scope"]: row["count"] for row in scope_rows},
        "statuses": {row["status"]: row["count"] for row in status_rows},
    })


def cmd_export(args: argparse.Namespace) -> None:
    path = db_path(args.db)
    output = Path(args.output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    with connect(path) as conn:
        init_db(conn)
        sql = "SELECT * FROM memories"
        if not args.include_forgotten:
            sql += " WHERE status = 'active'"
        sql += " ORDER BY created_at, id"
        rows = conn.execute(sql).fetchall()
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row_dict(row), ensure_ascii=False, sort_keys=True) + "\n")
    emit({"count": len(rows), "output": str(output)})


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument("--db", help="SQLite path; overrides AGENT_SKILL_MEMORY_DB")
    sub = root.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.set_defaults(func=cmd_init)

    add = sub.add_parser("add")
    add.add_argument("--scope", default="global")
    add.add_argument("--kind", default="fact", choices=sorted(VALID_KINDS))
    add.add_argument("--content", required=True)
    add.add_argument("--tags", default="")
    add.add_argument("--source", default="")
    add.add_argument("--confidence", type=float, default=1.0)
    add.add_argument("--sensitivity", default="internal", choices=sorted(VALID_SENSITIVITY))
    add.add_argument("--pin", action="store_true")
    add.set_defaults(func=cmd_add)

    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--scope")
    search.add_argument("--kind", choices=sorted(VALID_KINDS))
    search.add_argument("--limit", type=int, default=10)
    search.set_defaults(func=cmd_search)

    get = sub.add_parser("get")
    get.add_argument("id")
    get.set_defaults(func=cmd_get)

    update = sub.add_parser("update")
    update.add_argument("id")
    update.add_argument("--content")
    update.add_argument("--tags")
    update.add_argument("--source")
    update.add_argument("--confidence", type=float)
    update.add_argument("--sensitivity", choices=sorted(VALID_SENSITIVITY))
    update.set_defaults(func=cmd_update)

    pin = sub.add_parser("pin")
    pin.add_argument("id")
    pin.add_argument("--unpin", action="store_true")
    pin.set_defaults(func=cmd_pin)

    forget = sub.add_parser("forget")
    forget.add_argument("id")
    forget.set_defaults(func=cmd_forget)

    status = sub.add_parser("status")
    status.set_defaults(func=cmd_status)

    export = sub.add_parser("export")
    export.add_argument("--output", required=True)
    export.add_argument("--include-forgotten", action="store_true")
    export.set_defaults(func=cmd_export)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        args.func(args)
        return 0
    except (ValueError, sqlite3.Error, OSError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
