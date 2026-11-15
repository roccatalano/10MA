# tools — how the library cards are filled

Run from a work folder that sits next to the repo (`work/` and `10MA/` side by side), with the textbook PDFs converted by `pdftotext -layout` to `c7.txt c8.txt c9.txt c10.txt`.

1. `ck.py` → `checklist7–10.json` (Cambridge chapter checklists; uses `items.py`). Fixes known mislabels at the bottom.
2. `vocab.py` → `vocab.json` (bold terms in each KEY IDEAS box, read from the C10 PDF with PyMuPDF).
3. `build_rest.py` → writes the lesson-plan fields into `library/C10.json` for every C10 subchapter used in `courses/units.json` (Ch1 is from `build_ch1.py`, older).
   Hand-made choices live in `maps_vc.py` (VC2 per subchapter), `maps_apk.py` (Y7–9 checklist items as `(year,'sub.n')`), `maps_vid.py` (videos), `maps_vocab.py` (vocab clean-up + LI terms).

`data/` keeps the parsed outputs so nothing has to be re-extracted.
Do Now is left empty on purpose: it depends on lesson groupings (last lesson / earlier this chapter).

## G11 (Cambridge General U1&2) + E11 (Edrolo)
Text files: `g11.txt`, `e11.txt` (pdftotext -layout).
1. `g11parse.py` → LIs, examples + Now try this, exercises, Skills checklist (→ success criteria + exit tasks). Writes `g11_stage1.json`.
2. `g11gloss.py` → `g11_glossary.json` (glossary terms + definitions + page refs, via PyMuPDF).
3. `edrolo.py` → every VCAA-tagged question in Edrolo; `map_edrolo.py` matches each (unique by VCAA source) to a G11 subchapter by keywords, with a fallback by exam module (`mapped_by`).
4. `build_g11.py` → writes `library/G11.json` for G11 subchapters in units. Hand choices: `maps_apk_g11.py` (C9/C10 checklist skills), `maps_vid_g11.py`, and the Edrolo-lesson map `E2G` inside `build_g11.py`.
