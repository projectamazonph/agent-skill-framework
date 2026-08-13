---
name: "loop-engineering-v2"
description: Execute non-trivial software work through small, observable build-test-observe-adjust loops with explicit hypotheses, evidence, outcomes, and next actions. Use throughout feature implementation, debugging, refactoring, migrations, performance work, and complex verification where feedback must guide each subsequent step. Use when work is stalling, changes are growing too large, failures repeat, or an engineering ledger is required.
---

# Loop Engineering

## Mission

Own execution cadence and learning. Keep each loop small, observable, reversible with precise edits, and driven by evidence.

Do not own detailed test method, architecture policy, or final approval. Route behavior changes to `tdd-workflow`, structural decisions to `solid-code-design`, and completion to `engineering-quality-gates` through the orchestrator.

## Open a Loop

Define:

```text
Loop: <number or short ID>
Hypothesis: <what this step should prove or change>
Scope: <one behavior, diagnostic, or structural move>
Evidence plan: <test, inspection, metric, build, or runtime signal>
Stop condition: <observable success, failure, or split threshold>
```

Reject a loop that contains several independently verifiable outcomes. Split by behavior, dependency, caller group, migration batch, or risk.

## Run the Cycle

### 1. Observe

Inspect current code, tests, logs, runtime behavior, metrics, or errors. Separate known baseline failures from new failures. Never begin from an assumed state.

### 2. Frame

Choose the smallest uncertainty or behavior that blocks progress. State a falsifiable hypothesis and the evidence needed to decide.

### 3. Execute

- For new behavior or a defect, invoke `tdd-workflow` and complete one valid Red–Green–Refactor cycle.
- For a structural move, obtain a boundary decision from `solid-code-design`, preserve behavior with tests, and move one responsibility, dependency, contract, or caller group.
- For diagnosis, change one variable or add one observation point. Do not mix diagnosis with a broad fix.
- For bulk work, run one representative or low-risk batch before scaling.

### 4. Measure

Run the focused evidence check, then proportionate broader checks. Capture actual output, not memory or expectation.

### 5. Compare

Classify the loop:

- **Confirmed:** Evidence matches the hypothesis and acceptance behavior.
- **Refuted:** Evidence disproves the hypothesis.
- **Inconclusive:** The observation cannot distinguish causes.
- **Blocked:** A missing dependency, permission, decision, or broken baseline prevents a valid result.

### 6. Adjust

Choose exactly one next action:

- Advance to the next behavior or structural move.
- Tighten the test or observation.
- Reduce the scope.
- Return to architecture shaping.
- Repair the baseline or environment.
- Escalate a material user decision.
- Stop because acceptance is satisfied or the work is blocked.

Do not stack speculative fixes after a refuted or inconclusive loop.

## Keep the Ledger

Use an existing build log, engineering diary, task record, or project journal. If none exists, retain a concise ledger for the final report:

| Loop | Hypothesis | Action | Evidence | Outcome | Next |
| --- | --- | --- | --- | --- | --- |

Record exact commands and meaningful results. Do not dump noisy logs when a precise summary and failure excerpt are sufficient.

For long-running work, send the user brief progress updates at meaningful loop boundaries without turning the ledger into play-by-play commentary.

## Control Loop Size

Split the loop when:

- More than one acceptance behavior is changing.
- Several production modules must change for unrelated reasons.
- A test failure has more than one plausible cause.
- Review becomes difficult because the diff mixes behavior and structure.
- A migration batch cannot be independently verified or rolled back.
- The success condition cannot be stated in one sentence.

One loop may touch multiple files when they form one atomic behavior or contract change. File count alone does not define loop size.

## Recover from Failure

Read [references/loop-recovery.md](references/loop-recovery.md) when loops repeat, focused checks pass but broader checks fail, the environment is unreliable, or the next action is unclear.

Use precise patches to remove only the failed experiment's changes. Preserve unrelated user work. Never use destructive resets as a loop shortcut.

## Stop Correctly

Stop iteration when one condition holds:

- Requested acceptance behavior is satisfied and evidence is ready for `engineering-quality-gates`.
- A material decision or new authority is required from the user.
- The environment cannot produce trustworthy evidence.
- Continuing would expand scope beyond the request.

Do not stop merely because the first plausible implementation compiles or one focused test passes.

## Return the Handoff

Return to the orchestrator:

```text
Completed loops: <IDs and outcomes>
Acceptance status: <satisfied | partial | blocked>
Focused evidence: <results>
Broader observation: <results>
Architecture questions: <none or route to SOLID>
Residual risk: <specific gap>
Recommended next phase: <shape | red | observe | gate | blocked>
```
