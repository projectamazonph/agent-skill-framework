# Source Repositories

This framework combines skills, plugins, adapters, integrations, and templates from **5 source GitHub repositories** into a single unified collection.

## Source Repositories

### 1. agent-skills-library

- **GitHub:** [`projectamazonph/agent-skills-library`](https://github.com/projectamazonph/agent-skills-library)
- **Focus:** Community skill library — the largest collection of shared, system, and agent skills
- **Skills contributed:** 43 skills across `agent-skills/` and `mattpocock-skills/` categories
- **Also contributed:** Plugins, CLI tools, MCP server configs

| Local Path | Skill Name | Category |
|---|---|---|
| `skills/agent-skills/composio-cli/` | composio-cli | agent-skills |
| `skills/agent-skills/design-taste-frontend/` | design-taste-frontend | agent-skills |
| `skills/agent-skills/high-end-visual-design/` | high-end-visual-design | agent-skills |
| `skills/agent-skills/redesign-existing-projects/` | redesign-existing-projects | agent-skills |
| `skills/agent-skills/solid/` | solid | agent-skills |
| `skills/agent-skills/tdd/` | tdd | agent-skills |
| `skills/mattpocock-skills/engineering/ask-matt/` | ask-matt | mattpocock/eng |
| `skills/mattpocock-skills/engineering/code-review/` | code-review | mattpocock/eng |
| `skills/mattpocock-skills/engineering/codebase-design/` | codebase-design | mattpocock/eng |
| `skills/mattpocock-skills/engineering/diagnosing-bugs/` | diagnosing-bugs | mattpocock/eng |
| `skills/mattpocock-skills/engineering/domain-modeling/` | domain-modeling | mattpocock/eng |
| `skills/mattpocock-skills/engineering/grill-with-docs/` | grill-with-docs | mattpocock/eng |
| `skills/mattpocock-skills/engineering/implement/` | implement | mattpocock/eng |
| `skills/mattpocock-skills/engineering/improve-codebase-architecture/` | improve-codebase-architecture | mattpocock/eng |
| `skills/mattpocock-skills/engineering/prototype/` | prototype | mattpocock/eng |
| `skills/mattpocock-skills/engineering/research/` | research | mattpocock/eng |
| `skills/mattpocock-skills/engineering/resolving-merge-conflicts/` | resolving-merge-conflicts | mattpocock/eng |
| `skills/mattpocock-skills/engineering/setup-matt-pocock-skills/` | setup-matt-pocock-skills | mattpocock/eng |
| `skills/mattpocock-skills/engineering/tdd/` | tdd | mattpocock/eng |
| `skills/mattpocock-skills/engineering/to-spec/` | to-spec | mattpocock/eng |
| `skills/mattpocock-skills/engineering/to-tickets/` | to-tickets | mattpocock/eng |
| `skills/mattpocock-skills/engineering/triage/` | triage | mattpocock/eng |
| `skills/mattpocock-skills/engineering/wayfinder/` | wayfinder | mattpocock/eng |
| `skills/mattpocock-skills/in-progress/batch-grill-me/` | batch-grill-me | mattpocock/exp |
| `skills/mattpocock-skills/in-progress/claude-handoff/` | claude-handoff | mattpocock/exp |
| `skills/mattpocock-skills/in-progress/loop-me/` | loop-me | mattpocock/exp |
| `skills/mattpocock-skills/in-progress/setup-ts-deep-modules/` | setup-ts-deep-modules | mattpocock/exp |
| `skills/mattpocock-skills/in-progress/to-questionnaire/` | to-questionnaire | mattpocock/exp |
| `skills/mattpocock-skills/in-progress/wizard/` | wizard | mattpocock/exp |
| `skills/mattpocock-skills/in-progress/writing-beats/` | writing-beats | mattpocock/exp |
| `skills/mattpocock-skills/in-progress/writing-fragments/` | writing-fragments | mattpocock/exp |
| `skills/mattpocock-skills/in-progress/writing-shape/` | writing-shape | mattpocock/exp |
| `skills/mattpocock-skills/misc/git-guardrails-claude-code/` | git-guardrails-claude-code | mattpocock/misc |
| `skills/mattpocock-skills/misc/migrate-to-shoehorn/` | migrate-to-shoehorn | mattpocock/misc |
| `skills/mattpocock-skills/misc/scaffold-exercises/` | scaffold-exercises | mattpocock/misc |
| `skills/mattpocock-skills/misc/setup-pre-commit/` | setup-pre-commit | mattpocock/misc |
| `skills/mattpocock-skills/personal/edit-article/` | edit-article | mattpocock/personal |
| `skills/mattpocock-skills/personal/obsidian-vault/` | obsidian-vault | mattpocock/personal |
| `skills/mattpocock-skills/productivity/grill-me/` | grill-me | mattpocock/prod |
| `skills/mattpocock-skills/productivity/grilling/` | grilling | mattpocock/prod |
| `skills/mattpocock-skills/productivity/handoff/` | handoff | mattpocock/prod |
| `skills/mattpocock-skills/productivity/teach/` | teach | mattpocock/prod |
| `skills/mattpocock-skills/productivity/writing-great-skills/` | writing-great-skills | mattpocock/prod |
| `skills/mattpocock-skills/deprecated/design-an-interface/` | design-an-interface | mattpocock/deprecated |
| `skills/mattpocock-skills/deprecated/qa/` | qa | mattpocock/deprecated |
| `skills/mattpocock-skills/deprecated/request-refactor-plan/` | request-refactor-plan | mattpocock/deprecated |
| `skills/mattpocock-skills/deprecated/ubiquitous-language/` | ubiquitous-language | mattpocock/deprecated |
| `plugins/chromium-browser/` | chromium-browser | plugin |
| `plugins/ponytail/` | ponytail | plugin |

### 2. agent-skill-suite

- **GitHub:** [`projectamazonph/agent-skill-suite`](https://github.com/projectamazonph/agent-skill-suite)
- **Focus:** Portable operating system for AI agents — turns vague requests into controlled, testable, evidence-backed work
- **Skills contributed:** 6 suite core skills + adapters + schemas + validation scripts

| Local Path | Skill Name |
|---|---|
| `skills/suite-core/agent-control-plane/` | agent-control-plane |
| `skills/suite-core/artifact-production/` | artifact-production |
| `skills/suite-core/conversation-compiler/` | conversation-compiler |
| `skills/suite-core/engineering-orchestrator/` | engineering-orchestrator |
| `skills/suite-core/implementation-council/` | implementation-council |
| `skills/suite-core/local-memory/` | local-memory |
| `adapters/claude-code/` | (adapter) |
| `adapters/gemini-cli/` | (adapter) |
| `adapters/github-copilot/` | (adapter) |
| `schemas/handoff.schema.json` | (schema) |
| `scripts/validate_suite.py` | (validation) |

### 3. engineering-standards

- **GitHub:** [`projectamazonph/engineering-standards`](https://github.com/projectamazonph/engineering-standards)
- **Focus:** Agent-agnostic engineering quality gates, SOLID design, TDD, loop engineering
- **Skills contributed:** 5 core engineering skills + 1 specialist skill + agent integrations

| Local Path | Skill Name | Category |
|---|---|---|
| `skills/engineering/engineering-quality-gates/` | engineering-quality-gates | engineering |
| `skills/engineering/engineering-standards-orchestrator/` | engineering-standards-orchestrator | engineering |
| `skills/engineering/loop-engineering/` | loop-engineering | engineering |
| `skills/engineering/solid-code-design/` | solid-code-design | engineering |
| `skills/engineering/tdd-workflow/` | tdd-workflow | engineering |
| `skills/engineering/specialists/precision-workflow/` | precision-workflow | engineering/specialist |
| `integrations/claude/` | (Claude agents + rules) | integration |
| `integrations/cursor/` | (Cursor agents + rules) | integration |
| `integrations/openai/` | (OpenAI agent configs) | integration |

### 4. design-skill-pack

- **GitHub:** [`projectamazonph/design-skill-pack`](https://github.com/projectamazonph/design-skill-pack)
- **Focus:** 23 opinionated design skills for premium, non-template UIs
- **Skills contributed:** 2 curated design skills + full design docs

| Local Path | Skill Name | Category |
|---|---|---|
| `skills/design/amazon-ad-console-redesign/` | amazon-ad-console-redesign | design |
| `skills/design/design-system-master/` | design-system-master | design (orchestrator) |
| `docs/` | (design docs, catalog, architecture) | docs |

### 5. project-bootstrap-full

- **GitHub:** [`projectamazonph/project-bootstrap-full`](https://github.com/projectamazonph/project-bootstrap-full)
- **Focus:** Complete project foundation scaffolding with SOLID architecture, TDD protocols, and documentation
- **Skills contributed:** 1 bootstrap skill + reference templates

| Local Path | Skill Name | Category |
|---|---|---|
| `skills/bootstrap/SKILL.md` | project-bootstrap-full | bootstrap |
| `references/` | (template files, combined instructions) | templates |

---

## Plugins & CLI Tools

### Plugins

| Plugin | Source Repo | Version | Local Path |
|--------|-------------|---------|------------|
| Ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 4.8.4 | `plugins/ponytail/` |
| Chromium Browser | [opencode-chromium-browser-plugin](https://github.com/nicholasgriffintn/opencode-chromium-browser-plugin) | 0.1.1 | `plugins/chromium-browser/` |

### CLI Tools

| Tool | Source Repo | Local Path |
|------|-------------|------------|
| agent-browser | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | `cli-tools/` |
| skills CLI | [mattpocock/skills](https://github.com/mattpocock/skills) | (reference) |

### MCP Servers

| Server | Source Repo | Local Path |
|--------|-------------|------------|
| codebase-memory-mcp | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | `mcp-servers/README.md` |
| context7 | [upstash/context7](https://github.com/upstash/context7) | `mcp-servers/README.md` |
| sequential-thinking | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | `mcp-servers/README.md` |
| sentry | [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | `mcp-servers/README.md` |
| github | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | `mcp-servers/README.md` |
| supabase | [supabase/mcp](https://github.com/supabase/mcp) | `mcp-servers/README.md` |
| figma | [figma/mcp](https://mcp.figma.com/mcp) | `mcp-servers/README.md` |

---

## License

MIT — see [LICENSE](LICENSE). Individual skill files retain their original attribution where present.
