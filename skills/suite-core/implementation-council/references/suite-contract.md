# Suite Contract

## Design Rules

1. Give each skill one primary responsibility.
2. Activate the fewest skills required by the task.
3. Preserve user scope, existing content, and unrelated work.
4. Separate facts, inferences, decisions, and missing evidence.
5. Require observable evidence before reporting completion.
6. Keep platform-specific invocation, tools, and metadata outside the portable core.
7. Use progressive disclosure: load references and scripts only when needed.

## Task Packet

Every routed skill receives:

```yaml
task_id: stable identifier
outcome: requested result
scope: authorized files, systems, and mutations
inputs: source material and current state
constraints: requirements, exclusions, and permissions
acceptance: observable completion conditions
evidence_required: tests, inspections, renders, or readback
```

Unknown values remain `unknown`; never fill them with invented detail.

## Handoff Packet

Every routed skill returns:

```yaml
skill: emitting skill name
status: ready | active | pass | blocked | needs-input | not-applicable
scope_completed: work actually performed
decisions: material decisions and rationale
evidence: commands, checks, sources, and outcomes
outputs: files, changes, findings, or records produced
risks: residual uncertainty or limitations
next_skill: next responsible skill or null
next_action: smallest justified next step
```

Use `pass` only for the skill's own responsibility. Only the designated completion owner may mark the overall task complete.

## Failure Behavior

- Return `blocked` when required evidence or authority is unavailable.
- Return `needs-input` only when a user decision materially changes the result.
- Return `not-applicable` with a reason when a routed skill does not apply.
- Never weaken tests, checks, assertions, or scope controls to manufacture `pass`.
- Route remediation to the skill that owns the failed responsibility.

## Platform Neutrality

Refer to skills by their frontmatter `name`. Do not assume a slash command, dollar prefix, mention syntax, subagent feature, specific model, or specific tool API. Platform adapters may translate neutral activation into local syntax.
