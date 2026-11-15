# Handoff: build the Chapter 1 unit slide decks

Written 15 Nov 2026 (late). Read `CLAUDE.md`, then `PLANNER.md`, then `docs/HANDOVER.md`, then this file. **`git pull` first.**

## The job
Build one HTML slide deck per unit for **Algebra and Linear Relations (C10 Chapter 1)**:
- `lessons/10MAA Algebra and Linear Relations - Slides.html` (10MAA unit A1): subchapters 1A–1L **in Lesson planning order** (1L comes after 1H).
- `lessons/10MAG Algebra and Linear Relations - Slides.html` (10MAG unit G3): no 1D; 1L last.
Build both from **one shared source** (per-subchapter slide data + one builder script in `tools/slides/`), so a fix to a subchapter updates both decks. Start with 10MAA, check it with Rocco, then generate 10MAG.

## The locked template
`lessons/slides-template.html` (1A, 9 slides) is the agreed design. Copy its CSS/JS exactly; only the content changes. Live: https://roccatalano.github.io/10MA/lessons/slides-template.html

## Slide order
**Lesson level:** every lesson in the plan starts with the **Do Now** slide ("Complete the Do Now sheet in front of you…"). The Do Now itself is the printed half-page sheet (`planner/donow.html`), never on screen.

**Subchapter level, in this order:**
1. **Section title**: subchapter code + title, unit name, book pages.
2. **Learning intentions | Success criteria | Lesson sequence**: 3 columns. LIs = verbatim from the book (`learning_intentions` on the card). Success criteria = that subchapter's Chapter 1 checklist "I can…" items with ☐. Sequence = Do Now, APK, Key ideas and formulas, each Example · You try with its title, Exit tasks, Coursework.
3. **Activating prior knowledge**: 2×2 grid (or fewer cells if the subchapter has fewer than 4 items), each cell has a small "Year N · I can…" line, the question in KaTeX, then red working revealed one line per click, last line bold. Questions = the card's `apk` items (same as the worksheet's APK box, verbatim). Working by teacher.
4. **Key ideas | Key formulas**: 2 columns, items separated by dashed lines, filling the column. Book Key ideas wording + the worksheet's Key formulas table.
5. **Example N / You try N** pairs, one per worked example in the subchapter:
   - Title bar "Example N | title" (white) or "You try N | title" (grey), subchapter on the right.
   - Instruction line, plus a **Key idea box top-right** with the key idea/formula that example uses (same box on the Example and its You try).
   - One column per part (a, b, c…), maths never wraps (auto-shrinks), empty working space below.
   - **Solutions:** red, revealed one line per click going down the column, final line **bold**, lines start from "=" where the question is already shown.
   - Worked example = the book's SOLUTION lines (not the explanation column).
   - You try = **our own working, in exactly the same steps and format as its worked example** (Rocco OK'd); final answers checked against the book's Answers ("Now you try" answers are printed there).
   - Diagrams in a question: redraw as house-style SVG (see `tools/worksheets/svg.py`), never a screenshot.
6. **Exit tasks**: same 2×2 reveal layout; each cell starts with **☐ + the bold "I can…" statement**, then the checklist's e.g. question, then red working (by teacher). Source: Chapter 1 checklist, book p. 88–89.
7. **Coursework** (always last): the Good / Better / Best table for the exercise (card field `coursework`). Only Good keeps its sub-text ("Minimum for your coursework tick"). Note line explaining (½) and (⅓).

Review and assessment lessons: a simple title slide each ("Review", "CAT") is enough for now.

## Lesson plans (from `courses/lessons.json`; re-read it, Rocco may have changed it)
- **10MAA A1** (14 lessons): L1 1A+1B · L2 1C · L3 1D · L4 1E · L5–6 1F · L7 1G · L8 1H · L9 1L · L10 1I · L11 1J · L12 1K · L13 Review · L14 CAT. CFATs: 1A–1D | 1E–1F | 1G, 1H, 1L | 1I–1K.
- **10MAG G3** (17 lessons): 1A · 1B · 1C · 1E · 1F×2 · 1G · 1H×2 · 1I×2 · 1J · 1K · 1L×2 · Review · CAT. CFATs: 1A–1C | 1E–1F | 1G–1H | 1I–1J | 1K–1L.
- A split subchapter (e.g. 1F over L5–6) is just continued: no new slides, the teacher carries on where they stopped. Put a Do Now slide where each lesson starts only if the deck is ordered by lesson; simplest is one Do Now slide before each subchapter's title plus one at each split point.

## Where the content is
- **Cards:** `library/C10.json` → Ch1 subchapters: `learning_intentions`, `examples` (n, title, now_you_try), `apk`, `success_criteria`, `exit_tasks`, `coursework`, `retrieval`, `printed_page/printed_end`.
- **Worksheets (verbatim KaTeX already typed):** `lessons/C10-1A worksheet.html` … `C10-1L`. They hold the Key definitions, Key formulas, every Example with its You try (in `.pair` blocks), the APK questions and the skills checklist. Reuse this text; it has already been checked against the book.
- **Book:** `02 Sources/2024 - Essential Mathematics … 10 & 10A Third Edition.pdf` on G: (stage it with device_stage_files). **Printed page = PDF page − 21** (p. 6 = PDF 27; checklist p. 88 = PDF 109; Answers p. 956 = PDF 977).
  - Examples 1–32 run through the chapter (1A = Ex 1–5, 1B = Ex 6–8, 1C = 9–10, 1D = 11–12, 1E = 13–16, 1F = 17–19, 1G = 20–22, 1H = 23–24, 1I = 25–26, 1J = 27–28, 1K = 29–30, 1L = 31–32; check against the page).
  - Now you try answers: Answers section, Chapter 1 → "1A … Now you try → Example 1 …" (p. 956 onwards).
  - Y7–9 books (for APK) are also in 02 Sources.
- pdftotext garbles fractions and powers: use it only to find things; take the wording from the page image or the worksheets.

## House rules (non-negotiable)
- Never write questions. Copy verbatim and cite (footer on every slide). Our own working is fine, labelled "Working by teacher" where the book prints none.
- All maths in KaTeX. No screenshots of the book; diagrams redrawn in house style.
- Slides: 1280×720, scaled to fit; → / click = next working line then next slide, ← = back, F = full screen.

## When done
1. Check every slide by stepping through it fully revealed (headless browser screenshots; script pattern in this session: walk with ArrowRight, screenshot when all `.st` are shown). Nothing may overflow its box.
2. Push to the repo (`lessons/`), copy to G: `01 Lesson materials` (device_commit_files).
3. Add the slides to the Unit materials box: `courses/lessons.json` → `materials["10MAA|Algebra and Linear Relations"]` add `{kind:'slides',title:'Slides',html:'lessons/…Slides.html'}` and make the planner's "Slides: not made yet" show **Open ↗** when a slides entry exists (in `matBox()` in `planner/index.html`).
4. Update `docs/HANDOVER.md`.
