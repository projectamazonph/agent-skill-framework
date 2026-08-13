#!/usr/bin/env python3
"""Validate the portable Agent Skill Suite without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
RESOURCE_PATTERN = re.compile(r"(?:references|scripts|assets)/[A-Za-z0-9._/-]+")
TODO_PATTERN = re.compile(r"\[TODO|TODO:|Structuring This Skill")


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening YAML delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing closing YAML delimiter") from exc
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = unquote(value)
    return values


def parse_install_order(path: Path) -> list[str]:
    result: list[str] = []
    active = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line == "install_order:":
            active = True
            continue
        if active and line and not line.startswith("  "):
            break
        if active:
            match = re.match(r'^  - ["\']?([^"\']+)["\']?$', line)
            if match:
                result.append(match.group(1))
    return result


def validate_skill(skill_dir: Path, contract: bytes) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill_dir.name}: missing SKILL.md"]
    try:
        metadata = parse_frontmatter(skill_md)
    except ValueError as exc:
        return [f"{skill_dir.name}: {exc}"]
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name is {name!r}")
    if not NAME_PATTERN.fullmatch(name):
        errors.append(f"{skill_dir.name}: invalid name")
    if not description or len(description) > 1024:
        errors.append(f"{skill_dir.name}: description must contain 1-1024 characters")
    text = skill_md.read_text(encoding="utf-8")
    if len(text.splitlines()) >= 500:
        errors.append(f"{skill_dir.name}: SKILL.md must stay under 500 lines")
    if TODO_PATTERN.search(text):
        errors.append(f"{skill_dir.name}: unresolved template marker")
    for reference in RESOURCE_PATTERN.findall(text):
        if not (skill_dir / reference).exists():
            errors.append(f"{skill_dir.name}: missing referenced resource {reference}")
    contract_path = skill_dir / "references" / "suite-contract.md"
    if not contract_path.is_file() or contract_path.read_bytes() != contract:
        errors.append(f"{skill_dir.name}: suite contract is missing or inconsistent")
    openai = skill_dir / "agents" / "openai.yaml"
    if openai.is_file() and f"${name}" not in openai.read_text(encoding="utf-8"):
        errors.append(f"{skill_dir.name}: OpenAI adapter default prompt does not name ${name}")
    return errors


def run_memory_lifecycle(root: Path) -> list[str]:
    script = root / "skills" / "local-memory" / "scripts" / "memory_store.py"
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="agent-skill-memory-") as temp:
        temp_path = Path(temp)
        db = temp_path / "memory.sqlite3"

        def run(*args: str) -> dict:
            command = [sys.executable, "-B", str(script), "--db", str(db), *args]
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return json.loads(result.stdout)

        try:
            run("init")
            added = run(
                "add", "--scope", "project:validation", "--kind", "decision",
                "--content", "Use evidence before completion", "--tags", "quality,evidence"
            )
            memory_id = added["memory"]["id"]
            duplicate = run(
                "add", "--scope", "project:validation", "--kind", "decision",
                "--content", "Use evidence before completion"
            )
            if not duplicate.get("duplicate"):
                errors.append("local-memory: duplicate detection failed")
            search = run("search", "evidence completion", "--scope", "project:validation")
            if search.get("count") != 1:
                errors.append("local-memory: search failed")
            run("update", memory_id, "--content", "Use verified evidence before completion")
            export_path = temp_path / "export.jsonl"
            run("export", "--output", str(export_path))
            rows = [json.loads(line) for line in export_path.read_text(encoding="utf-8").splitlines()]
            if len(rows) != 1:
                errors.append("local-memory: export failed")
            run("forget", memory_id)
            after = run("search", "verified evidence", "--scope", "project:validation")
            if after.get("count") != 0:
                errors.append("local-memory: forget verification failed")
        except (subprocess.CalledProcessError, KeyError, json.JSONDecodeError, OSError) as exc:
            errors.append(f"local-memory: lifecycle error: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deep", action="store_true", help="run executable lifecycle checks")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    skills_dir = root / "skills"
    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    contract = (skills_dir / "suite-orchestrator" / "references" / "suite-contract.md").read_bytes()
    errors: list[str] = []

    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir, contract))

    installed = parse_install_order(root / "bundle.yaml")
    names = [path.name for path in skill_dirs]
    if sorted(installed) != sorted(names):
        errors.append("bundle.yaml install_order does not match skills directory")
    if installed[-1:] != ["suite-orchestrator"]:
        errors.append("suite-orchestrator must be installed last")

    try:
        json.loads((root / "schemas" / "handoff.schema.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"handoff schema is invalid: {exc}")

    if args.deep:
        errors.extend(run_memory_lifecycle(root))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    mode = "deep" if args.deep else "structural"
    print(f"PASS: {len(skill_dirs)} skills validated ({mode}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
