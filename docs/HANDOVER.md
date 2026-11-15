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
