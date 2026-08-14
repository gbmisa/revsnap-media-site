#!/usr/bin/env python3
"""Prep Clark's automotive photographs for web use.

Generates responsive AVIF, WebP, and JPEG sizes from originals in Assets/.
No cropping — the camera framing is final. Preserves aspect ratio and EXIF
rotation. Originals in Assets/ are left untouched; outputs go to images/.

Asset subfolders map 1:1 to output folders, and filenames map 1:1 to output
numbers: Assets/cars/007.jpg -> images/cars/007-{400,800,1200,1600}.{jpg,webp,avif}.
Folders starting with "_" are skipped (curation rejects live in _excluded-*).

AVIF needs an encoder Pillow does not ship by default. Debian/Ubuntu block a
plain `pip install` (PEP 668), so this project keeps one in tools/.venv:

    python3 -m venv --system-site-packages tools/.venv
    tools/.venv/bin/pip install pillow-avif-plugin
    tools/.venv/bin/python tools/prep_images.py

Run it any other way and it will stop rather than silently emit a WebP-only
set — which is exactly what happened between Phase 1 and Phase 6.
"""
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("PIL required: pip install Pillow")

try:  # registers the AVIF plugin on Pillow builds without native libavif
    import pillow_avif  # noqa: F401
except ImportError:
    pass

if "AVIF" not in Image.SAVE:
    sys.exit(
        "No AVIF encoder available — refusing to write a partial image set.\n"
        "  python3 -m venv --system-site-packages tools/.venv\n"
        "  tools/.venv/bin/pip install pillow-avif-plugin\n"
        "  tools/.venv/bin/python tools/prep_images.py"
    )

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Assets"
OUT = ROOT / "images"

# Responsive sizes: mobile-first, desktop hero, etc.
SIZES = {
    "400": 400,      # mobile thumbnail
    "800": 800,      # mobile full-width
    "1200": 1200,    # tablet / small desktop
    "1600": 1600,    # desktop hero
}

JPEG_QUALITY = 82
WEBP_QUALITY = 80
AVIF_QUALITY = 75  # AVIF can be more aggressive

if not SRC.is_dir():
    sys.exit(f"Source folder not found: {SRC}")

OUT.mkdir(parents=True, exist_ok=True)

# Gather all images from all subdirectories
all_images = {}
for shoot_dir in sorted(SRC.iterdir()):
    if not shoot_dir.is_dir() or shoot_dir.name.startswith("_"):
        continue
    shoot_name = shoot_dir.name
    all_images[shoot_name] = sorted(
        list(shoot_dir.glob("*.jpeg")) + list(shoot_dir.glob("*.jpg"))
    )

total_written = 0
failures = []
for shoot_name, files in all_images.items():
    shoot_out = OUT / shoot_name
    shoot_out.mkdir(parents=True, exist_ok=True)

    print(f"\n{shoot_name}: {len(files)} images")

    for i, path in enumerate(files, start=1):
        try:
            with Image.open(path) as raw:
                im = ImageOps.exif_transpose(raw).convert("RGB")

            orig_size = im.size

            for label, target_px in SIZES.items():
                # Resize down if needed (never upscale)
                scale = min(1.0, target_px / max(orig_size[0], orig_size[1]))
                new_size = (round(orig_size[0] * scale), round(orig_size[1] * scale))

                if scale < 1.0:
                    sized = im.resize(new_size, Image.LANCZOS)
                else:
                    sized = im.copy()

                # Source filenames are already the published numbers, so keep
                # them — renumbering on enumerate order would silently reshuffle
                # every <picture> on the site if a file were ever added.
                slug = path.stem if path.stem.isdigit() else f"{i:03d}"

                # No try/except on any of these. A format that fails to write
                # must stop the run, not leave the site half a format short.
                sized.save(shoot_out / f"{slug}-{label}.jpg",
                           "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
                sized.save(shoot_out / f"{slug}-{label}.webp",
                           "WEBP", quality=WEBP_QUALITY)
                sized.save(shoot_out / f"{slug}-{label}.avif",
                           "AVIF", quality=AVIF_QUALITY, speed=4)

                total_written += 1

            if i % 10 == 0 or i == len(files):
                print(f"  ✓ {i}/{len(files)}")

        except Exception as e:
            print(f"  ✗ {path.name}: {e}")
            failures.append(f"{shoot_name}/{path.name}: {e}")

print(f"\n✓ Total: {total_written} sized images written to images/ (×3 formats)")
if failures:
    print(f"\n✗ {len(failures)} source images failed:")
    for f in failures:
        print(f"    {f}")
    sys.exit(1)
print("  Next: python3 tools/scrub_exif.py")
