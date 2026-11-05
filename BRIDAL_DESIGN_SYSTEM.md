# Bridal Pearson — Design System Handoff
**For use in: NextMove (career intelligence dashboard)**
**Source: bridalpearson.com / bridalpearson.github.io/index.html**
**Extracted: November 2026 — all values verified directly from source code**

---

## 1. Color System

### CSS Custom Properties (Design Tokens)

All colors are defined on `:root` in the global `<style>` block at the top of `index.html`.

```css
:root {
  /* Backgrounds — layered dark system */
  --bg:  #080a0f;   /* Page background — near-black with slight blue tint */
  --bg2: #0d1117;   /* Card / panel surface — 1 step lighter */
  --bg3: #111520;   /* Hover state surface, flip-card back, row hover */

  /* Borders */
  --border:        rgba(255, 255, 255, 0.07);   /* Default border — very subtle */
  --border-bright: rgba(255, 255, 255, 0.14);   /* Bright border — focus / hover */

  /* Text */
  --text:  #e8eaf0;   /* Primary text — near-white, slight blue cast */
  --text2: #8890a4;   /* Secondary text — mid grey-blue */
  --text3: #555d72;   /* Tertiary / muted — labels, metadata, timestamps */

  /* Accent colors */
  --accent:  #7c9fff;   /* Primary accent — cornflower blue (interactive, headings, highlights) */
  --accent2: #a78bfa;   /* Secondary accent — soft violet (italic subheads, tags) */
  --gold:    #c9a96e;   /* Gold — used for "featured" labels only */

  /* Glow */
  --glow: rgba(124, 159, 255, 0.15);   /* Box-shadow glow using accent */
}
```

### Computed RGB Values

| Token | Hex | RGB |
|-------|-----|-----|
| `--bg` | `#080a0f` | `8, 10, 15` |
| `--bg2` | `#0d1117` | `13, 17, 23` |
| `--bg3` | `#111520` | `17, 21, 32` |
| `--text` | `#e8eaf0` | `232, 234, 240` |
| `--text2` | `#8890a4` | `136, 144, 164` |
| `--text3` | `#555d72` | `85, 93, 114` |
| `--accent` | `#7c9fff` | `124, 159, 255` |
| `--accent2` | `#a78bfa` | `167, 139, 250` |
| `--gold` | `#c9a96e` | `201, 169, 110` |

### Derived / One-Off Colors

These appear inline (not as variables) — extract them into tokens for NextMove:

| Usage | Value |
|-------|-------|
| Nav scrolled background | `rgba(8, 10, 15, 0.88)` |
| Mobile menu background | `rgba(8, 10, 15, 0.97)` |
| `.btn-primary` hover bg | `#a3baff` (accent lightened ~15%) |
| Accent glow box-shadow | `0 8px 30px rgba(124, 159, 255, 0.3)` |
| Metric card hover shadow | `0 20px 40px rgba(124, 159, 255, 0.08)` |
| Company tag bg | `rgba(124, 159, 255, 0.08)` |
| Exp status badge bg | `rgba(124, 159, 255, 0.10)` |
| Beyond tag hover bg | `rgba(124, 159, 255, 0.05)` |
| Connect link hover bg | `rgba(124, 159, 255, 0.07)` |
| Grid lines (hero) | `rgba(255, 255, 255, 0.025)` |

### Gradients

```css
/* Progress bar + experiment card top border */
background: linear-gradient(90deg, var(--accent), var(--accent2));
/* = linear-gradient(90deg, #7c9fff, #a78bfa) */

/* Hero radial glows (decorative, behind content) */
background:
  radial-gradient(ellipse 80% 60% at 50% 0%,   rgba(124,159,255,0.08) 0%, transparent 60%),
  radial-gradient(ellipse 50% 40% at 80% 80%,  rgba(167,139,250,0.06) 0%, transparent 50%),
  radial-gradient(ellipse 40% 30% at 10% 60%,  rgba(201,169,110,0.04) 0%, transparent 50%);

/* Scroll indicator line */
background: linear-gradient(to bottom, var(--text3), transparent);
```

