# TDD Workflow (Cursor agent)

Drive one observable software behavior at a time through a valid Test-Driven Development cycle:
select the test, prove Red for the intended reason, implement the smallest Green change, preserve the
test as regression evidence. Use before adding production behavior, fixing defects, changing
contracts, or characterizing legacy behavior.

**Full procedure:** read `tdd-workflow/SKILL.md`. Require an entry contract; run Red → Green →
Refactor. Never delete, skip, loosen, or rewrite a valid test to reach Green. Return a handoff and
route back to the orchestrator and loop-engineering.