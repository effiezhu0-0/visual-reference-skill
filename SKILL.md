---
name: reference-image-scraper
description: Browse Pinterest and Behance in Codex's internal browser, guide login when needed, search user-provided visual keywords, click into relevant result/detail pages, save related reference images with the asset-export method into one organized folder, generate a PNG confirmation board pairing categories/descriptions with images, and after user confirmation create a 16:9 presentation slide in Figma via the Figma MCP. Use when the user asks for Pinterest/Behance image scraping, visual reference collection, moodboard asset export, reference-image folders, PNG review boards, or Figma presentation slides from collected references.
metadata:
  short-description: Scrape Pinterest/Behance references into a Figma slide
---

# Reference Image Scraper

## Purpose

Use this skill to collect reference images from Pinterest and Behance, preserve source metadata, save all chosen images into one folder, create a PNG confirmation board, and only after user approval build a 16:9 presentation slide in Figma.

## Reference Files

Read these files only when needed:

- `references/overview.md`: background, scope, concepts, and visual direction.
- `references/rules.md`: collection rules, output rules, manifest requirements, Figma rules, and rights boundaries.
- `references/workflow.md`: detailed phased workflow, revision loop, and exception handling.
- `examples/input-01.md` and `examples/output-01.md`: sample task and expected output format for QA or regression checks.

## Required Visual Template

All PNG confirmation boards and final Figma slides MUST follow the user's fixed Figma template:

- Reference Figma node: `https://www.figma.com/design/xYlbfA0qLquW7Ht0PEcpXX/AI%E5%B7%A5%E4%BD%9C%E6%B5%81%E5%B0%9D%E8%AF%95?node-id=88-3&m=dev`
- Canvas/frame: 16:9, preferably `1920 x 1080`.
- Background: solid dark charcoal `#171719`.
- Typography: white text, PingFang SC Medium when available.
- Top title:
  - Position: `x=60`, `y=48`.
  - Font size: `32px`.
  - Text should be the board/project title, e.g. the search keywords or visual direction.
- Category section titles:
  - First row title at `x=60`, `y=205`, font size `26px`.
  - Second row title at `x=60`, `y=638`, font size `26px`.
  - Use concise category names. If there are more than two categories, merge them into two meaningful groups for the board.
- Image grid:
  - Two rows of five images.
  - Each image slot is `344 x 245`.
  - Top row y-position: `261`; bottom row y-position: `694`.
  - X positions: `60`, `424`, `788`, `1152`, `1516`.
  - Images should fill/crop to the slot, preserving visual quality.
- Do not use card borders, long descriptions, source labels, beige backgrounds, or multi-line prose on the confirmation board. Keep the board image-forward and close to the Figma template.
- Keep detailed descriptions, source URLs, creator/project names, and capture methods in `manifest.json`, not on the visual board.

Primary sites:
- Pinterest: `https://www.pinterest.com/`
- Behance: `https://www.behance.net/`

## Required Tooling

- Load and use the `browser:browser` skill for Codex internal browser navigation, login checks, search, clicking, scrolling, screenshots, and local preview verification.
- Use the `asset-export` method for saving user-requested related images:
  - Prefer direct visible image export/download from detail pages when available.
  - Use screenshot/crop capture when direct export is blocked or unreliable.
  - Never bypass login, paywalls, private content, or anti-download restrictions.
- Load `figma:figma-use` before any `use_figma` call.
- If a new Figma file is needed, load `figma:figma-create-new-file` before `create_new_file`, then load `figma:figma-use` before writing nodes.

## Workflow

1. Clarify the collection scope only when necessary: keywords, platform(s), approximate image count, categories, and whether the Figma output should go into an existing file or a new file.
2. Create one output folder under the active workspace. Use a stable name such as `reference-images-<keyword-slug>-YYYYMMDD`.
3. Open the requested platform(s) in the internal browser:
   - Pinterest: `https://www.pinterest.com/`
   - Behance: `https://www.behance.net/`
4. Check login state.
   - If the site is not logged in and login is required to view or save useful results, pause and ask the user to log in inside the browser.
   - Do not ask for credentials. Continue after the user logs in.
5. Search the user-provided keywords. If multiple style directions are provided, search each direction separately and treat each as a category unless the user supplies their own categories.
6. Browse result pages by scrolling and clicking into relevant detail/project pages. Prefer images that visibly match the requested subject, art direction, composition, medium, color, UI pattern, campaign style, or category.
7. Save selected images into the single output folder using stable filenames:
   - `001-<category-slug>-<short-title>.jpg`
   - `002-<category-slug>-<short-title>.png`
8. Record source metadata in `manifest.json` in the same output folder. Include filename, platform, keyword, category, description, source page URL, creator/project title when visible, and capture method.
9. Generate a PNG confirmation board from the manifest:
   - The board MUST use the "Required Visual Template" above.
   - If the bundled helper does not match the required template, create or adapt a local generator for the active workspace that renders the exact dark 16:9 two-row grid.
   - The output filename must remain `confirmation-board.png` next to the manifest.
   - Show the PNG to the user and ask for confirmation before creating the Figma slide.
10. After user confirmation, use Figma MCP to create a 16:9 presentation slide:
   - Frame size: `1920 x 1080`.
   - Recreate the same "Required Visual Template" in Figma.
   - Use two category title rows and ten image slots when ten images are collected.
   - Do not add descriptions or source labels on the slide unless the user explicitly asks; source details stay in `manifest.json`.
   - Use the local saved images from the output folder.
11. Final response should include the output folder path, the confirmation PNG path, the manifest path, and the Figma file/frame status.

## Source And Attribution Rules

- Save only assets visible to the logged-in user during the browsing session.
- Keep source URLs and creator/project names whenever visible.
- Mark each asset as `direct-image` or `screenshot` in `capture_method`.
- Do not claim ownership of exported images. Treat outputs as visual research/reference material unless the user provides rights-cleared assets.
- If a site blocks direct downloads, use browser screenshots/crops and label the capture method clearly.

## Output Folder Structure

```text
reference-images-<keyword-slug>-YYYYMMDD/
├── 001-<category>-<short-title>.jpg
├── 002-<category>-<short-title>.png
├── manifest.json
└── confirmation-board.png
```

Recommended `manifest.json` shape:

```json
{
  "title": "Reference image board",
  "created_at": "YYYY-MM-DD",
  "platforms": ["pinterest", "behance"],
  "keywords": ["keyword one", "keyword two"],
  "items": [
    {
      "filename": "001-layout-neon-grid.jpg",
      "platform": "pinterest",
      "keyword": "interactive campaign visual",
      "category": "Layout",
      "description": "Dense modular composition with high-contrast image blocks.",
      "source_url": "https://...",
      "creator_or_project": "Visible creator/project name if available",
      "capture_method": "direct-image",
      "notes": ""
    }
  ]
}
```

## Confirmation PNG Helper

Run:

```bash
python3 <skill-dir>/scripts/build_confirmation_board.py <output-folder>/manifest.json
```

The helper creates `confirmation-board.png`. Read or patch the script only when the board layout needs customization.
