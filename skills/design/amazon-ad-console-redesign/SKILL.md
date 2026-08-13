---
name: amazon-ad-console-redesign
description: Complete premium redesign of the Amazon Ad Console Training Simulator using the Design Skill Pack. Applies high-end-visual-design + premium + editorial + beautiful-shadows + staggered-word-reveal.
---

# Amazon Ad Console — Redesign Specification

## Design Read
> **"Reading this as: B2B SaaS training dashboard for ad operations teams, with a premium/minimalist language leaning toward Apple-inspired precision + Amazon's brand warmth (orange accent on light canvas)."**

## Dials
- `DESIGN_VARIANCE: 6` — Clean, structured, but with premium touches
- `MOTION_INTENSITY: 5` — Subtle, purposeful motion
- `VISUAL_DENSITY: 5` — Data-dense but breathable

## Core Design Tokens
```css
:root {
  /* Surfaces — Warm light canvas */
  --surface-0: #f5f6f6;
  --surface-1: #ffffff;
  --surface-2: #f8f9fa;
  --surface-raised: #ffffff;
  --surface-3: #232f3e;
  --surface-4: #1a252f;
  
  /* Ink — High contrast */
  --ink-900: #0f1111;
  --ink-800: #1a1c1e;
  --ink-700: #3d464d;
  --ink-500: #6b7278;
  --ink-300: #c4c9cc;
  --ink-inverse: #ffffff;
  
  /* Border — Refined hairlines */
  --border: #d5d9d9;
  --border-light: #e8eaeb;
  --border-focus: #007185;
  
  /* Brand — Amazon orange */
  --accent: #ff9900;
  --accent-hover: #e68a00;
  --accent-active: #cc7a00;
  --accent-soft: #fff8e6;
  
  /* Semantic */
  --success: #067d62;
  --warning: #b45309;
  --danger: #c40000;
  --info: #007185;
  
  /* Typography — Premium */
  --font-display: 'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-body: 'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'Geist Mono', 'SF Mono', 'Fira Code', monospace;
  
  /* Radius — Squircle-inspired */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-2xl: 20px;
  
  /* Shadows — Beautiful-shadows layered */
  --shadow-sm: 0px 2px 3px -1px rgba(0,0,0,0.1),0px 1px 0px 0px rgba(25,28,33,0.02),0px 0px 0px 1px rgba(25,28,33,0.08);
  --shadow-md: 0px 0px 0px 1px rgba(0,0,0,0.06),0px 1px 1px -0.5px rgba(0,0,0,0.06),0px 3px 3px -1.5px rgba(0,0,0,0.06),0px 6px 6px -3px rgba(0,0,0,0.06),0px 12px 12px -6px rgba(0,0,0,0.06),0px 24px 24px -12px rgba(0,0,0,0.06);
  --shadow-lg: 0 2.8px 2.2px rgba(0,0,0,0.034),0 6.7px 5.3px rgba(0,0,0,0.048),0 12.5px 10px rgba(0,0,0,0.06),0 22.3px 17.9px rgba(0,0,0,0.072),0 41.8px 33.4px rgba(0,0,0,0.086),0 100px 80px rgba(0,0,0,0.12);
  
  /* Motion */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --duration-fast: 120ms;
  --duration-base: 200ms;
  --duration-slow: 400ms;
}
```

## Layout Architecture

### Global Nav (Top Bar)
- Dark slate (`--surface-3`) with Amazon branding
- Fixed height 52px
- Left: hamburger (mobile) + brand
- Center: section nav (campaigns, portfolio, dashboard)
- Right: sync, user menu, create campaign button
- Bottom border: hairline 1px solid `--surface-4`

### Sidebar (Left Rail)
- Width: 240px on desktop, 220px on tablet
- Background: `--surface-1`
- Border-right: 1px solid `--border-light`
- Section group titles with subtle uppercase labels
- Items with active state using `--accent` left border indicator
- Bottom: simulation controls with `--ink-500`

### Content Area
- Background: `--surface-0`
- Padding: 24px (desktop), 16px (mobile)
- Max-width: 1440px

### KPI Tiles (Dashboard)
- Use beautiful-shadows `--shadow-md`
- Background: `--surface-raised`
- Border-radius: `--radius-lg`
- 3x3 grid on desktop, 2x2 on tablet, 1x1 on mobile
- Value in large semibold, label in --ink-500
- Subtle border: 1px solid `--border-light`

### Cards
- Background: `--surface-1`
- Beautiful-shadows `--shadow-md`
- Border-radius: `--radius-lg`  
- Padding: 20px
- Subtle border: 1px solid `--border-light`

### Buttons
- Primary: `--accent` background, `--ink-900` text
- Hover: `--accent-hover`
- Active: scale(0.98) for physical press feel
- Border-radius: `--radius-md`
- Transition: all `--duration-fast` `--ease-out`

### Tables
- Header: `--surface-2` background, semibold
- Row hover: `--accent-soft` background
- Border: 1px solid `--border-light`
- Pill badges for statuses

### Tabs
- Active: bottom border 2px solid `--accent`
- Hover: `--surface-2` background
- Font: medium weight

## Component-Specific Guidelines

### Landing Page
- Hero: Dark background (`zinc-950`) transitioning to warm light
- CTA buttons: Pill-shaped (`rounded-full`) with beautiful-shadows
- Feature grid: Premium cards with nested architecture
- Motion: staggered-word-reveal on headline, animation-on-scroll on sections

### Campaign Wizard
- Multi-step with progress indicator
- Card-style step panels with beautiful-shadows
- Choice grid for ad type selection
- Form fields with proper label placement

### Mobile Responsive
- Hamburger drawer navigation
- Single-column layout
- Touch targets ≥ 44px
- Bottom sheet for filters

## Motion Guidelines
- Entry: fade-up with translate-y-8 and blur-sm → translate-y-0 blur-0
- Duration: 600ms
- Ease: cubic-bezier(0.16, 1, 0.3, 1)
- Stagger: 80ms between elements
- Buttons: scale(0.98) on active
- Cards: subtle lift on hover (translateY(-2px))
- Never animate: top, left, width, height
- Respect prefers-reduced-motion

## Implementation Order
1. Global CSS tokens (update globals.css)
2. Landing page redesign
3. App layout (Topbar, Sidebar, content area)
4. Dashboard KPI tiles
5. Campaign manager cards
6. Campaign detail tabs
7. Mobile navigation
8. Motion and animation
