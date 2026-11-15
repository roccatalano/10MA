# 10MA course planner — instructions for Claude

Owner: Rocco (teacher). Explain in plain words, ask before anything destructive, no jargon without a one-line explanation.

**CFAT decisions: log them in `courses/cfat-log.json` (shown on the planner).** **New chat? Read `PLANNER.md` next, then `docs/HANDOVER.md`** (latest state, decisions, open items). **Building slides? Also read `docs/SLIDES-HANDOFF.md`. Building 10MAG Modified material? Read `docs/MODIFIED-HANDOFF.md`. Building CFATs? Read `docs/CFAT-HANDOFF.md` (and `docs/CFAT-CH9-HANDOFF.md` for Univariate Statistics).**

## What this repo is
The Year 10 Maths course planner for two linked streams:
- **10MAG** = Year 10 General: Cambridge Essential Mathematics 10 & 10A only.
- **10MAA** = Year 10 Advanced: Cambridge 10 & 10A, with some units replaced by their Cambridge General Maths U1&2 counterparts to accelerate.

Design: a **subchapter library** (one card per subchapter in both books) and **course plans** that pick cards into units for each stream. Shared subchapters are one card, built once, used by both streams.

## G: drive folder
`Y7-10 Vic. Curric\Year 10 Advanced\10MAA 2027\10MA Course Planner`
- `01 Lesson materials` = everything we make, flat, named by card ID (`C10-1A worksheet.pdf`)
- `02 Sources` = textbook PDFs + VC2 curriculum
- `03 Assessments` = CFATs, CATs, topic tests, exams (shared by both streams)

## Sources (flat in 02 Sources)
- `C10` = 2024 - Essential Mathematics for the Victorian Curriculum 10 & 10A Third Edition.pdf — main Year 10 book (both streams)
- `G11` = 2023-cambridge-units-1-2.pdf (solutions: 2023-cambridge-units-1-2-solutions.pdf) — General Maths U1&2, for the accelerated 10MAA units
- `E11` = Edrolo General Maths U1&2 — exam-style questions (VCAA reprints at the back of subchapters) for the G11-based units
- `J10` = 2022-jacaranda-10-10a-maths-quest.pdf — extra questions to pull from
- `O10` = 2022-oxford-10-10a-maths.pdf — extra questions to pull from
- VC2 curriculum: not yet copied in

## Rules (carried over from 12MAG; confirm or change with Rocco)
1. **Never write questions.** Copy verbatim and cite. Adapt only when unavoidable and label it "adapted".
2. **Card IDs are permanent:** `C10-1A`, `G11-2B`. Never renumber; everything else references them.
3. **Index now, fill on first use:** library cards start at index level; extract verbatim content the first time a lesson uses the card, and save it so it is never re-extracted.
4. **Every lesson gets:** guided slides, guided worksheet (questions only, active engagement) + solutions copy, bound reference (log book) entry (notes, definitions, formulas, cited example). Old per-subchapter all-in-one handouts are discontinued.
5. **Example → You try pairs:** every Cambridge Worked Example is followed by its own 'Now you try' (same skill, new numbers). Lessons use them as pairs: teacher models the Example, students do its Now you try. Card field: `examples[].now_you_try`.
6. G11 cards: curriculum = VCE Mathematics Study Design 2023 (General Maths U1&2), never VC2. C10 cards: VC2.
7. Finished materials go in `lessons/` here and flat into `01 Lesson materials` on G:.

## Git
The planner page saves `courses/units.json` straight to GitHub. Always `git pull` before you change or push anything.

## Not to touch
`roccatalano/12MAG` and `roccatalano/teaching-dashboard-2027` — don't change unless Rocco asks.
