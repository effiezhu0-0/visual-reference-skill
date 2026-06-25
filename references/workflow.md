# Reference Image Scraper Workflow

## Phase 1: Scope

Collect or infer:

- Search keywords or visual direction.
- Target platforms: Pinterest, Behance, or both.
- Desired count, usually up to ten images for the default template.
- Category grouping, usually two groups for the visual board.
- Figma target: existing file or new file.

Ask only when missing information would make the result materially worse. Otherwise make a reasonable default and state it briefly.

## Phase 2: Browse And Search

1. Open Pinterest and/or Behance in the internal browser.
2. Check login state.
3. If login is required, pause and ask the user to log in manually.
4. Search each keyword or category.
5. Browse results by scrolling and opening promising detail/project pages.
6. Prefer images that match the requested subject, visual style, medium, composition, color direction, UI pattern, or brand mood.

## Phase 3: Export Assets

1. Create `reference-images-<keyword-slug>-YYYYMMDD/`.
2. Save all selected images into that folder.
3. Use ordered, descriptive filenames.
4. Record metadata in `manifest.json`.
5. If only screenshots are possible, use them and mark `capture_method` as `screenshot`.

## Phase 4: Build Confirmation PNG

1. Run the bundled helper:

   ```bash
   python3 <skill-dir>/scripts/build_confirmation_board.py <output-folder>/manifest.json
   ```

2. Confirm that `confirmation-board.png` follows the dark 16:9 template.
3. Show the PNG to the user.
4. Ask the user to confirm, reject, or request changes.

## Phase 5: Revise If Needed

If the user requests changes:

- Replace off-target images.
- Reassign categories.
- Update filenames or manifest entries when needed.
- Regenerate `confirmation-board.png`.
- Ask for confirmation again.

Do not proceed to Figma until the user approves the PNG.

## Phase 6: Create Figma Moodboard

After confirmation:

1. Load required Figma skills.
2. Use a `1920 x 1080` frame.
3. Recreate the dark template exactly.
4. Place title, two category labels, and up to ten images.
5. Crop/fill images to the specified slots.
6. Return the created frame/file status.

## Exception Handling

- **Platform blocks direct image export**: Use screenshots/crops and record `screenshot` in the manifest.
- **Too many categories**: Merge into two meaningful visual groups for the board and keep original details in the manifest notes.
- **Fewer than ten images**: Fill only available slots; do not invent placeholders unless the user asks.
- **Missing source metadata**: Record what is visible and leave unknown fields empty rather than guessing.
- **User asks for final slide immediately**: Still create and show the PNG first unless the user explicitly waives confirmation.
