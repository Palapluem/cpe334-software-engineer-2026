# CPE334 — Software Engineering (Semester 1/2026)

Course materials, lab work, and midterm preparation for CPE334 Software Engineering. This repository keeps the course-facing materials together; the TokTickIT application is maintained in its own repository.

## Course materials

- [Lecture materials](lectures/): slides, examples, and study notes for the course.
- [Week 10 midterm and project guide](lectures/Week%2010/README.md): exam-topic map, project-launch material, and source-document notes.
- [Lab materials and reports](labs/): lab sheets, evidence, and submitted reports for Labs 1–4.
- [TokTickIT product repository](https://github.com/Palapluem/toktickit_cpe334): the application repository used for the engineering labs. It is separate from this course-material repository.

## Midterm preparation

- [Two-page cheat sheet](preparation/cheat-sheet/README.md) — a compact Thai review of Lectures 1–7 and Practice Midterm. The PDF is prepared as a clean handout; source mapping, glossary, and review questions with answers are kept in the companion README.
- [Practice midterm paper and sources](preparation/mock-exam/README.md#published-files) — one 30-page A4 paper with a Thai cover, English-first questions followed by Thai and one landscape Gantt sheet; supplementary exercises remain in source form.
- [Bilingual midterm mock exam (30 pages; English first, Thai below)](preparation/mock-exam/midterm/output/pdf/CPE334_Midterm_Mock_TH_EN.pdf)
- [Thai solutions and marking guide: core edition (15 pages)](preparation/mock-exam/midterm/output/pdf/CPE334_Midterm_Mock_Solutions.pdf)
- [Thai solutions and marking guide: with supplementary answers (18 pages)](preparation/mock-exam/midterm/output/pdf/CPE334_Midterm_Mock_Solutions_With_Supplements.pdf)
- [Cheat sheet (PDF)](preparation/cheat-sheet/midterm/output/pdf/CPE334_Midterm_Cheat_Sheet.pdf)

The practice papers are student-created study materials, not actual or officially approved examinations, and do not predict the questions on the real exam. The cover reproduces institutional exam-form elements for practice; its publication checkbox and committee/signature fields are examples, not records of actual permission or approval. See the preparation READMEs for scope, sources, and build instructions.

## Repository layout

```text
lectures/                  Course slides, examples, and study notes
labs/                      Lab sheets, reports, evidence, and project workflow
preparation/
  cheat-sheet/             Editable LaTeX source and two-page PDF
  mock-exam/               Bilingual exam source, printable paper and Thai solutions
```

LaTeX source files and their printable PDFs are kept together in `preparation/`. Build intermediates and operating-system metadata are excluded. When revising course content, keep the source and its generated deliverable in sync, and verify the rendered PDF before replacing the published copy.
