# Quality Gate Matrix

## Risk Signals

Increase risk for:

- Public API, schema, serialization, authentication, authorization, billing, or data-loss impact
- Irreversible migration or broad automated rewrite
- Concurrency, distributed state, caching, retries, or idempotency
- External integration or infrastructure change
- Security-sensitive input, secrets, or personal data
- Large blast radius or weak rollback
- Sparse tests or unreliable baseline

## Applicability Matrix

| Change type | Required evidence |
| --- | --- |
| Pure domain behavior | Valid Red/Green, focused unit tests, related regression, diff review |
| New implementation of a port | Shared contract tests and adapter integration evidence |
| Refactor | Characterization/contract tests, unchanged public behavior, architecture review |
| Defect | Reproducing Red, permanent regression test, root-cause verification |
| UI interaction | Component/browser behavior, responsive or visual inspection when layout changes |
| Public API | Consumer contract, compatibility, error schema, documentation |
| Database migration | Forward migration, representative data, rollback or recovery, idempotency, partial failure |
| CI/build/config | Syntax/schema validation, representative execution, secret and environment review |
| Performance | Baseline, repeatable measurement, target threshold, regression comparison |
| Security | Threat-relevant tests, validation/auth boundaries, secret and logging review |

## Finding Severity

- **Critical:** Likely data loss, security compromise, or unrecoverable production failure.
- **High:** Requested behavior is wrong, compatibility breaks, required tests fail, or evidence is materially unreliable.
- **Medium:** Significant maintainability, resilience, or operational issue with credible impact.
- **Low:** Local quality issue with limited practical impact.

Do not inflate subjective style preferences into SOLID or gate failures.

## Remediation Routing

| Finding | Route |
| --- | --- |
| Missing behavior proof or weak assertion | tdd-workflow |
| Responsibility, extension, substitution, interface, dependency issue | solid-code-design |
| Repeated failure, regression, or unclear cause | loop-engineering |
| Scope or authorization problem | engineering-standards-orchestrator Intake |
| Required evidence unavailable | orchestrator Blocked state |

After remediation, rerun the failed gate and all downstream gates affected by the change.
