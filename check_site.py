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
]

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

    print(f"\n✅ {len(passed)} checks passed")
    if failed:
        print(f"❌ {len(failed)} checks FAILED:\n")
        for marker, label in failed:
            print(f"   MISSING: {label}")
            print(f"            (looked for: {marker!r})\n")
        print("⛔  Do NOT push until these are resolved.\n")
        sys.exit(1)
    else:
        print("🟢 All components present — safe to push.\n")

if __name__ == "__main__":
    check()
