# Handoff: 10MAG Univariate Statistics CFATs (C10 9A–9E)

Written 16 Nov 2026. Read `CLAUDE.md`, `PLANNER.md`, `docs/HANDOVER.md`, **`docs/CFAT-HANDOFF.md` (the CFAT rules and tools)**, then this. **`git pull` first.**

## Where things stand
- Unit **G1 Univariate Statistics** (10MAG only; 10MAA does Data Analysis from G11 instead).
- Done: worksheets 9A–9E, unit workbook, slide deck (see `docs/WORKSHEETS-CH9-HANDOFF.md`).
- Lesson planning (`courses/lessons.json → plans["10MAG|Univariate Statistics"]`): 9A · 9B · 9C · 9D · 9E · 9E · Review · CAT.
- CFAT groupings (`cfats["10MAG|Univariate Statistics"]`): **CFAT 1 = 9A, 9B, 9C** · **CFAT 2 = 9D, 9E**. Re-read these; Rocco may change them.

## The job
1. **Build CFAT blocks** `tools/cfat/C10-9A.json` … `C10-9E.json` in the same format as `C10-1A.json` (one entry per checklist skill, items with `level`, `type` mc/sa, `marks`, `q`, `options`/`answer`, `sol`, `src`, `vc2`; `"fill": true` for spare MCs).
   - Skills = the **Chapter 9 checklist** (C10 p. 853–854; PDF page = printed + 21):
     - 9A: 1 describe types of data · 2 choose a survey sample
     - 9B: 3 present data in a histogram · 4 analyse data in a statistical graph
     - 9C: 5 interpret a two-way table · 6 construct a two-way table
     - 9D: 7 five-figure summary and IQR · 8 find outliers
     - 9E: 9 construct a box plot
   - Levels: 10MAG uses **L1 (Level 9 review) + L2 (Level 10)** only, so L3 is not needed for this unit (add it only if Rocco asks).
   - L1 sources: **Cambridge Year 9** Ch 9 (Probability and statistics) chapter review MC + short answer; Cambridge Year 8 Ch 8 if Year 9 has nothing for a skill. L2 sources: **Oxford 10** statistics chapter review / exercises, else Jacaranda 10. All in `02 Sources` on G:.
   - Verbatim + cited (`src`). Rewording a stem so a single part stands alone is fine ("adapted: stem reworded for a single part"), and so is adding an instruction like "and graph the solution on a number line" (Rocco OK'd, 16 Nov); label it in `src`.
   - Don't reuse questions already on the worksheets, slides or exit tasks (Cambridge 10 Examples, Now you try, checklist e.g. questions, Y7–9 checklist e.g. questions used as APK).
2. **Teach `paper.py` the new answer spaces** (CFAT 1 rules otherwise unchanged):
   - Histogram questions → a blank grid with axes in the right column (like the −10…10 grid for sketches, but first-quadrant).
   - Box-plot questions → a blank number line with the right scale (number lines already work: `viewBox="0 -6` figures).
   - Frequency / two-way tables to complete → blank table in the question.
   - Stem-and-leaf / dot plots / box plots in the **question** → black house-style SVG or HTML table (see `tools/worksheets/ch9.py` helpers `stemleaf`, `numline`, `tbl`; `tools/slides/ch9_data.py` `boxplot`, `hist`).
   - Title map in `paper.py`: add `10MAG` Univariate titles.
3. **Build and check:** `python3 tools/cfat/paper.py 10MAG <n> "Univariate Statistics"`. Print to PDF → **2 pages max**, no question split, graphs readable, no lone MC; look at screenshots. CFAT 2 has only 3 skills → short week → both levels per skill (already automatic: `FEW`).
4. **Deliver:** copy to G: `03 Assessments`, add `materials["10MAG|Univariate Statistics"]` cfat entries (`{kind:'cfat', n, title, html, solutions}`), push, update `docs/HANDOVER.md`.

## Ask Rocco
- (Settled 16 Nov) CFAT code = unit.chapter.CFAT, so these are **CFAT 1.9.1** and **1.9.2**; `paper.py` does this automatically.
- Calculators allowed? (Still open from the Algebra CFATs.)
