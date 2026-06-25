# Reference Image Scraper Rules

## Collection Rules

1. Use the Codex internal browser for Pinterest and Behance browsing.
2. If login is required, ask the user to log in manually in the browser. Never ask for or handle credentials.
3. Do not bypass platform login, paywalls, private content, anti-download restrictions, or technical access controls.
4. Save only images that are visible to the logged-in user during the browsing session.
5. Prefer direct visible image export/download when the site exposes an accessible image. Use screenshots or crops when direct export is blocked or unreliable.
6. Mark the capture method in `manifest.json` as `direct-image` or `screenshot`.
7. Preserve source URLs and visible creator/project names whenever possible.

## Output Rules

1. Create one output folder per task named `reference-images-<keyword-slug>-YYYYMMDD`.
2. Save all selected images in that folder with stable ordered filenames, for example `001-layout-neon-grid.jpg`.
3. Always create `manifest.json` in the same folder.
4. Always create `confirmation-board.png` before final Figma output.
5. Do not create the final Figma slide until the user confirms the PNG board.
6. The final response must include:
   - Output folder path.
   - Confirmation PNG path.
   - Manifest path.
   - Figma file/frame status, when Figma output was created.

## Manifest Rules

Each manifest item should include:

- `filename`
- `platform`
- `keyword`
- `category`
- `description`
- `source_url`
- `creator_or_project`
- `capture_method`
- `notes`

Keep source details in the manifest, not on the visual board.

## Visual Template Rules

All confirmation PNG boards and final Figma slides must follow the fixed template:

- Frame: `1920 x 1080`.
- Background: `#171719`.
- Text color: white.
- Title position: `x=60`, `y=48`, font size `32`.
- Category title positions: `x=60`, `y=205` and `x=60`, `y=638`, font size `26`.
- Image grid: two rows of five.
- Image slot size: `344 x 245`.
- X positions: `60`, `424`, `788`, `1152`, `1516`.
- Row y positions: `261` and `694`.
- Images should crop/fill to the slot.

The board must not include:

- Card borders.
- Long descriptions.
- Source labels.
- Beige or light moodboard backgrounds.
- Extra explanatory prose.

## Figma Rules

1. Load `figma:figma-use` before calling `use_figma`.
2. If a new Figma file is needed, load `figma:figma-create-new-file` before `create_new_file`.
3. Recreate the same visual template in Figma after user confirmation.
4. Use local saved images from the output folder.
5. Do not add source labels or descriptions to the final slide unless the user explicitly asks.

## Rights And Safety Rules

1. Treat all collected images as visual research references unless the user provides rights-cleared assets.
2. Do not claim ownership or commercial usage rights.
3. If the user intends external publication, remind them to verify source rights.
