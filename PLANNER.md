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

## Units (built 15 Nov, reworked same day)
- `courses/units.json`: `{units:[{name, assessment, note, versions:{'10MAG':{lessons, items:[{id}]}, '10MAA':{...}}}]}`.
  - A unit has a 10MAG version and/or a 10MAA version, side by side. Each version has its own subchapters and its own `lessons` (number of 79-min lessons). Lengths can differ.
  - A missing version = that stream doesn't do the unit. Items only in one version are highlighted yellow; ⇄ copies a version's subchapters to the other.
  - Library tags show use as U1G / U1A.
- **Saving:** edits are kept in the browser as a draft until **Save to GitHub**, which commits `courses/units.json` straight to the repo (GitHub API, using an access key kept in that browser via the 🔑 button). **Discard changes** drops the draft. The live site updates about 1 minute after a save.
- **Claude: the page commits to main too.** Always `git pull` before editing/pushing, and never overwrite `courses/units.json` without pulling first.
- Seeded from the 10MAA 2027 folder names (whole chapters, 10MAA only) — Rocco to edit.
- Page layout: 3 columns: Year 10 textbook (C10) | Year 11 textbook (G11) | Planned units.
