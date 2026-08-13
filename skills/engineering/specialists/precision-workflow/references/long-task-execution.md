# Long Task Execution

Managing multi-step work that spans many tool calls, files, or reasoning cycles.

## When to use this

Any task that requires more than 5–10 tool calls, involves multiple files, has branching logic, or cannot be completed in a single pass.

## Execution philosophy

- **Do the simplest thing that could work first.** Expand complexity only when the simple approach fails or is provably insufficient.
- **Keep the user informed** — not with narrating every step, but with meaningful milestones.
- **Never silently swallow failures.** If a step fails, decide: retry, work around, or report and stop.
- **Verify as you go** rather than waiting until the end to check everything.

## Progress communication

Send an update when:

- The approach is clear and the first real step is about to begin.
- A meaningful milestone is reached (e.g., data fetched, core logic written, first test passing).
- A finding changes or invalidates the planned direction.
- The task hits a blocker that needs user input to resolve.
- The work is complete.

Keep updates short: one or two sentences. The user can ask for details if needed.

## Branching logic

When a task forks into parallel workstreams:

```
[TASK A] ──┬── [subtask 1]
           └── [subtask 2]
```

Use `delegate_task` for independent subtasks that don't depend on each other's output. This saves context and runs them in parallel.

When subtasks must run sequentially, handle dependencies explicitly — don't start step 2 until step 1's output is verified.

## Error recovery

| Error type | Response |
|---|---|
| Tool call failed (network, permissions) | Retry once or twice with backoff; then report |
| File write failed | Check path, disk space, permissions; retry once |
| Build / test failed | Read the error; fix the root cause, not the symptom |
| Task blocked on missing info | Ask the user; don't guess at critical parameters |
| Tool not available | Report and propose an alternative approach |

## Retries

Retry at most twice with exponential backoff (2s, 4s). After that, stop and report. Silent repeated failures waste time and may indicate a deeper issue.

## End-of-task summary

When the work is done:

```
### Completed
What was done.

### Verified
Checks that ran and their results (e.g., "build passed", "3 files written").

### Remaining
Only genuine open issues. If nothing remains, omit this section entirely.
```

Do not pad the summary with caveats or repeat everything that was already said in progress updates.

## What to save after

- Durable facts → main memory (via the memory tool)
- Recurring procedures → skills (via skill_manage)
- Project-specific rules → AGENTS.md in the project root