---

## 2. Typography

### Font Families

```css
--serif: 'Fraunces', Georgia, serif;
--sans:  'DM Sans', system-ui, sans-serif;
```

#### Loading (Google Fonts, `<head>`)

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap" rel="stylesheet" />
```

**Fraunces** — optical size variable serif. Loaded weights: 300, 400, 500 (upright); 300, 400 (italic). Used for all display headings, section titles, card titles, metric values.

**DM Sans** — geometric sans-serif. Loaded weights: 300, 400, 500 (upright); 300 (italic). Used for all body copy, navigation, buttons, tags, metadata.

### Type Scale (exact values from source)

| Role | Font | Size | Weight | Letter-spacing | Line-height | Color |
|------|------|------|--------|---------------|-------------|-------|
| Hero headline | Fraunces | `clamp(2.8rem, 6vw, 5.5rem)` | 300 | `-0.02em` | `1.1` | `--text` |
| Hero sub (italic) | Fraunces italic | `clamp(1rem, 1.5vw, 1.2rem)` | 300 | `0.01em` | — | `--accent2` |
| Section title | Fraunces | `clamp(2rem, 4vw, 3rem)` | 300 | `-0.02em` | `1.15` | `--text` |
| Card / company name | Fraunces | `1.5rem` | 300 | `-0.01em` | — | `--text` |
| Notebook title | Fraunces | `1.1rem` | 400 | `-0.01em` | `1.4` | `--text` |
| Experiment name | Fraunces | `1.2rem` | 400 | `-0.01em` | — | `--text` |
| Metric value | Fraunces | `2.2rem` | 300 | `-0.02em` | — | `--text` |
| Writing title | Fraunces | `clamp(1.1rem, 1.5vw, 1.4rem)` | 300 | `-0.02em` | `1.3` | `--text` |
| Body / section desc | DM Sans | `15px` | 300 | — | `1.8` | `--text2` |
| Card body / excerpt | DM Sans | `13px` | 300 | — | `1.8` | `--text2` |
| Company desc | DM Sans | `14px` | 300 | — | `1.8` | `--text2` |
| Metric label | DM Sans | `12px` | 300 | `0.02em` | `1.5` | `--text2` |
| Nav links | DM Sans | `13px` | 400 | `0.04em` | — | `--text2` |
| Buttons | DM Sans | `13px` | 500 (primary) / 400 (ghost) | `0.04em` | — | — |
| Section label (eyebrow) | DM Sans | `10px` | — | `0.25em` | — | `--accent` |
| Hero eyebrow | DM Sans | `11px` | — | `0.2em` | — | `--accent` |
| Tags / badges | DM Sans | `10px` | — | `0.08–0.1em` | — | `--text3` |
| Footer / metadata | DM Sans | `12px` | — | — | — | `--text3` |
| Nav logo | Fraunces | `18px` | 400 | `0.01em` | — | `--text` |
| Mobile nav links | DM Sans | `16px` | — | `0.04em` | — | `--text2` |

### Rendering

```css
body { -webkit-font-smoothing: antialiased; }
```

### Key typographic conventions

- **Fraunces for display, DM Sans for UI.** Never mix them at the same level.
- **Negative tracking on headings** (`-0.01em` to `-0.02em`) — gives the serif its elegant, editorial feel.
- **Wide tracking on ALL-CAPS labels** (`0.1em` to `0.25em`) — eyebrows and tags.
- **Weight 300 dominates** — the site feels light and refined. Weight 500 only on primary buttons.
- **Italic Fraunces** used sparingly for subheads and pull-quotes (use `font-style: italic`).

---

## 3. Layout and Spacing

### Page Container

```css
section {
  padding: 100px 24px;
  max-width: 1200px;
  margin: 0 auto;
}
```

Full-bleed sections (metrics band) use `max-width: 100%` with an inner `max-width: 1200px`.

### Spacing Scale (inferred from usage)

| Token (for NextMove) | Value | Used for |
|----------------------|-------|----------|
| `--space-xs` | `6px` | Tag gap, icon gap |
| `--space-sm` | `12px` | Button padding, inline gap |
| `--space-md` | `16–20px` | Card gap, label margin |
| `--space-lg` | `24–28px` | Card padding, section gap |
| `--space-xl` | `32–40px` | Hero padding, grid gaps |
| `--space-2xl` | `48px` | Section inner top margin |
| `--space-3xl` | `64px` | Grid margin-top, big sections |
| `--space-4xl` | `80–100px` | Section padding |
| `--space-5xl` | `120px` | Hero section padding |

### Responsive Breakpoints

| Breakpoint | Rule | Change |
|------------|------|--------|
| `≤480px` | `@media (max-width: 480px)` | Full-width connect links, tighter letter-spacing |
| `≤768px` | `@media (max-width: 768px)` | Mobile nav (hamburger), stacked company rows, 64px section padding |
| `≤900px` | `@media (max-width: 900px)` | 2-col metric grid, single-col case studies |
| `≥1024px` | `@media (min-width: 1024px)` | 2-col "Now" grid |

### Grid Patterns

```css
/* Process (How I Think) — auto-fill, min 280px */
grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
gap: 1px;  /* Creates grid-line-style borders via container background */

