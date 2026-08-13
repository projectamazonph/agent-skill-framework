---
name: local-memory
description: Maintain fast, durable, curated local memory for AI agents on Android, Termux, Linux, macOS, Windows, or other lightweight environments. Use when an agent must remember stable preferences, project facts, decisions, procedures, failure resolutions, and task state across sessions; retrieve relevant memories before planning; resolve conflicting or stale memories; or provide explicit remember, search, pin, update, forget, status, and export controls without a cloud dependency.
---

# Local Memory

## Mission

Make useful memory persist and reappear at the right moment without turning every conversation into permanent clutter. Use a lightweight SQLite store, explicit scopes, deterministic retrieval, and user-controlled curation.

## Suite Protocol

When another skill routes work here, read [references/suite-contract.md](references/suite-contract.md). Accept the Task Packet and return the standard Handoff Packet. Mark `pass` only after memory mutations are read back and retrieval or removal behaves as requested.

## Store Only Durable Memory

Capture:

- Stable user preferences and standing constraints
- Project identity, architecture, paths, commands, and state
- Explicit decisions and rejected alternatives
- Reusable procedures and successful workflows
- Failure signatures, root causes, and verified resolutions
- Commitments, owners, and durable task handoffs

Do not capture:

- Casual conversation and temporary moods
- Guesses presented as facts
- Duplicate paraphrases
- Raw secrets, passwords, API tokens, private keys, or sensitive credential values
- Short-lived details with no future decision value

Read [references/memory-policy.md](references/memory-policy.md) for retention, conflict, sensitivity, and consolidation rules.

## Use the Local Store

The bundled script uses only Python's standard library and SQLite:

```bash
python3 scripts/memory_store.py init
python3 scripts/memory_store.py add --scope project:amph --kind decision --content "Use PostgreSQL from day one" --tags architecture,database --source user
python3 scripts/memory_store.py search "database architecture" --scope project:amph --limit 8
python3 scripts/memory_store.py get <memory-id>
python3 scripts/memory_store.py update <memory-id> --content "Updated durable fact"
python3 scripts/memory_store.py pin <memory-id>
python3 scripts/memory_store.py forget <memory-id>
python3 scripts/memory_store.py status
python3 scripts/memory_store.py export --output memory-backup.jsonl
```

Set `AGENT_SKILL_MEMORY_DB` to override the default database at `~/.local/share/agent-skill-suite/memory.sqlite3`.

The store enables WAL mode, busy timeout, scoped deduplication, full-text search when FTS5 is available, and a safe LIKE fallback.

## Retrieve Before Planning

At task intake:

1. Form a short query from the user outcome, project, named artifacts, and constraints.
2. Search global memory and the relevant project scope.
3. Prefer pinned, explicit, recent, and frequently useful memories.
4. Load only the smallest useful set, normally 5–10 records.
5. Separate durable fact from previous inference.
6. Check current source files when the fact may have changed.

Do not let memory override an explicit current user instruction or authoritative current source.

## Curate After Work

After a verified outcome:

1. Propose only new durable memories.
2. Search for duplicates and conflicts.
3. Update or supersede stale records instead of adding paraphrases.
4. Record source, scope, kind, confidence, tags, and sensitivity.
5. Pin only high-value standing rules or canonical project facts.
6. Keep failures only when their cause and resolution are reusable.

## Use Scopes

- `global`: stable preferences and universal rules
- `project:<name>`: architecture, paths, commands, decisions, and state
- `workflow:<name>`: reusable procedures
- `task:<id>`: temporary handoff state that should later be consolidated or forgotten
- `agent:<name>`: agent-specific operating knowledge

Prefer the narrowest scope that still allows reliable retrieval.

## Integrate with an Agent

Read [references/agent-hooks.md](references/agent-hooks.md) for pre-plan retrieval, post-run curation, failure-memory, and user-control hooks.

Keep memory proposals separate from automatic writes when sensitivity is high, the fact is inferred, or the user has not authorized persistent storage.

## Resolve Conflicts

Use this precedence:

1. Explicit current user instruction
2. Authoritative current project source
3. Newer explicit durable memory
4. Older memory and inference

Mark superseded records forgotten or update them with a source note. Never silently keep two active memories that prescribe incompatible behavior.

## Verify Memory Operations

After writes, search or read back the affected record. After forget, confirm it no longer appears in active search. After export, confirm the file exists and each line parses as JSON.

Report memory actions concisely: records added, updated, pinned, forgotten, retrieved, and any unresolved conflict.
