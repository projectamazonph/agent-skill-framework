---
name: implementation-council
description: Pressure-test codebases, specifications, architecture notes, implementation plans, test strategies, migrations, and deployment plans through a structured council of fixed engineering leaders and task-specific specialists. Use when the user requests an expert panel, adversarial review, debate, gap analysis, implementation improvement, production-readiness assessment, or deployment verdict. Require evidence, disagreement, rebuttal, prioritized gaps, and a clear readiness decision.
---

# Implementation Council

## Mission

Create useful engineering friction. Surface gaps that a single agreeable reviewer misses, force tradeoffs into the open, and convert debate into a better implementation and verification plan.

Do not invent criticism for theater. Every finding must connect to supplied code, documents, requirements, or a clearly labeled missing-evidence risk.

## Suite Protocol

When another skill routes work here, read [references/suite-contract.md](references/suite-contract.md). Accept the Task Packet and return the standard Handoff Packet. The council verdict is evidence for the next skill, not permission to perform unauthorized mutations.

## Choose the Council

Use hybrid mode by default: select fixed leaders plus stack and domain specialists.

Fixed roster:

- Moderator
- Principal Engineer
- Backend Architect
- Frontend Architect
- DevOps and SRE Lead
- QA Automation Lead
- Security Engineer
- Database Engineer
- Product Engineer
- Code Reviewer
- Release Manager

Select only roles relevant to the task. Add specialists for React, Next.js, Node.js, Python, mobile, PostgreSQL, AWS, Docker, payments, authentication, AI systems, accessibility, data migration, or other material technologies.

Recommended size:

- Small scope: 5–7 members
- Medium scope: 8–12 members
- Complex or release-critical scope: 12–16 members

Read [references/council-roles.md](references/council-roles.md) for role mandates and conflicts to test.

## Establish Intake

Record:

- Product outcome and acceptance criteria
- Materials reviewed and versions
- Architecture and stack
- Deployment target
- User, data, security, and operational constraints
- Known gaps and unresolved decisions
- Review mode: plan, implementation, codebase, migration, or release

Do not treat missing evidence as proof that the implementation is correct.

## Run the Council

### Round 1: Independent Review

Each selected member identifies:

- Strongest aspect
- Highest-risk gap
- Hidden assumption
- Required evidence
- Recommended change

### Round 2: Challenge and Rebuttal

Require at least three material disagreements for medium or complex work. Examples:

- Simplicity versus extensibility
- Delivery speed versus operational safety
- Unit isolation versus integration realism
- Normalization versus query performance
- Client convenience versus security boundary
- Migration speed versus rollback safety

Each disagreement must include claim, evidence, counterargument, tradeoff, and proposed resolution.

### Round 3: Failure Simulation

Test likely failures:

- Invalid input and partial state
- Dependency outage and timeout
- Concurrency and retry behavior
- Permission or authentication failure
- Migration interruption and rollback
- Data corruption or compatibility drift
- Build, deployment, monitoring, and incident response gaps

### Round 4: Synthesis

The Moderator removes duplicates, preserves unresolved disagreements, and converts findings into a prioritized gap register.

## Build the Gap Register

For every gap, include:

```text
ID
Severity: critical | high | medium | low
Area
Evidence
Failure mode
Affected requirement
Recommended correction
Owner
Verification
Blocks readiness: yes | no
```

Order by user impact, security, data integrity, correctness, compatibility, operability, and maintainability. Do not inflate style preferences into production blockers.

## Enhance the Plan

Produce an implementation plan that:

- Resolves critical and high gaps first
- Splits work into independently verifiable steps
- Includes test, rollback, monitoring, documentation, and ownership
- Preserves accepted design strengths
- Identifies explicit tradeoffs and deferred risks
- Routes coding through `engineering-orchestrator`

## Issue the Verdict

Use one:

- **GO:** Required evidence passes and no blocking gap remains.
- **CONDITIONAL GO:** Named preconditions must pass before execution or release.
- **NO-GO:** A critical gap, missing required evidence, or unsafe recovery path blocks progress.

Read [references/output-contract.md](references/output-contract.md) for the final structure.

For read-only reviews, do not edit code or publish changes. A completed review can still return NO-GO.