/* Notebook cards */
grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
gap: 20px;

/* Experiments */
grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
gap: 20px;

/* Metrics — 5 equal columns */
grid-template-columns: repeat(5, 1fr);
gap: 24px;

/* Case studies — 3 equal columns */
grid-template-columns: repeat(3, 1fr);
gap: 24px;

/* Work / company row */
grid-template-columns: 1fr 2fr auto;
gap: 48px;

/* Now — responsive 2-col */
grid-template-columns: 1fr 1fr;  /* ≥1024px */
gap: 48px;
```

### Navigation

```css
.nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 48px;         /* desktop */
  /* Mobile: padding: 16px 24px */
}
.nav.scrolled {
  background: rgba(8,10,15,0.88);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
}
```

Nav height: ~58px (20px top + 20px bottom + 18px logo text).

### Cards

| Pattern | Radius | Background | Border |
|---------|--------|------------|--------|
| Standard card | `12px` | `var(--bg2)` | `1px solid var(--border)` |
| Large card / list container | `16px` | `var(--bg2)` | `1px solid var(--border)` |
| Pill tag / button | `40px` | transparent | `1px solid var(--border-bright)` |
| Small tag | `20px` | transparent | `1px solid var(--border-bright)` |
| Metric card | `12px` | `var(--bg)` | `1px solid var(--border)` |

### Shadows

```css
/* Primary button hover */
box-shadow: 0 8px 30px rgba(124,159,255,0.3);

/* Metric card hover */
box-shadow: 0 20px 40px rgba(124,159,255,0.08);

/* Notebook card hover */
box-shadow: 0 16px 40px rgba(0,0,0,0.3);

