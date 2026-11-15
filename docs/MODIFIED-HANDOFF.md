# Handoff: plan and build the whole 10MAG Modified curriculum

Written 16 Nov 2026. Read `CLAUDE.md`, `PLANNER.md`, `docs/HANDOVER.md`, then this. **`git pull` first, and again before every push** (the planner page commits to the repo too).

## The goal
Every 10MAG unit gets a **10MAG Modified** version at **Year 7–8 level** for students on a modified program. It runs alongside 10MAG lesson for lesson:
- **Same units, same lessons, same CFAT weeks and skills.** The modified students sit their CFAT in the same lesson as everyone else.
- For each lesson: a **modified worksheet** (Cambridge 7/8/9 Example → You try pairs) and its **Freefall sheets** (practice).
- For each unit: a **modified unit workbook** (cover, then worksheet and Freefall sheets per lesson) and **modified CFATs** (code = 10MAG code + M, e.g. `CFAT 1.9.1M`).
- No modified slides (Rocco, 16 Nov: not important).

**Done (pilot): G1 Univariate Statistics.** Use it as the model for everything else. Rocco still has to review it, so check the decisions log for his feedback before copying its choices.

## Rules (Rocco's; don't change without asking)
1. **Never write questions.** Copy verbatim from the books and cite. Rewording a stem so a single part stands alone, or keeping only some parts, is OK but must say "adapted: …" in the source.
2. **Level:** Cambridge Essential Mathematics **7 and 8** first. Use **Cambridge 9** only where the skill is first taught in Year 9 (e.g. box plots, trigonometry, simultaneous equations). Say so in the decisions log when you do.
3. **Freefall is licensed to the school.** Never copy Freefall pages or files into this repo, and never publish them on the website. The workbook goes to G: only; the planner may link to it via its Google Drive URL (Rocco, 16 Nov: "you can link it all"), because only staff with shared-drive access can open it. `courses/freefall.json` (titles + page numbers only) is fine to keep in the repo.
4. **Freefall 8 is the Teacher Edition.** Each topic is notes page, worksheet, answers (then worksheet, answers … for multi-sheet topics). The workbook builder keeps the notes + worksheets and drops the answer pages; check by eye on every new workbook. Freefall 7 and Velocity 9 are Student Editions (all pages usable).
5. **Log every decision** in `courses/cfat-log.json` (shown on the planner: Lesson planning → CFAT planning). Especially: which Year 7–9 subchapters each lesson uses, and every gap decision.
6. CFAT house rules from `docs/CFAT-HANDOFF.md` still apply (2 A4 pages max, never a lone MC, answer spaces, solutions copy, no sources on the student copy).

## Sources (G: `02 Sources`)
- `2024 - Essential Mathematics for the Victorian Curriculum 7 / 8 / 9 Third Edition.pdf`
- `Freefall Modified Activities/`: `FREEFALL7STUDENT.pdf`, `FREEFALL8TEACHER.pdf`, `FreefallVelocity9Student.pdf` (+ docx copies)
- Year 7–9 chapter checklists are already indexed: `tools/data/checklist7.json`, `checklist8.json`, `checklist9.json` (some `text` fields are cut short: check against the book).
- Text extraction that works: `pdftotext -raw` then split on `\f` (form feed) to get PDF pages. The text order inside a page is jumbled (worked examples, Now you try and margin notes interleave), so **always render the page to an image and look** before copying a question, and for any table, dot plot, box plot or graph. Redraw graphics in house style (`tools/worksheets/ch9.py` helpers, `tools/cfat/gen_ch9.py` helpers); never paste screenshots.

