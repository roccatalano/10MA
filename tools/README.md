# tools — how the library cards are filled

Run from a work folder that sits next to the repo (`work/` and `10MA/` side by side), with the textbook PDFs converted by `pdftotext -layout` to `c7.txt c8.txt c9.txt c10.txt`.

1. `ck.py` → `checklist7–10.json` (Cambridge chapter checklists; uses `items.py`). Fixes known mislabels at the bottom.
2. `vocab.py` → `vocab.json` (bold terms in each KEY IDEAS box, read from the C10 PDF with PyMuPDF).
3. `build_rest.py` → writes the lesson-plan fields into `library/C10.json` for every C10 subchapter used in `courses/units.json` (Ch1 is from `build_ch1.py`, older).
   Hand-made choices live in `maps_vc.py` (VC2 per subchapter), `maps_apk.py` (Y7–9 checklist items as `(year,'sub.n')`), `maps_vid.py` (videos), `maps_vocab.py` (vocab clean-up + LI terms).

`data/` keeps the parsed outputs so nothing has to be re-extracted.
Do Now is left empty on purpose: it depends on lesson groupings (last lesson / earlier this chapter).
