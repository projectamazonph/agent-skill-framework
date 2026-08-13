---
name: test-driven-development
description: "Drive one observable software behavior at a time through a valid Test-Driven Development cycle: select the test, prove Red for the intended reason, implement the smallest Green change, and preserve the test as regression evidence. Use before adding production behavior, fixing defects, changing contracts, or safely characterizing legacy behavior. Also use when tests are brittle, over-mocked, skipped, weakened, or passing without proving the requirement."
---

# Test-Driven Development

## Mission

Own behavioral proof. Move one requirement from absent or defective to verified without broadening scope.

Do not own project sequencing, architecture policy, or final completion. Return evidence to `engineering-orchestrator`, use `solid-design` for structural decisions, and let `loop-engineering` record and adjust the larger loop.

## Suite Protocol

When another skill routes work here, read [references/suite-contract.md](references/suite-contract.md). Accept the Task Packet and return the standard Handoff Packet. Mark `pass` only for one valid Red–Green–Refactor behavior cycle.

## Require an Entry Contract

Before changing production code, obtain or determine:

- One observable behavior or defect
- Acceptance example with inputs, outputs, state, side effects, and errors
- Relevant public contract
- Existing baseline result
- Smallest suitable test level

If the behavior cannot be stated clearly, return to the orchestrator for scope clarification.

## Run Red–Green–Refactor

### 1. Select

Choose one independently verifiable behavior. Keep structural cleanup and unrelated requirements out of this cycle.

Select the narrowest test that proves the real contract:

- Unit test for pure policy or calculation
- Shared contract test for all implementations of one abstraction
- Integration test for a database, API, filesystem, queue, or framework adapter
- Component test for a use case crossing several internal collaborators
- Acceptance or end-to-end test for a critical user-visible journey

Read [references/test-strategies.md](references/test-strategies.md) when test level, doubles, contract testing, or legacy seams are unclear.

### 2. Prove Red

1. Write or update the test before production behavior.
2. Run the smallest command that exercises it.
3. Confirm the test fails because the selected behavior is missing or defective.
4. Record the command, failing test, and relevant failure message.

Reject false Red states:

- Syntax, import, compilation, fixture, environment, or setup failure
- Failure in an unrelated test
- A test that never reaches the intended assertion
- A skipped, quarantined, or filtered-out test
- A failure caused solely by changing the test contract incorrectly

Repair the test harness and rerun until Red is valid.

### 3. Reach Green

1. Change the smallest amount of production code that satisfies the test.
2. Avoid speculative options, layers, and adjacent cleanup.
3. Run the focused test.
4. Confirm it passes without weakening assertions or bypassing execution.
5. Run immediately related tests when the behavior shares a contract or state.

Do not add production code before valid Red evidence except minimal compilation scaffolding that contains no behavior. Treat exploratory code as a disposable spike, not TDD evidence.

### 4. Refactor Safely

Improve names, local duplication, and cohesion only while the focused tests remain green. Invoke `solid-design` before extracting architectural boundaries, interfaces, strategies, adapters, or inheritance relationships.

Run the focused test after every structural step. Stop and reduce the step when behavior drifts.

### 5. Return Evidence

Return this handoff:

```text
Behavior: <observable requirement>
Test level: <unit | contract | integration | component | e2e>
Red: <command and intended failure>
Green: <minimal production change and passing command>
Refactor: <none or behavior-preserving cleanup>
Related checks: <results>
Remaining risk: <none or concrete gap>
```

Do not declare the whole task complete. Return control to the orchestrator and Loop Engineering.

## Handle Common Modes

### Defect

Reproduce the defect first at the lowest level that captures the real cause. Keep the reproducing test permanently unless stronger existing coverage makes it genuinely redundant.

### Legacy Code

1. Characterize current observable behavior, including relied-upon quirks.
2. Add the smallest seam needed to control a volatile dependency.
3. Move or change one behavior per cycle.
4. Add an explicit new test before intentionally changing a characterized quirk.

### Contract Change

Update or add consumer-facing contract tests first. Run them against every implementation. Treat compatibility breaks as intentional only when the user authorizes them.

### UI Behavior

Test stable user-observable behavior at the component or browser level. Avoid fragile selectors and snapshots that prove markup but not behavior. Perform visual inspection when layout matters, but keep automated assertions for interaction and state.

### External Integration

Use a boundary fake for domain tests and a focused integration test for the real adapter. Do not mock the vendor so deeply that the adapter contract becomes imaginary.

## Protect Test Quality

- Name the condition and expected behavior.
- Assert outputs, state transitions, emitted events, or required side effects.
- Keep one primary failure reason per test.
- Control time, randomness, IDs, concurrency, and shared state.
- Prefer real values and small fakes over deep mock graphs.
- Mock architectural boundaries, not every internal call.
- Do not test private methods or incidental call order unless part of the contract.
- Do not delete, skip, loosen, or rewrite a valid test merely to reach Green.

## Stop and Return When

- The requested behavior is ambiguous.
- Red cannot be made valid without a broader environment fix.
- Green requires several unrelated changes.
- A shared contract exposes an LSP or architecture defect.
- The baseline contains relevant failures that make new evidence unreliable.

Return the evidence and blocker to the orchestrator instead of manufacturing progress.