/* Case card hover */
box-shadow: 0 20px 60px rgba(0,0,0,0.3);
```

### Dividers

```css
.divider {
  width: 100%;
  height: 1px;
  background: var(--border);   /* rgba(255,255,255,0.07) */
}
```

---

## 4. UI Components and Interactions

### Buttons

```css
/* Primary — filled accent */
.btn-primary {
  padding: 12px 28px;
  background: var(--accent);       /* #7c9fff */
  color: #080a0f;                  /* dark text on accent bg */
  border: none;
  border-radius: 40px;
  font-family: var(--sans);
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.04em;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-primary:hover {
  background: #a3baff;
  transform: translateY(-1px);
  box-shadow: 0 8px 30px rgba(124,159,255,0.3);
}

/* Ghost — outline pill */
.btn-ghost {
  padding: 12px 28px;
  background: transparent;
  color: var(--text);
  border: 1px solid var(--border-bright);
  border-radius: 40px;
  font-family: var(--sans);
  font-size: 13px;
  font-weight: 400;
  letter-spacing: 0.04em;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-ghost:hover {
  border-color: var(--text2);
  transform: translateY(-1px);
}

/* Nav CTA — small outline */
.nav-cta {
  font-size: 13px;
  padding: 8px 20px;
  border: 1px solid var(--border-bright);
  border-radius: 40px;
  color: var(--text);
  background: transparent;
  transition: all 0.2s;
}
.nav-cta:hover {
  background: rgba(124,159,255,0.1);
  border-color: var(--accent);
  color: var(--accent);
}
```

### Tags and Badges

```css
/* Content tags (skills, topics) */
.tag {
  font-size: 10px;
  padding: 3px 10px;
  border: 1px solid var(--border-bright);
  border-radius: 20px;
  color: var(--text3);
  letter-spacing: 0.08em;
  transition: all 0.2s;
}
.tag:hover { border-color: var(--accent); color: var(--accent); }

/* Accent-filled badge (company skill tag, experiment status) */
.company-tag, .exp-status {
  font-size: 10px;
  padding: 3px 10px;
  border-radius: 20px;
  background: rgba(124,159,255,0.08–0.10);
  color: var(--accent);
  letter-spacing: 0.08–0.1em;
}

/* Gold featured label */
.writing-featured-label {
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);     /* #c9a96e */
}
```

### Section Eyebrow Pattern

Used at the top of every section to label it:

```css
.section-label {
  font-size: 10px;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 16px;
  display: block;
}
```

Followed by `.section-title` (Fraunces 300) then `.section-desc` (DM Sans 300, `--text2`).

### Card Hover Pattern (universal)

All cards follow the same hover convention:
1. `transform: translateY(-2px to -4px)` — subtle lift
2. `border-color` shifts from `--border` → `--border-bright` (or `--accent` on feature hover)
3. Optional `box-shadow` glow
4. `transition: all 0.3s` (cards) or `0.2s` (buttons/nav)

### Flip Cards (How I Think section)

```css
.flip-card-inner {
  transition: transform 0.55s cubic-bezier(0.4, 0, 0.2, 1);
}
.flip-card.flipped .flip-card-inner {
  transform: rotateX(180deg);
}
```

### Reveal / Scroll Animation

```css
/* Component: Reveal (React, IntersectionObserver) */
transition: `opacity 0.3s ease, transform 0.3s ease`
/* Initial state: opacity 0, translateY(16px) */
/* Visible state: opacity 1, translateY(0) */
/* Stagger: delay={i * 0.03} to {i * 0.04} — max 0.05s per item */
```

### Squiggle Underline (signature accent)

Applied to key heading words. Blue SVG wave under text:

```css
.squiggle {
  display: inline-block;
  position: relative;
  padding-bottom: 6px;
}
.squiggle::after {
  content: '';
  position: absolute;
  left: -2px; right: -2px; bottom: -2px;
  height: 10px;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 10' preserveAspectRatio='none'%3E%3Cpath d='M0 7 C20 3 35 9 55 6 C75 3 90 8 110 5 C130 2 148 9 168 6 C182 4 192 7 200 6' fill='none' stroke='%237c9fff' stroke-width='3.5' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-size: 100% 100%;
}
```

### Progress Bar (scroll position indicator)

```css
.progress-bar {
  position: fixed;
  top: 0; left: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  z-index: 1000;
  transition: width 0.1s linear;
}
```

### Mobile Navigation

```css
/* Hamburger button (hidden on desktop) */
.hamburger { display: none; font-size: 20px; color: var(--text); }
@media (max-width: 768px) { .hamburger { display: block; } }

/* Slide-down menu */
.mobile-menu {
  display: none;
  position: fixed;
  top: 60px;
  background: rgba(8,10,15,0.97);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 24px;
  z-index: 99;
  flex-direction: column;
}
.mobile-menu.open { display: flex; }
.mobile-menu a {
  font-size: 16px;
  color: var(--text2);
  padding: 14px 0;
  border-bottom: 1px solid var(--border);
  letter-spacing: 0.04em;
}
```

### Scrollbar

```css
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border-bright); border-radius: 2px; }
```

---

## 5. Visual Identity

### Design Principles

**Dark, editorial, and considered.** The site reads as a premium portfolio: opinionated, unhurried, and confident. It avoids the visual noise of typical SaaS products.

**Key characteristics:**

1. **Near-black background with a cool blue undertone** (`#080a0f`) — not pure black. Creates depth without feeling harsh.