## How the pilot was built (copy this recipe per unit)
| Step | File | Notes |
|---|---|---|
| Freefall sheet → subchapter map | `courses/modified.json` → `sheets` | Draft for all 10MAG subchapters exists. Rocco edits it on the planner (click a Modified lesson: ✕ / add a sheet) and ticks **Freefall mapping approved** per unit (`approved`). |
| Modified worksheets | `tools/worksheets/ch9m.py` (unit-specific content) | Per lesson: title box `9AM`, Learning intentions + Key ideas (verbatim from the Y7–9 subchapter), 2–3 Example → You try pairs (questions only), skills checklist ("I can…" from the Y7–9 chapter checklist, no e.g.), sources line. Output `lessons/C10-<sub> modified worksheet[ (part n)].html/.pdf`. Part n when a subchapter spans two lessons. |
| Modified CFAT questions | `tools/cfat/gen_ch9m.py` | Adds level **L0** items to `tools/cfat/C10-<sub>.json`. **Run after `gen_ch9.py`**, because `gen_ch9.py` rewrites the blocks without L0. Skill `n` restarts at 1 in each subchapter's block (key L0 items by `(sub, n)`). One L0 question per skill; two per skill in short weeks (<6 skills). Must not reuse any worksheet question. |
| Modified CFAT papers | `python3 tools/cfat/paper.py 10MAGM <n> "<unit>"` | Stream `10MAGM` reads 10MAG's CFAT groupings, uses only L0, codes `<unit>.<chapter>.<n>M`, title "10MAG Modified". 10MAG/10MAA papers are untouched. Print to PDF and check 2 pages. |
| Modified workbook | `python3 tools/worksheets/workbook_m.py "<unit>" "<Freefall folder>" <out dir outside repo>` | Refuses to write inside the repo. Each Freefall sheet appears once per unit (first lesson that maps it). |
| Deliver | `device_commit_files` | Worksheet PDFs + workbook → G: `01 Lesson materials`; CFAT M PDFs → G: `03 Assessments`. |
| Link on planner | `courses/modified.json` → `materials["10MAG|<unit>"]` | `cfats` [{n, html, solutions}], `worksheets` {lesson index from 0: html path}, `workbook`, `workbook_url` (Drive URL: find it with the Google Drive connector, `title contains '...'`). The planner reads these automatically. |
| Log + handover | `courses/cfat-log.json`, `docs/HANDOVER.md` | |

**Next session should generalise first:** move the shared page/render code out of `ch9m.py` into `tools/worksheets/modified.py` and put each unit's content in its own file (e.g. `tools/worksheets/mod_algebra.py`); same for `gen_ch9m.py` → one L0 generator per chapter. Keep the G1 output identical (diff the HTML before/after).

## Units still to do (in 10MAG order) and a starting map
Lesson groupings and CFAT weeks come from `courses/lessons.json` (`plans`, `cfats`), so re-read them; Rocco may have changed them. The Year 7–9 picks below are **suggestions** from the contents pages: confirm by reading each subchapter.

| Unit | 10MAG subchapters | Suggested Year 7–9 sources | Freefall (draft map) | Gaps to decide with Rocco |
|---|---|---|---|---|
| **G2 Sequences and Recursion** | none yet | Y7 2H Number patterns, 2I Spatial patterns, 2J Tables and rules | FF7 10-01, FF8 06-01 Number patterns | Unit has no subchapters: Rocco must pick the C10 content first. Skip until he does. |
| **G3 Algebra and Linear Relations** (1A–1C, 1E–1L) | 1A review of algebra · 1B linear equations · 1C inequalities · 1E graphing lines · 1F equation of a line · 1G length, midpoint · 1H parallel, perpendicular · 1I–1K simultaneous equations · 1L regions | 1A ← Y8 5C, 5D, 5G (Y7 4B substitution) · 1B ← Y8 7A–7E · 1C ← Y8 7I–7J · 1E ← Y8 9B, 9F · 1F ← Y8 9C (Y9 4G) · 1G ← Y9 4H (Y8 4K–4L Pythagoras) · 1H ← Y8 9G gradient / Y9 4I · 1I–1K ← Y8 9D graphical solutions, Y9 4K; algebraic methods only in Y9 2I–2K (EXTENDING) · 1L ← Y8 9E using graphs to solve inequalities | mapped except 1I, 1J, 1L | **1I, 1J, 1L have no Freefall.** Options: Cambridge 8/9 exercise pages as practice, closest Freefall (FF8 14-05 straight lines), or leave unmodified. 10MAG has 5 CFATs here (3.1.1–3.1.5). |
| **G4 Quadratics and Parabolas** (5A–5C) | expanding · factorising · algebraic fractions | 5A ← Y8 5G (Y9 8A) · 5B ← Y8 5H (Y9 8C) · 5C ← Y8 5F (EXTENDING) | mapped (FF8 06-10 to 06-14) | No parabola work in Y7–8: fine, the 10MAG unit only has 5A–5C. |
| **G5 Bivariate Data** (9C, 9H–9J) | two-way tables · time-series · scatter plots · line of best fit | 9C ← reuse the G1 L3 worksheet (Y8 8J) · 9H ← Y7 8D Line graphs, Y8 8A Interpreting graphs · 9I, 9J ← no Y7–9 Cambridge subchapter: check Y9 9G–9L and Y8 8A exercises | 9C, 9H, 9I mapped | **9J no match anywhere**; 9I thin (FF8 08-10, 08-11 scatter only). |
| **G6 Trigonometry and Measurement** (4E–4G, 4I, 4K, 6A–6D) | length · Pythagoras · area · surface area · volume · trig ratios, angles, 2D, bearings | 4E ← Y8 4A–4B · 4F ← Y8 4K–4M · 4G ← Y8 4C–4E · 4I ← Y8 4G (Y9 5F–5G) · 4K ← Y8 4H–4I · 6A–6D ← Y9 3E–3J (trig is first taught in Year 9) | measurement well mapped | **6A–6D no Freefall.** Cambridge 9 pages as practice, or unmodified. |
| **G7 Networks** (2K–2N) | networks, Euler, shortest path | none in Cambridge 7–9 | none | **Whole unit has no Year 7–9 source.** Ask Rocco: unmodified 10MAG with support, or a simplified version (would need his OK to adapt). |
| **G8 Probability** (8A–8D, 8F) | review · Venn and two-way · addition rule · conditional · tree diagrams | 8A ← Y7 8G–8I, Y8 8G · 8B ← Y8 8J (Y9 9B–9C) · 8C ← Y8 8J ('or' examples) · 8D ← Y8 8J Example 17 b–c ('given that') · 8F ← Y8 8I Tree diagrams (Y8 8H two-step) | mapped except 8D | **8D no Freefall** (FF9 03-07 two-way tables is closest). |

