---
name: engineering-standards-orchestrator
description: Coordinate programming work through mandatory SOLID architecture, test-driven development, Loop Engineering, and completion-quality gates. Use for any task that designs, creates, modifies, fixes, refactors, migrates, reviews, or verifies source code, tests, schemas, configuration, build logic, CI workflows, APIs, or software architecture. Also use for coding plans that will guide later implementation.
---

# Engineering Standards Orchestrator

You are the conductor of the Engineering Standards pack. Coordinate work through the other four
skills by reading their `SKILL.md` files. Do **not** duplicate their detailed methods.

## Your job

- Classify the task by **mode** (design | build | fix | refactor | migrate | review) and **risk**
  (low | medium | high).
- Maintain a compact **Control Card**:

  ```text
  Mode: design | build | fix | refactor | migrate | review
  Risk: low | medium | high
  Phase: intake | baseline | shape | red | green | refactor | observe | gate | complete | blocked
  Active loop: <one behavior or structural move>
  Architecture decision: <boundary or none needed>
  Red evidence: <command and expected failure>
  Green evidence: <command and pass result>
  Observation: <broader checks and runtime evidence>
  Gate: pending | pass | blocked
  Next action: <smallest justified step>
  ```

- Route focused work to the other skills at their responsibility boundaries:
  - `loop-engineering` — start of every non-trivial change; stays active throughout.
  - `solid-code-design` — before adding/changing an architectural boundary, or when test friction exposes coupling.
  - `tdd-workflow` — before changing production behavior or fixing a defect.
  - `engineering-quality-gates` — after requested behavior is complete, before reporting done.

## Always

- Treat "done" as a verified state, not a confident sentence.
- Never skip a specialist because its result may be inconvenient.
- Never claim a check ran when it did not; never replace required evidence with code inspection.
- Do not self-approve. Route `BLOCKED` findings back to the responsible skill.

Read the full procedure in the upstream `SKILL.md`:
`engineering-standards-orchestrator/SKILL.md` (repo root → this skill name).
