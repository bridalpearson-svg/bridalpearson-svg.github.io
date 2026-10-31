#!/usr/bin/env python3
"""
Regression test suite for bridalpearson.com
Runs BEFORE every push — catches broken pages, missing components, and render errors.
Usage: python3 test_site.py
"""

import sys
import re
import subprocess
import time

SITE_URL = "https://bridalpearson.com"
INDEX = "index.html"

PASS = []
FAIL = []

def ok(label):
    PASS.append(label)
    print(f"  ✅  {label}")

def fail(label, detail=""):
    FAIL.append(label)
    print(f"  ❌  {label}" + (f"\n      → {detail}" if detail else ""))

# ─────────────────────────────────────────────
# 1. STATIC CHECKS (index.html on disk)
# ─────────────────────────────────────────────
print("\n── Static checks ──────────────────────────────")

with open(INDEX) as f:
    content = f.read()

# Script tag integrity — must be exactly 8 (no accidental splits)
script_tags = re.findall(r'<script[^>]*>', content)
inline_scripts = [t for t in script_tags if 'src=' not in t and 'async' not in t]
if len(script_tags) == 8:
    ok(f"Script tag count correct ({len(script_tags)})")
else:
    fail("Script tag count wrong", f"found {len(script_tags)}, expected 8 — possible broken injection")

# No double closing/opening script tags
if '</script>\n\n<script>' in content or '</script>\n<script>' in content:
    fail("Split script block detected — injection likely broke a <script> tag boundary")
else:
    ok("No split script blocks")

# All window image variables present and non-empty
IMAGE_VARS = [
    "__WORLD_MAP__", "__PHOTO_GYM__", "__PHOTO_PARIS__",
    "__PHOTO_LONDON__", "__PHOTO_MOROCCO__", "__PHOTO_EGYPT__", "__PHOTO_INDIA__",
]
for var in IMAGE_VARS:
    pattern = f'window.{var} = "data:image/'
    if pattern in content:
        ok(f"{var} present with data URI")
    else:
        fail(f"{var} missing or not a data URI")

# React components
COMPONENTS = [
    ("function AboutSection()",     "AboutSection"),
    ("function NotebookSection()",  "NotebookSection"),
    ("function WorkSection()",      "WorkSection"),
    ("function DestinationsGrid()", "DestinationsGrid"),
    ("function PhotoGallery()",     "PhotoGallery"),
    ("function ConnectSection()",   "ConnectSection"),
]
for marker, label in COMPONENTS:
    if marker in content:
        ok(f"{label} component present")
    else:
        fail(f"{label} component MISSING")

# Section anchors
ANCHORS = ["about","think","work","notebook","experiments","writing","now","connect"]
for anchor in ANCHORS:
    if f'id="{anchor}"' in content:
        ok(f"#{anchor} anchor present")
    else:
        fail(f"#{anchor} anchor MISSING")

# Data arrays non-empty
DATA_CHECKS = [
    ("const NOTEBOOK = [\n  {",      "NOTEBOOK has entries"),
    ("const FALLBACK_WRITING = [\n  {", "FALLBACK_WRITING has entries"),
    ("const GALLERY_PHOTOS = [\n  {", "GALLERY_PHOTOS has entries"),
    ("DESTINATIONS_BY_CONTINENT = [\n  {", "DESTINATIONS_BY_CONTINENT has entries"),
]
for marker, label in DATA_CHECKS:
    if marker in content:
        ok(label)
    else:
        fail(label + " — array may be empty or missing")

# Squiggle on all section titles
squiggle_count = content.count('className="squiggle"')
if squiggle_count >= 9:
    ok(f"Squiggle present on {squiggle_count} headings")
else:
    fail(f"Only {squiggle_count} squiggle headings — expected 9+")

# Travel section block
if "Travel Section" in content and "travel-intro-row" in content:
    ok("Travel section present")
else:
    fail("Travel section missing")

# ─────────────────────────────────────────────
# 2. LIVE SITE CHECK (Playwright headless)
# ─────────────────────────────────────────────
print("\n── Live site checks ────────────────────────────")

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # 2a. Page loads without crash
        try:
            response = page.goto(SITE_URL, timeout=20000, wait_until="domcontentloaded")
            if response and response.status == 200:
                ok(f"Site loads (HTTP {response.status})")
            else:
                fail(f"Site returned HTTP {response.status if response else 'no response'}")
        except PWTimeout:
            fail("Site timed out loading")
            browser.close()
            raise

        # 2b. Wait for React to render
        try:
            page.wait_for_selector("nav", timeout=10000)
            ok("Nav rendered (React hydrated)")
        except PWTimeout:
            fail("Nav never appeared — React may have crashed")

        # 2c. No JS console errors
        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.wait_for_timeout(3000)  # let page settle
        if errors:
            fail(f"Console errors detected", "; ".join(errors[:3]))
        else:
            ok("No JS console errors")

        # 2d. Hero headline visible
        try:
            headline = page.locator("h1").first.inner_text(timeout=5000)
            if headline:
                ok(f"Hero h1 visible: \"{headline[:60]}\"")
            else:
                fail("Hero h1 empty")
        except PWTimeout:
            fail("Hero h1 not found")

        # 2e. Key sections visible
        SECTION_IDS = ["about", "notebook", "work", "writing", "connect"]
        for sid in SECTION_IDS:
            count = page.locator(f"#{sid}").count()
            if count > 0:
                ok(f"#{sid} section in DOM")
            else:
                fail(f"#{sid} section NOT in DOM")

        # 2f. World map image loads
        map_img = page.locator('img[alt*="map"]')
        if map_img.count() > 0:
            ok("World map image present in DOM")
        else:
            fail("World map image not found in DOM")

        browser.close()

except ImportError:
    print("  ⚠️  Playwright not available — skipping live checks")
    print("      Install with: pip install playwright && playwright install chromium")
except Exception as e:
    fail(f"Live site check crashed: {e}")

# ─────────────────────────────────────────────
# 3. SUMMARY
# ─────────────────────────────────────────────
print(f"\n── Summary ─────────────────────────────────────")
print(f"  ✅  {len(PASS)} passed")
print(f"  ❌  {len(FAIL)} failed")

if FAIL:
    print(f"\n⛔  DO NOT PUSH — fix the above failures first.\n")
    sys.exit(1)
else:
    print(f"\n🟢  All checks passed — safe to push.\n")