2. **Layered surface system** — three background levels (`bg`, `bg2`, `bg3`) create visual hierarchy without borders everywhere. Cards "float" on the page.

3. **Fraunces as the voice.** The variable serif is expressive and distinctive. Its weight-300 setting gives headlines a delicate, high-fashion quality. The italic variant adds personality to subheadings.

4. **DM Sans as the workhorse.** Clean, geometric, legible at small sizes. Pairs perfectly with Fraunces without competing.

5. **Cornflower blue accent (`#7c9fff`) is the only strong color.** Everything else is desaturated. This makes the accent highly meaningful — it marks interactivity, emphasis, and personality touches (nav logo dot, squiggle underlines, hover states).

6. **The squiggle.** The hand-drawn SVG underline on key words is the single most distinctive visual element. It signals where Bridal is being emphatic without shouting.

7. **Horizontal rhythm and restraint.** Section labels are 10–11px ALL-CAPS with wide tracking. They separate sections without being loud. This creates a journalistic, long-form reading experience.

8. **Hover as delight, not noise.** Micro-lifts (`translateY(-2 to -4px)`) and glow shadows appear only on hover. The page at rest is calm.

9. **Typography does the heavy lifting.** No illustrations, no icons beyond emoji flags and social SVGs. The design trusts words and space.

### What Makes It Distinctive

- The Fraunces / DM Sans pairing is unusual — most dark personal sites use system fonts or Inter. Fraunces gives an arts-editorial, not tech-startup, feel.
- Weight-300 serif at large sizes is rare and immediately recognizable.
- The three-level dark background creates real depth without resorting to shadows everywhere.
- The gold color (`#c9a96e`) used only on "Featured" labels signals curation and taste.
- The progress bar gradient (`accent → accent2`) is a small but memorable touch.

### Extending to NextMove Dashboard

To carry this identity into an authenticated dashboard without looking like a generic SaaS admin panel:

1. **Keep the same background stack** (`bg`, `bg2`, `bg3`). Sidebar on `bg2`, main content on `bg`, modal surfaces on `bg3`.

2. **Use Fraunces only for display elements** — page title, section headers, large stats/KPIs, empty-state headings. Never for table headers, form labels, or sidebar nav items.

3. **Cornflower blue as the sole interactive color.** All buttons, links, active states, selected items, and progress indicators use `--accent`. Don't introduce new colors for "success/warning/error" without first checking if they need to be prominent.

4. **Suggested semantic palette for dashboard** (new tokens, same language):
   - `--success: #4ade80` (green, muted) — status indicators only
   - `--warning: #fbbf24` (amber) — status only
   - `--danger: #f87171` (rose) — destructive actions only
   - Keep all three low-saturation and smaller than the accent

5. **Cards follow the same 12px radius + `--bg2` + `--border` pattern.** Tables sit on `--bg`, with `--bg3` on row hover.

6. **Form inputs:** `background: var(--bg3); border: 1px solid var(--border); border-radius: 8px; color: var(--text);` with `:focus { border-color: var(--accent); outline: none; }`.

7. **No heavy shadows on layout chrome** (sidebar, topbar). Let the background-level system carry the depth. Save shadows for floating elements (dropdowns, modals, tooltips).

8. **Typography in the dashboard:** use DM Sans 400 for all functional text. Reserve 300 for descriptive copy (empty states, helper text). Use Fraunces 300 sparingly for KPI values and section headers.

---

## 6. Technical Implementation

### Framework and Stack

| Layer | Technology |
|-------|-----------|
| Framework | React 18 (via Babel CDN — no build step) |
| Styling | Vanilla CSS custom properties (no Tailwind, no CSS-in-JS) |
| Scripting | Inline `<script type="text/babel">` blocks |
| Fonts | Google Fonts (Fraunces + DM Sans) via `<link>` |
| Analytics | Google Analytics 4 (gtag) + Hotjar |
| Deployment | GitHub Pages (auto-deploy on push to `main`) |
| QA | `check_site.py` — 67-check Python suite, must pass before every push |

