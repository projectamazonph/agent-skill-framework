# Control Files

## AGENTS.md Minimum Contract

Include:

- Canonical workspace root and project purpose
- Required files to read before work
- Allowed scope and prohibited actions
- Verified install, test, typecheck, lint, build, and deploy commands
- Test-first and Loop Engineering rules
- Documentation update requirements
- Working-tree preservation rules
- Permission and approval boundaries
- Stop and handoff conditions

## Project Manifest

Recommended fields:

```json
{
  "project": "name",
  "workspace_root": "/absolute/path",
  "stack": [],
  "commands": {
    "install": "",
    "test": "",
    "typecheck": "",
    "lint": "",
    "build": "",
    "deploy": ""
  },
  "environment": {
    "files": [],
    "required_variable_names": []
  },
  "policy": {
    "network": "deny|ask|allow",
    "delete": "deny|ask|allow",
    "git_commit": "deny|ask|allow",
    "git_push": "deny|ask|allow",
    "deploy": "deny|ask|allow"
  },
  "limits": {
    "max_iterations": 50,
    "max_minutes": 45,
    "max_patch_lines_per_loop": 250
  }
}
```

Use project-specific values. Do not copy empty commands into an active manifest.

## Logging Rule

Append concise, factual entries. Include timestamp, task, command, result, files, and next action. Keep raw noisy output in a separate attachment only when needed for diagnosis.

## State Repair

When files disagree:

1. Prefer executable reality and current repository instructions.
2. Compare the last verified logs and decisions.
3. Update stale state explicitly.
4. Record the repair and superseded value.
