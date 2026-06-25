# Example Output 01

## Expected Local Folder

```text
reference-images-cyberpunk-ui-20260625/
├── 001-layout-neon-dashboard.jpg
├── 002-layout-layered-hud.png
├── 003-layout-card-grid.jpg
├── 004-layout-game-menu.png
├── 005-layout-terminal-panel.jpg
├── 006-color-blue-magenta.jpg
├── 007-color-acid-green.png
├── 008-color-dark-glow.jpg
├── 009-color-neon-gradient.png
├── 010-color-contrast-ui.jpg
├── manifest.json
└── confirmation-board.png
```

## Expected Manifest Shape

```json
{
  "title": "赛博朋克 UI",
  "created_at": "2026-06-25",
  "platforms": ["pinterest", "behance"],
  "keywords": ["赛博朋克 UI"],
  "items": [
    {
      "filename": "001-layout-neon-dashboard.jpg",
      "platform": "pinterest",
      "keyword": "赛博朋克 UI",
      "category": "版式",
      "description": "High-density neon dashboard layout with layered panels.",
      "source_url": "https://www.pinterest.com/...",
      "creator_or_project": "Visible creator or board name if available",
      "capture_method": "direct-image",
      "notes": ""
    }
  ]
}
```

## Expected Confirmation Board

`confirmation-board.png` should be:

- `1920 x 1080`.
- Dark charcoal background `#171719`.
- White title at top left.
- Two category rows: `版式` and `配色`.
- Five cropped images per row.
- No long descriptions or source labels on the board.

## Expected User-Facing Response Before Figma

已整理好确认看板，请先确认图片和分类是否符合预期：

- 输出文件夹：`/path/to/reference-images-cyberpunk-ui-20260625`
- 确认看板：`/path/to/reference-images-cyberpunk-ui-20260625/confirmation-board.png`
- 来源清单：`/path/to/reference-images-cyberpunk-ui-20260625/manifest.json`

确认无误后，我再生成 Figma 16:9 情绪板。

## Expected Figma Output After Confirmation

After the user confirms, create a Figma frame:

- Size: `1920 x 1080`.
- Same dark two-row grid template as the confirmation board.
- Uses the saved local images.
- Does not include descriptions or source labels unless explicitly requested.

Final response should include:

- Output folder path.
- Confirmation board path.
- Manifest path.
- Figma file URL or created frame status.
