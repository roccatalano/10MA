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
- Classes: Ms Chan, Mr Amon, Mr Lloyd (10MAG); Mr Catalano (10MAG + 10MAA, one merged view: clicking a session cycles 10MAG → 10MAA → empty). Pick a teacher (◀ ▶ / arrow keys), click sessions; "→ term / → year" copies a week forward (all that teacher's classes). "All classes" shows everyone, red outline = same teacher twice in a session.
- Lessons are numbered in date order (Step Up week first) and laid onto that stream's units in order using each unit's lesson count; a unit with no lesson count is skipped.
- Step Up week defaults to 30 Nov–4 Dec 2026 (a guess; editable on the tab).

## Lesson planning tab (built 15 Nov)
- Tabs: Unit planning | Lesson planning | 2027. Stream switch 10MAG / 10MAA; unit cards follow `courses/units.json` (order, names, subchapters).
- `courses/lessons.json` = `{plans:{"<stream>|<unit name>":[{kind:'teach'|'review'|'assess', items:[{id}], note}]}}`. A subchapter in 2+ lessons = split ("1 of 2"); 2 ids in one lesson = combined. Subchapters removed from a unit drop out; new ones show under "Not in a lesson yet". A unit with no plan defaults to 1 lesson per subchapter + review + assessment. Renaming a unit loses its plan (key is the name).
- "Use N" sets the unit's lesson count on Unit planning to the plan's length (feeds the 2027 tab).
- Claude's first suggestion (15 Nov): 10MAG slow (most subchapters 2 lessons); 10MAA standard (1 each; heavy ones split, light pairs combined: G2A+2B, G1E+1F, G4A+4B, G8E+8F). Every unit ends Review + its assessment.
- **CFATs (15 Nov, rebuilt):** 1 CFAT = 1 week = 3 × 79-min lessons; groupings chosen for similar content, then each week's lessons laid out under it; kind `practice` = consolidation lesson in a short week. `lessons.json` also has `cfats:{"<stream>|<unit>":[{items:[{id}],note}]}`. Purple strip at the top of each open unit: drag subchapters between CFATs, ✕ remove, ↑ reorder, drop on "+" for a new one. Each CFAT shows in the lesson list after the last lesson that teaches any of its subchapters; lesson chips carry C1, C2… Claude's first grouping = similar content per CFAT (e.g. 10MAA Indices: index laws 3A–3D | exponentials 3E–3F | logs 3I–3L | surds 4A–4D).

## Lesson materials in the repo (15 Nov)
- Finished materials live in `lessons/` (served on the public site so teachers without G: access can open them): `C10-1A worksheet.html/.pdf` …, `<stream> <unit name> - Unit workbook.pdf`.
- Library cards: `materials:[{kind,title,html,pdf}]` → "Lesson materials" box at the top of the card + 📄 on the library list.
- `lessons.json` `materials:{"<stream>|<unit>":[{kind,title,pdf}]}` → "Unit materials" box under the CFATs (slides, workbook, plus each subchapter worksheet in plan order).
- Unit workbook = subchapter worksheet PDFs merged in Lesson planning order (rebuild if the order changes).

## Do Now (15 Nov, Rocco's idea)
- Each subchapter card holds a `retrieval` pool: verbatim questions ABOUT ITSELF (C10: progress quiz + chapter review SA/MC, one part each, KaTeX in `stem`/`tex`, `src`, `page`, `tenA`). Ch1 done (84 items, `tools/donow/c10_ch1_pool.py`); questions needing a graph/number-line picture left out for now.
- `planner/donow.js` picks each lesson's Do Now from the plan: 3 questions = last lesson · 3–6 lessons back · 7+ back (falls back when a slot is empty); each question once per stream; 10A items skipped for 10MAG. Review/assessment lessons get none.
- Lesson planning shows the picks under each lesson + "Sheet ↗"; Unit materials has "Do Now sheets ↗" (whole unit).
- `planner/donow.html?s=10MAA&u=1[&l=8]`: A4, two identical half-page copies per sheet (cut line), KaTeX, cited. Uses the browser's unsaved drafts if any, so it matches the planner.
