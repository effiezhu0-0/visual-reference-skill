#!/usr/bin/env python3
"""Build a PNG confirmation board from a reference-image manifest."""

from __future__ import annotations

import json
import math
import sys
from datetime import date
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError as exc:
    raise SystemExit(
        "Missing dependency: Pillow. Install pillow in the active environment or create the PNG board manually."
    ) from exc


W, H = 1920, 1080
MARGIN = 64
GAP = 24
BG = (248, 247, 242)
INK = (30, 32, 34)
MUTED = (99, 104, 110)
CARD = (255, 255, 255)
LINE = (222, 219, 210)
ACCENT = (196, 62, 48)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


TITLE = font(42, True)
SUBTITLE = font(20)
LABEL = font(19, True)
BODY = font(16)
SMALL = font(13)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int, max_lines: int) -> list[str]:
    words = (text or "").split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        if draw.textlength(test, font=fnt) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
        if len(lines) >= max_lines:
            break
    if current and len(lines) < max_lines:
        lines.append(current)
    if len(lines) == max_lines and words:
        while lines[-1] and draw.textlength(lines[-1] + "...", font=fnt) > max_width:
            lines[-1] = lines[-1][:-1]
        lines[-1] = lines[-1].rstrip() + "..."
    return lines


def fit_image(path: Path, size: tuple[int, int]) -> Image.Image:
    try:
        img = Image.open(path).convert("RGB")
    except Exception:
        img = Image.new("RGB", size, (230, 230, 230))
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def draw_card(draw: ImageDraw.ImageDraw, canvas: Image.Image, folder: Path, item: dict, box: tuple[int, int, int, int]) -> None:
    x, y, w, h = box
    draw.rounded_rectangle((x, y, x + w, y + h), radius=8, fill=CARD, outline=LINE, width=2)
    img_h = int(h * 0.64)
    img = fit_image(folder / item.get("filename", ""), (w - 24, img_h))
    canvas.paste(img, (x + 12, y + 12))

    text_x = x + 16
    text_y = y + 24 + img_h
    text_w = w - 32
    category = item.get("category") or item.get("keyword") or "Reference"
    description = item.get("description") or item.get("filename") or ""
    source = item.get("creator_or_project") or item.get("platform") or ""
    method = item.get("capture_method") or ""

    draw.text((text_x, text_y), category, fill=INK, font=LABEL)
    text_y += 30
    for line in wrap_text(draw, description, BODY, text_w, 2):
        draw.text((text_x, text_y), line, fill=INK, font=BODY)
        text_y += 22
    source_line = " | ".join(part for part in [source, method] if part)
    for line in wrap_text(draw, source_line, SMALL, text_w, 1):
        draw.text((text_x, y + h - 32), line, fill=MUTED, font=SMALL)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: build_confirmation_board.py <manifest.json>", file=sys.stderr)
        return 2

    manifest_path = Path(sys.argv[1]).expanduser().resolve()
    folder = manifest_path.parent
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    items = data.get("items", [])[:12]

    canvas = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(canvas)

    title = data.get("title") or "Reference image board"
    platforms = ", ".join(data.get("platforms", []))
    keywords = ", ".join(data.get("keywords", []))
    created_at = data.get("created_at") or date.today().isoformat()
    subtitle = " | ".join(part for part in [platforms, keywords, created_at] if part)

    draw.text((MARGIN, 42), title, fill=INK, font=TITLE)
    draw.rectangle((MARGIN, 106, MARGIN + 96, 112), fill=ACCENT)
    draw.text((MARGIN, 128), subtitle, fill=MUTED, font=SUBTITLE)

    if not items:
        draw.text((MARGIN, 240), "No image items found in manifest.", fill=INK, font=SUBTITLE)
    else:
        count = len(items)
        cols = 4 if count > 6 else 3
        rows = math.ceil(count / cols)
        top = 190
        available_w = W - MARGIN * 2 - GAP * (cols - 1)
        available_h = H - top - MARGIN - GAP * (rows - 1)
        card_w = available_w // cols
        card_h = available_h // rows
        for idx, item in enumerate(items):
            row, col = divmod(idx, cols)
            x = MARGIN + col * (card_w + GAP)
            y = top + row * (card_h + GAP)
            draw_card(draw, canvas, folder, item, (x, y, card_w, card_h))

    output = folder / "confirmation-board.png"
    canvas.save(output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
