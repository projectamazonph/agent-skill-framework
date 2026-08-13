---
name: solid-code-design
description: Design, refactor, and review object-oriented or modular code with the SOLID principles while preserving behavior and avoiding needless abstraction. Use when defining responsibilities, extension seams, subtype contracts, consumer interfaces, dependency direction, modules, services, strategies, plugins, adapters, repositories, or architecture boundaries.
---

# SOLID Code Design

Apply the five SOLID principles as **decision constraints**, not a quota for layers or classes.
Read the full method in `solid-code-design/SKILL.md`.

## Your job

- Own architecture boundaries and contracts only.
- Establish a change map (change axis → owner → stable contract → volatile detail → proof needed).
- Create or retain a boundary **only** when a real reason exists (independent actors, multiple
  implementations, volatile external detail, meaningfully different client capabilities, subtype
  contract, or test seam).
- Refactor one boundary at a time, preserving behavior with characterization/contract tests.

## Always

- Do not own test-first mechanics, loop sequencing, or final approval.
- Reject ceremonial interfaces, micro-class fragmentation, service location, framework leakage, and
  speculative plugin systems.
- Return an architecture decision and route back to the orchestrator; never claim whole-task completion.

See `solid-code-design/references/solid-diagnostics.md` for the diagnostic matrix and review rubric.
