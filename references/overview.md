# Reference Image Scraper Overview

## Background

This skill supports early-stage visual research for design work. It helps an agent collect visual reference images from platforms such as Pinterest and Behance, preserve source metadata, create a reviewable confirmation board, and then generate an editable Figma moodboard only after the user confirms the collected assets.

## Scope

Use this skill for:

- Visual reference collection for UI style, brand visuals, campaign design, interactive experiences, illustration direction, layout systems, or color/mood exploration.
- Multi-platform inspiration gathering from Pinterest and Behance.
- Organizing scraped or captured reference images into one local folder with a manifest.
- Creating a dark 16:9 confirmation board that follows the fixed Figma template.
- Creating a final editable 16:9 Figma moodboard after user confirmation.

Do not use this skill for:

- Downloading private, paid, or restricted images.
- Claiming ownership or usage rights for collected references.
- Generating final production-ready licensed assets.
- Creating a final Figma board before the user has approved the confirmation PNG.

## Core Concepts

- **Reference image**: A visual example collected for research and direction setting. It is not assumed to be licensed for production use.
- **Asset-export method**: The best available lawful capture method in the browser session. Prefer direct visible image export when available; use screenshots or crops when direct export is unreliable or blocked.
- **Manifest**: A `manifest.json` file that records every image, source URL, platform, category, description, creator/project name when visible, and capture method.
- **Confirmation board**: A local `confirmation-board.png` shown to the user before Figma output. It uses the same visual template as the final slide.
- **Figma moodboard**: The final editable 16:9 Figma board generated only after the user confirms the PNG.

## Required Visual Direction

The visual board is intentionally image-forward:

- Dark charcoal background.
- White title and category labels.
- Two category rows.
- Five image slots per row.
- No card borders, long descriptions, source labels, beige backgrounds, or decorative prose on the board.

Detailed source context belongs in `manifest.json`, not on the visual board.
