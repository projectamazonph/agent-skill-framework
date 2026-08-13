# Contributing

## How to Add a New Skill

### 1. Create the skill file

```
skills/your-skill-name.md
```

With YAML frontmatter:
```markdown
---
name: your-skill-name
description: One-line description of what this skill does
---
```

### 2. Structure your content

Every design skill should include these sections in order:

```markdown
## Design Tokens
```css
:root { /* colors, typography, spacing, shadows, motion */ }
```

## Anti-Patterns
- What to avoid
- Specific banned values (fonts, colors, shadows, layouts)

## Layout Archetypes
- Pattern name + description
- Mobile collapse behavior (required: <768px)

## Component Rules
- Anatomy, states (default, hover, focus-visible, active, disabled)
- Spacing, typography, color tokens used

## Motion Guidelines
- Entry/exit animation specs
- Easing curves (custom cubic-bezier, not linear/ease-in-out)
- Reduced-motion fallback

## Quality Gates
- [ ] Testable acceptance criteria
- [ ] Accessibility checks (WCAG 2.2 AA)
```

### 3. Update the catalog

Add your skill to `docs/SKILL-CATALOG.md` with:
- Name, type, description
- Key features, tokens, fonts
- Anti-patterns
- Source reference (if adapted from elsewhere)

### 4. Validate

```bash
python3 scripts/validate.py
```

## Skill Quality Standards

| Criterion | Required |
|-----------|----------|
| YAML frontmatter with `name` + `description` | ✅ |
| Anti-patterns section with specific banned values | ✅ |
| CSS custom property tokens | ✅ |
| Mobile responsive rules (<768px collapse) | ✅ |
| Reduced-motion fallback (`prefers-reduced-motion`) | ✅ |
| Quality gate checklist | ✅ |
| Implementation-ready examples | ✅ |
| Agent-agnostic (no platform-specific references) | ✅ |

## Code Review Checklist

- [ ] Skill has unique `name` (no conflicts with existing skills)
- [ ] No placeholder or TODO content
- [ ] Anti-patterns are specific (not generic like "make it look good")
- [ ] Tokens use CSS custom properties (`--var-name`)
- [ ] Mobile responsive behavior explicitly defined
- [ ] Reduced-motion alternatives provided
- [ ] No platform-specific tooling references
- [ ] Validation passes
