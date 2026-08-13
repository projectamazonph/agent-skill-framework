---
name: tdd-workflow
description: Drive one observable software behavior at a time through a valid Test-Driven Development cycle (Red, Green, Refactor). Use before adding production behavior, fixing defects, changing contracts, or safely characterizing legacy behavior.
---

# TDD Workflow

Own behavioral proof. Move one requirement from absent/defective to verified without broadening
scope. Read the full method in `tdd-workflow/SKILL.md`.

## Your job

- Require an entry contract: one observable behavior, an acceptance example (inputs/outputs/state/
  side effects/errors), the relevant public contract, the existing baseline, and the smallest test
  level.
- Run **Red → Green → Refactor**:
  1. **Select** one independently verifiable behavior; write the narrowest test that proves the real contract.
  2. **Prove Red** — the test fails *because the behavior is missing/defective*, not from syntax, setup, an unrelated test, or a skip.
  3. **Reach Green** — the smallest production change; no speculative options or adjacent cleanup.
  4. **Refactor safely** — only while focused tests stay green; invoke `solid-code-design` before extracting boundaries.

## Always

- Do not own project sequencing, architecture policy, or final approval.
- Never delete, skip, loosen, or rewrite a valid test merely to reach Green.
- Return a handoff (behavior, test level, Red, Green, refactor, related checks, remaining risk) and
  route back to the orchestrator and `loop-engineering`.

See `tdd-workflow/references/test-strategies.md` for the selection matrix and test-double rules.
