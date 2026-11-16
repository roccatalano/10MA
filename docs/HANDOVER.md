# Handover

## 15 Nov 2026 — repo created
- Decided: subchapter library across C10 + G11, courses pick cards. Supersedes the per-unit handout approach in 10MAA 2027.
- Next: index C10, then G11.
- Current 10MAA 2027 units (for reference): 1 Algebra & Linear Relations (C10 Ch1), 2 Data Analysis (G11 Ch2 & 7), 3 Indices/Logs/Exponentials/Surds (C10 Ch3 & 4), 4 Sequences & Finance (G11 Ch1 & 3), 5 Trig & Unit Circle (C10 Ch6 & 4), 6 Quadratics & Parabolas (C10 Ch5 & 7), 7 Matrices & Networks (G11 Ch4 & 8), 8 Probability (C10 Ch8), 9 Functions & Polynomials (C10 Ch10, extension).
- Open: 10MAG unit list; question sources per lesson part; burnt-items rule; G: folder for finished materials.

## 15 Nov 2026 — Chapter 1 test run (C10)
- `library/C10.json`: Chapter 1 card + 12 nested subchapter cards. `planner/index.html` shows them (chapter card → click subchapter → lesson-plan fields).
- Fields per subchapter, with sources:
  - Learning intentions: start of subchapter (verbatim).
  - Success criteria: C10 chapter checklist items for that subchapter.
  - VC2: chapter codes printed in the book, assigned to subchapters by Claude (Level 9 review codes on consolidating subchapters); 10A codes tagged.
  - Key vocab: bold terms in Key ideas (book has no glossary) + a few LI terms where none were bold.
  - Videos: found by web search (Class Mathematics pages match Cambridge subchapter names; Khan Academy). Rocco to vet. 1L has none yet.
  - APK: Cambridge Y7/8/9 chapter checklist items (skill + e.g. question), one per year where possible.
  - Do Now: last lesson / earlier this chapter / previous year, from C10 progress quiz + review MC (labelled by subchapter) and C9 progress quizzes. Each item used once.
  - Exit tasks: C10 checklist e.g. questions (students tick each skill).
- Question text from pdftotext is a LOCATOR only (fractions garble): extract verbatim on first use.
- Indexed (not yet in library): all 114 C10 subchapters at basic level (tools/parse.py), Y7–Y10 checklists.
- 15 Nov later: 3-column planner + draggable units (courses/units.json). All C10 + G11 subchapters loaded at basic level.
- Open: Rocco to review the test run; MC4 assumed 1D (check); 1J has no PQ/MC item so its Do Now uses review SA Q15.

