# Handoff: 10MAG Unit 1 (Univariate Statistics) guided worksheets, C10 9A–9E

Written 16 Nov 2026. Read `CLAUDE.md`, `PLANNER.md`, `docs/HANDOVER.md`, then this. **`git pull` first.**

## Context
- 10MAG unit order on the planner (`courses/units.json`): **G1 Univariate Statistics (C10 9A–9E)**, G2 Sequences and Recursion, G3 Algebra and Linear Relations (done: worksheets, workbook, CFATs).
- Library cards C10-9A…9E are indexed (LIs, examples, APK locators, exit tasks/checklist, coursework pathways). No materials yet. Unit has no lesson count on the planner yet (Rocco to set).

## The job (in order)
1. **DONE 16 Nov:** Guided worksheets 9A–9E → `lessons/C10-9X worksheet.html` + `.pdf`, flat copy to G: `01 Lesson materials`.
2. Unit workbook (`tools/worksheets/workbook.py "10MAG|Univariate Statistics"`) once Lesson planning exists.
3. CFAT blocks 9A–9E + CFATs (see `docs/CFAT-HANDOFF.md`; CFAT groupings come from Lesson planning).
4. Slide deck (see `docs/SLIDES-HANDOFF.md`).

## Worksheet format (match the Chapter 1 worksheets exactly, e.g. `lessons/C10-1A worksheet.html`)
A4 pages, boxed sections with grey header bars, in this order:
1. **Title**: subchapter code | title | Cambridge pages.
2. **Learning intentions**: verbatim from the card.
3. **Key definitions**: book Key ideas, bold key terms.
4. **Key formulas**: table (row label | formula + e.g.), where the subchapter has formulas.
5. **Activating prior knowledge**: the card's `apk` items = Year 7/8/9 chapter checklist e.g. questions, verbatim, numbered, with working space; cite under the box.
6. **Example N · title | You try N** pairs: questions only (no solutions), verbatim from the Example and its Now you try, parts a, b, c with dotted working space.
7. **Skills checklist**: ☐ + bold "I can…" + the e.g. question, from the Ch 9 Chapter checklist (book p. 853+).
8. **Coursework** box: Good/Better/Best from `tools/worksheets/hw.py` / `pw_all.py` (9A–9E rows already there), signatures + teacher stamp.

## Rules
- Never write questions: copy verbatim and cite. Wording may be added to make a single part work (Rocco OK'd, e.g. "and graph the solution on a number line"); mark it "adapted" in the citation.
- Tables and graphs (stem-and-leaf, histograms, dot plots, box plots, two-way tables) are redrawn as house-style HTML tables / SVG (`tools/worksheets/svg.py` style), never screenshots.
- Solutions copy for each worksheet is still an open item for all units.
