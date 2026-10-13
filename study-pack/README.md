# CPE334 STEP I — Midterm Study Pack

This package contains two independent A4 PDFs: a **91-page Thai/English study book** and a **30-page bilingual mock midterm with solutions**. Page counts include covers and front matter. The study book is under the 120-page limit; the mock is under the 30-page limit.

## Open the PDFs

- [`CPE334_STEP_I_Study_Notes.pdf`](CPE334_STEP_I_Study_Notes.pdf) — Lecture 1–7 study notes, worked examples, diagrams, exam blueprint and quick review.
- [`CPE334_Mock_Midterm_Exam_with_Solutions.pdf`](CPE334_Mock_Midterm_Exam_with_Solutions.pdf) — candidate paper first, followed by worked solutions and practice scoring guidance.

The mock follows the instructor's supplied 25/25/50 structure and bilingual KU registration sample. It is an authored practice paper, not an official exam or marking scheme.

## Scope and sources

The book teaches Lectures 1–7 and uses Lecture 10 for the midterm blueprint and sample style. Kaching/POS, WorkshopHub, DormFix, ShuttleNow, KU Registration and UML examples are applications of the lecture ideas. Unknown performance thresholds, payment protocols, permissions and missing meeting-note assignments remain labeled as open questions or assumptions.

The repository's Week 8 and Week 9 materials remain useful course sources, but are outside this midterm edition's stated scope. See `docs/SOURCE_AND_LAB_MAP.md` for the links to lectures, labs, examples and the instructor sample. The separate Computer Architecture files are not used as Software Engineering sources.

## Authoring approach

The lesson sequence follows need → requirements → design/specification → security → planning → execution/evidence. Each idea is taught once in the lecture chapter; later case studies apply it without repeating the whole definition. Diagrams are vector redraws where a source image was incomplete or hard to read. Source crops are retained only when the original artifact itself matters.

See `docs/WRITING_AND_DIAGRAM_GUIDE.md` for the writing and visual rules, and `content_inventory.md`, `source_trace.md` and `figure_manifest.md` for coverage and provenance.

## Build the PDFs

Run XeLaTeX from this directory; the font files and figure source are local.

```sh
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build mock_exam.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build mock_exam.tex
```

Final rendering and validation checks are recorded in [`qa_checklist.md`](qa_checklist.md) and [`final_pdf_validation.json`](final_pdf_validation.json).