> **Note for NextMove:** You are free to use any modern framework (Next.js, Vite + React, etc.) and Tailwind CSS. The design tokens below translate directly to Tailwind's `theme.extend` configuration.

### Existing Reusable Patterns (from `index.html`)

| Pattern | Description |
|---------|-------------|
| `Reveal` component | IntersectionObserver scroll animation wrapper (React) |
| `GALLERY_PHOTOS` array | Data-driven photo gallery with flag/label/position |
| `NOTEBOOK` array | Card content with expand/collapse |
| `DESTINATIONS_BY_CONTINENT` | Nested data structure for world map |
| `FALLBACK_WRITING` | Writing post array with tags, meta |
| Flip card | 3D rotateX flip on click (CSS + React state) |
| Progress bar | `window.scrollY / documentElement.scrollHeight` |
| Hamburger nav | `useState` toggle for mobile menu |
| Scroll-to-section | Anchor `href="#id"` + `scroll-behavior: smooth` |

### CSS Variables File (copy to NextMove)

See `nextmove-tokens.css` (delivered alongside this file).

### Accessibility and Responsive Conventions

- `html { scroll-behavior: smooth; overflow-x: hidden; }`
- `-webkit-overflow-scrolling: touch` on horizontal scroll containers
- `passive: true` on scroll event listeners
- Viewport meta: `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`
- `-webkit-font-smoothing: antialiased` on `body`
- Mobile nav hides desktop links + CTA, shows hamburger button
- All flex layouts use `flex-wrap: wrap` for responsive overflow

---

## 7. Asset Inventory

### Files to reference (bridalpearson.github.io repo)

| File | Purpose |
|------|---------|
| `index.html` | Complete site source — all CSS, JS, React, and base64 images |
| `check_site.py` | 67-check QA regression suite |
| `photo_reference.html` | Visual map of all photo variables (delivered earlier in session) |

### Photo variables in `index.html` (base64 embedded)

```
window.__WORLD_MAP__         World map SVG/PNG for travel section
window.__PHOTO_GYM__         Fitness / gym
window.__PHOTO_PARIS__       Paris 🇫🇷
window.__PHOTO_LONDON__      London 🇬🇧
window.__PHOTO_MOROCCO__     Morocco 🇲🇦
window.__PHOTO_EGYPT__       Egypt 🇪🇬
window.__PHOTO_INDIA__       India 🇮🇳 (position: center 90%)
window.__PHOTO_GHANA1__      Ghana 1 🇬🇭
window.__PHOTO_GHANA2__      Ghana 2 🇬🇭
window.__PHOTO_JAPAN__       Japan 1 🇯🇵
window.__PHOTO_JAPAN4__      Japan 4 🇯🇵
window.__PHOTO_JAPAN5__      Japan 5 🇯🇵
window.__PHOTO_JAPAN6__      Japan 6 🇯🇵
window.__PHOTO_JAPAN7__      Japan 7 🇯🇵
window.__PHOTO_JAPAN8__      Japan 8 🇯🇵
window.__PHOTO_JAPAN9__      Japan 9 🇯🇵
window.__PHOTO_JAPAN10__     Japan 10 🇯🇵
window.__PHOTO_JAPAN11__     Japan 11 🇯🇵
window.__PHOTO_JAPAN12__     Japan 12 🇯🇵
```

> Photos cannot be extracted from this document for NextMove — they are personal photos embedded in the personal site. NextMove will use its own imagery.

### Squiggle SVG (copy verbatim)

```
data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 10' preserveAspectRatio='none'%3E%3Cpath d='M0 7 C20 3 35 9 55 6 C75 3 90 8 110 5 C130 2 148 9 168 6 C182 4 192 7 200 6' fill='none' stroke='%237c9fff' stroke-width='3.5' stroke-linecap='round'/%3E%3C%2Fsvg%3E
```

---

*End of design specification. All values verified directly from `bridalpearson.github.io/index.html` source code.*
