#!/usr/bin/env python3
import os
import sys
from PIL import Image, ImageOps

IMG_EXTS = (".jpg", ".jpeg", ".png", ".webp")

def ask_quality(default=75):
    raw = input(f"Compression quality (1–100) [{default}]: ").strip()
    if not raw:
        return default
    try:
        q = int(raw)
        if 1 <= q <= 100:
            return q
    except ValueError:
        pass
    print("Please enter a number between 1 and 100.")
    return ask_quality(default)

def human_bytes(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"

def compress_file(path, quality):
    ext = os.path.splitext(path)[1].lower()
    before = os.path.getsize(path)
    try:
        with Image.open(path) as im:
            # Auto-apply EXIF orientation for JPEGs
            im = ImageOps.exif_transpose(im)

            if ext in (".jpg", ".jpeg"):
                if im.mode not in ("RGB", "L"):
                    im = im.convert("RGB")  # strip alpha if any
                im.save(
                    path,
                    optimize=True,
                    quality=quality,      # 70–80 recommended for web
                    progressive=True,     # smaller & web-friendly
                    subsampling="auto",   # keep reasonable chroma subsampling
                )

            elif ext == ".webp":
                # Keep alpha if present
                im.save(
                    path,
                    format="WEBP",
                    quality=quality,      # 60–80 often indistinguishable
                    method=6,             # better compression
                )

            elif ext == ".png":
                # PNG is lossless; just optimize (no 'quality' parameter)
                # This keeps alpha intact and reduces size without visual loss.
                im.save(
                    path,
                    optimize=True,
                    compress_level=9,     # max deflate; slower, smaller
                )

            else:
                return before, before, "skipped (unsupported)"

    except Exception as e:
        return before, before, f"error: {e}"

    after = os.path.getsize(path)
    return before, after, "ok"

def main():
    # Work on the current working directory by default
    root = os.getcwd()
    print(f"Target folder (including subfolders): {root}")

    quality = ask_quality(default=75)
    print(f"Using quality={quality}\n")

    total_before = 0
    total_after = 0
    processed = 0
    skipped = 0

    for subdir, _, files in os.walk(root):
        for name in files:
            if name.lower().endswith(IMG_EXTS):
                path = os.path.join(subdir, name)
                b, a, status = compress_file(path, quality)
                total_before += b
                total_after += a
                if status == "ok":
                    processed += 1
                    delta = b - a
                    sign = "-" if delta >= 0 else "+"
                    print(f"[OK] {path}")
                    print(f"     {human_bytes(b)} → {human_bytes(a)} ({sign}{human_bytes(abs(delta))})")
                else:
                    skipped += 1
                    print(f"[{status.upper()}] {path}")

    saved = total_before - total_after
    pct = (saved / total_before * 100) if total_before else 0.0

    print("\n— Summary —")
    print(f"Images processed: {processed}")
    print(f"Images skipped/errors: {skipped}")
    print(f"Total size: {human_bytes(total_before)} → {human_bytes(total_after)}")
    print(f"Saved: {human_bytes(saved)} ({pct:.1f}%)")

if __name__ == "__main__":
    try:
        from PIL import Image  # noqa: F401 (ensure Pillow is available)
    except Exception:
        print("Pillow is not installed. Run:\n  python -m pip install pillow\n")
        sys.exit(1)
    main()
