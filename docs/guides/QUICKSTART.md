# Quick Start Guide

## One-Time Setup

Clone or copy the pack into your project:

```bash
git clone <repo-url> design-skill-pack
# Or just copy the skills/ directory into your project
cp -r design-skill-pack/skills/ my-project/skills/
```

## Invoke a Skill

Tell your AI agent to load a skill file and apply it:

**Examples:**

```
Read skills/premium.md and apply its design system to my project.
```

```
Read skills/hallmark.md. Do a hallmark redesign of src/app/landing/page.tsx — audit, pick a theme, restructure the visual layer.
```

```
Read skills/design-system-master.md and recommend the right design direction for my SaaS dashboard.
```

## Common Workflows

### 1. Redesign an Existing Page
Tell your agent:
```
Read skills/hallmark.md. Redesign src/app/landing/page.tsx:
- Audit the current design
- Pick one of the 20 themes
- Restructure the visual layer
- Apply tokens, layout, motion
- QA against the checklist
```

### 2. Add Premium Polish
```
Read skills/premium.md. Apply premium design tokens to the entire app:
- Update CSS custom properties
- Refine spacing and typography
- Apply beautiful-shadows to cards and panels
- Add smooth transitions with custom easings
```

### 3. Build a Landing Page from Scratch
```
Read skills/design-system-master.md and skills/landing-page.md.
Follow the orchestrator to pick the right aesthetic, then use landing-page.md for structure.
```

### 4. Design a Pricing Page
```
Read skills/pricing-page.md for the structure and conversion patterns.
Read skills/premium.md for the visual design tokens.
```

### 5. Audit Design Quality
```
Read skills/styleseed-design-review.md.
Review my UI components against its criteria and return a punch list.
```

### 6. Study an Existing Design
If you have the hallmark skill:
```
Read skills/hallmark.md and use its 'study' mode on this URL: https://example.com
Extract the design DNA — macrostructure, archetypes, type pairing, color anchor.
```

## Agent-Specific Tips

### Claude
Claude excels at following structured Markdown instructions. Reference the skill file explicitly:
```
Attached is skills/premium.md. Read it fully and apply every section in order.
```

### ChatGPT / GPT
GPT works well with sequential instructions. Paste skill content or reference a file:
```
I'm sharing a design skill file. Read it and apply the design system to my project step by step.
```

### Copilot / Cursor
Use the workspace context:
```
@workspace Read skills/design-system-master.md and tell me which skill to use for my project.
Then read that skill and apply it.
```

## Tips

- **Combine skills**: Layer utility skills (beautiful-shadows, staggered-word-reveal) on top of design system skills (premium, editorial)
- **Use the orchestrator**: When unsure, `design-system-master` is the safest starting point
- **Override dials**: For `design-taste-frontend` skills, set explicit DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY values
- **Quality gates**: Always ask the agent to run the QA checklist at the end
