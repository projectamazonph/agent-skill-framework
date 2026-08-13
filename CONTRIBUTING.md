# Contributing

This pack enforces engineering discipline through a division of concerns:

- core/ and specialists/ hold skill logic as plain SKILL.md + references/.
  No runtime syntax (no $skill, no embedded agents/) belongs here.
- integrations/ holds vendor bindings only.

## Rules
1. Keep every SKILL.md runtime-neutral. Add a new vendor under integrations/.
2. Each skill owns one responsibility; the orchestrator routes, it does not duplicate.
3. "Done" is a verified state: add/adjust evidence, not prose.
4. Frontmatter must stay valid YAML (name, description).

## Adding a skill
1. Create core/<name>/SKILL.md (or specialists/ for non-core).
2. Add references/ as needed, no code or agent bindings inside.
3. Add the runtime manifest under each integrations/<runtime>/ directory.
4. Update README skill tables and integrations/README.md.

## Verify before pushing
- grep -rn '\$skill' core/ specialists/ -> must be empty.
- no openai.yaml / agents/ inside core/ or specialists/.
- frontmatter parses.

All contributions are released under the MIT License.
