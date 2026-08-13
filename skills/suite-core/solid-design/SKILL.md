---
name: solid-design
description: Design, refactor, and review object-oriented or modular code with the SOLID principles while preserving behavior and avoiding needless abstraction. Use when defining responsibilities, extension seams, subtype contracts, consumer interfaces, dependency direction, modules, services, strategies, plugins, adapters, repositories, or architecture boundaries; also use when test friction, tangled dependencies, large classes, unsupported methods, framework leakage, or repeated variant branches signal a structural problem.
---

# SOLID Design

## Mission

Own architecture boundaries and contracts. Create the smallest design that separates real reasons to change and keeps stable policy insulated from volatile details.

Do not own test-first mechanics, loop sequencing, or final approval. Receive behavior and test evidence from the orchestrator, return an architecture decision, and preserve behavior while structure changes.

Treat SOLID as five decision constraints, not a quota for layers, classes, or interfaces.

## Suite Protocol

When another skill routes work here, read [references/suite-contract.md](references/suite-contract.md). Accept the Task Packet and return the standard Handoff Packet. Mark `pass` only for the boundary decision and required proof; do not claim implementation completion.

## Establish the Change Map

Inspect relevant callers, tests, public contracts, data flow, side effects, and dependencies. Record:

| Change axis | Owner | Stable contract | Volatile detail | Proof needed |
| --- | --- | --- | --- | --- |

Create or retain a boundary only when at least one is true:

- Different actors or policies cause independent changes.
- Multiple implementations exist or are explicitly required.
- An external system, time, randomness, filesystem, database, queue, or network must be isolated.
- Consumers need meaningfully different capabilities.
- A subtype contract must hold across implementations.
- Tests require control of a volatile dependency.

Record “no new boundary needed” when the code is local, cohesive, stable, and simpler without abstraction.

## Apply the Principles

### S: Single Responsibility

Give a class or module one cohesive responsibility and one primary reason to change.

1. Describe its job in one sentence without joining unrelated actions with “and.”
2. Group behavior that changes for the same actor and policy.
3. Separate orchestration, domain decisions, persistence, transport, formatting, and side effects when they change independently.
4. Keep closely related data and behavior together; do not split by method count alone.
5. Preserve a coordinator when its single job is executing one use case through focused collaborators.

A large cohesive module can satisfy SRP. A tiny utility that mixes policy and I/O can violate it.

### O: Open/Closed

Keep stable policy closed to repeated edits while allowing a known variation point to accept new behavior.

1. Name the dimension that varies.
2. Define the smallest stable contract around it.
3. Extend with composition, strategy, handler, policy object, plugin, registry, or data-driven rule as the language permits.
4. Keep registration and construction outside stable decision logic when possible.
5. Prove the seam by adding a variant without editing the stable core.

Do not create an extension framework for hypothetical variation. An exhaustive match over a truly closed domain can be better than polymorphism.

### L: Liskov Substitution

Ensure every implementation can replace its declared base type for every valid caller.

- Do not strengthen preconditions.
- Do not weaken postconditions.
- Preserve invariants, units, ordering, nullability, errors, state, and promised side effects.
- Do not add unsupported operations, silent no-ops, or new failures for valid base inputs.
- Preserve material resource or performance guarantees when part of the contract.

Require one shared contract suite across implementations. Replace inheritance with composition or narrower contracts when the relationship is not a true behavioral subtype.

### I: Interface Segregation

Make clients depend only on capabilities they use.

1. Define contracts from the consumer's perspective.
2. Split broad interfaces by cohesive capability such as read, write, publish, administer, or transact.
3. Compose small contracts only for consumers that need several capabilities.
4. Remove methods implemented with “not supported,” irrelevant defaults, or no-ops.
5. Prefer protocols, traits, structural types, function types, or narrow parameter shapes when idiomatic.

Do not fragment cohesive behavior into ceremonial one-method interfaces without a client boundary.

### D: Dependency Inversion

Make high-level policy depend on stable abstractions and volatile details implement them.

1. Let the policy-owning layer define the port it needs.
2. Place databases, APIs, frameworks, queues, clocks, randomness, and filesystems behind boundary adapters.
3. Inject dependencies explicitly through constructors, parameters, or a composition root.
4. Keep dependency direction pointing toward policy.
5. Keep construction and vendor configuration outside business logic.

Avoid service locators, hidden globals, framework objects in the domain, and pass-through wrappers that isolate no meaningful volatility.

## Refactor One Boundary at a Time

Require characterization or contract tests before moving structure. Then:

1. Move one responsibility, dependency, contract, or caller group.
2. Keep compatibility adapters when callers cannot migrate atomically.
3. Run focused tests after each structural step.
4. Remove old paths only when callers and tests prove them unused.
5. Return unexpected behavior changes to `test-driven-development` rather than hiding them inside the refactor.

## Control Overengineering

Before keeping an abstraction, answer:

1. What concrete change does it isolate?
2. Which actor, client, policy, or external detail owns that change?
3. What behavioral contract can tests prove?
4. Does it remove coupling or merely relocate it?
5. Is direct code or composition simpler?

Collapse the abstraction when these questions have no concrete answer. Tests do not justify an interface that merely mirrors one implementation without a useful seam.

## Verify the Architecture

- Run shared contract tests against every subtype or implementation.
- Add an extension proof that introduces a variant without editing stable policy.
- Inspect imports or dependency graphs for policy depending on infrastructure.
- Search for unsupported methods, no-op implementations, service location, vendor types in policy, and duplicate rules.
- Confirm public API changes are intentional and compatible or authorized.
- Confirm the final design follows repository and language idioms.

Read [references/solid-diagnostics.md](references/solid-diagnostics.md) for ambiguous violations, inheritance-heavy designs, broad refactors, and evidence-based review scoring.

## Return the Architecture Handoff

```text
Change axes: <real reasons to change>
Boundary decision: <new, retained, changed, or none needed>
Contracts: <consumer and behavioral guarantees>
Dependency direction: <policy and adapters>
SOLID rationale: <applicable principles only>
Required proof: <contract, extension, characterization, or architecture checks>
Risks: <compatibility or overengineering concerns>
Next phase: <TDD Red, refactor loop, or quality gate>
```

Do not claim whole-task completion. Return control to `engineering-orchestrator`.
