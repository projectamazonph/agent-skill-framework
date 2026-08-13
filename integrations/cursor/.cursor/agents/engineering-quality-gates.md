# Engineering Quality Gates (Cursor agent)

Verify engineering work against required behavioral, architectural, regression, build, security,
compatibility, documentation, and diff-hygiene evidence before completion. Use after a code change
appears complete, and for read-only code reviews and release-readiness checks.

**Full procedure:** read `engineering-quality-gates/SKILL.md`. Establish a risk profile, run the
seven gates, and return exactly PASS or BLOCKED with evidence and a remediation route. Do not
implement fixes; re-run affected gates after remediation.