# Agent Hooks

## Pre-Plan Hook

1. Derive query and scopes from task and workspace.
2. Search project scope.
3. Search global scope for standing rules.
4. Load at most 10 relevant active memories.
5. Check current sources for unstable facts.
6. Build a short memory digest for the planner.

## Post-Run Hook

1. Inspect verified decisions, new procedures, and resolved failures.
2. Exclude transient details and unverified guesses.
3. Search for duplicate or conflicting records.
4. Propose or perform authorized add, update, pin, or forget operations.
5. Read back mutations.

## Failure Hook

Store only after diagnosis:

```text
Failure signature
Environment and command
Root cause
Known-bad attempts
Verified resolution
Prevention rule
Source run or log
```

## User Controls

Support direct requests:

- Remember this
- What do you remember about X?
- Update that memory
- Forget this
- Pin this rule
- Export memory
- Show memory status

Never argue with an explicit forget request. Remove the active record and confirm through readback.
