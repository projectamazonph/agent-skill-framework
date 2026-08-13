# Agent Skill Suite

Use this file as the platform-neutral entrypoint for repository agents.

## Start Here

1. Read `skills/suite-orchestrator/SKILL.md` for multi-stage, ambiguous, or cross-domain work.
2. Select skills by their `name` and `description` frontmatter.
3. Load only the selected skill body and references required by the task.
4. Preserve the Task Packet and Handoff Packet defined in `skills/suite-orchestrator/references/suite-contract.md`.
5. Use `bundle.yaml` as the canonical inventory and installation order.

## Global Rules

- Preserve user scope, existing content, formatting, and unrelated work.
- Use no placeholders in completed outputs.
- Distinguish facts, inferences, decisions, and missing evidence.
- Do not claim a command, test, render, review, or write succeeded unless it ran and produced trustworthy evidence.
- Keep platform-specific invocation syntax and tool configuration outside portable `SKILL.md` instructions.
- Never weaken a test, gate, permission, or acceptance criterion to manufacture completion.
- Stop and return `blocked` when required authority or evidence is unavailable.

## Primary Routes

| Task | Skill |
| --- | --- |
| Multi-stage or unclear | `suite-orchestrator` |
| Agent workspace, state, commands, permissions, recovery | `agent-control-plane` |
| Conversation or notes to execution package | `conversation-compiler` |
| Software implementation, fix, refactor, migration, review | `engineering-orchestrator` |
| Adversarial expert review | `implementation-council` |
| Documents, PDFs, decks, spreadsheets, dashboards, SOPs | `artifact-production` |
| Durable local memory | `local-memory` |

The Engineering Orchestrator owns the internal sequence across `solid-design`, `test-driven-development`, `loop-engineering`, and `quality-gates`.

## Completion

Only the skill designated as completion owner may mark the overall task complete. A specialist `pass` means its responsibility passed, not that the whole task is finished.
