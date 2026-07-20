---
name: Fasolaki Core
colors:
  surface: '#051424'
  surface-dim: '#051424'
  surface-bright: '#2c3a4c'
  surface-container-lowest: '#010f1f'
  surface-container-low: '#0d1c2d'
  surface-container: '#122131'
  surface-container-high: '#1c2b3c'
  surface-container-highest: '#273647'
  on-surface: '#d4e4fa'
  on-surface-variant: '#bcc9cd'
  inverse-surface: '#d4e4fa'
  inverse-on-surface: '#233143'
  outline: '#869397'
  outline-variant: '#3d494c'
  surface-tint: '#4cd7f6'
  primary: '#4cd7f6'
  on-primary: '#003640'
  primary-container: '#06b6d4'
  on-primary-container: '#00424f'
  inverse-primary: '#00687a'
  secondary: '#bec6e0'
  on-secondary: '#283044'
  secondary-container: '#3f465c'
  on-secondary-container: '#adb4ce'
  tertiary: '#bcc7de'
  on-tertiary: '#263143'
  tertiary-container: '#9ca7be'
  on-tertiary-container: '#313c4f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#acedff'
  primary-fixed-dim: '#4cd7f6'
  on-primary-fixed: '#001f26'
  on-primary-fixed-variant: '#004e5c'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#d8e3fb'
  tertiary-fixed-dim: '#bcc7de'
  on-tertiary-fixed: '#111c2d'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#051424'
  on-background: '#d4e4fa'
  surface-variant: '#273647'
typography:
  display-lg:
    fontFamily: Outfit
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Outfit
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Outfit
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  mono:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

The design system is engineered for high-performance reading and technical clarity. It adopts a **Corporate Modern** style infused with **Glassmorphism** and **Minimalist** traits to create a "Developer-First" editorial experience. The brand personality is clinical, efficient, and forward-leaning, prioritizing information density without sacrificing aesthetic precision.

The emotional response should be one of "Technical Authority"—the user should feel they are interacting with a highly tuned instrument. Visual interest is generated through light refraction, subtle gradients, and rigorous alignment rather than decorative flourishes.

## Colors

The palette is strictly cool-toned to maintain a focused, high-tech atmosphere. 

- **Primary (#06B6D4):** A bright cyan used exclusively for calls to action, active states, and critical highlights. It represents "the spark" of data within the system.
- **Surface Deep (#0F172A):** The foundational background color, providing a low-strain environment for long-form reading.
- **Surface Elevated (#1E293B):** Used for cards, navigation bars, and structural elements to create depth.
- **Neutral (#94A3B8):** A slate gray utilized for secondary text and borders, ensuring high legibility against the dark backgrounds.

## Typography

This design system utilizes a dual-sans-serif approach to balance impact with utility. 

**Outfit** is used for headlines and display text. Its geometric construction conveys a modern, tech-forward vibe. **Geist** is employed for body copy, labels, and UI elements; its monospaced-influenced proportions and clear terminals provide the "clinical" and "developer-friendly" legibility required for technical blogging. 

Maintain strict hierarchy by using the `label-sm` for categories and metadata, and ensure code blocks utilize the `mono` scale with a slightly reduced opacity for non-critical syntax.

## Layout & Spacing

The layout follows a **Fluid Grid** model with a maximum container width to prevent line lengths from becoming unreadable on ultra-wide displays. 

- **Desktop (1280px+):** 12-column grid, 24px gutters, 80px side margins.
- **Tablet (768px - 1279px):** 8-column grid, 24px gutters, 40px side margins.
- **Mobile (<767px):** 4-column grid, 16px gutters, 16px side margins.

A 4px baseline grid governs all vertical rhythm. Use `lg` (40px) spacing between major sections and `sm` (16px) for internal component padding. Content should be centered with ample whitespace to emphasize the minimalist, "utility-first" aesthetic.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Glassmorphism**, rather than traditional heavy shadows. 

1. **Base:** `#0F172A` (The canvas).
2. **Surface:** `#1E293B` (Cards and sidebar).
3. **Overlay:** A semi-transparent `#1E293B` (80% opacity) with a `20px` backdrop blur for navigation headers and modals.
4. **Accents:** High-frequency elements (buttons/active tags) use a "Micro-shadow": `0px 2px 4px rgba(0, 0, 0, 0.4)` combined with a subtle `1px` inner-stroke of `#ffffff10` to simulate a precision-milled edge.

Borders should be used sparingly, primarily in a low-contrast `#FFFFFF10` (10% white) to define boundaries without breaking the visual flow.

## Shapes

To maintain the "clinical" and "efficient" brand personality, the design system utilizes **Soft** roundedness. 

- **Standard Elements (Buttons, Inputs):** 4px (`0.25rem`) corner radius. This conveys precision and sits between the aggression of sharp corners and the playfulness of fully rounded ones.
- **Containers (Cards, Modals):** 8px (`0.5rem`) corner radius.
- **Iconography:** Use linear, 2px stroke-width icons with slight rounding to match the UI components.

## Components

### Buttons
Primary buttons use the Cyan accent with `#0F172A` text. Secondary buttons use a "Ghost" style: a `1px` border of `#FFFFFF20` and transparent background, shifting to a solid `#1E293B` on hover.

### Cards
Cards are flat `#1E293B` surfaces. On hover, they should translate `-2px` vertically and gain a thin `#06B6D4` top-border (2px) to indicate interactivity.

### Input Fields
Inputs are dark-themed with a `#0F172A` fill and `#FFFFFF10` border. On focus, the border transitions to Cyan with a subtle outer glow (Cyan at 20% opacity).

### Chips & Tags
Metadata tags use a "monochrome-plus" approach: `#1E293B` background with `label-sm` typography. The active category tag should use a subtle Cyan glow for the text.

### Progress & Loading
Use thin, 2px horizontal bars for loading states. Use the Primary Cyan color with a pulse animation to maintain the high-tech feel.

### Code Blocks
Essential for a tech blog, code blocks should feature a `#0B1120` background, 1px border, and a "Copy" button that only appears on hover to reduce visual noise.