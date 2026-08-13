# Design Skill Catalog

Complete catalog of all skills in the Design Skill Pack.

---

## Core Design Skills

### 1. hallmark
- **Type:** Universal design skill
- **Invocations:** `hallmark`, `hallmark audit <target>`, `hallmark redesign <target>`, `hallmark study <URL|screenshot>`
- **Description:** Anti-AI-slop design with 20 named themes, structural variety, audit/redesign/study verbs
- **Key Features:** 20 named themes, macrostructure variety, design DNA extraction, URL study mode
- **Anti-Patterns:** Template rhythm, symmetrical grids, AI-purple gradients
- **Source:** `/root/.shared-skills/hallmark/`

### 2. high-end-visual-design
- **Type:** Premium agency skill
- **Description:** Awwwards-tier agency aesthetics with double-bezel nested architecture, fluid motion, variance engine
- **Key Features:** Double-bezel (Doppelrand) architecture, fluid island nav, magnetic button physics, scroll interpolation, 3 vibe + 3 layout archetypes
- **Banned:** Inter, Roboto, Arial, standard shadows, generic icons
- **Mobile:** Aggressive collapse to single-column below 768px
- **Source:** `/root/.agents/skills/high-end-visual-design/`

### 3. premium
- **Type:** Design system skill (Universal)
- **Description:** Apple-inspired precise spacing, modern typography, refined polished visual language
- **Tokens:** primary=#3B82F6, secondary=#8B5CF6
- **Fonts:** Inter (display), JetBrains Mono (code)
- **Source:** `/root/.shared-skills/premium/`

### 4. editorial
- **Type:** Design system skill (Universal)
- **Description:** Magazine-inspired editorial layout with refined serif typography, structured grids
- **Fonts:** Gelasio (primary), Ubuntu Mono (code)
- **Spacing:** 8pt baseline grid
- **Source:** `/root/.shared-skills/editorial/`

### 5. sleek
- **Type:** Design system skill (Universal)
- **Description:** Modern minimalist with clean lines, intentional color palette, subtle interactions
- **Style:** Less is more, 60-30-10 color rule
- **Spacing:** 8pt baseline grid
- **Source:** `/root/.shared-skills/sleek/`

### 6. modern
- **Type:** Design system skill (Universal)
- **Description:** Contemporary editorial style with serif typography, minimal palettes
- **Fonts:** IBM Plex Serif (primary/display)
- **Source:** `/root/.shared-skills/modern/`

### 7. minimal
- **Type:** Design system skill (Universal)
- **Description:** Stripped-back design emphasizing whitespace, clean typography, restrained color
- **Colors:** primary=#0C0C09, surface=#F4F4F1
- **Fonts:** Open Sans (primary), Inter (display)
- **Source:** `/root/.shared-skills/minimal/`

### 8. professional
- **Type:** Design system skill (Universal)
- **Description:** Polished, business-ready design with modern typography, structured layouts
- **Colors:** primary=#FECE14, secondary=#000000
- **Fonts:** Poppins (primary/display), IBM Plex Mono (code)
- **Source:** `/root/.shared-skills/professional/`

### 9. refined
- **Type:** Design system skill (Universal)
- **Description:** Carefully curated, modern minimal style with elegant serif typography
- **Fonts:** Playfair Display (primary/display)
- **Source:** `/root/.shared-skills/refined/`

### 10. neobrutalism
- **Type:** Design system skill (Universal)
- **Description:** Modern take on brutalism with bold borders, vivid accent colors, raw high-contrast layouts
- **Colors:** primary=#FDC800, secondary=#432DD7, surface=#FBFBF9
- **Fonts:** Inter (primary/display)
- **Source:** `/root/.shared-skills/neobrutalism/`

### 11. glassmorphism
- **Type:** Design system skill (Universal)
- **Description:** Frosted glass with translucent layers, subtle blur, luminous borders
- **Colors:** primary=#1856FF, secondary=#3A344E
- **Fonts:** Plus Jakarta Sans (primary/display)
- **Style:** Bento cards, liquid glass effect
- **Source:** `/root/.shared-skills/glassmorphism/`

### 12. impeccable
- **Type:** Design system skill (Universal)
- **Description:** Modern graphic editorial-poster aesthetic, warm and confident, alternating cream and burnt orange
- **Colors:** primary=#CC8800, secondary=#C55221
- **Fonts:** Chakra Petch (primary/display)
- **Source:** `/root/.shared-skills/impeccable/`

---

## Utility & Animation Skills

### 13. beautiful-shadows
- **Type:** Utility skill
- **Description:** Polished layered neutral elevation with exact Tailwind arbitrary shadow utilities
- **Tiers:** sm (compact cards), md (cards/panels), lg (hero/modal)
- **Source:** `/root/.shared-skills/beautiful-shadows/`

### 14. staggered-word-reveal
- **Type:** Animation skill
- **Description:** Editorial word-by-word text reveal using IntersectionObserver
- **Motion:** 0.8s duration, cubic-bezier(0.16, 1, 0.3, 1), 0.07s stagger
- **Source:** `/root/.shared-skills/staggered-word-reveal/`

### 15. animation-on-scroll
- **Type:** Animation skill
- **Description:** Scroll-triggered animation using IntersectionObserver with Tailwind classes
- **Source:** `/root/.shared-skills/animation-on-scroll/`

---

## Specialized Skills

### 16. landing-page
- **Type:** Conversion skill
- **Description:** High-converting landing page patterns — structure, layout, copywriting, SEO/AEO
- **Source:** `/root/.shared-skills/landing-page/`

### 17. pricing-page
- **Type:** Conversion skill
- **Description:** Pricing page structure, plan design, conversion optimization, FAQs
- **Source:** `/root/.shared-skills/pricing-page/`

### 18. design-taste-frontend
- **Type:** Design inference skill
- **Description:** Anti-slop frontend with 3-dial system (variance, motion, density), brief inference, pre-flight checks
- **Source:** `/root/.agents/skills/design-taste-frontend/`

### 19. redesign-existing-projects
- **Type:** Redesign skill
- **Description:** Upgrades existing websites to premium quality — audits, preserves functionality
- **Source:** System skill (shared)

### 20. styleseed-design-review
- **Type:** Review skill
- **Description:** AI-generated design detection, quality scoring, actionable fixes
- **Source:** `/root/.shared-skills/styleseed-design-review/`

---

## Theme Skills

### 21. clean-minimal-beige-light-mode
- **Type:** Theme skill
- **Description:** Warm neutral shells, quiet process grids, restrained accent, elegant low-contrast
- **Source:** `/root/.shared-skills/clean-minimal-beige-light-mode/`

### 22. nested-container-clean-agency
- **Type:** Theme skill
- **Description:** Agency nested containers, outer editorial shell, inset dark feature blocks
- **Source:** `/root/.shared-skills/nested-container-clean-agency/`

### 23. split-layout-technical
- **Type:** Layout skill
- **Description:** Technical split-screen with dual panels, fine frame lines, mono metadata
- **Source:** `/root/.shared-skills/split-layout-technical/`

---

## Orchestrator

### ∞. design-system-master
- **Type:** Orchestrator skill
- **Description:** Auto-selects the right skill combination based on project context
- **Matrix:** See SKILL.md for full selection matrix
- **Source:** `skills/design-system-master.md`
