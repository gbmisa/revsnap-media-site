#!/usr/bin/env python3
"""Prep Clark's automotive photographs for web use.

Generates responsive AVIF, WebP, and JPEG sizes from originals in Assets/.
No cropping — the camera framing is final. Preserves aspect ratio and EXIF
rotation. Originals in Assets/ are left untouched; outputs go to images/.

Scans Asset subfolders to organize output (e.g., Assets/cav-photos/ ->
images/cav-photos/).
"""
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("PIL required: pip install Pillow")

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
    if not shoot_dir.is_dir():
        continue
    shoot_name = shoot_dir.name
    all_images[shoot_name] = sorted(
        list(shoot_dir.glob("*.jpeg")) + list(shoot_dir.glob("*.jpg"))
    )

total_written = 0
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

                slug = f"{i:03d}"

                # JPEG
                jpeg_dest = shoot_out / f"{slug}-{label}.jpg"
                sized.save(jpeg_dest, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)

                # WebP (requires Pillow with webp support)
                try:
                    webp_dest = shoot_out / f"{slug}-{label}.webp"
                    sized.save(webp_dest, "WEBP", quality=WEBP_QUALITY)
                except Exception as e:
                    pass  # WebP support optional

                # AVIF (requires pillow-avif or similar)
                try:
                    avif_dest = shoot_out / f"{slug}-{label}.avif"
                    sized.save(avif_dest, "AVIF", quality=AVIF_QUALITY)
                except Exception as e:
                    pass  # AVIF support optional

                total_written += 1

            if i % 10 == 0 or i == len(files):
                print(f"  ✓ {i}/{len(files)}")

        except Exception as e:
            print(f"  ✗ {path.name}: {e}")

print(f"\n✓ Total: {total_written} sized images written to images/")
print("  Next: python3 tools/scrub_exif.py")
