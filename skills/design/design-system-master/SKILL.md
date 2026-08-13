---
name: design-system-master
description: Master design system orchestrator — selects, combines, and applies the right design skills from the pack based on the project context. Coordinates 20+ design skills into a coherent output.
---

# Design System Master (Orchestrator Skill)

## Overview
This skill orchestrates the entire Design Skill Pack. It reads the project context, selects the appropriate design direction from the available skills, and applies them in the right order.

## Skill Selection Matrix

### Project Type → Primary Skills
| Project Type | Primary Skill | Secondary Skills |
|---|---|---|
| **SaaS App / Dashboard** | `premium` | `beautiful-shadows`, `animation-on-scroll`, `design-taste-frontend` |
| **Landing Page** | `hallmark` or `design-taste-frontend` | `landing-page`, `staggered-word-reveal`, `animation-on-scroll` |
| **Marketing Site** | `hallmark` | `pricing-page`, `staggered-word-reveal`, `beautiful-shadows` |
| **Agency Portfolio** | `high-end-visual-design` | `staggered-word-reveal`, `split-layout-technical`, `animation-on-scroll` |
| **Editorial / Blog** | `editorial` or `modern` | `staggered-word-reveal`, `animation-on-scroll` |
| **E-commerce** | `professional` | `beautiful-shadows`, `glassmorphism` |
| **Mobile App UI** | `sleek` | `animation-on-scroll`, `beautiful-shadows` |
| **Design System Docs** | `refined` or `premium` | `split-layout-technical`, `design-first-ui-prompting` |
| **Pricing Page** | `pricing-page` | `hallmark`, `beautiful-shadows`, `animation-on-scroll` |
| **Full Redesign** | `redesign-existing-projects` + `hallmark redesign` | `high-end-visual-design`, `design-taste-frontend` |

### Mood/Aesthetic → Skill
| Desired Mood | Skill to Use |
|---|---|
| Apple-inspired, premium | `premium` |
| Anti-AI-slop, structured | `hallmark` |
| Awwwards-tier, experimental | `high-end-visual-design` |
| Warm, beige, calm | `clean-minimal-beige-light-mode` |
| Magazine, editorial | `editorial` |
| Frosted glass, depth | `glassmorphism` |
| Bold, high-contrast | `neobrutalism` |
| Minimalist, clean | `minimal` or `sleek` |
| Technical, split-screen | `split-layout-technical` |
| Modern, contemporary | `modern` |
| Polished, business | `professional` |
| Understated, refined | `refined` |
| Agency nested shells | `nested-container-clean-agency` |
| Warm, poster-like | `impeccable` |

## Workflow

### Phase 1: Discovery
1. Identify project type from the prompt
2. Identify desired mood/aesthetic (or infer from context)
3. Select primary + secondary skills from the matrix above
4. Load the selected skill's SKILL.md

### Phase 2: Design Read (from design-taste-frontend)
Before any code, state:
> **"Reading this as: [page kind] for [audience], with a [vibe] language, leaning toward [design system or aesthetic]."**

### Phase 3: Configure Three Dials
Set: `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY` (1-10)
See design-taste-frontend for baseline values.

### Phase 4: Apply Design Tokens
Use the selected skill's token system. Common token structure:
```css
:root {
  --surface-0: #f5f6f6;
  --surface-1: #ffffff;
  --ink-900: #0f1111;
  --accent: #ff9900;
  --radius-md: 8px;
  --shadow-sm: ...
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Phase 5: Layout & Component Architecture
Apply the selected layout archetype:
- **Asymmetrical Bento** (high-end-visual-design)
- **Z-Axis Cascade** (high-end-visual-design)
- **Editorial Split** (high-end-visual-design / split-layout-technical)
- **Double-Bezel Nested** (high-end-visual-design / nested-container-clean-agency)
- **Fluid Island Nav** (high-end-visual-design)
- **Editorial Grid** (editorial / modern)
- **Minimal Single-Column** (minimal / sleek)

### Phase 6: Motion & Animation
- Apply `staggered-word-reveal` for headings
- Apply `animation-on-scroll` for section entries
- Apply custom cubic-bezier curves (not linear/ease-in-out)
- Use `transform` and `opacity` only (GPU-safe)

### Phase 7: Shadows & Depth
Apply `beautiful-shadows` utilities for cards, panels, and surfaces.

### Phase 8: QA Checklist
- [ ] No banned fonts (Inter, Roboto, Arial, Open Sans, Helvetica for premium)
- [ ] No generic shadows (`shadow-md`, `rgba(0,0,0,0.3)`)
- [ ] No default transitions (`linear`, `ease-in-out`)
- [ ] All surfaces use proper elevation tokens
- [ ] Responsive: mobile-first, collapses below 768px
- [ ] Motion uses GPU-safe properties only
- [ ] WCAG 2.2 AA contrast
- [ ] Reduced motion respected
- [ ] Touch targets ≥ 44px on mobile
- [ ] Layout has structural variety (not 3-column default grid)
