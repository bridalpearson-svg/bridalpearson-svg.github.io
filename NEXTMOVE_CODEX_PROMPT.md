# NextMove — Codex Implementation Prompt

**Copy this prompt verbatim as your system context when starting NextMove with Codex.**

---

## Context

You are building **NextMove**, a personal career intelligence web application for Bridal Pearson. NextMove includes: job application tracking, interview preparation, professional analytics, a learning dashboard, and personal career insights.

The design system is derived directly from Bridal's personal website, bridalpearson.com. The complete specification lives in `BRIDAL_DESIGN_SYSTEM.md`. The CSS tokens and utility classes live in `nextmove-tokens.css`. Both files are in this repository.

**Your job is to make NextMove feel like a natural extension of bridalpearson.com — the same design voice, elevated into a richer application.**

---

## Design Rules (non-negotiable)

### Typography
- **Fraunces** (Google Font, weight 300/400/500, optical size variable) for ALL display text: page headings, section headers, KPI values, empty-state headlines.
- **DM Sans** (Google Font, weight 300/400/500) for ALL functional UI: nav, buttons, labels, table text, form inputs, body copy, tags.
- **Never use any other font family.**
- Load both fonts from Google Fonts exactly as specified in `nextmove-tokens.css`.

### Colors
Use only the CSS variables defined in `nextmove-tokens.css`. Do not introduce new colors except the semantic additions already defined there (`--success`, `--warning`, `--danger`). The accent color `--accent: #7c9fff` (cornflower blue) is the **only** strongly-colored interactive element.

### Backgrounds
The three-level dark system must be preserved:
- `--bg` (`#080a0f`) — page/outer background
- `--bg2` (`#0d1117`) — card/panel/sidebar surface
- `--bg3` (`#111520`) — hover state/elevated/modal surface

### Borders
- Default: `1px solid var(--border)` — `rgba(255,255,255,0.07)`
- Active/hover: `1px solid var(--border-bright)` — `rgba(255,255,255,0.14)`
- Accent focus: `1px solid var(--accent)`

### Buttons
Follow the three button styles defined in `nextmove-tokens.css`:
- `.btn-primary` — filled accent, dark text, pill shape
- `.btn-ghost` — outline pill, text color
- `.btn-accent-ghost` — small pill, accent on hover

### Cards
- Standard: `--bg2` background, `--border` border, `12px` radius, `0.3s` hover transition
- Hover: lift `translateY(-3px)`, `--border-bright` border, optional box-shadow
- Never use heavy drop shadows on non-interactive cards at rest

### Spacing
Use the `--space-*` variables from `nextmove-tokens.css`. Standard card padding is `var(--space-xl)` (32px). Section padding is `var(--space-5xl)` (100px) on desktop, `var(--space-3xl)` (64px) on mobile.

---

## Layout Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  Fixed top nav (--nav-height: 60px, bg2 + blur on scroll)       │
├──────────────┬──────────────────────────────────────────────────┤
│              │                                                   │
│  Sidebar     │  Main content area                               │
│  (--bg2)     │  (--bg)                                          │
│  220–240px   │  max-width: var(--max-width) = 1200px            │
│              │  padding: 0 var(--space-lg)                      │
│              │                                                   │
└──────────────┴──────────────────────────────────────────────────┘
```

- **Top nav:** `position: fixed`, `background: rgba(8,10,15,0.88)`, `backdrop-filter: blur(20px)`, `border-bottom: 1px solid var(--border)`.
- **Sidebar:** `background: var(--bg2)`, `border-right: 1px solid var(--border)`, fixed height, scrollable.
- **Main content:** `background: var(--bg)`.
- **Page sections:** `padding: var(--space-5xl) var(--space-lg)`, `max-width: var(--max-width)`, `margin: 0 auto`.

---

## Component Specifications

### Section headers (use on every page)
```jsx
<span className="eyebrow">Section Label</span>
<h2 className="heading-display">Section Title</h2>
<p className="body-lg">Optional descriptor text in secondary color.</p>
```

### KPI / stat tiles
```jsx
<div className="card" style={{ textAlign: 'center', padding: '32px 16px' }}>
  <div style={{ fontFamily: 'var(--serif)', fontSize: '2.2rem', fontWeight: 300, color: 'var(--text)', letterSpacing: '-0.02em', marginBottom: 8 }}>
    42
  </div>
  <div style={{ fontSize: 12, color: 'var(--text2)', fontWeight: 300, letterSpacing: '0.02em' }}>
    Applications sent
  </div>
</div>
```

### Data tables
```jsx
<table style={{ width: '100%', borderCollapse: 'collapse' }}>
  <thead>
    <tr style={{ borderBottom: '1px solid var(--border)' }}>
      <th style={{ fontSize: 10, letterSpacing: '0.2em', textTransform: 'uppercase', color: 'var(--text3)', padding: '12px 16px', textAlign: 'left', fontWeight: 400 }}>
        Column
      </th>
    </tr>
  </thead>
  <tbody>
    <tr className="table-row">
      <td style={{ padding: '14px 16px', fontSize: 14, color: 'var(--text)' }}>
        Value
      </td>
    </tr>
  </tbody>
