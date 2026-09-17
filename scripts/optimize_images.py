"""Generate web images from retained originals. Requires Pillow: pip install Pillow."""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "optimized"
OUTPUT.mkdir(exist_ok=True)

for source in sorted((ROOT / "assets" / "gallery").iterdir()):
    if source.suffix.lower() not in {".jpg", ".png"}:
        continue
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        for width in (400, 800, 1280):
            size = min(width, image.width)
            resized = image.resize((size, round(image.height * size / image.width)), Image.Resampling.LANCZOS)
            resized.save(OUTPUT / f"{source.stem}-{width}.webp", "WEBP", quality=82, method=6)

with Image.open(ROOT / "assets" / "Final Logo.png") as logo:
    logo.thumbnail((280, 280), Image.Resampling.LANCZOS)
    logo.save(OUTPUT / "logo.webp", "WEBP", lossless=True, method=6)

with Image.open(ROOT / "assets" / "Icon.png") as icon:
    icon.thumbnail((48, 48), Image.Resampling.LANCZOS)
    icon.save(OUTPUT / "icon.png", optimize=True)
