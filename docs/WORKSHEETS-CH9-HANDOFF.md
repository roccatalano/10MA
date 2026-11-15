# Handoff: 10MAG Unit 1 (Univariate Statistics) guided worksheets, C10 9A–9E

Written 16 Nov 2026. Read `CLAUDE.md`, `PLANNER.md`, `docs/HANDOVER.md`, then this. **`git pull` first.**

## Context
- 10MAG unit order on the planner (`courses/units.json`): **G1 Univariate Statistics (C10 9A–9E)**, G2 Sequences and Recursion, G3 Algebra and Linear Relations (done: worksheets, workbook, CFATs).
- Library cards C10-9A…9E are indexed (LIs, examples, APK locators, exit tasks/checklist, coursework pathways). No materials yet. Unit has no lesson count on the planner yet (Rocco to set).

## The job (in order)
1. **DONE 16 Nov:** Guided worksheets 9A–9E → `lessons/C10-9X worksheet.html` + `.pdf`, flat copy to G: `01 Lesson materials`.
2. **DONE 16 Nov:** Unit workbook (`tools/worksheets/workbook.py "10MAG|Univariate Statistics"`), 25 pages, linked in materials.
3. CFAT blocks 9A–9E + CFATs: see **`docs/CFAT-CH9-HANDOFF.md`**.
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

## Slides (16 Nov): sample deck 9A–9B with New learning slides
- `python3 tools/slides/ch9.py 9A 9B` → `lessons/10MAG Univariate Statistics - Slides (9A-9B sample).html`. Content in `tools/slides/ch9_data.py` (same format as `ch1_data.py`); reuses `build.py` (template look, APK, Key ideas, Example/You try, coursework).
- Order per subchapter: Do Now · Title · LI/SC/sequence · APK · Key ideas · **New learning** · Example/You try pairs · Exit · Coursework.
- **New learning slides** (Rocco's idea): animated or interactive, built only from the book's Key ideas / Building understanding (cited). 9A: types-of-data tree (click to build), "Sort it" categorical/numerical cards (BU Q3–4), population vs sample dot grid (random / library / one class). 9B: frequency table → histogram (bars grow per click, % axis), symmetrical/skewed slider with live mean and median, stem-and-leaf build. Clicks on buttons/sliders don't advance the slide.
- 16 Nov: full unit deck built (9A–9E, 68 slides): `python3 tools/slides/ch9.py` → `lessons/10MAG Univariate Statistics - Slides.html`, linked in materials. 9C: reading a two-way table (click cells), completing one (BU Q1). 9D: quartiles on tiles (odd/even), outlier fences slider. 9E: parts of a box plot, live box plot with outlier slider. Order is by subchapter with a Do Now before each (no Lesson planning yet). Rocco to review slide by slide.
