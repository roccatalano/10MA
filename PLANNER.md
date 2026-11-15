# 10MA planner spec

## Data
- `library/C10.json`, `library/G11.json` — one entry per subchapter:
  `id, book, chapter, chapter_title, sub, title, pages, learning_intentions[], examples[], exercise{building_understanding, fluency, problem_solving, reasoning, enrichment}, tenA (bool, C10 only), vc2_codes[] (C10 only), notes`
- `courses/10MAG.json`, `courses/10MAA.json` — units in order: `{unit, title, assessment, cards: [ids]}`
- `courses/years/<year>.json` — dates only (term dates, lesson counts), so the plan is reusable.

## Planner page (planner/index.html)
- **Library tab:** every card, filter by book / chapter / used by 10MAG / 10MAA / unused.
- **Course tabs:** 10MAG and 10MAA unit lists with their cards.
- **Year tab:** plan laid against term dates.

## Build order
1. Index C10 (all chapters) → library/C10.json
2. Index G11 → library/G11.json
3. Browse page
4. Rocco picks units for each stream (start from the current 10MAA 2027 unit list)

## Units (built 15 Nov)
- `courses/units.json` = the saved unit plan: `{units:[{name, streams:[10MAG|10MAA], assessment, note, items:[{id, lessons}]}]}`. Units are shared across both streams; a unit's `streams` says who does it.
- The planner page saves edits in the browser (localStorage = the browser's own storage, one computer only). To make changes permanent/shared: **Export units** → give the file to Claude → Claude commits it to `courses/units.json`. **Reset** throws away browser edits and reloads the repo version.
- Seeded from the 10MAA 2027 folder names (whole chapters, 1 lesson each) — Rocco to edit.
- Page layout: 3 columns: Year 10 textbook (C10) | Year 11 textbook (G11) | Planned units. Chapter cards hold nested VC2 + chapter-resources cards; click a subchapter for its lesson-plan fields.
