# Memory Policy

## Memory Kinds

| Kind | Example | Review rule |
| --- | --- | --- |
| preference | Preferred response or workflow style | Keep until explicitly changed |
| fact | Stable user or project fact | Verify when time-sensitive |
| decision | Chosen approach and rejected alternative | Preserve source and date |
| procedure | Repeatable successful workflow | Update when tools or commands change |
| failure | Failure signature, cause, and resolution | Keep only after cause is verified |
| handoff | Current task state and next action | Consolidate or expire after completion |

## Quality Test

Store a memory only when it is:

- Durable enough to matter later
- Specific enough to guide a decision
- Supported by an explicit source or verified outcome
- Scoped correctly
- Not already represented
- Safe to retain locally

## Confidence

- 1.0: explicit user statement or authoritative verified source
- 0.8–0.99: directly observed successful behavior
- 0.5–0.79: supported inference that must remain labeled
- Below 0.5: do not persist as durable memory

## Sensitivity

Use public, internal, confidential, or restricted. Never store credential values. For sensitive personal or client data, require explicit need and local protection appropriate to the environment.

## Consolidation

Periodically:

1. Merge duplicates.
2. Remove stale task handoffs.
3. Verify pinned rules.
4. Resolve conflicts.
5. Convert repeated failure entries into one procedure or known limitation.
6. Export a backup before destructive maintenance.
