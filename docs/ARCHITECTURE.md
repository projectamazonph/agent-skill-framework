# Architecture

## Overview

The Design Skill Pack is a portable collection of standalone Markdown files. Each file encodes a complete design system as **structured, opinionated instructions** that any AI agent can follow. There is no runtime, no dependencies, no special tooling — just Markdown.

```
design-skill-pack/
├── skills/                   # Individual *.md skill files
│   ├── design-system-master.md
│   └── amazon-ad-console-redesign.md
├── docs/                     # Documentation
│   ├── SKILL-CATALOG.md
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   └── guides/
├── scripts/validate.py       # Validation (optional, Python 3)
└── README.md                 # Entry point
```

## Skill File Format

Every skill file must have YAML frontmatter:

```markdown
---
name: <skill-name>              # Slug used to reference this skill (required)
description: <one-liner>        # What this skill does (required)
---
```

### Required Sections

A complete design skill must contain these sections in order:

**1. Design Tokens**
CSS custom properties defining the entire visual language:
```css
:root {
  --surface-0: #...;
  --ink-900: #...;
  --accent: #...;
  --font-display: '...', sans-serif;
  --radius-md: 8px;
  --shadow-md: ...;
  --ease-out: cubic-bezier(...);
}
```

**2. Anti-Patterns**
Explicit list of what NOT to do — specific banned fonts, colors, shadows, layouts, and motion patterns.

**3. Layout Archetypes**
Structural patterns with mobile collapse behavior:
- Asymmetrical Bento / Z-Axis Cascade / Editorial Split
- Mobile: collapses to single-column below 768px

**4. Component Rules**
For each key component: anatomy, variants, required states (default, hover, focus-visible, active, disabled, loading, error), responsive behavior.

**5. Motion Guidelines**
- Entry/exit animation specs (duration, easing, stagger)
- GPU-safe properties only (`transform`, `opacity`)
- `prefers-reduced-motion` fallback

**6. Quality Gates**
Testable acceptance criteria as a checklist:
- [ ] No banned fonts present
- [ ] All transitions use custom cubic-bezier
- [ ] Mobile layout collapses below 768px
- [ ] Reduced motion respected

## Orchestrator Pattern

`design-system-master.md` is a meta-skill. It doesn't design anything itself — it reads project context and dispatches to the appropriate skill(s) via a selection matrix:

| Project Type | Recommended Skill |
|-------------|------------------|
| SaaS / Dashboard | premium, beautiful-shadows |
| Landing Page | hallmark or design-taste-frontend |
| Agency Portfolio | high-end-visual-design |
| Editorial / Blog | editorial or modern |
| E-commerce | professional |
| Full Redesign | redesign-existing-projects + hallmark |

## Execution Flow

```
1. Agent reads the skill file (Markdown)
2. Agent applies CSS tokens to :root
3. Agent structures layout per archetype
4. Agent builds components per rules
5. Agent adds motion per guidelines
6. Agent verifies against quality gates
```

That's it. No framework, no runtime, no plugin system required.

## File Independence

Each skill file is **fully self-contained**. An agent can read a single file and execute it without needing any other file in the pack. This means you can:

- Copy individual skills into other projects
- Use skills offline
- Share skills with other teams
- Version skills independently

## Validation

The optional `scripts/validate.py` script checks:
- YAML frontmatter has `name` and `description`
- Skills directory has `.md` files
- All required docs exist

No package.json, no npm install, no dependencies.
