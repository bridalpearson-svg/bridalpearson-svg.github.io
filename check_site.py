#!/usr/bin/env python3
"""
Site integrity check — run before every push to bridalpearson.github.io
Verifies all critical components are present in index.html
"""

import sys

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
    ("travel-intro-row",             "Travel intro CSS"),
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

    # World map must be in photos script block (not in babel block)
    # Validated separately below via script block inspection
]

SCRIPT_BLOCK_CHECKS = True  # validated in main check() below

def check(filepath="index.html"):
    import re

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
    # Find the babel block
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
