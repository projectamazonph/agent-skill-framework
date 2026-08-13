# Permission Model

| Level | Examples | Default |
| --- | --- | --- |
| 0: Observe | Read in-scope files, inspect status, run non-mutating discovery | Allow within registered workspace |
| 1: Local reversible | Edit in-scope files, run tests, format code | Allow when requested by task |
| 2: Local sensitive | Delete files, alter migrations, rewrite generated assets | Ask or require explicit scope |
| 3: External reversible | Create drafts, branches, preview deployments | Ask unless explicitly requested |
| 4: External consequential | Send, publish, push, merge, deploy production, purchase, rotate secrets | Require explicit authorization |

## Permanent Denials

- Expose secret values in prompts, logs, or memory
- Read denied system paths
- Bypass a sandbox or approval boundary
- Use destructive cleanup to erase unrelated work
- Silently mutate locked memory or published skills

## Approval Record

Record action, scope, target, expiration, and result. Do not treat approval for one repository, recipient, environment, or deployment as permission for another.
