# Integrations

The skill logic lives in the five root-level `SKILL.md` files — plain Markdown with **no**
vendor-specific syntax. This folder holds the runtime bindings that point each agent framework at
that shared logic. Add your own runtime here without touching the skills.

| Runtime | Path | Mechanism | How a skill is invoked |
| --- | --- | --- | --- |
| **OpenAI** | `openai/agents/*.yaml` | Native agent bindings | `$skill-name` (e.g. `$tdd-workflow`) |
| **Claude Code** | `claude/.claude/agents/*.md` + `CLAUDE.md` | Subagents that read `SKILL.md` | `@agent` or auto-delegation |
| **Cursor** | `cursor/.cursor/agents/*.md` + `rules/*.mdc` | Rules + agents that read `SKILL.md` | Rule auto-apply + agent invocation |

Because every binding reads the **same** `SKILL.md`, editing a skill updates all runtimes at once.

---

## OpenAI

Files: `openai/agents/<skill>.yaml` (the original `interface`/`policy` bindings, relocated from each
skill folder so the skills stay vendor-neutral).

Install:

```bash
# from the repo root
SKILLS_DIR="$HOME/.codex/skills"   # adjust to your runtime's skills path
mkdir -p "$SKILLS_DIR"
for s in engineering-standards-orchestrator solid-code-design tdd-workflow loop-engineering engineering-quality-gates; do
  mkdir -p "$SKILLS_DIR/$s/agents"
  cp "$s/SKILL.md"                 "$SKILLS_DIR/$s/SKILL.md"
  cp "$s/references"/*             "$SKILLS_DIR/$s/references/" 2>/dev/null || mkdir -p "$SKILLS_DIR/$s/references" && cp "$s/references"/* "$SKILLS_DIR/$s/references/"
  cp "integrations/openai/agents/$s.yaml" "$SKILLS_DIR/$s/agents/openai.yaml"
done
```

Each binding sets `allow_implicit_invocation: true`, so the model may invoke skills automatically,
or you can target one explicitly with `$tdd-workflow`, `$engineering-quality-gates`, etc.

---

## Claude Code

Files: `claude/.claude/agents/*.md` (five subagents) + `claude/CLAUDE.md` (project instruction).

Install: copy the `.claude/agents/` directory and `CLAUDE.md` into your project (or user config):

```bash
cp -r claude/.claude /your/project/.claude
cp claude/CLAUDE.md /your/project/CLAUDE.md
```

The subagents delegate to the canonical `SKILL.md` files. Keep this repo accessible (or adjust the
relative paths noted in each agent file) so the subagents can read the procedures.

---

## Cursor

Files: `cursor/.cursor/rules/*.mdc` (an always-on `engineering-standards.mdc` plus one per skill)
and `cursor/.cursor/agents/*.md` (optional agent definitions).

Install: copy the `.cursor` directory into your project:

```bash
cp -r cursor/.cursor /your/project/.cursor
```

The always-apply rule keeps the standards active for every coding task; the per-skill `.mdc` files
and agents reference the canonical `SKILL.md` for full procedure.

---

## Adding another runtime

1. `mkdir integrations/<runtime>` and add the manifest files your framework expects.
2. Point each manifest at the matching root-level `SKILL.md` / `references/` — do **not** duplicate
   the skill text inside the integration.
3. Add a row to the table above and a short install snippet.
4. Keep `SKILL.md` bodies free of any runtime syntax.
