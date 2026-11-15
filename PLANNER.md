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

## Units (built 15 Nov; split into two lists same day)
- `courses/units.json`: `{units:[{name, stream:'10MAG'|'10MAA', lessons, assessment, note, items:[{id}]}]}`. Order in the array = teaching order within each stream.
- Two separate unit lists side by side (10MAG | 10MAA). Each unit belongs to one stream and has its own subchapters, number of 79-min lessons and assessment type.
- Unit numbers: G1, G2… (10MAG) and A1, A2… (10MAA). Library tags show where a subchapter is used.
- ⧉ copies a unit to the other stream. Dragging a subchapter between units in the same stream moves it; to the other stream copies it.
- **Saving:** edits are kept in the browser as a draft until **Save to GitHub**, which commits `courses/units.json` straight to the repo (GitHub API, using an access key kept in that browser via the 🔑 button). **Discard changes** drops the draft. The live site updates about 1 minute after a save.
- **Claude: the page commits to main too.** Always `git pull` before editing/pushing, and never overwrite `courses/units.json` without pulling first.
- Seeded from the 10MAA 2027 folder names (whole chapters, 10MAA only) — Rocco to edit.
- Page layout: 3 columns: Year 10 textbook (C10) | Year 11 textbook (G11) | Planned units.

## 2027 tab (built 15 Nov)
- Tabs at the top: **Unit planning** (the 3-column page) | **2027**.
- Dates: `courses/years/2027.json` (Vic gov term dates, public holidays in term: Labour Day 8 Mar, King's Birthday 14 Jun, Melbourne Cup 2 Nov; 4 sessions a day, 3 on Wednesdays, 79 min).
- Timetable: `courses/timetable.json` = `{classes:[{id,teacher,stream}], stepup:{start,end}|null, days_off:{date:reason}, slots:{classId:{date:[session numbers]}}}`. Saved to GitHub by the same Save button as the units.
- Classes: Ms Chan, Mr Amon, Mr Lloyd, Mr Catalano (10MAG); Mr Catalano (10MAA). Pick one (◀ ▶ / arrow keys), click sessions to give it lessons; "→ term / → year" copies a week's pattern forward. "All classes" shows everyone, red outline = same teacher twice in a session.
- Lessons are numbered in date order (Step Up week first) and laid onto that stream's units in order using each unit's lesson count; a unit with no lesson count is skipped.
- Step Up week defaults to 30 Nov–4 Dec 2026 (a guess; editable on the tab).
