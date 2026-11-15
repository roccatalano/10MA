# Handoff: build the 10MAG CFATs for Algebra and Linear Relations

Written 15 Nov 2026 (late). Read `CLAUDE.md`, `PLANNER.md`, `docs/HANDOVER.md`, then this. **`git pull` first.**

## Where things are
- **Blocks** (one per subchapter, the question bank): `tools/cfat/C10-1A.json` … `C10-1L.json`. Each checklist skill has 3 questions: **L1** (Level 9 review, mostly Cambridge Y9), **L2** (Level 10, mostly Oxford), **L3** (extension / 10A). Every question verbatim + cited (`src`, `vc2`); "adapted" in `src` = stem reworded for a single part. Items with `"fill": true` are spare MCs, used only so a paper never has a lone multiple-choice question.
  - Preview of any block: `python3 tools/cfat/build.py C10-1A` → `lessons/C10-1A CFAT block - test build.html` (tabs only for streams that teach the subchapter).
  - `tools/cfat/gen_ch1b.py` wrote the 1E–1L blocks once; edit the JSON now, don't rerun it.
- **Paper builder**: `python3 tools/cfat/paper.py <stream> <n>` → `assessments/CFAT 1.<n> - <stream> - <first>-<last>.html` + `- Solutions.html`. Subchapters come from `courses/lessons.json` → `cfats["<stream>|Algebra and Linear Relations"][n-1]`.
- **Done**: 10MAA CFATs 1.1–1.4 (`assessments/`, G: `03 Assessments`, linked on the planner's CFAT strip via `materials[...]` entries `{kind:'cfat', n, html, solutions}`).

## Rules Rocco agreed (don't change without asking)
- 20-minute formative, **one double-sided A4 sheet max**, shown as A4 sheets on screen.
- **One question per skill** (each skill tested once). Levels: **10MAG = L1 + L2, 10MAA = L2 + L3**. Within a subchapter the level alternates by skill (odd skill → lower level, even → higher); 10A subchapters take the higher level. Short weeks (<6 skills) test both of the stream's levels per skill.
- Layout = Rocco's example CFAT: title box (CFAT code, Name, score box), Section A multiple choice in a 2-col grid, **options A–E always vertical**; Section B short answers **stacked full width**, spare page space shared out by marks.
- Sketch questions: **two columns** — question left, large blank −10…10 grid right (worked sketch in the same spot on the solutions copy). Number-line answers get a blank number line.
- Multiple equations/inequalities in a stem: **one per line**. Refer to equations as **[1], [2]**.
- **No sources on the student copy** (solutions copy only). No skill tick table at the end.
- Never a single multiple-choice question in Section A (add a `fill` MC to a block if needed).

## The job: 10MAG
10MAG CFATs (`lessons.json`): **1** 1A–1C · **2** 1E–1F · **3** 1G–1H · **4** 1I–1J · **5** 1K–1L. No 1D.
1. `git pull`, then `for n in 1 2 3 4 5; do python3 tools/cfat/paper.py 10MAG $n; done`.
2. The title map in `paper.py` (`title={1:…,2:…,3:…,4:…}`) is 10MAA-numbered; make titles per stream (10MAG has 5 CFATs, different groupings).
3. Check every paper: print to PDF (headless Chrome, `page.pdf(format='A4')`) → **2 pages max**, no question split, graphs readable, no lone MC. Look at screenshots, don't trust counts.
4. Check the L1 questions fit 10MAG (they've only been seen in block previews so far). 1G.3 L1 is the only "find a coordinate from a distance" question; 1E.5/1E.6 L1 are simple sketches.
5. Copy to G: `03 Assessments` (device_commit_files), add `materials["10MAG|Algebra and Linear Relations"]` cfat entries (n 1–5) in `courses/lessons.json`, push, update `docs/HANDOVER.md`.

## Open
- 10MAG slides deck: `python3 tools/slides/build.py "10MAG|Algebra and Linear Relations"` (see SLIDES-HANDOFF) — not built yet.
- Calculator / bound-reference line on CFATs: Rocco hasn't said.
