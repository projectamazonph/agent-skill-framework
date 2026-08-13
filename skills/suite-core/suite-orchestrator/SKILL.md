---
name: suite-orchestrator
description: Route complex work across the complete Agent Skill Suite while enforcing content preservation, explicit scope, correct specialist timing, evidence-backed completion, and durable state. Use when a task involves coding, agent operations, repository bootstrapping, conversation compilation, artifact generation, expert review, persistent memory, or several of these together. Also use when the correct skill is unclear or work must pass through multiple specialist skills in a controlled sequence.
---

# Suite Orchestrator

## Mission

Own task classification, sequencing, handoffs, and suite-wide standards. Keep specialist responsibilities separate and activate each at the moment its evidence becomes necessary.

## Suite Protocol

Read [references/suite-contract.md](references/suite-contract.md). Create the Task Packet, preserve it across every handoff, and require each specialist to return the standard Handoff Packet. Use neutral skill names; let the active platform adapter translate invocation syntax.

## Enforce Global Rules

1. Preserve existing content and formatting unless the user explicitly requests a change.
2. Change only the authorized scope.
3. Use no placeholders in a completed deliverable.
4. Read current state and evidence before acting.
5. Keep user work and unrelated changes intact.
6. Report only checks that actually ran.
7. Do not declare completion until the responsible quality gate passes.

## Route the Work

| Need | Primary skill | Invoke when |
| --- | --- | --- |
| Establish agent state, workspace, permissions, logs, recovery, or repo controls | `agent-control-plane` | Before agents execute non-trivial project work or when prior sessions have been unreliable |
| Convert raw conversations into projects and deliverables | `conversation-compiler` | Before generating artifacts or implementation tasks from conversation history |
| Coordinate software delivery standards | `engineering-orchestrator` | For every code, schema, config, CI, migration, refactor, fix, or software review task |
| Pressure-test code, specs, plans, and deployments | `implementation-council` | At architecture checkpoints, before high-risk implementation, or before release readiness |
| Generate polished files and export-ready artifacts | `artifact-production` | Once content requirements and sources are stable |
| Capture and retrieve durable local memory | `local-memory` | At task intake and after decisions, failures, reusable procedures, or preferences become durable |

The Engineering Standards Orchestrator owns its internal SOLID, TDD, Loop Engineering, and quality-gate sequence. Do not bypass it by routing directly to one engineering specialist unless the task is intentionally limited to that specialist's job.

Read [references/routing-map.md](references/routing-map.md) for combined workflows and conflict resolution.

## Maintain the Suite Card

```text
Outcome: <requested result>
Source: <conversation, repository, files, or direct request>
Primary route: <skill>
Supporting routes: <ordered skills>
State source: <control plane or current context>
Authorized mutations: <files/systems in scope>
Required evidence: <tests, renders, review, or memory confirmation>
Completion gate: <responsible skill and status>
```

Update the card at each handoff. Never pass guessed state as fact.

## Sequence Common Workflows

### Conversation to Working Software

1. Use Conversation Compiler to extract requirements, corrections, constraints, deliverables, and dependency order.
2. Use Agent Control Plane to establish the workspace manifest, permissions, state files, known commands, and failure history.
3. Use the Engineering Standards Orchestrator to implement through SOLID, TDD, loops, and gates.
4. Use the Implementation Council at material architecture or release checkpoints.
5. Use Artifact Production for polished documentation, decks, spreadsheets, PDFs, or handoff artifacts.
6. Use Local Memory to retain durable decisions, procedures, and resolved failures.

### Existing Repository Work

1. Load Agent OS state and locate the registered workspace.
2. Read relevant repository instructions and dirty-tree state.
3. Route implementation through Engineering Standards.
4. Route broad audit or readiness questions through the Implementation Council.
5. Update state, logs, and memory after verified completion.

### Artifact-Only Work

1. Use Conversation Compiler when the source is a raw conversation or mixed notes.
2. Use Artifact Production to create, render, and verify the artifact.
3. Preserve the artifact's stable identity and version history when updating an existing file.

### Read-Only Review

Use the Implementation Council for adversarial review and the relevant quality gate for evidence. Do not mutate code, publish, send, or deploy without explicit authorization.

## Handle Conflicts

Follow this precedence:

1. System and safety requirements
2. Explicit current user request
3. Repository or artifact instructions
4. Suite-wide standards
5. Specialist defaults

When two specialists conflict, choose the stricter evidence requirement unless it violates scope or user intent. Escalate only a choice that would materially change the outcome.

## Completion

Lead with the verified result. Report the route used, material decisions, evidence, artifact or code produced, gate status, and any unresolved blocker. Keep internal orchestration concise unless the user requests the full ledger.