Avoid re-using a Year 7–9 Example in two units (e.g. Y8 8J is in G1, G5 and G8): pick different Examples or exercise questions, and record which ones are used.

## Order of work (suggested)
1. Generalise the pilot code (above), check G1 rebuilds identically.
2. Ask Rocco the open questions in one go (AskUserQuestion): G2 content, Networks, the gap subchapters (1I, 1J, 1L, 9J, 6A–6D, 8D), and whether he's reviewed G1.
3. G3 Algebra (biggest, 5 CFAT weeks), then G8, G6, G4, G5, G7, G2.
4. Per unit: map lessons → Y7–9 subchapters (log it) → worksheets → L0 CFAT items → CFAT papers → workbook → deliver to G: → link → log → handover → push. Send Rocco each unit as it's done.

## Checks before delivering each unit
- Render every worksheet and CFAT page to an image and look (2 pages max per CFAT; no question split across pages; graphs readable; blank answer spaces on the student copy, red answers on the solutions copy).
- Every question has a `src` citation with page number; any change is labelled "adapted".
- Work every answer yourself; for a large unit, have a separate agent re-check the solutions.
- Workbook: scan the Freefall pages for any answer page (handwritten-style blue answers in the boxes).
- `git ls-files | grep -i freefall` should only list `courses/freefall.json`.

## Gotchas from the pilot
- **Don't run `git clean` with a pathspec like `'*.pdf'`**: it deleted untracked PDFs across the whole repo (pilot worksheets had to be restored from the delivered copies). CFAT PDFs are not committed (they live on G:); worksheet PDFs are.
- `paper.py` with a glob of `assessments/*.html` will re-print everyone's CFATs: pass exact file names.
- KaTeX for the worksheet builder: `mkdir -p /home/claude/kx && cd /home/claude/kx && npm i katex@0.16.11`.
- Stage the source PDFs with `device_stage_files` (they arrive under `/mnt/user-data/uploads/10MA Course Planner/02 Sources/...`).
- The planner's 4-column 10MAG view (10MAG lessons | 10MAG assessments | Modified lessons | Modified assessments) reads `courses/modified.json`; test with a local server (`python3 -m http.server` in the repo root, open `/planner/`).

## Kick-off prompt for a new session
> Read CLAUDE.md, PLANNER.md, docs/HANDOVER.md and docs/MODIFIED-HANDOFF.md in roccatalano/10MA. Then plan and build the complete 10MAG Modified curriculum following MODIFIED-HANDOFF.md: generalise the G1 pilot code, ask me the open questions in one go, then do the units in the suggested order, sending me each unit as it's finished.
