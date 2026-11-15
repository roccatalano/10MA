# Unit slide decks
- `ch1_data.py`: the slide content for each C10 Chapter 1 subchapter (APK working, examples + You try working, exit-task working, key-idea boxes, diagrams). One source for both streams.
- `svgs.py`: house-style number lines and Cartesian sketches (solution marks red, question graphs black).
- `build.py`: builds a deck in Lesson planning order (`courses/lessons.json`), copying the look from `lessons/slides-template.html`. Learning intentions, success criteria, coursework and APK skills come from `library/C10.json`; Key ideas / Key formulas come from the subchapter worksheet.
  - `python3 tools/slides/build.py "10MAA|Algebra and Linear Relations"`
  - `python3 tools/slides/build.py "10MAG|Algebra and Linear Relations"`
- Rebuild after changing the lesson order. The page fits itself on load: maths never wraps (shrinks to the column), long working shrinks then flows into two columns.
