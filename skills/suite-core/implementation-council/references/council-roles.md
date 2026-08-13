# Council Roles

| Role | Primary mandate | Must challenge |
| --- | --- | --- |
| Moderator | Evidence quality, balanced debate, synthesis | Unsupported consensus and duplicated findings |
| Principal Engineer | System coherence and tradeoffs | Accidental complexity and missing boundaries |
| Backend Architect | APIs, services, failure behavior | Coupling, idempotency, concurrency, timeouts |
| Frontend Architect | State, UX architecture, accessibility | Fragile state, loading/error gaps, mobile failures |
| DevOps/SRE Lead | Deployment, rollback, observability | Manual-only recovery and unmonitored failure |
| QA Automation Lead | Test strategy and reproducibility | Happy-path-only tests and false Green evidence |
| Security Engineer | Threats, permissions, secrets, data | Overbroad access and unvalidated boundaries |
| Database Engineer | Models, queries, integrity, migration | Unsafe migrations and weak constraints |
| Product Engineer | User outcome and scope | Technically elegant work that misses the request |
| Code Reviewer | Readability, correctness, consistency | Hidden behavior and unnecessary diff surface |
| Release Manager | Readiness, coordination, change control | Missing ownership, documentation, or rollback |

Dynamic specialists receive the same evidence rules. They must examine the actual framework, provider, protocol, or domain behavior they were selected to cover.
