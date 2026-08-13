---
name: engineering-standards-orchestrator
description: Coordinate programming work through mandatory SOLID architecture, test-driven development, Loop Engineering, and completion-quality gates. Use for any task that designs, creates, modifies, fixes, refactors, migrates, reviews, or verifies source code, tests, schemas, configuration, build logic, CI workflows, APIs, or software architecture. Also use for coding plans that will guide later implementation. Route focused work to the installed solid-code-design, tdd-workflow, loop-engineering, and engineering-quality-gates skills at the required moments.
---

# Engineering Standards Orchestrator

## Mission

Keep engineering standards active from intake through completion. Own sequencing, routing, state, and enforcement. Do not duplicate the specialists' detailed methods.

Treat “done” as a verified state, not a confident sentence.

## Coordinate the Pack

Apply each specialist only at its responsibility boundary:

| Skill | Invoke at | Required return |
| --- | --- | --- |
| `loop-engineering` | Start of every non-trivial implementation, fix, refactor, or migration; keep active throughout | Current loop, evidence, outcome, and next action |
| `solid-code-design` | Before adding or changing architectural boundaries; during design review; when test friction exposes coupling | Change map, boundary decision, contracts, dependency direction, and architecture risks |
| `tdd-workflow` | Before changing production behavior or fixing a defect | Valid Red evidence, minimal Green change, and focused test result |
| `engineering-quality-gates` | After the requested behavior is complete and before reporting completion | PASS or BLOCKED with evidence and remediation route |

Read [references/pack-contract.md](references/pack-contract.md) when a task spans several modes, a specialist handoff is ambiguous, or a gate fails.

## Maintain the Control Card

Maintain this compact state internally or in the repository's existing engineering log. Surface it only when useful to the user.

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

Update the card at every phase transition. Never carry a guessed or stale status forward.

## Run the State Machine

### 1. Intake

1. Read repository instructions and user constraints.
2. Classify the mode and risk.
3. Inspect the working tree before planning edits; preserve unrelated changes.
4. Define the requested outcome, observable acceptance behavior, and out-of-scope work.
5. Start `loop-engineering` for non-trivial work.

### 2. Establish the Baseline

1. Inspect relevant code, callers, tests, interfaces, and dependency edges.
2. Run the smallest relevant existing checks.
3. Record pre-existing failures separately from failures introduced by the task.
4. Stop and report when the baseline cannot be established and proceeding would risk destructive or misleading work.

### 3. Shape the Change

Invoke `solid-code-design` when any of these conditions apply:

- Add a class, module, service, interface, adapter, repository, strategy, plugin, or inheritance relationship.
- Move responsibilities or invert a dependency.
- Change a public contract, schema, API boundary, or cross-module data flow.
- Introduce another implementation or variation point.
- Encounter a test that requires excessive setup, irrelevant mocks, real infrastructure, or subtype exceptions.

Skip a new abstraction when the change is local, cohesive, and has no credible variation or infrastructure boundary. Record “no new boundary needed” as a valid architecture decision.

### 4. Drive Behavior Test-First

Invoke `tdd-workflow` before the first production-code change for every behavior addition or defect repair.

Require this order:

1. Select one observable behavior.
2. Prove a valid Red state for the intended reason.
3. Make the smallest Green change.
4. Refactor only while tests remain green.

Do not accept a syntax error, broken fixture, unrelated failure, skipped test, or weakened assertion as Red or Green evidence.

For a behavior-preserving refactor, require characterization or contract tests before moving structure. For a pure review, do not mutate files and do not manufacture a TDD cycle.

### 5. Continue Tight Loops

Return control to `loop-engineering` after each Green state or structural move.

Require the loop to:

1. Observe focused and proportionate broader evidence.
2. Compare the result with the hypothesis and acceptance behavior.
3. Record the outcome.
4. Choose the next smallest behavior, structural move, or diagnostic action.

Split any loop that contains several independently verifiable outcomes. Diagnose unexpected failures before adding more changes.

### 6. Enforce Completion

Invoke `engineering-quality-gates` only after all requested acceptance behavior appears complete.

Do not report completion unless the gate returns PASS. Route BLOCKED findings back to the appropriate phase:

| Finding | Return to |
| --- | --- |
| Missing or invalid behavior proof | `tdd-workflow` at Red |
| Coupled or unjustified design | `solid-code-design` at Shape |
| Regression, build, lint, type, or runtime failure | `loop-engineering` at Observe/Adjust |
| Scope drift or unrelated diff | Intake/Shape |
| Missing required migration, security, or rollback evidence | Baseline/Shape |

Re-run the gate after remediation. Never self-approve an unresolved required finding.

## Adapt by Task Mode

### Design or Planning Only

Use `solid-code-design` to define change axes, contracts, dependency direction, and test seams. Use the quality gate to check that the plan contains acceptance criteria and verification strategy. Do not pretend tests were run.

### Build or Feature

Run the full sequence: Loop → SOLID when needed → TDD per behavior → Loop observation → quality gate.

### Defect Fix

Reproduce first with `tdd-workflow`. Keep the regression test. Use `solid-code-design` only if the root cause is structural or the fix adds a boundary.

### Behavior-Preserving Refactor

Characterize behavior first. Use `solid-code-design` to choose one structural move per loop. Do not mix unrelated feature work into the refactor.

### Migration or Bulk Change

Define invariants, rollback or compatibility needs, and a representative test slice. Execute in batches through `loop-engineering`; gate each risky batch and the completed migration.

### Read-Only Review

Inspect through `solid-code-design`, then use `engineering-quality-gates` in review mode. Report findings first. Do not edit, send, publish, or open changes unless authorized.

### Exploratory Spike

Isolate and label the spike. Use it to learn, not as completion evidence. Before shipping, convert the learned behavior into normal TDD loops and pass all gates.

## Protect Integrity

- Follow user requirements and repository instructions; apply the pack where they do not conflict.
- Preserve unrelated work and existing behavior unless change is authorized.
- Never skip a specialist because its result may be inconvenient.
- Never claim a check ran when it did not run.
- Never replace required evidence with code inspection alone.
- Never create abstractions solely to score well against SOLID terminology.
- Never weaken tests or gates to reach completion.
- State unavailable tools, blocked checks, and residual uncertainty plainly.

## Report the Outcome

Lead with the verified result. Include:

- What changed or what was found
- Acceptance behavior satisfied
- Important architecture decision
- Tests and checks run with outcomes
- Gate result
- Remaining limitation or next step, if any

Keep the loop ledger concise unless the user requests full engineering logs.
