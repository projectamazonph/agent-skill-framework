# Engineering Standards

This repository is an **agent-agnostic** engineering-standards skill pack. The canonical procedure
lives in the five `SKILL.md` files at the repo root. This project is governed by them.

## How to use

When a coding task arrives, coordinate through the five subagents (defined in `.claude/agents/`):

1. **engineering-standards-orchestrator** — classifies mode/risk, keeps the Control Card, and routes
   work to the specialists.
2. **solid-code-design** — shapes proportionate SOLID boundaries and stable contracts.
3. **tdd-workflow** — proves one behavior at a time via valid Red → Green → Refactor.
4. **loop-engineering** — runs small, observable, reversible build-test-adjust loops.
5. **engineering-quality-gates** — independently returns `PASS` or `BLOCKED`.

## Invariants (non-negotiable)

1. No production behavior changes before valid Red evidence.
2. Behavior is preserved during structural refactoring.
3. No abstraction without a named change axis, client contract, or infrastructure seam.
4. One independently verifiable outcome per loop.
5. Record actual evidence — never infer a pass from code inspection.
6. Unrelated changes and user scope are preserved.
7. Work completes only after the quality gate returns `PASS`.

## Install

Copy `.claude/agents/*.md` into your project's `.claude/agents/` (or user-level equivalent). The
subagents read the `SKILL.md` files directly from this repo, so keep the directory structure intact
or adjust the relative paths noted in each agent file.

Other runtimes: see `../openai/` (OpenAI agents) and `../cursor/` (Cursor rules + agents).
