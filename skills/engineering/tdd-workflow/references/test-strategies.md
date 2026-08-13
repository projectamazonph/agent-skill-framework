# Test Strategies

## Selection Matrix

| Target | Test through | Avoid |
| --- | --- | --- |
| Domain policy | Public function or method with real values | Database, network, framework boot |
| Use-case coordinator | Public execute method with small boundary fakes | Mocking every internal method |
| Port implementation | Shared contract suite | Implementation-specific assertions in the contract |
| Database adapter | Real test database or faithful isolated environment | Mocking the ORM until no query runs |
| HTTP/API adapter | Recorded or sandbox contract where practical | Assuming vendor behavior from a hand-written mock alone |
| UI component | Accessible user interaction and visible state | Private state or brittle DOM structure |
| Critical journey | Stable end-to-end flow | Exhaustive edge cases only at the browser level |

## Test Double Rules

- Use a **stub** to supply controlled input from a boundary.
- Use a **fake** for a lightweight working implementation such as an in-memory store.
- Use a **spy** only when an interaction is itself observable contract behavior.
- Use a **mock** sparingly for strict boundary protocols.

Prefer state and output assertions. Excessive interaction assertions make refactoring expensive and may signal an overly broad collaborator contract.

## Shared Contract Tests

Run one behavioral suite against every implementation of an abstraction. Cover:

- Valid inputs and results
- Boundary values and nullability
- Error semantics
- State and side-effect guarantees
- Ordering, units, and idempotency when promised

If one implementation needs an exception to the shared suite, revisit Liskov substitution or split the contract.

## Legacy Seams

Introduce the smallest control point around:

- Time, randomness, or ID generation
- Network, filesystem, database, or queue access
- Global state or environment configuration
- Static framework entry points

Do not redesign the entire subsystem merely to insert the first seam. Characterize, isolate, then move one behavior at a time.

## Invalid Evidence

Do not accept:

- Snapshot changes approved without checking behavioral meaning
- Tests that pass before the requested behavior is implemented
- Tests filtered so the relevant case never runs
- Retries that hide deterministic defects
- Coverage percentage without assertions for the requirement
- A mocked adapter test as proof the real external contract works
