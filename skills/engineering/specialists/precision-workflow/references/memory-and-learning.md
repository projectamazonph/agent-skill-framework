# Memory and Learning

Deciding what to remember, what to turn into a skill, and how to keep both current.

## When to use this

After completing a complex task, fixing an error, discovering a non-trivial approach, or learning something that will be needed again.

## What goes in main memory

Durable facts about:

- The user's preferences, habits, and corrections
- Environment specifics (installed tools, path quirks, OS version)
- Project conventions (naming, structure, build commands)
- Credentials and access patterns (without exposing the actual secrets)
- Lessons from errors or debugging sessions that prevent future repeats

**Do not store:**
- Task progress or session logs
- Temporary state or intermediate outputs
- Raw data dumps
- Obvious things easily re-discovered

## What goes in skills

Reusable procedures with:

- Clear trigger conditions (when to use this skill)
- Exact commands or steps
- Pitfalls and edge cases discovered during use
- Verification steps

Skills are loaded on demand. They are the user's procedural memory — the difference between knowing the right way to do something and having to rediscover it every time.

## Decision tree

```
Is it a recurring procedure with steps?
  YES → Skill (skill_manage create)
  NO ↓

Is it a durable fact the user shouldn't have to repeat?
  YES → Memory (memory tool → main memory)
  NO ↓

Is it a project-specific rule or convention?
  YES → AGENTS.md in the project root
  NO → Discard (can be re-derived if needed)
```

## Keeping memory current

- When a memory entry becomes wrong or outdated, update it immediately.
- When a skill produces unexpected results, fix it before the next use.
- Periodically review memory entries — discard what no longer matters.
- The `memory_curation_review` skill handles this systematically.

## Memory write approval

The config snippet enables `write_approval: true` for memory writes. This means the user is prompted before any durable memory is written. This is a safety catch — it prevents runaway memory inflation and accidental overwrites. Leave it on unless you've established clear trust in the workflow.

## Skill write approval

Same principle as memory. When enabled, skill installations require user confirmation. This prevents accidental skill bloat and ensures the user knows when a new procedural memory is being created.
