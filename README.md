# CPE334 — Software Engineering (Semester 1/2026)

Course materials, lab work, and midterm preparation for CPE334 Software Engineering. This repository keeps the course-facing materials together; the TokTickIT application is maintained in its own repository.

## Course materials

- [Lecture materials](lectures/): slides, examples, and study notes for the course.
- [Week 10 midterm and project guide](lectures/Week%2010/README.md): exam-topic map, project-launch material, and source-document notes.
- [Lab materials and reports](labs/): lab sheets, evidence, and submitted reports for Labs 1–4.
- [TokTickIT product repository](https://github.com/Palapluem/toktickit_cpe334): the application repository used for the engineering labs. It is separate from this course-material repository.

## Midterm preparation

- [Two-page cheat sheet](preparation/cheat-sheet/README.md) — natural-Thai review of Lectures 1–7 and Practice Midterm; includes topic-to-source pages, a glossary, and 10 review questions with answers in the companion README.
- [Practice midterm (Thai and English)](preparation/mock-exam/README.md#midterm) — 21-page booklets: the 17-page timed paper plus supplementary Use Case, State and Git graph exercises outside the 100 marks; 18-page Thai solutions with worked diagrams and a marking guide.
- [Thai practice paper (PDF)](preparation/mock-exam/midterm/output/pdf/CPE334_Midterm_Mock_Exam.pdf)
- [English practice paper (PDF)](preparation/mock-exam/midterm/output/pdf/CPE334_Midterm_Mock_Exam_EN.pdf)
- [Thai solutions and marking guide (PDF)](preparation/mock-exam/midterm/output/pdf/CPE334_Midterm_Mock_Solutions.pdf)
- [Cheat sheet (PDF)](preparation/cheat-sheet/midterm/output/pdf/CPE334_Midterm_Cheat_Sheet.pdf)

The practice papers are student-created study materials, not actual or officially approved examinations, and do not predict the questions on the real exam. The cover reproduces institutional exam-form elements for practice; its publication checkbox and committee/signature fields are examples, not records of actual permission or approval. See the preparation READMEs for scope, sources, and build instructions.

## Repository layout

```text
lectures/                  Course slides, examples, and study notes
labs/                      Lab sheets, reports, evidence, and project workflow
preparation/
  cheat-sheet/             Editable LaTeX source and two-page PDF
  mock-exam/               Editable Thai/English exam sources and solution PDFs
```

LaTeX source files and their printable PDFs are kept together in `preparation/`. Build intermediates and operating-system metadata are excluded. When revising course content, keep the source and its generated deliverable in sync, and verify the rendered PDF before replacing the published copy.
