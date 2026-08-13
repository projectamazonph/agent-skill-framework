# Agent Skill Framework

> A comprehensive, unified framework of **54+ agent skills** — combining engineering standards, design systems, workflow suites, bootstrap templates, and a curated library of community skills into one portable, installable collection.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 54+](https://img.shields.io/badge/Skills-54%2B-brightgreen.svg)](#skills)
[![Python](https://img.shields.io/badge/scripts-Python-blue.svg)](#scripts)
[![YAML](https://img.shields.io/badge/bundle-YAML-orange.svg)](#bundleyaml)

---

## What This Is

This repository fuses **5 previously separate GitHub repositories** into a single comprehensive agent skill framework:

| Source Repo | Focus | Skills Contributed |
|---|---|---|
| [agent-skills-library](https://github.com/projectamazonph/agent-skills-library) | Community skill library | 43 skills (agent-skills, mattpocock-skills) + plugins + CLI tools + MCP servers |
| [agent-skill-suite](https://github.com/projectamazonph/agent-skill-suite) | Suite orchestration | 6 core skills + adapters + schemas + validation |
| [engineering-standards](https://github.com/projectamazonph/engineering-standards) | Engineering quality gates | 6 engineering skills + agent integrations |
| [design-skill-pack](https://github.com/projectamazonph/design-skill-pack) | Design system skills | 2 design skills + docs + validation |
| [project-bootstrap-full](https://github.com/projectamazonph/project-bootstrap-full) | Project scaffolding | 1 bootstrap skill + reference templates |

**Total: 54 SKILL.md files · 407 files · 1 comprehensive framework**

---

## Quick Start

```bash
# Clone
git clone https://github.com/projectamazonph/agent-skill-framework.git
cd agent-skill-framework

# Validate the bundle
python3 scripts/validate_suite.py

# Or validate design skills
python3 scripts/validate.py
```

### How Skills Work

Each skill is a self-contained directory with a `SKILL.md` file containing YAML frontmatter and step-by-step agent instructions:

```yaml
---
name: project-bootstrap-full
description: Create a complete project foundation with SOLID architecture...
allowed-tools: Bash, Read, Write, Edit
---
```

1. **Agent detects** task matches a skill's description
2. **Reads** `skills/<category>/<name>/SKILL.md`
3. **Follows** the instructions in the body
4. **Uses** `allowed-tools` as specified in frontmatter

### Using the Bundle

```bash
# Install all skills from the bundle
python3 scripts/validate_suite.py --install

# Validate only specific categories
python3 scripts/validate_suite.py --category engineering
python3 scripts/validate_suite.py --category design
python3 scripts/validate_suite.py --category bootstrap
```

---

## Repository Structure

```
agent-skill-framework/
├── README.md                     # This file
├── LICENSE                       # MIT License
├── CONTRIBUTING.md               # Contribution guidelines
├── CHANGELOG.md                  # Version history
├── AGENTS.md                     # Instructions for AI agents
├── bundle.yaml                   # Unified skill bundle manifest
├── SOURCE-REPOS.md               # Source repository mapping
├── .gitignore
├── .codex-plugin/
│   └── plugin.json               # Codex plugin manifest
├── .github/workflows/
│   └── validate.yml              # CI validation pipeline
│
├── skills/                       # All agent skills (54 total)
│   ├── agent-skills/             # 6 core agent skills (library)
│   │   ├── composio-cli/
│   │   ├── design-taste-frontend/
│   │   ├── high-end-visual-design/
│   │   ├── redesign-existing-projects/
│   │   ├── solid/
│   │   └── tdd/
│   ├── mattpocock-skills/        # 37 Matt Pocock engineering skills
│   │   ├── engineering/          # 17 active engineering skills
│   │   ├── deprecated/           # 4 deprecated skills
│   │   ├── in-progress/          # 9 experimental skills
│   │   ├── misc/                 # 4 utility skills
│   │   ├── personal/             # 2 personal productivity skills
│   │   └── productivity/         # 5 workflow productivity skills
│   ├── suite-core/               # 6 suite orchestration skills
│   │   ├── agent-control-plane/
│   │   ├── artifact-production/
│   │   ├── conversation-compiler/
│   │   ├── engineering-orchestrator/
│   │   ├── implementation-council/
│   │   └── local-memory/
│   ├── engineering/              # 6 engineering quality skills
│   │   ├── engineering-quality-gates/
│   │   ├── engineering-standards-orchestrator/
│   │   ├── loop-engineering/
│   │   ├── solid-code-design/
│   │   ├── tdd-workflow/
│   │   └── specialists/
│   │       └── precision-workflow/
│   ├── design/                   # 2 design system skills
│   │   ├── amazon-ad-console-redesign/
│   │   └── design-system-master/
│   ├── bootstrap/                # 1 project bootstrap skill
│   │   └── SKILL.md
│
├── integrations/                 # Agent integrations (from engineering-standards)
│   ├── README.md
│   ├── claude/                   # Claude Code agents + rules
│   ├── cursor/                   # Cursor agents + rules
│   └── openai/                   # OpenAI agent configs
│
├── adapters/                     # Agent platform adapters (from agent-skill-suite)
│   ├── claude-code/
│   ├── gemini-cli/
│   └── github-copilot/
│
├── plugins/                      # External plugins (from agent-skills-library)
│   ├── chromium-browser/
│   └── ponytail/
│
├── cli-tools/                    # CLI tool configurations
├── mcp-servers/                  # MCP server configurations
├── schemas/                      # JSON schemas
│   └── handoff.schema.json
├── scripts/                      # Validation & tooling
│   ├── validate_suite.py         # Suite validation
│   └── validate.py               # Design skill validation
├── docs/                         # Documentation
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   ├── SKILL-CATALOG.md
│   └── guides/
│       └── QUICKSTART.md
└── references/                   # Bootstrap templates (from project-bootstrap-full)
```

---

## Skills by Category

### 🎯 Agent Skills (6)
From `agent-skills-library` — foundational skills used by all Omnibot agents.

| Skill | What It Does |
|-------|-------------|
| `composio-cli` | Composio tool management |
| `design-taste-frontend` | Anti-slop frontend with 3-dial system (variance, motion, density) |
| `high-end-visual-design` | Awwwards-tier agency aesthetics with double-bezel architecture |
| `redesign-existing-projects` | Upgrade existing UIs to premium quality |
| `solid` | SOLID principles & clean code design |
| `tdd` | Test-driven development workflow |

### 🧠 Matt Pocock Engineering Skills (37)
From `agent-skills-library` (mattpocock-skills) — engineering skills organized into 6 sub-categories.

| Sub-category | Count | Key Skills |
|---|---|---|
| **engineering** (active) | 17 | `ask-matt`, `code-review`, `implement`, `tdd`, `to-spec`, `to-tickets`, `grill-with-docs` |
| **in-progress** (experimental) | 9 | `claude-handoff`, `loop-me`, `wizard`, `writing-beats` |
| **misc** | 4 | `git-guardrails-claude-code`, `setup-pre-commit`, `scaffold-exercises` |
| **productivity** | 5 | `grill-me`, `handoff`, `teach`, `writing-great-skills` |
| **personal** | 2 | `edit-article`, `obsidian-vault` |
| **deprecated** | 4 | `design-an-interface`, `qa`, `request-refactor-plan`, `ubiquitous-language` |

### ⚙️ Suite Core Skills (6)
From `agent-skill-suite` — portable operating system for AI agents.

| Skill | What It Does |
|-------|-------------|
| `agent-control-plane` | Maintain workspaces, permissions, commands, state, logs, and failure recovery |
| `artifact-production` | Create, render, version, and verify professional artifacts |
| `conversation-compiler` | Convert raw conversations and notes into governed execution packages |
| `engineering-orchestrator` | Coordinate software work through architecture, TDD, loops, and gates |
| `implementation-council` | Pressure-test plans, code, migrations, and releases through expert debate |
| `local-memory` | Capture, retrieve, curate, and forget durable local agent memory |

### 🔧 Engineering Standards Skills (6)
From `engineering-standards` — quality gates and engineering discipline.

| Skill | What It Does |
|-------|-------------|
| `engineering-quality-gates` | Return PASS or BLOCKED from required engineering evidence |
| `engineering-standards-orchestrator` | Orchestrates all 5 engineering standards skills |
| `loop-engineering` | Control iteration size, evidence, observation, and adjustment |
| `solid-code-design` | Define proportionate responsibilities, contracts, extension seams |
| `tdd-workflow` | Prove one behavior through a valid Red-Green-Refactor cycle |
| `specialists/precision-workflow` | Long-task execution, memory, safety, and artifact production |

### 🎨 Design Skills (2)
From `design-skill-pack` — opinionated design systems for premium UIs.

| Skill | What It Does |
|-------|-------------|
| `design-system-master` | Master orchestrator — auto-selects the right design skill combination |
| `amazon-ad-console-redesign` | Redesign guidance for Amazon ad console projects |

> **Note:** The full Design Skill Pack includes 23 design skills. The 2 here are the curated core set. See [docs/SKILL-CATALOG.md](docs/SKILL-CATALOG.md) for the complete design catalog from the source pack.

### 🚀 Bootstrap Skills (1)
From `project-bootstrap-full` — complete project foundation scaffolding.

| Skill | What It Does |
|-------|-------------|
| `project-bootstrap-full` | Create a complete project foundation with SOLID architecture, TDD protocols, documentation suite, data logic wireframes, and scaffold |

---

## Integrations

Agent integrations for running skills across platforms:

| Platform | Location | Description |
|----------|----------|-------------|
| Claude Code | `integrations/claude/` | Claude agents + CLAUDE.md |
| Cursor | `integrations/cursor/` | Cursor agents + rules (.mdc, .md) |
| OpenAI | `integrations/openai/` | OpenAI agent configs (.yaml) |

## Adapters

Platform-specific adapters for skill portability:

| Adapter | Description |
|---------|-------------|
| `claude-code` | Claude Code integration |
| `gemini-cli` | Gemini CLI integration |
| `github-copilot` | GitHub Copilot integration |

## Plugins

External plugin integrations:

| Plugin | Description | Source |
|--------|-------------|--------|
| `ponytail` | Lazy senior dev mode (YAGNI, stdlib first) | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) |
| `chromium-browser` | Browser automation via Chrome extension | opencode-chromium-browser-plugin |

---

## Validation

### Suite Validation (`scripts/validate_suite.py`)
Validates the bundle structure, skill definitions, installation order, and schema compliance.

```bash
python3 scripts/validate_suite.py              # Full validation
python3 scripts/validate_suite.py --install    # Validate + install
python3 scripts/validate_suite.py --category engineering  # Category-only
```

### Design Validation (`scripts/validate.py`)
Validates design skills against the format specification (frontmatter, sections, quality gates).

```bash
python3 scripts/validate.py                    # Validate all design skills
python3 scripts/validate.py --verbose         # Show details
```

### CI Pipeline
GitHub Actions automatically runs validation on every push and PR:

```bash
# .github/workflows/validate.yml runs:
python3 scripts/validate_suite.py
python3 scripts/validate.py
```

---

## Bundle Manifest

The unified `bundle.yaml` declares the full skill catalog with install order and responsibilities. It extends the original `agent-skill-suite` bundle to include engineering, design, and bootstrap skills:

```bash
# View the full bundle
cat bundle.yaml
```

---

## Source Repositories

This framework consolidates content from 5 source repositories. See [SOURCE-REPOS.md](SOURCE-REPOS.md) for the complete mapping of every skill to its origin.

1. **agent-skills-library** — `projectamazonph/agent-skills-library`
2. **agent-skill-suite** — `projectamazonph/agent-skill-suite`
3. **engineering-standards** — `projectamazonph/engineering-standards`
4. **design-skill-pack** — `projectamazonph/design-skill-pack`
5. **project-bootstrap-full** — `projectamazonph/project-bootstrap-full`

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Key points:

- Each skill is a self-contained directory with `SKILL.md`
- Use the validation scripts before submitting changes
- Follow the `bundle.yaml` install_order for new skills
- Add agent integrations in `integrations/<platform>/`

---

## License

MIT — use freely, attribute appreciated.

---

*This is a combined work of 5 source repositories. Individual skill files retain their original headers and attribution where present.*
