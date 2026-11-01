#!/usr/bin/env python3
"""
Site integrity check — run before every push to bridalpearson.github.io
Verifies all critical components are present in index.html
"""

import sys
import re

REQUIRED = [
    # Data arrays
    ("const NOTEBOOK = [",           "Product Notebook entries"),
    ("const FALLBACK_WRITING = [",   "Blog / writing entries"),
    ("const GALLERY_PHOTOS = [",     "Photo gallery"),
    ("const DESTINATIONS_BY_CONTINENT", "Travel destinations data"),
    ("window.__WORLD_MAP__",         "World map image"),
    ("window.__PHOTO_GYM__",         "Gym photo"),
    ("window.__PHOTO_PARIS__",       "Paris photo"),
    ("window.__PHOTO_LONDON__",      "London photo"),
    ("window.__PHOTO_MOROCCO__",     "Morocco photo"),
    ("window.__PHOTO_EGYPT__",       "Egypt photo"),
    ("window.__PHOTO_INDIA__",       "India photo"),

    # Japan photos (added in Oct 2026)
    ("window.__PHOTO_JAPAN__",       "Japan photo 1"),
    ("window.__PHOTO_JAPAN4__",      "Japan photo 4"),
    ("window.__PHOTO_JAPAN5__",      "Japan photo 5"),
    ("window.__PHOTO_JAPAN6__",      "Japan photo 6"),
    ("window.__PHOTO_JAPAN7__",      "Japan photo 7"),
    ("window.__PHOTO_JAPAN8__",      "Japan photo 8"),
    ("window.__PHOTO_JAPAN9__",      "Japan photo 9"),
    ("window.__PHOTO_JAPAN10__",     "Japan photo 10"),
    ("window.__PHOTO_JAPAN11__",     "Japan photo 11"),
    ("window.__PHOTO_JAPAN12__",     "Japan photo 12"),
    ("window.__PHOTO_JAPAN13__",     "Japan photo 13 (with geisha)"),
    ("window.__PHOTO_JAPAN14__",     "Japan photo 14 (geisha close-up)"),
    ("window.__PHOTO_GHANA2__",      "Ghana photo 2"),

    # React components
    ("function AboutSection()",      "About Me section"),
    ("function NotebookSection()",   "Product Notebook section"),
    ("function WorkSection()",       "Where I've Built section"),
    ("function DestinationsGrid()",  "Destinations grid"),
    ("function PhotoGallery()",      "Photo gallery component"),
    ("function ConnectSection()",    "Let's Talk section"),

    # Section IDs
    ('id="about"',                   "#about anchor"),
    ('id="think"',                   "#think anchor"),
    ('id="work"',                    "#work anchor"),
    ('id="notebook"',                "#notebook anchor"),
    ('id="experiments"',             "#experiments anchor"),
    ('id="writing"',                 "#writing anchor"),
    ('id="now"',                     "#now anchor"),
    ('id="connect"',                 "#connect anchor"),

    # Key content markers
    ("Travel Section",               "Travel section block"),
    ("Exploring the World",          "Travel section heading"),
    ("squiggle",                     "Squiggle underline style"),
    ("FALLBACK_WRITING",             "Writing fallback array reference"),

    # November 2026 notebook entry
    ("AI, Headcount, and the Wrong Question", "Nov 2026 notebook entry title"),
    ('maxHeight: expanded ? 4000 : 0', "Notebook expand height fix (4000px)"),
    ('isLast ? "var(--accent)"',      "Last paragraph accent color"),

    # Layout fixes
    ("paddingTop: 60",               "About section reduced top padding"),
    ("A Little About Me",            "Title case: About Me heading"),
    ("Exploring the World",          "Travel section heading"),

    # Responsiveness
    ("@media (max-width: 768px)",    "Mobile breakpoint (768px)"),
    ("@media (max-width: 480px)",    "Small phone breakpoint (480px)"),
    (".hamburger",                   "Hamburger nav button"),
    (".mobile-menu",                 "Mobile nav menu"),
    ("flex-wrap: wrap",              "Flex wrap for responsive layouts"),
    ("clamp(",                       "Fluid typography (clamp)"),
    ("-webkit-overflow-scrolling: touch", "Touch scrolling for iOS"),

    # Performance
    ("IntersectionObserver",         "Intersection Observer for lazy reveal"),
    ("passive: true",                "Passive scroll listener (perf)"),
    ("transition: `opacity 0.3s",    "Snappy reveal transition (0.3s)"),

    # World map must be in photos script block (not in babel block)
    # Validated separately below via script block inspection
]

SCRIPT_BLOCK_CHECKS = True  # validated in main check() below

