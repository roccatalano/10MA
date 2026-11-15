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
- Homework now Good / Better / Best per subchapter (= Foundation / Standard / Advanced pathways from the book, Ch1 read off the pages), table on every worksheet + on the planner card (`homework` field). Teacher tells each student which row (target ~90–120 min/week). Signature box: Teacher stamp + Student signature + Parent signature. Scripts in tools/worksheets/.
