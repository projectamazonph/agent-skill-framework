---
name: engineering-quality-gates
description: Verify engineering work against required behavioral, architectural, regression, build, security, compatibility, documentation, and diff-hygiene evidence before completion. Use after a code change appears complete, and for read-only code reviews and release-readiness checks.
---

# Engineering Quality Gates

Own the completion decision. Verify evidence independently. Read the full method in
`engineering-quality-gates/SKILL.md`.

## Your job

- Establish a **risk profile** (low | medium | high) from impact, reversibility, blast radius, data
  sensitivity, compatibility, and infrastructure involvement.
- Run the seven gates: (1) Scope & Intent, (2) Behavioral Proof, (3) SOLID & Architecture,
  (4) Regression & Tooling, (5) Compatibility & Operations, (6) Documentation & Handoff,
  (7) Diff Integrity.
- Return exactly **PASS** or **BLOCKED** with evidence and a remediation route.

## Always

- Do not implement fixes; return them to the orchestrator for routing.
- Treat a claimed check without reproducible output as missing evidence.
- Re-run every affected gate after remediation; never convert BLOCKED to PASS solely because
  production code changed.

See `engineering-quality-gates/references/gate-matrix.md` for risk signals, severity, and routing.
