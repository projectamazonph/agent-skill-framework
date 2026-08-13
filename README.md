# Agent Skill Framework

> A comprehensive, unified framework of **71 agent skills** — fusing engineering quality gates, design systems, workflow orchestration, project bootstrapping, and a curated library of community + personal skills into one portable collection.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 71](https://img.shields.io/badge/Skills-71-brightgreen.svg)](#skills)
[![Commits: 4](https://img.shields.io/badge/Commits-4-blue.svg)](CHANGELOG.md)

---

## ✨ What Is This

The **Agent Skill Framework** is a curated library of skills that enable AI agents to perform specialized work. Each skill is a self-contained directory containing a [`SKILL.md`](https://github.com/ryanluu/agentskill-spec) manifest with YAML frontmatter (name, description, allowed tools) and natural-language instructions for the agent.

This framework was created by **combining 5 source repositories** plus adding **5 personal own skills**:

| # | Source | GitHub | Focus | Skills |
|---|--------|--------|-------|--------|
| 1 | agent-skills-library | `projectamazonph/agent-skills-library` | Community skill library | 46 |
| 2 | agent-skill-suite | `projectamazonph/agent-skill-suite` | Suite orchestration | 11 |
| 3 | engineering-standards | `projectamazonph/engineering-standards` | Engineering quality gates | 6 + 1 specialist |
| 4 | design-skill-pack | `projectamazonph/design-skill-pack` | Design system skills | 2 |
| 5 | project-bootstrap-full | `projectamazonph/project-bootstrap-full` | Project scaffolding | 1 |
| 6 | own (personal) | `skills-lock.json` curated | Personal engineering skills | 5 |

**Total: 71 unique SKILL.md files · ~317 files · 7 categories**

---

## 🚀 Quick Start

### Option 1: Use as an installed skill pack

```bash
# Install the framework into your agent environment
git clone https://github.com/projectamazonph/agent-skill-framework.git
cp -r agent-skill-framework/skills /path/to/.omnibot/skills/
```

### Option 2: Use individual skills

Navigate to any skill directory and read its `SKILL.md`:

```bash
# See all available skills
find skills/ -name "SKILL.md" | sort

# Read a specific skill
cat skills/engineering/quality-gates/SKILL.md
```

### Option 3: Validate the framework

```bash
# Validate bundle structure and skill definitions
python3 scripts/validate_suite.py

# Validate design skills
python3 scripts/validate.py

# See full bundle manifest
cat bundle.yaml
```

---

## 🎯 Quick Reference

### Key Skills to Know

| Skill | Category | When to Use |
|-------|----------|-------------|
| **quality-gates** | engineering | Before any PR merge — returns PASS or BLOCKED |
| **test-driven-development** | suite-core | When you need to prove one behavior via Red-Green-Refactor |
| **loop-engineering** | suite-core | For long-running work that needs evidence-driven iteration |
| **solid-design** | suite-core | Define architecture, responsibilities, contracts |
| **implementation-council** | suite-core | Pressure-test plans, code, migrations through expert debate |
| **artifact-production** | suite-core | Create, render, version, and verify professional deliverables |
| **agent-control-plane** | suite-core | Manage workspaces, permissions, state, logs |
| **project-bootstrap-full** | bootstrap | Starting a brand-new project from scratch |
| **systematic-debugging** | own | Debugging mysterious failures, production incidents |
| **critical-thinking** | own | Stress-testing claims, evaluating reasoning quality |

### Install Order (from bundle.yaml)

The `bundle.yaml` declares a 23-step install order. The first 5 phases establish the foundation:

```yaml
install_order:
  - "test-driven-development"    # Red-Green-Refactor discipline
  - "solid-design"               # SOLID architecture patterns
  - "loop-engineering"           # Evidence-driven iteration loops
  - "quality-gates"              # PASS/BLOCKED validation gates
  - "engineering-orchestrator"   # Coordinates engineering work
  # ... then 8 more suite skills ...
  - "implementation-council"
  - "artifact-production"
  - "local-memory"
  - "conversation-compiler"
  - "agent-control-plane"
  - "suite-orchestrator"
```

---

## 📁 Repository Structure

```
agent-skill-framework/
├── README.md                    # This file
├── LICENSE                      # MIT
├── CHANGELOG.md                 # Version history
├── AGENTS.md                    # Agent integration instructions
├── bundle.yaml                  # Unified skill bundle manifest
├── SOURCE-REPOS.md              # Mapping of every skill to its origin
├── .gitignore
├── .codex-plugin/
│   └── plugin.json              # Codex plugin manifest
├── .github/workflows/
│   └── validate.yml             # CI: validates docs + templates
│
├── skills/                      # ── ALL 71 SKILLS ──
│   ├── agent-skills/            # 6 foundational skills
│   │   ├── composio-cli/            Browser automation CLI
│   │   ├── design-taste-frontend/     Anti-slop frontend design (3-dial system)
│   │   ├── high-end-visual-design/    Awwwards-tier agency aesthetics
│   │   ├── redesign-existing-projects/    Upgrade existing UIs to premium
│   │   ├── solid/                     SOLID principles & clean code
│   │   └── tdd/                       Test-driven development
│   │
│   ├── mattpocock-skills/       # 40 Matt Pocock engineering skills
│   │   ├── engineering/             # 16 active engineering skills
│   │   ├── in-progress/             # 9 experimental skills
│   │   ├── misc/                    # 4 utility skills
│   │   ├── personal/                # 2 personal productivity
│   │   ├── productivity/            # 7 workflow skills
│   │   └── deprecated/              # 4 deprecated (kept for reference)
│   │
│   ├── suite-core/               # 11 suite orchestration skills
│   │   ├── agent-control-plane/
│   │   ├── artifact-production/
│   │   ├── conversation-compiler/
│   │   ├── engineering-orchestrator/
│   │   ├── implementation-council/
│   │   ├── local-memory/
│   │   ├── loop-engineering/
│   │   ├── quality-gates/
│   │   ├── solid-design/
│   │   ├── suite-orchestrator/
│   │   └── test-driven-development/
│   │
│   ├── engineering/              # 6 engineering quality standards + 1 specialist
│   │   ├── engineering-quality-gates/
│   │   ├── engineering-standards-orchestrator/
│   │   ├── loop-engineering-v2/      # Renamed: different from suite-core's loop-engineering
│   │   ├── solid-code-design/
│   │   ├── tdd-workflow/
│   │   └── specialists/
│   │       └── precision-workflow/
│   │
│   ├── design/                   # 2 design system skills
│   │   ├── design-system-master/        Orchestrator skill
│   │   └── amazon-ad-console-redesign/
│   │
│   ├── bootstrap/                # 1 project bootstrap skill
│   │   └── SKILL.md
│   │
│   └── own/                      # 5 personal skills (from skills-lock.json)
│       ├── critical-thinking-logical-reasoning/
│       ├── receiving-code-review/
│       ├── requesting-code-review/
│       ├── systematic-debugging/
│       └── tdd-addyosmani/        # Renamed: different from suite-core TDD
│
├── integrations/                 # Agent platform integrations
│   ├── README.md
│   ├── claude/                    # Claude agents + CLAUDE.md rules
│   ├── cursor/                    # Cursor agents + .mdc/.md rules
│   └── openai/                    # OpenAI agent configs (.yaml)
│
├── adapters/                     # Agent platform adapters
│   ├── claude-code/
│   ├── gemini-cli/
│   └── github-copilot/
│
├── plugins/                      # External plugins
│   ├── chromium-browser/
│   └── ponytail/                   # Lazy senior dev mode
│
├── cli-tools/                    # CLI tool configs
├── mcp-servers/                  # MCP server configs
├── schemas/                      # JSON schemas
│   └── handoff.schema.json
├── scripts/                      # Validation & tooling
│   ├── validate_suite.py          # Suite structure + install order validation
│   └── validate.py                # Design skill format validation
├── docs/                         # Reference documentation
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   ├── SKILL-CATALOG.md
│   └── guides/
│       └── QUICKSTART.md
└── references/                   # Bootstrap templates
```

---

## 📖 Skills Guide by Category

### 🎯 Agent Skills (6)
From `agent-skills-library` — foundational skills used by all Omnibot agents.

| Skill | Purpose |
|-------|---------|
| `composio-cli` | Composio tool management for browser automation |
| `design-taste-frontend` | Anti-slop frontend with 3-dial system (variance, motion, density) |
| `high-end-visual-design` | Awwwards-tier agency aesthetics with double-bezel architecture |
| `redesign-existing-projects` | Upgrade existing UIs to premium quality |
| `solid` | SOLID principles & clean code design |
| `tdd` | Test-driven development workflow |

### 🧠 Matt Pocock Skills (40)
From `agent-skills-library` (mattpocock-skills) — engineering skills by Matt Pocock, organized into sub-categories.

| Sub-category | Count | Notable Skills |
|---|---|---|
| **engineering** | 16 | `ask-matt`, `code-review`, `implement`, `to-spec`, `to-tickets`, `triage` |
| **in-progress** | 9 | `claude-handoff`, `loop-me`, `wizard`, `writing-beats` |
| **misc** | 4 | `git-guardrails-claude-code`, `setup-pre-commit`, `scaffold-exercises` |
| **productivity** | 7 | `grill-me`, `handoff`, `teach`, `writing-great-skills` |
| **personal** | 2 | `edit-article`, `obsidian-vault` |
| **deprecated** | 4 | `design-an-interface`, `qa`, `request-refactor-plan`, `ubiquitous-language` |

> **Note on aliases:** `grill-me` and `grill-with-docs` are thin redirect skills that route to the canonical `grilling` skill.

### ⚙️ Suite Core Skills (11)
From `agent-skill-suite` — the portable operating system for AI agents.

| Skill | Purpose |
|-------|---------|
| `agent-control-plane` | Maintain workspaces, permissions, commands, state, logs, failure recovery |
| `artifact-production` | Create, render, version, and verify professional artifacts |
| `conversation-compiler` | Convert raw conversations into governed execution packages |
| `engineering-orchestrator` | Coordinate software work through architecture, TDD, loops, and gates |
| `implementation-council` | Pressure-test plans, code, migrations, releases through expert debate |
| `local-memory` | Capture, retrieve, curate, and forget durable local agent memory |
| `loop-engineering` | Evidence-driven iteration loops (suite protocol version) |
| `quality-gates` | Return PASS or BLOCKED from required engineering evidence |
| `solid-design` | SOLID architecture patterns — responsibilities, contracts, seams |
| `suite-orchestrator` | Classify tasks, route skills, preserve state, enforce completion |
| `test-driven-development` | One observable behavior at a time — Red-Green-Refactor |

### 🔧 Engineering Standards (6 + 1 specialist)
From `engineering-standards` — quality gates and discipline.

| Skill | Purpose |
|-------|---------|
| `engineering-quality-gates` | PASS/BLOCKED validation from engineering evidence |
| `engineering-standards-orchestrator` | Orchestrates all engineering standards skills |
| `loop-engineering-v2` | Alternative loop-engineering routing to tdd-workflow/solid-code-design |
| `solid-code-design` | Define proportionate responsibilities, contracts, extension seams |
| `tdd-workflow` | Red-Green-Refactor cycle with review-stage refactoring |
| `specialists/precision-workflow` | Long-task execution, memory, safety, artifact production |

> **Naming note:** `loop-engineering-v2` is the engineering-standards version (routes to `tdd-workflow`, `solid-code-design`, `quality-gates`). The `loop-engineering` in `suite-core/` is the suite protocol version (routes to `test-driven-development`, `solid-design`, `quality-gates`). Both are kept for cross-compatibility.

### 🎨 Design Skills (2)
From `design-skill-pack` — opinionated design systems for premium UIs.

| Skill | Purpose |
|-------|---------|
| `design-system-master` | Master orchestrator — auto-selects the right design skill combination |
| `amazon-ad-console-redesign` | Redesign guidance for Amazon ad console projects |

> The full Design Skill Pack includes 23 design skills in the upstream repo. Only the 2 core skills are included here. See [docs/SKILL-CATALOG.md](docs/SKILL-CATALOG.md) for the complete upstream catalog.

### 🚀 Bootstrap Skills (1)
From `project-bootstrap-full` — complete project scaffolding.

| Skill | Purpose |
|-------|---------|
| `project-bootstrap-full` | Create a complete project foundation with SOLID architecture, TDD protocols, documentation suite, data logic wireframes, and scaffold |

### 👤 Own Skills (5)
Personal skills curated via `skills-lock.json` from various upstream sources.

| Skill | Source | Purpose |
|-------|--------|---------|
| `critical-thinking-logical-reasoning` | `sammcj/agentic-coding` | Stress-test claims and evaluate reasoning quality |
| `receiving-code-review` | `obra/superpowers` | Best practices for receiving code review feedback |
| `requesting-code-review` | `obra/superpowers` | How to request and structure effective code reviews |
| `systematic-debugging` | `obra/superpowers` | Debug mysterious failures and production incidents |
| `tdd-addyosmani` | `addyosmani/agent-skills` | Lightweight TDD workflow (alternative to suite-core version) |

> **Naming note:** `tdd-addyosmani` is an alternative to the `test-driven-development` suite-core skill. The suite version (139 lines) emphasizes suite protocol; the addyosmani version (398 lines) is a standalone implementation-friendly guide.

---

## 🔌 Integrations & Adapters

**Integrations** (platform-specific agent configs):

| Platform | Path | Contents |
|----------|------|----------|
| Claude Code | `integrations/claude/` | Claude agents + CLAUDE.md |
| Cursor | `integrations/cursor/` | Cursor agents + rules (.mdc, .md) |
| OpenAI | `integrations/openai/` | OpenAI agent configs (.yaml) |

**Adapters** (platform bridges):

| Adapter | Contents |
|---------|----------|
| `claude-code` | CLAUDE.md |
| `gemini-cli` | GEMINI.md |
| `github-copilot` | copilot-instructions.md |

**Plugins:**

| Plugin | Purpose |
|--------|---------|
| `ponytail` | Lazy senior dev mode (YAGNI, stdlib first) |
| `chromium-browser` | Browser automation via Chrome extension |

---

## 🔍 Validation

### Suite Validation (`scripts/validate_suite.py`)

Validates the bundle structure, skill definitions, installation order, and schema compliance.

```bash
python3 scripts/validate_suite.py              # Full validation
python3 scripts/validate_suite.py --install    # Validate + install
python3 scripts/validate_suite.py --category engineering  # Category-only
```

### Design Validation (`scripts/validate.py`)

Validates design skills against format spec (frontmatter, sections, quality gates).

```bash
python3 scripts/validate.py                    # Validate all design skills
python3 scripts/validate.py --verbose         # Show details
```

### CI Pipeline (`.github/workflows/validate.yml`)

GitHub Actions automatically validates documentation and templates on every push and PR.

---

## 📦 Bundle Manifest

The [`bundle.yaml`](bundle.yaml) declares the full skill catalog. Key sections:

```yaml
name: "Agent Skill Framework"
version: "1.0.0"
orchestrator: "suite-orchestrator"
install_order:           # 23 core skills in dependency order
  - "test-driven-development"
  - "solid-design"
  ...
skills:                  # 11 skills with categories + responsibilities
  - name: "agent-control-plane"
    category: "core"
    ...
```

---

## 📝 Contributing

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md).

**Quick rules:**
1. Each skill is a directory with `SKILL.md` + frontmatter (`name`, `description`)
2. Run validation before submitting: `python3 scripts/validate_suite.py`
3. Add new skills to `bundle.yaml` `install_order` and `SOURCE-REPOS.md`
4. Use the `aliases:` frontmatter field to handle name collisions across source repos

---

## 📄 License

MIT — see [`LICENSE`](LICENSE). Individual skill files retain their original attribution where present.

*This is a combined work from 5 source repositories + 5 personal own skills. See [`SOURCE-REPOS.md`](SOURCE-REPOS.md) for the complete origin mapping.*
