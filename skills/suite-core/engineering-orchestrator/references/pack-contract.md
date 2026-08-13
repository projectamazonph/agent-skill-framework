# Engineering Standards Pack Contract

## Responsibility Map

| Skill | Owns | Must not own |
| --- | --- | --- |
| engineering-orchestrator | Classification, sequencing, state, routing, enforcement | Detailed design, test mechanics, loop diagnosis, self-approval |
| solid-design | Change axes, contracts, boundaries, SOLID decisions | Project sequencing, test-first mechanics, completion approval |
| test-driven-development | One behavior's Red–Green–Refactor proof | Broad architecture, multi-loop planning, final approval |
| loop-engineering | Iteration size, hypotheses, observations, ledger, adjustment | Test policy details, architecture rules, final approval |
| quality-gates | Independent completion evidence and PASS/BLOCKED decision | Implementing remediation or weakening gates |

## Canonical Sequence

```text
Intake
  -> Loop opened
  -> SOLID shape when a boundary is involved
  -> TDD Red
  -> TDD Green
  -> SOLID-aware refactor
  -> Loop observe and adjust
  -> repeat as needed
  -> Quality gate
  -> PASS or route back
```

## Cross-Skill Invariants

1. Change no production behavior before valid Red evidence.
2. Preserve behavior during structural refactoring.
3. Add no abstraction without a named change axis, client contract, or infrastructure seam.
4. Keep one independently verifiable outcome per loop.
5. Record actual evidence; never infer a pass from code inspection.
6. Preserve unrelated changes and user scope.
7. Complete only after the quality gate returns PASS.

## Routing Matrix

| Signal | Primary skill | Secondary skill |
| --- | --- | --- |
| New behavior | test-driven-development | loop-engineering |
| Defect | test-driven-development | loop-engineering |
| New module/interface/adapter | solid-design | test-driven-development |
| Behavior-preserving refactor | solid-design | test-driven-development for characterization |
| Repeated failed attempt | loop-engineering | test-driven-development or solid-design based on cause |
| Test needs many irrelevant mocks | solid-design | test-driven-development |
| Migration batch | loop-engineering | solid-design and quality gates |
| Completion claim | quality-gates | route by finding |

## Handoff Rules

- Pass evidence and decisions, not entire noisy transcripts.
- Preserve exact commands and meaningful results.
- Mark unknown information as unknown.
- Return to the orchestrator after each specialist completes its single job.
- Route a failed gate to the responsible skill, then rerun every affected gate.

## Exceptions

- Skip TDD for read-only reviews, pure explanations, and non-executable prose edits.
- Use characterization tests instead of new-behavior Red for behavior-preserving legacy refactors.
- Treat exploratory spikes as disposable learning; they cannot pass completion gates until converted into tested production work.
- When required checks cannot run, remain BLOCKED if the missing evidence is material to risk.