def check(filepath="index.html"):
    with open(filepath, "r") as f:
        content = f.read()

    passed = []
    failed = []

    for marker, label in REQUIRED:
        if marker in content:
            passed.append(label)
        else:
            failed.append((marker, label))

    # ── Script block integrity checks ──────────────────────────────────────
    # 1. Exactly 8 script tags
    script_tags = re.findall(r'<script[^>]*>', content)
    if len(script_tags) == 8:
        passed.append("Script tag count (8)")
    else:
        failed.append((f"8 script tags", f"Script tag count wrong — found {len(script_tags)}, expected 8"))

    # 2. No split script blocks
    if '</script>\n\n<script>' in content or '</script>\n<script>' in content:
        failed.append(("no split scripts", "Split <script> block detected — injection broke a tag boundary"))
    else:
        passed.append("No split script blocks")

    # 3. World map variable must be in the PHOTOS script block, not the babel block
    babel_start = content.find('type="text/babel"')
    if babel_start != -1:
        babel_block = content[babel_start:]
        babel_end = babel_block.find('</script>')
        babel_content = babel_block[babel_block.find('>')+1:babel_end]
        if 'window.__WORLD_MAP__ =' in babel_content:
            failed.append(("__WORLD_MAP__ location", "__WORLD_MAP__ is inside the babel/JSX block — must be in photos script block"))
        else:
            passed.append("__WORLD_MAP__ is outside babel block (correct)")

    # 4. Connect section must NOT be center-aligned
    cs_idx = content.find('.connect-section')
    if cs_idx != -1:
        cs_ctx = content[cs_idx:cs_idx+300]
        if 'text-align: center' in cs_ctx:
            failed.append((".connect-section alignment", "Connect section has text-align:center — should be left-aligned"))
        else:
            passed.append("Connect section is left-aligned")

    # ── Performance checks ─────────────────────────────────────────────────
    # 5. File size must be under 5MB (images compressed)
    size_mb = len(content) / 1024 / 1024
    if size_mb <= 5.0:
        passed.append(f"File size OK ({size_mb:.1f} MB ≤ 5.0 MB)")
    else:
        failed.append(("file size", f"File too large: {size_mb:.1f} MB (limit 5 MB) — compress images before pushing"))

    # 6. No single image over 300KB (base64 encoded)
    img_matches = re.findall(r'window\.(__[A-Z0-9_]+__) = "data:image/[^;]+;base64,([^"]+)"', content)
    oversized = []
    for varname, b64 in img_matches:
        size_kb = len(b64) * 3 / 4 / 1024
        if size_kb > 300:
            oversized.append(f"{varname} ({size_kb:.0f} KB)")
    if oversized:
        failed.append(("image sizes", f"Oversized images (>300 KB): {', '.join(oversized)}"))
    else:
        passed.append(f"All {len(img_matches)} images under 300 KB")

    # 7. Stagger delays must be fast (i * 0.05 or less)
    bad_delays = re.findall(r'delay=\{i \* (0\.[1-9][0-9]*)\}', content)
    bad_delays = [d for d in bad_delays if float(d) > 0.05]
    if bad_delays:
        failed.append(("stagger delays", f"Slow stagger delays found: {bad_delays} — use 0.05 or less"))
    else:
        passed.append("Stagger delays are snappy (≤ 0.05s)")

    # 8. Reveal component transition must be 0.5s or faster (gallery crossfade at 0.8s is intentional)
    reveal_trans = re.findall(r'transition: `opacity (0\.[0-9]+)s ease', content)
    slow_reveal = [t for t in reveal_trans if float(t) > 0.5]
    if slow_reveal:
        failed.append(("reveal speed", f"Slow Reveal transitions: {slow_reveal}s — use 0.5s or less"))
    else:
        passed.append("Reveal transitions are fast (≤ 0.5s)")

    # ── Responsiveness checks ──────────────────────────────────────────────
    # 9. Gallery uses aspectRatio not fixed height
    if 'aspectRatio: "4/3"' in content or "aspectRatio: '4/3'" in content:
        passed.append("Gallery uses aspectRatio (responsive height)")
    else:
        failed.append(("gallery responsive", "Gallery missing aspectRatio — may not scale on mobile"))

    # 10. No hard-coded pixel widths on section containers > 100%
    bad_section_widths = re.findall(r'<section[^>]*style[^>]*width:\s*(\d{4,})px', content)
    if bad_section_widths:
        failed.append(("section widths", f"Hard-coded wide section widths: {bad_section_widths}"))
    else:
        passed.append("No hard-coded oversized section widths")

    # 11. Viewport meta tag present
    if 'name="viewport"' in content and 'width=device-width' in content:
        passed.append("Viewport meta tag present")
    else:
        failed.append(("viewport meta", "Missing <meta name='viewport'> — site won't scale on mobile"))

    # ── Summary ────────────────────────────────────────────────────────────
    print(f"\n✅ {len(passed)} checks passed")
    if failed:
        print(f"❌ {len(failed)} checks FAILED:\n")
        for marker, label in failed:
            print(f"   MISSING: {label}")
            if isinstance(marker, str) and not label.startswith(marker):
                print(f"            (looked for: {marker!r})\n")
        print("⛔  Do NOT push until these are resolved.\n")
        sys.exit(1)
    else:
        print("🟢 All components present — safe to push.\n")

if __name__ == "__main__":
    check()
