---
name: agent-control-plane
description: "Establish and maintain a persistent control plane for coding agents and project agents: registered workspaces, source-of-truth state, permissions, tool routing, known commands, environment-variable locations, atomic tasks, logs, checkpoints, failure memory, and stop conditions. Use before agents work on a new or continuing repository, when sessions repeatedly rediscover paths or repeat failed commands, when deployment or credential-location knowledge is lost, or when AGENTS.md and project-state documentation must govern execution."
---

# Agent Control Plane

## Mission

Make agents resume from known state instead of improvising the environment on every session. Own control files, permissions, routing, checkpoints, failure memory, and operational continuity.

Do not implement product behavior. Hand coding work to `engineering-orchestrator` after the control plane is ready.

## Suite Protocol

When another skill routes work here, read [references/suite-contract.md](references/suite-contract.md). Accept the Task Packet and return the standard Handoff Packet. Mark `pass` only when workspace state, permissions, and recovery controls are ready for the next skill.

## Resolve the Workspace Once

1. Prefer an explicit path from the user or active environment.
2. Read the nearest repository instructions and project manifest.
3. Confirm the repository root with bounded checks such as `.git`, package manifests, and configured markers.
4. Register the canonical root, active branch, project type, and known commands.
5. Never scan the entire device or storage when the registry or current environment provides the location.

If the registered path is missing, perform one bounded search in approved roots, update the registry, and record the repair.

## Establish the Source of Truth

Use existing equivalent files when present. Otherwise define only the files the project needs:

| File | Responsibility |
| --- | --- |
| `AGENTS.md` | Non-negotiable agent behavior, scope, commands, and prohibited actions |
| `.agent/project.json` | Canonical root, stack, checks, permissions, limits, and workflows |
| `docs/AI_CONTEXT.md` | Current architecture, state, goals, and constraints |
| `docs/TODO.md` | Atomic task queue and dependency order |
| `docs/BUILD_LOG.md` | Completed work, files changed, commands, and outcomes |
| `docs/ERROR_LOG.md` | Failures, root causes, attempted fixes, and known-bad actions |
| `docs/DECISIONS.md` | Durable decisions and rejected alternatives |
| `docs/TEST_LOG.md` | Test commands, results, baseline failures, and coverage gaps |
| `docs/DEV_DIARY.md` | Concise observations and next-session handoff |
| `docs/CHANGELOG.md` | User-facing changes by version |
| `docs/API_SPEC.md` and `docs/STATE_SCHEMA.md` | Contracts when the project has APIs or stateful behavior |

Read [references/control-files.md](references/control-files.md) before creating or repairing this stack.

## Maintain the Operational Registry

Record names and locations, never secret values:

```text
Workspace root
Primary manifests
Runtime and package manager
Install, dev, test, typecheck, lint, build, deploy, and release commands
Environment file locations and required variable names
Credential provider or secret-store reference
Deployment target and verified workflow
Known restrictions and approval requirements
Last successful command and date
Known-bad commands and why they failed
```

Never print, copy, or store tokens, passwords, private keys, or secret values in logs or memory.

## Enforce the Tool Gateway

Route tool use through explicit capabilities. Default-deny:

- Actions outside the registered workspace
- Network access not required by the task
- File deletion or destructive reset
- Git commit, push, merge, release, or deployment without authorization
- Reading secret files or credential stores
- Sending, publishing, purchasing, or external mutation
- Silent memory or skill modification

Read [references/permission-model.md](references/permission-model.md) for risk levels and approval boundaries.

## Run One Atomic Task

1. Load the manifest, AI context, task queue, decisions, error log, and last handoff.
2. Select one acceptance outcome.
3. State the plan, required tools, permissions, and stop condition.
4. Route implementation through Engineering Standards.
5. Record files changed, commands, test results, errors, and decisions.
6. Update the task queue and next-session handoff.
7. Create a checkpoint only when project policy permits.
8. Stop when the acceptance check and required quality gate pass.

Keep derived UI, dashboards, or summaries subordinate to the canonical state model.

## Prevent Repeated Failure

Before running a command or workflow, check the Error Log and operational registry.

After two materially similar failures:

1. Stop repeating the action.
2. Record the command, environment, failure signature, and attempted fixes.
3. Identify the shared assumption.
4. Gather one new observation that can falsify it.
5. Change strategy or request a material decision.

Never spend another hour rediscovering that the same door is still a wall.

## Use Agent Roles Deliberately

Use only roles required by the task:

- Router: classify and dispatch
- Planner: decompose work and dependencies
- Executor: perform approved atomic actions
- Reviewer/Critic: inspect against requirements
- Tester: run and interpret checks
- Judge: enforce stop conditions
- Security Sentinel: enforce capabilities and approvals
- Memory Curator: propose durable updates
- Skill Builder: version reusable procedures after approval

Keep tool execution behind the gateway. Agents propose actions; policy authorizes them.

## Return the Control Handoff

```text
Workspace: <canonical root>
State loaded: <files and versions>
Task: <one atomic outcome>
Known commands: <verified commands>
Permissions: <allowed, denied, approval-required>
Known failures: <relevant entries>
Required route: <engineering, review, artifact, or memory skill>
Stop condition: <evidence required>
```