</table>
```

### Form inputs
```jsx
<label style={{ fontSize: 11, letterSpacing: '0.15em', textTransform: 'uppercase', color: 'var(--text3)', marginBottom: 8, display: 'block' }}>
  Field Label
</label>
<input className="input" type="text" placeholder="Placeholder…" />
```

### Status badges
```jsx
/* Use tag-accent for active/positive, custom for semantic states */
<span className="tag-accent">Active</span>
<span style={{ ...tagAccentBase, background: 'rgba(74,222,128,0.1)', color: 'var(--success)' }}>Offer</span>
<span style={{ ...tagAccentBase, background: 'rgba(248,113,113,0.1)', color: 'var(--danger)' }}>Rejected</span>
```

### Empty states
```jsx
<div style={{ textAlign: 'center', padding: 'var(--space-6xl) var(--space-lg)' }}>
  <h3 style={{ fontFamily: 'var(--serif)', fontSize: '1.5rem', fontWeight: 300, color: 'var(--text)', marginBottom: 12 }}>
    Nothing here yet
  </h3>
  <p className="body-md" style={{ marginBottom: 'var(--space-xl)', maxWidth: 400, margin: '0 auto var(--space-xl)' }}>
    Start by adding your first application.
  </p>
  <button className="btn-primary">Add Application</button>
</div>
```

---

## Animations and Transitions

- Card hover: `transition: all 0.3s ease`
- Button hover: `transition: all 0.2s ease`
- Nav scroll state: `transition: all 0.3s ease`
- Page-load reveals: opacity 0→1, translateY 16px→0, `0.3s ease`, stagger `i * 0.03s`
- Modal open: `opacity 0→1`, `translateY 8px→0`, `0.2s ease`
- **No bounce, spring, or elastic easing.** Only `ease` and `cubic-bezier(0.4,0,0.2,1)`.

---

## Anti-patterns (what NOT to do)

- ❌ Do not use `Inter`, `Roboto`, `SF Pro`, or any font other than Fraunces + DM Sans
- ❌ Do not use Tailwind color classes like `blue-500`, `gray-900` — use CSS variables only
- ❌ Do not use white or light backgrounds anywhere
- ❌ Do not add color gradients to buttons or cards (gradient is progress bar and top-border accent only)
- ❌ Do not use `border-radius` values other than 8px / 12px / 16px / 20px / 40px (50% for avatars)
- ❌ Do not use heavy box-shadows at rest — only on hover
- ❌ Do not use `font-weight: 700` or `bold` — the design never goes above 500
- ❌ Do not center-align body text or card body copy
- ❌ Do not use horizontal rules or decorative separators other than `--border` color
- ❌ Do not use colored backgrounds on cards (all cards are `--bg2`)

---

## Responsive Breakpoints

| Breakpoint | Behavior |
|------------|----------|
| `≤480px` | Full-width buttons, tighter padding |
| `≤768px` | Sidebar collapses to bottom nav or hamburger drawer, 64px section padding |
| `≤900px` | KPI grid goes 2-column, some grids collapse to 1-column |
| `≥1024px` | Full layout with sidebar |

---

## Tailwind Configuration (if using Tailwind)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        bg:     '#080a0f',
        bg2:    '#0d1117',
        bg3:    '#111520',
        text:   '#e8eaf0',
        text2:  '#8890a4',
        text3:  '#555d72',
        accent: '#7c9fff',
        accent2:'#a78bfa',
        gold:   '#c9a96e',
      },
      fontFamily: {
        serif: ['Fraunces', 'Georgia', 'serif'],
        sans:  ['DM Sans', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        sm:   '8px',
        md:   '12px',
        lg:   '16px',
        tag:  '20px',
        pill: '40px',
      },
      boxShadow: {
        button:  '0 8px 30px rgba(124,159,255,0.3)',
        card:    '0 16px 40px rgba(0,0,0,0.3)',
        'card-lg':'0 20px 60px rgba(0,0,0,0.3)',
        accent:  '0 20px 40px rgba(124,159,255,0.08)',
      },
      maxWidth: {
        content: '1200px',
      },
    },
  },
}
```

---

## Files to include in NextMove repo

| File | Action |
|------|--------|
| `BRIDAL_DESIGN_SYSTEM.md` | Reference document — read but do not ship to users |
| `nextmove-tokens.css` | Import as global stylesheet |
| `NEXTMOVE_CODEX_PROMPT.md` | This file — use as Codex system prompt |

---

*Design extracted from bridalpearson.com source — November 2026.*
