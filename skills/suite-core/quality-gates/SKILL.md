---
name: quality-gates
description: Verify engineering work against required behavioral, architectural, regression, build, security, compatibility, documentation, and diff-hygiene evidence before completion. Use after a code change, defect fix, refactor, migration, generated-code update, or implementation plan appears complete; also use for read-only code reviews and release-readiness checks. Return PASS or BLOCKED without implementing the remediation.
---

# Quality Gates

## Mission

Own the completion decision. Verify evidence independently enough to catch false Green states, regressions, scope drift, and unjustified architecture.

Do not implement fixes. Return failures to `engineering-orchestrator`, which routes remediation to the appropriate specialist.

## Suite Protocol

When another skill routes work here, read [references/suite-contract.md](references/suite-contract.md). Accept the Task Packet and return the standard Handoff Packet. This skill owns the engineering completion decision and must return `blocked` whenever required evidence is missing or failed.

## Establish the Gate Profile

Classify risk from impact, reversibility, blast radius, data sensitivity, compatibility, and infrastructure involvement.

| Risk | Minimum profile |
| --- | --- |
| Low | Acceptance check, focused tests, diff review, relevant formatting or static check |
| Medium | Low profile plus related regression suite, type/lint/build checks, architecture review, error-path coverage |
| High | Medium profile plus integration or end-to-end evidence, compatibility/migration/rollback checks, security and data-integrity review, operational observability |

Repository-required checks always apply. Increase the profile when uncertainty remains; do not reduce it to match available evidence.

Read [references/gate-matrix.md](references/gate-matrix.md) for risk signals, gate applicability, and remediation routing.

## Inspect Required Evidence

Obtain:

- Requested acceptance behavior and scope
- Relevant baseline result
- TDD Red and Green evidence for changed behavior
- Loop ledger or equivalent change evidence
- Architecture decision when a boundary changed
- Test, build, type, lint, runtime, or visual results appropriate to the work
- Final diff and working-tree state

Treat a claimed check without reproducible result or trustworthy output as missing evidence.

## Run the Gates

### Gate 1: Scope and Intent

- Confirm the implementation satisfies the actual request.
- Identify unrelated edits, missing requirements, placeholders, dead code, and accidental generated changes.
- Confirm breaking changes, deletions, migrations, and external effects were authorized.

### Gate 2: Behavioral Proof

- Confirm each new behavior or defect has valid Red evidence.
- Confirm the intended test reached Green without weaker assertions, skips, filters, or bypasses.
- Confirm tests assert observable contracts rather than only implementation detail.
- Confirm legacy refactors have characterization or contract coverage.

Mark this gate not applicable only for work that changes no executable behavior, such as a read-only review or prose-only document edit.

### Gate 3: SOLID and Architecture

- Confirm responsibilities align with real reasons to change.
- Confirm extension seams match actual variation points.
- Confirm implementations honor substitutable contracts.
- Confirm clients depend only on required capabilities.
- Confirm policy does not depend on volatile infrastructure details.
- Reject ceremonial interfaces, micro-class fragmentation, service location, framework leakage, and speculative plugin systems.

### Gate 4: Regression and Tooling

- Run focused tests and the relevant broader suite.
- Run required type checks, linting, formatting checks, builds, schema validation, or generated-code verification.
- Inspect error paths, boundary values, state changes, and material side effects.
- Separate pre-existing failures from introduced failures with evidence.

### Gate 5: Compatibility and Operations

Apply when relevant:

- Public API, schema, serialization, event, or CLI compatibility
- Migration forward path, rollback, idempotency, and partial-failure handling
- Security boundaries, secrets, authorization, validation, and sensitive data
- Performance constraints, resource use, concurrency, and timeouts
- Logging, metrics, alerts, and diagnosability

### Gate 6: Documentation and Handoff

- Confirm public behavior, configuration, migration steps, and operational changes are documented when needed.
- Confirm code comments explain non-obvious intent rather than restating code.
- Confirm the loop ledger reflects actual outcomes and remaining uncertainty.

### Gate 7: Diff Integrity

- Review the final diff for scope drift, duplicate logic, stale compatibility code, debug output, skipped tests, and accidental file changes.
- Confirm unrelated user changes remain intact.
- Confirm no destructive cleanup was used to hide unresolved work.

## Decide

Return exactly one status:

- **PASS:** All applicable required gates have trustworthy evidence and no unresolved blocking finding.
- **BLOCKED:** At least one applicable required gate lacks evidence or has an unresolved failure.

Do not use “mostly passed” for completion. A non-applicable gate is not a failure, but explain why it does not apply.

For read-only reviews, PASS means the review process is complete, not that the code has no findings. Report material findings by severity.

## Report the Gate

Use this structure:

```text
Status: PASS | BLOCKED
Risk profile: low | medium | high
Acceptance: <result>
Evidence: <commands/checks and outcomes>
Architecture: <result or not applicable>
Diff integrity: <result>
Blocking findings: <none or ordered list>
Limitations: <unavailable checks or residual uncertainty>
Route: <complete or specialist/phase for remediation>
```

Order findings by practical severity. Cite files, symbols, tests, or commands. Distinguish confirmed defects from risks and missing evidence.

## Route Failures

- Missing or invalid Red/Green evidence → `test-driven-development`
- Coupling, contract, responsibility, interface, or dependency issue → `solid-design`
- Regression, tooling, environment, or observation failure → `loop-engineering`
- Scope ambiguity, authorization, or conflicting requirements → orchestrator Intake

Re-run every affected gate after remediation. Do not convert BLOCKED to PASS solely because production code changed.