## 15 Nov 2026 (evening) — state at hand-off to the new Project
**Built:** planner page https://roccatalano.github.io/10MA/ (3 columns: C10 library | G11 library | two unit lists 10MAG / 10MAA). Saves `courses/units.json` straight to GitHub (Rocco's browser has the key).
**Library:** C10 all 10 chapters + Ch11 activities + semester reviews (basic); C10 Ch1 has FULL lesson-plan fields (the test run). G11 all chapters (basic: titles + pages only).
**Units (Rocco's plan, 15 Nov):** see `courses/units.json` — always read it fresh (`git pull`), Rocco edits it on the page.
**Open / next jobs (agreed order):**
1. Rocco reviews the C10 Ch1 test run fields (LIs, success criteria, VC2 mapping, key vocab, videos, APK Y7→9, Do Now, exit tasks, Example→Now you try).
2. Fill the same fields for every chapter used in a unit, one chapter at a time (tools/ has the scripts; Y7–10 checklists already parsed in the work notes — re-run tools/items.py).
3. Index G11 properly (LIs, examples, exercises, chapter review / checklist) and add E11 (Edrolo) exam questions for G11-based units.
4. Year tab: lay units against 2027 term dates (needs Rocco's term-dates file).
5. Then lesson materials per the 12MAG model: guided slides, guided worksheet + solutions, bound reference entry.
**Gaps seen in units.json (15 Nov):** 10MAG 'Sequences and Recursion' has 12 lessons but no subchapters; 9C is in two 10MAG units; most 10MAA units have no lesson count yet.

## 15 Nov 2026 (night) — lesson-plan fields for every C10 subchapter in a unit
- Rocco: Ch1 test-run method is fine as is. Scope = only subchapters placed in units (not the whole book).
- Filled 60 C10 cards (2K–2N, 3A–3F, 3I–3L, 4A–4G, 4I, 4K, 5A–5J, 6A–6H, 7A–7F, 8A–8D, 8F, 9A–9E, 9H–9J): VC2, success criteria, exit tasks, key vocab, videos, APK (Y7→9), Example→Now you try flags. Same sources and method as Ch1.
- **Do Now left empty on purpose** (`do_now_note: waiting for lesson groupings`): its slots are "last lesson / earlier this chapter", so it can only be filled once Rocco groups subchapters into lessons.
- No video found yet: 2N, 3L (the Class Mathematics page for it holds polynomial content), 6E, 9H. All videos still need Rocco to vet; 5C link pattern not checked (site blocked).
- Scripts + parsed checklists now saved in `tools/` and `tools/data/` (see tools/README.md), so nothing needs re-extracting.
- Checklist parser fixes: 10A-tagged labels, label on the same line as the item, "checklist and success criteria" heading (C9 Ch7–8 were missing).
- Next: G11 units (Ch 1, 2, 3, 4, 7, 8) need proper indexing first (LIs, examples, chapter review), then the same fields; G11 has no "I can" checklist, so success criteria/exit tasks need another source (chapter review or Edrolo) — Rocco to choose. Then Do Now once lessons are grouped.

## 15 Nov 2026 (night, later) — G11 cards filled
- Rocco's rules for G11: LIs from the start of each subchapter; success criteria + exit tasks from the chapter Skills checklist; key definitions from the glossary; worked examples + Now try this; Do Now from **Edrolo U1&2 VCAA exam questions** (for the lesson after the subchapter); APK not decided, so Claude used **C9/C10 checklist skills** (Rocco to confirm).
- Filled all 46 G11 subchapters in units (1A–1F, 2A–2I, 3A–3I, 4A–4I, 7A–7E, 8A–8H). New fields: `key_definitions`, `edrolo_lessons`, `do_now_pool`. The planner card shows them.
- Edrolo is the 2020 edition (old study design): 230 unique VCAA questions, mostly in "Questions from multiple lessons". Each is matched to a G11 subchapter by its content, so **check the matches**. Not matched: 95 (mostly geometry/linear topics outside these units). No Edrolo lesson for 4G–4H (transition matrices). Empty pools: 1E 1F 2B 2G 3B 3F 4A 4B 4C 4F 4G 4H 7A 8E 8F 8H.
- Book has no LI box for 1B, 1D, 1E, 1F. Some examples have no Now try this in the book (e.g. 2A Ex 1–4, 2G).
- No video yet: 2G, 4G, 4H. Videos are from Class Mathematics VIC Y11 General; Rocco to vet.
- Next: Rocco groups lessons → then fill Do Now slots (C10 from progress quiz/review; G11 from do_now_pool).
- **Correction (Rocco):** G11 cards use the **VCE Mathematics Study Design 2023** (02 Sources/2023MathematicsSD.docx), not VC2. Each G11 card has `study_design` = General Maths U1&2 content dot points (`GM-U1-AoS2-c8` etc.) + Outcome 1 key knowledge (`kk`), mapped by Claude (`tools/sd.py`, `tools/sd_map.py`). Recurrence/explicit-rule formulas didn't survive the docx text extract; those dot points say so.

## 15 Nov 2026 (late) — 2027 tab
- Added the 2027 tab (see PLANNER.md): term calendar, 4 sessions/day (3 Wed), 5 classes, Step Up week from 2026, timetable saved to `courses/timetable.json`.
- Open: real timetables (not out yet); Step Up dates (guessed 30 Nov–4 Dec 2026); pupil-free days (mark by clicking a date); fortnightly timetable not supported yet (copy is week-by-week); Step Up lessons currently count as the first unit lessons; 10MAG unit 1 has no lesson count so it is skipped.

## 15 Nov 2026 (late) — Lesson planning tab
- Added the Lesson planning tab + `courses/lessons.json` with Claude's suggested grouping (see PLANNER.md). Rocco to review/edit and press "Use N" to push lesson counts to the units.
- Next once groupings are agreed: fill Do Now slots per lesson (C10 progress quiz/review; G11 do_now_pool).
- CFAT sequence added for every unit (46 CFATs: 10MAG 16, 10MAA 30 — see lessons.json `cfats`). Rocco to review. Sequences and Recursion (10MAG) has none (no subchapters yet).
- Rebuilt same night: **1 CFAT = 1 week = 3 × 79-min lessons** (Rocco: classes get 3 lessons a week). 10MAG 20 weeks, 10MAA 34 weeks; + Review + Assessment per unit. Practice lessons fill short weeks.

## 15 Nov 2026 (late) — Ch1 worksheets moved + APK fixed
- Rocco's Ch1 worksheet HTMLs (old 10MAA 2027 'Lesson Handouts' folder = archive) copied to `01 Lesson materials` as `C10-1A worksheet.html/.pdf` … `C10-1L`.
- Their "Activating prior knowledge" used the same subchapter's Building understanding Qs; replaced with the library's APK picks (Y7/8/9 chapter checklist skill + e.g. question), retyped verbatim with KaTeX maths, diagrams redrawn as house-style SVG (checked against the Y7–9 pages; generator in ~apk2 build.py/svg.py, not in repo) and cited with printed pages. 1E's missing citation fixed. No Do Now on worksheets (it goes on the slides, lesson-dependent).
- Unit workbooks rebuilt per stream (10MAA order puts 1L after 1H; 10MAG has no 1D) and, with the worksheets, pushed to `lessons/` in the repo and linked from the planner. Solutions copies not regenerated yet. 1D, 1G, 1H, 1I, 1K grew by one page.
- Decided: one HTML slide deck per unit (sections per subchapter, exit-task slides from the subchapter checklist at the end of each section), built from shared subchapter source so 10MAG/10MAA share slides. Worksheets stay per subchapter → later one unit booklet. A buffer lesson per unit for catch-up.
- House rules (Rocco): all maths in KaTeX, never screenshots; diagrams redrawn in house style; A4 HTMLs display as an A4 sheet on screen; material buttons read "Open ↗" / "PDF ⬇".

## 15 Nov 2026 (late) — Do Now rebuilt as retrieval pools
- Cards now hold retrieval pools about themselves; each lesson's Do Now is computed from what was taught before it (see PLANNER.md). Printable half-page sheets per lesson. Ch1 pools done (84 verbatim items).
- Next: pools for the other chapters in units (C10 2K–9J, G11 from Edrolo/chapter review in KaTeX); diagram questions (redraw in house style); first lesson of the year has no Do Now (no C9 pool yet).
- Coursework (renamed from homework) Good / Better / Best per subchapter, now on all 72 C10 cards in units (`coursework` field; cross-checked against extracted pathways, 268/270 match, 2 differences = garbled extraction) (= Foundation / Standard / Advanced pathways from the book, Ch1 read off the pages), table on every worksheet + on the planner card (`homework` field). Teacher tells each student which row (target ~90–120 min/week). Signature box: Teacher stamp + Student signature + Parent signature. Scripts in tools/worksheets/.
- Year 11 (G11) coursework = the whole exercise for every student (Rocco). `coursework.all` on 46 G11 cards with the last question checked against the book (19 exercises spill onto the next subchapter's first page; the old `exercise` ranges undercount these, e.g. 7B ends at Q6, 3D at Q14).
- Unit workbooks now start with a house-style cover (unit code + name, stream, Name/Class/Teacher, coursework option to circle, contents grouped by CFAT week with page numbers). Build: `python3 tools/worksheets/workbook.py "10MAA|Algebra and Linear Relations"` (order = Lesson planning; rerun after reordering).

## 15 Nov 2026 (late) — slide templates (Worked example / You try)
- `lessons/slides-template.html` (1A Example 1 + You try 1): 1280×720 scaled, worksheet-style title bar (You try = grey bar), instruction + one column per part (maths never wraps; shrinks to fit), empty working space, citation footer.
- Key idea box top-right (book Key ideas wording + the matching worksheet Key formula), same box on the Example and its You try.
- Solutions animate one line per click, red, down the column; final line bold. Worked example = the book's solution lines (starting from "="). You try = our own working in exactly the same steps/format as its worked example (Rocco OK'd), final answer checked against the book's Answers (Now you try answers are printed there).
- Next: lock template → build the 10MAA A1 deck (all 1A–1L examples + You trys), then Do Now / exit-task slides.
- Template deck now has every subchapter slide type, in teaching order: Section title (subchapter + unit name) → LI | Success criteria | Lesson sequence → APK (reveal, like examples; Y7–9 checklist items, working by teacher) → Key ideas | Key formulas → Example/You try pairs → Exit tasks (subchapter checklist items, reveal) → Coursework (last). Do Now = printed half-page sheet; deck has one "Do Now: complete the sheet in front of you" slide at the start of each lesson. Coursework slide: only Good keeps its sub-text.
- **Next session: build the Chapter 1 unit slide decks → read `docs/SLIDES-HANDOFF.md`.**

## 15 Nov 2026 (late) — 10MAA Chapter 1 slide deck
- Built `lessons/10MAA Algebra and Linear Relations - Slides.html` (161 slides, Lesson planning order, 1L after 1H). Also copied to G: `01 Lesson materials`. Linked in Unit materials (planner shows **Slides Open ↗**).
- Source: `tools/slides/` (see README). `ch1_data.py` holds every subchapter's content once; both streams build from it.
- Worked examples = book SOLUTION lines; You try = teacher working in the same steps, answers checked against pp. 956–969. APK + exit-task working by teacher. Graphs/number lines redrawn as SVG (solutions red, question graphs black).
- Do Now slide at the start of each lesson; split subchapter 1F gets a second Do Now ("Lesson 6 · 1F continued") halfway through its examples. Review and CAT = title slides.
- Template fixes (Rocco): page numbers show just the number; LI slide spaced to fill; footer pinned to the bottom (coursework slide).
- Extras: type a slide number + Enter to jump; Home/End; URL keeps the slide number.
- Exit/APK slides with a diagram show 2 questions per slide (so 1E exit tasks = 3 slides, some APKs = 2 slides).
- Next: Rocco checks the 10MAA deck → then `python3 tools/slides/build.py "10MAG|Algebra and Linear Relations"`, add its materials entry, copy to G:.

## 15 Nov 2026 (late) — CFAT blocks + 10MAA CFATs
- Subchapter CFAT blocks (L1/L2/L3 per checklist skill, verbatim + cited) for 1A–1L in `tools/cfat/`; paper builder `tools/cfat/paper.py`.
- 10MAA CFATs 1.1–1.4 built with solutions, on G: `03 Assessments` and linked on the planner CFAT strip.
- Next: 10MAG CFATs — see `docs/CFAT-HANDOFF.md`.

## 15 Nov 2026 (late, cont.) — 10MAG CFATs
- 10MAG CFATs 1.1–1.5 built with solutions (1A–1C, 1E–1F, 1G–1H, 1I–1J, 1K–1L), each 2 A4 pages, on G: `03 Assessments`, linked on the planner CFAT strip.
- `paper.py`: titles now per stream; empty Section A is dropped (CFAT 1.5 is all short answer, no MC in 1K/1L); two equations/inequalities joined by "and" in a stem now go one per line, labelled [1], [2].
- 10MAA papers were NOT rebuilt with the one-per-line rule: doing so pushes all four onto 3 pages. Ask Rocco whether to trim them.
- 10MAG CFATs: adjacent sketch questions sit side by side with 62 mm grids underneath (automatic for 10MAG in paper.py). Spare space per box is capped at 22 mm per mark, so boxes no longer stretch to fill a page (10MAA unchanged).
- 1C.2 L2 (Oxford Ch 4 review Q6a): stem now adds "and graph the solution on a number line" (Rocco OK with adding wording like this).
- Open: Rocco to check the 10MAG L1 questions suit the class (e.g. 1.3 Q4 find a missing coordinate from a length).

## 16 Nov 2026 — 10MAG Unit 1 (Univariate Statistics) worksheets
- Guided worksheets C10-9A…9E built (`tools/worksheets/ch9.py`, content verbatim + cited inside the script; CSS = `tools/worksheets/ws.css`, copied from the Ch1 worksheets). Linked on the library cards, on G: `01 Lesson materials`.
- Worksheets show as A4 sheets on screen (same pagination as the CFATs); PDF = the same sheets.
- Histogram parts get a blank grid, box-plot parts a blank number line, two-way-table parts a blank table.
- Next for this unit: Rocco sets lesson count + Lesson planning → workbook, CFAT blocks/CFATs, slides (see `docs/WORKSHEETS-CH9-HANDOFF.md`).
- 16 Nov: 10MAG Univariate Statistics unit workbook built (25 pp., linked). Next: CFATs, see `docs/CFAT-CH9-HANDOFF.md`.
- 16 Nov: CFAT code is now **unit.chapter.CFAT number** (unit = position in that stream's unit list). Existing CFATs renamed only (content untouched): 10MAA 1.1.1–1.1.4, 10MAG 3.1.1–3.1.5. `paper.py` skips the one-equation-per-line rule for 10MAA so a rebuild matches what was published.
- 16 Nov: 10MAG Univariate Statistics CFATs 1.9.1 and 1.9.2 built (see `docs/CFAT-CH9-HANDOFF.md`).
- 16 Nov: **Lesson planning tab redesigned to match the 12MAG planner.** It now opens in a read-only **Course plan** view: per unit, a grid of lesson cards (L1 · 9A, numbered through the stream, colour by kind, CFAT tag on the lesson each CFAT follows) with a **Formative assessments** column (CFAT cards with Open/Solutions + unit materials). Clicking a lesson opens its plan underneath in 12MAG-style collapsible sections built from the library cards (materials, learning intentions, success criteria, VC2/Study Design, vocab, videos, Do Now, APK, worked examples, exit tasks, coursework) plus an editable lesson note. **Edit lessons** toggle = the old drag/split/CFAT editor, unchanged. Code: `renderPlanView()` in `planner/index.html`.
- 16 Nov: **CFAT planning** view added to Lesson planning (third toggle). Decisions log (add/delete, saved to `courses/cfat-log.json` with Save to GitHub), a cross-stream table (each subchapter → its 10MAG and 10MAA CFAT, built or to build), standing CFAT rules and open questions. **Log every CFAT decision there.**
- 16 Nov: **10MAG Modified.** Course plan view for 10MAG is now 4 columns: 10MAG lessons (solid unit-materials card on top) | 10MAG assessments (CFATs + CAT) | Modified lessons (solid modified-materials card + approve tick on top) | Modified assessments (M CFATs + Modified CAT (e.g. 1.9.1M, "to plan"). Freefall worksheet index (titles + PDF pages only) in `courses/freefall.json`; draft subchapter → Freefall mapping in `courses/modified.json` (Rocco edits on the planner: click a modified lesson, ✕ / add a sheet; tick "mapping approved" per unit). **Freefall PDFs are licensed to the school: never commit them or pages from them to this repo or link them on the site; modified workbooks go to G: `01 Lesson materials` only.** FF8 copy is the Teacher Edition: check its sheets have no answers before using for students. No Freefall match yet: 1I, 1J, 1L, 9J, 6A–6D, 2K–2N, 8D (and Sequences & Recursion has no subchapters). Next: Rocco approves a unit → build its modified workbook (cover + Freefall pages by CFAT week) on G:.
- 16 Nov: **10MAG Modified pilot, G1 Univariate Statistics (built, Rocco to review).**
  - Lessons (same order as 10MAG): L1 9A ← Y7 8A · L2 9B ← Y8 8B, 8C + Y7 8E · L3 9C ← Y8 8J · L4 9D ← Y7 8B · L5 9E part 1 ← Y8 8E (range, IQR) · L6 9E part 2 ← Y9 9L (box plots).
  - Worksheets: `python3 tools/worksheets/ch9m.py` → `lessons/C10-9X modified worksheet[ (part n)].html/.pdf` (LIs, Key ideas, Example → You try pairs verbatim, I-can checklist; no APK/coursework: Freefall is the practice).
  - CFATs: L0 level added to `tools/cfat/C10-9A…9E.json` by `tools/cfat/gen_ch9m.py` (run after gen_ch9.py). `python3 tools/cfat/paper.py 10MAGM <n> "Univariate Statistics"` → CFAT 1.9.1M / 1.9.2M (+ Solutions). 10MAG papers unchanged.
  - Workbook: `python3 tools/worksheets/workbook_m.py "Univariate Statistics" "<Freefall folder>" /tmp/out` (refuses to write inside the repo) → cover + worksheet + Freefall sheets per lesson (each sheet once), 50 pp. FF8 Teacher Edition = notes, worksheet, answers: only notes + worksheets are taken.
  - On G:: worksheets + workbook in `01 Lesson materials`, CFAT M PDFs in `03 Assessments`. Planner links in `courses/modified.json` → `materials`.
  - Next: Rocco reviews; then the same recipe for G3 Algebra (Freefall gaps 1I, 1J, 1L to decide first).
- 16 Nov: **docs/MODIFIED-HANDOFF.md** = plan + recipe for the whole 10MAG Modified curriculum (start there). workbook_m.py: CFAT week codes now use the unit's chapter (was hard-coded 9).
- 16 Nov: **10MAG Modified G3 Algebra and Linear Relations built (Rocco to review).** 15 modified worksheets (`tools/worksheets/mod_algebra.py`; shared code `modified.py` now has a Practice box for no-Freefall lessons 1I, 1J, 1L), CFAT 3.1.1M–3.1.5M (`tools/cfat/gen_ch1m.py`, run after gen_ch1b.py; shared `modified_l0.py`), workbook 76 pp. on G: (Drive link not synced yet: fill `workbook_url` in modified.json). Lesson → Year 8/9 map in the CFAT log. Workbook builder now detects FF8 answer pages by colour (old rule let 2 answer pages into G3). Next: G8 Probability.
- 16 Nov: **10MAG Univariate Statistics slides critiqued + extended** (76 slides). New step-by-step slides: 9B *Finding the median step by step* (cross-off animation, odd + even), 9B *Mode and mean step by step* (BU Q1 dot plot), 9E *Drawing a box plot step by step* (Example 9 explanation steps on Test A, p. 798), 9E *Comparing data with parallel box plots* (Tests A/B; covers the 9E LI that had no slide). 9E split: "Lesson 6 · 9E continued" Do Now before the parallel box plots. Review + CAT title slides at the end. Formatting: 9C/9D APK split over 2 slides (`apk_split`), bigger Key ideas text, 9A types table full width, 9C exit table bigger.
- 16 Nov: CAT lesson cards (both streams) hold nested Practice / Final Task / Redemption (Draft until a file is linked: `materials` entry `{kind:'cat',title:'Practice'|'Final Task'|'Redemption',html|pdf,solutions}`). Rocco makes these by hand.
- 16 Nov: Rocco's 9A slide edits applied deck-wide (ch9.py): LI/SC rows aligned (grid), APK + exit tasks in vertical columns with the last line bold, 9A Key ideas types-of-data flow chart, flow chart with arrows, 12-card two-step sort (Y9 9G Ex 11, Now you try, Ex Q2), good-sample panel + study-hours averages, two-step scaffold on Ex1/You try 1/exit 1, population panels on Ex2/You try 2, coursework slides show an example A4 page (red margin, two columns).
- 16 Nov: Rocco's second pass (9B–9E) applied: tile engine (order → cross off → middle; quartiles = medians of halves) used on median, quartiles, stem-and-leaf and box-plot-steps slides; data → frequency table → histogram (0–9, 10–19 … intervals) on New learning and Example/You try 3 (rows then bars then tail); Example/You try 4 stem built row by row with i/ii/iii in separate columns; Mean/Median/Mode three columns; Example/You try 7 working models the halves method; five-figure summary tables on Example/You try 8 and the box plot slides; house-price fences slider and walking-time box plot slider (both fences); parallel box plots reporting templates with blanks filled step by step; stronger skew tails with a 'tail' arrow.
- 16 Nov: Do Now slides removed from the 10MAG Univariate Statistics deck (and from the Lesson sequence column). Controls: click/tap = forward only (double = next slide); → / ← single = step, double → = next slide, double ← = previous slide cleared; double Backspace clears the slide.
- 16 Nov: Course plan view: units are collapsible cards in term rows (Step Up, Term 1–4; term = where the unit's first lesson falls at 3 lessons/week, Step Up first, public holidays skipped). Click a card to open the full unit layout under its row; Open/Close all units. Open state kept in the browser (10ma-uopen). 10MAA Unit materials now a solid card at the top of Lessons, like 10MAG.
- 16 Nov: Course plan: 10MAA CAT/assessment lesson cards moved to the Assessments column (like 10MAG); every unit gets a Pre-assessment card (Draft) at the top of its assessments column (link one via lessons.json materials {kind:'pre',title:'Pre-assessment',html|pdf,solutions}). Unit cards: Year 11 content green, shared units two colours.
- 16 Nov: **Lesson counts set from the 2027 draft scope and sequence** (Rocco OK'd). Every unit = content + Buffer (practice) + Review + Assessment (Quadratics 10MAG and Sequences & Finance 10MAA: Review, Assessment, Buffer, so revision lands before the T2 exam block). 10MAG 84 lessons (9/12/16/7/8/15/8/9), 10MAA 92 (13/13/12/12/10/14/12/6) with paired subchapters; 10MAA Matrices & Networks dropped 4G, 4H, 8E, 8F. Capacity rule (years/2027.json): full week 3 lessons, short week 2, Step Up 3, Year 10 blocked weeks per stream (T2 revision/exams/Work Experience, T4 from the exams). 10MAG Sequences & Recursion lessons have no subchapters yet (Edrolo content to choose). Built 10MAA Algebra slides/workbook still follow the old grouping (1F was split, 1G/1H separate): rebuild if wanted.
- 16 Nov: Course plan term rows are now week-by-week: Year 10 events are their own cards (years/2027.json y10_events, both streams): T2 wk 7 exam revision, wk 8–9 exams, wk 11 Work Experience; T4 wk 5 exam revision, wk 6–7 exams (Rocco: exams 2 weeks in both semesters), wk 8 camp, wk 9 Step Up into Year 11, wk 10–11 end of year. Rows show spare/over; units that don't fit say so. 10MAA is 3 lessons over (Probability).
- 16 Nov: Lesson planning is year-independent: term rows use courses/structure.json (weeks per term 9/11/10/11, 3 lessons/week, Step Up 3, Year 10 event weeks). Event cards show only name + number of weeks. Dates/holidays stay in years/2027.json for the 2027 tab.
- 16 Nov: 10MAG Quadratics is a small 1-week unit fixed in T2 wk 10 (between the Semester 1 exams and Work Experience): 5A+5B, 5C, topic test (structure.json 'pins').
- 16 Nov: 10MAG final layout (Rocco): Univariate 9 (Step Up→T1), Sequences 12, Algebra 18 (1F,1H,1I,1L split), Bivariate 9 (moved before Quadratics; 9I,9J split), Quadratics 7 (starts T2 wk 10 after exams, finishes T3), Trigonometry & Measurement 21 (every subchapter split except 4E... see lessons.json), Networks 8 (T3→T4), Probability 9 (T4). 93 lessons = full year-independent capacity; pins removed.
- 16 Nov: 10MAG trimmed to 89 lessons so it fits a real year (2027 calendar for Rocco's Mon/Wed/Thu S1 class = 89 slots): Algebra 17 (1L single), Trigonometry & Measurement 18 (4E, 4G, 6B single).
