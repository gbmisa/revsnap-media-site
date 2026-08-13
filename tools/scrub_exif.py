#!/usr/bin/env python3
"""Strip all EXIF (GPS, timestamps, device) from originals in Assets/.

Rewrites each file IN PLACE, recursively through subdirectories. Rotation is
baked into the pixels first, so prep_images.py keeps producing identical output
afterwards.

If you want to keep a private copy of the untouched originals with GPS intact,
copy Assets/ somewhere OUTSIDE this repo BEFORE running this.
"""
import glob
import os
from pathlib import Path
from PIL import Image, ImageOps

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Assets")
QUALITY = 95  # near-lossless; these are source files

# Recursively find all jpg/jpeg in all subdirectories
files = []
for pattern in ["**/*.jpeg", "**/*.jpg"]:
    files.extend(glob.glob(os.path.join(SRC, pattern), recursive=True))

files = sorted(set(files))  # dedupe in case both patterns match

if not files:
    raise SystemExit(f"No images found in {SRC}")

for path in files:
    before = os.path.getsize(path) / 1024

    try:
        im = Image.open(path)
        im = ImageOps.exif_transpose(im)   # bake rotation into pixels
        im = im.convert("RGB")

        # Re-save with no exif= argument -> no EXIF block written.
        im.save(path, "JPEG", quality=QUALITY, optimize=True, progressive=True)

        after = os.path.getsize(path) / 1024
        w, h = im.size
        relpath = os.path.relpath(path, SRC)
        print(f"  {relpath:40} {before:7.0f} KB -> {after:7.0f} KB  {w}x{h}")
    except Exception as e:
        print(f"  ✗ {path}: {e}")

print(f"\n{len(files)} files processed.")
