# Week 10 — Midterm Review and Group Project Launch

This page indexes the Week 10 source files and turns their main requirements into a working study and project checklist. These are the PDFs currently present in this workspace, not a determination that every file is final or internally consistent. In particular, the group-work specification is marked as a draft; use instructor-approved handouts and confirm conflicts before making grading decisions.

## Source files

| File | Use it for |
| --- | --- |
| [`CPE334_Lecture10 - Midterm Exam Prep_Group Work Project.pdf`](CPE334_Lecture10%20-%20Midterm%20Exam%20Prep_Group%20Work%20Project.pdf) | 141-slide midterm review, UML and Git practice, spec-driven development (SDD), project milestones, and group labs. |
| [`CPE334_Midterm Samples by Suthep.pdf`](CPE334_Midterm%20Samples%20by%20Suthep.pdf) | Bilingual requirements case, UML exercises, Git repository-graph problems, and worked solutions. |
| [`group_project_spec_files/group_work_specs_v1.pdf`](group_project_spec_files/group_work_specs_v1.pdf) | Draft group-project specification covering scope, team rules, themes, engineering workflow, and Lab 5–7. It is marked “Draft for instructor review”; do not assume it is the approved master without confirmation. |
| [`group_project_spec_files/project_deliverable_1_v1.pdf`](group_project_spec_files/project_deliverable_1_v1.pdf) | Sprint 1 baseline and working increment requirements (80 points). |
| [`group_project_spec_files/project_deliverable_2_v1.pdf`](group_project_spec_files/project_deliverable_2_v1.pdf) | Sprint 2 completion, Sprint 3 progress, and integrated release candidate (70 points). |
| [`group_project_spec_files/project_final_delivery_v1.pdf`](group_project_spec_files/project_final_delivery_v1.pdf) | Complete product, final verification, and release handoff (100 points). |

## Midterm review map

The slides divide the review into three parts:

| Part | Points | Practice focus |
| --- | ---: | --- |
| Dr. Piyanit | 25 | Analyze and improve requirements; evaluate a lightweight proposal; construct a role/operation access matrix; reason about attack surfaces, trust boundaries, security objectives, and mitigations. Review access-control/authentication failures, SQL injection, XSS, CSRF, SSRF, unsafe errors/configuration/secrets, and dependencies. |
| Dr. Santawat | 25 | Waterfall planning: WBS (3), RACI (2), and Gantt chart (5); backlog grooming (10); sprint planning (5). Be ready to turn facts into a coherent schedule, responsibilities, issue/story, acceptance criteria, estimates, and sprint backlog. |
| Dr. Suthep | 50 | Requirements-to-UML questions (30 points selected from sequence, activity, list/form UI, use-case, and state diagrams); Git workflow/repository graphs (20 points selected from predicting state, explaining graphs, and writing commands). |

The sample packet includes solutions. For Git questions, track `HEAD`, local branch pointers, and `origin/*` remote-tracking pointers separately. Switching branches moves `HEAD`; it does not contact GitHub. A fast-forward is possible when the current branch tip is an ancestor of the merged tip; diverged histories require a three-way merge if the merge succeeds. A graph alone cannot prove that file edits will conflict.

For UML practice, first identify the required scope: a workflow with branches is an activity diagram; one concrete scenario is a sequence diagram. Use the given requirements and state assumptions explicitly. The sample packet covers requirements for a KU Course Registration System and provides Git problems for repeated graph-and-command practice.

## Group project at a glance

Work in the same two-person team, repository, and application across the project and Group Labs 5–7. The assigned theme is based on the last digit of a student ID: digits 1–9 map to themes 1–9, and digit 0 maps to theme 10. When partners have different digits, the master specification allows the team to choose between their themes. Confirm the final theme/context and any material ambiguity with the instructor or TA.

The product must be a real full-stack application: UI → API/application layer → persistent database. It needs a meaningful domain workflow, backend-enforced authentication/authorization with at least two useful roles from Sprint 1, and tests for domain rules, persistence, and access restrictions. A modular monolith is acceptable. Keep credentials/secrets out of Git and use synthetic data; real payments and external messaging/API integrations are not required.

### Three-sprint and submission timeline

Dates below reproduce the supplied Week 10 schedule. The draft `group_work_specs_v1.pdf` says submissions are due at 23:59, but confirm each deadline against the instructor-approved handout or announcement. For example, the supplied Deliverable 2 handout states 29 November 2026 but does not specify a time.

| Due | Assessment | Expected checkpoint | Points / course weight |
| --- | --- | --- | ---: |
| 8 Nov 2026 | Project Deliverable 1 | Product baseline and released, tested Sprint 1 vertical slice. | 80 / 8% |
| 15 Nov 2026 | Group Lab 5 | Docker, CI/CD quality gate, and repeatable GCP deployment of Sprint 1. | 100 / 5% |
| 22 Nov 2026 | Group Lab 6 | Cross-team UAT, defect triage, fix, and independent re-test. | 100 / 5% |
| 29 Nov 2026 | Project Deliverable 2 | All Sprint 2 features complete; Sprint 3 contracts and tested progress; deployed release candidate. | 70 / 7% |
| 29 Nov 2026 | Group Lab 7 | Approved maintenance change, regression evidence, metrics, and release readiness. | 100 / 5% |
| 13 Dec 2026 | Final Project Delivery | Complete integrated product, final verification, deployed release, report, and demo video. | 100 / 10% |

The project specifications allocate 250 raw points (25% of the course) across the three project deliverables. Group Labs 5–7 have a separate 300 raw points (15%); together with Labs 1–4, the specifications state that all labs are 700 points (35%).

### Work checklist

#### Before implementation

- [ ] Confirm the assigned theme, domain context, actors, scope, exclusions, assumptions, and decisions.
- [ ] Write an SRS with stable IDs for functional requirements (FR), business rules (BR), and measurable non-functional requirements (NFR).
- [ ] Build a feature inventory and map every baseline requirement to a feature/responsibility, sprint, and planned verification.
- [ ] Write the system-level SDS: component/stack choices, data model and constraints, UI/API conventions, role/permission matrix, authentication/session approach, configuration, and deployment design.
- [ ] Allocate the complete product across three sprints. Plan Sprint 1 as a small end-to-end vertical slice with authentication, authorization, persistence, and a tested domain rule.

#### Before implementing each feature

- [ ] Create a feature engineering contract: feature SDS/workflow, linked requirements, applicable UI/API/data details, validation/errors/permissions, stable acceptance criteria (AC), Software Test Specification (STS), and Definition of Done (DoD).
- [ ] Create a bounded GitHub Issue linked to the feature and contract. Preserve contract/test-design history before implementation and record justified changes.
- [ ] Map every AC to an appropriate test. Use unit tests for important logic, API/database integration tests for persistence and permissions, and selected UI/end-to-end tests for critical journeys. Include negative and boundary cases.

#### Implement and release

- [ ] Implement one bounded Issue on a feature/fix branch from the sprint staging branch; run relevant checks and inspect the diff.
- [ ] Open a PR to sprint staging and obtain a substantive teammate review. Authors do not approve their own PRs.
- [ ] Run sprint integration/system and acceptance checks; fix failures on an Issue/branch and re-test.
- [ ] Open a reviewed release PR from sprint staging to `main`; record the accepted commit/tag. After Lab 5, deploy accepted releases through the repeatable delivery process.
- [ ] Use agents for bounded specification/coding assistance, then inspect their output, tests, and diff. Both students remain responsible for and able to explain the product. Include the brief AI-use declaration requested by the deliverables; full transcripts are not required.

#### Evidence to retain

- [ ] Stable requirement, feature, sprint, AC, test, and result/version links; disclose uncovered, failed, skipped, or incomplete items.
- [ ] Actual build/test/CI commands, outputs and counts tied to the assessed commit; meaningful test excerpts and TDD red/green history where applicable.
- [ ] Demonstrations with feature/AC IDs, role, preconditions, expected/actual result, persisted-data retrieval, a meaningful rejection, and backend evidence for restricted access.
- [ ] Issue/branch/PR/review/staging/release history, both students’ contributions, setup/migration/seed instructions, and a current known-limitations/defects list.
- [ ] Put the required engineering documents and selected execution evidence directly in each submitted PDF; the repository alone does not replace the PDF contents.

## Source details to confirm

The source documents contain material status/rubric differences. Confirm these with the instructor/TA before treating them as final:

1. `group_work_specs_v1.pdf` is explicitly marked “Draft for instructor review” and issued 6 October 2026.
2. `project_deliverable_1_v1.pdf` names `group_work_specs.docx` as the master specification, but the supplied Week 10 folder contains `group_work_specs_v1.pdf`, not that DOCX. Confirm that the supplied draft is the intended and approved version before using it to settle scope or grading questions.
3. Final video duration differs: the master specification and the required-outcome paragraph in `project_final_delivery_v1.pdf` allow up to 10 minutes, but that PDF's Part E rubric says a maximum of 4 minutes.
4. Final assessment points differ: the master specification allocates 8 points to the demo and 2 to a one-page release summary; `project_final_delivery_v1.pdf` allocates 10 points to the demo and has no separate 2-point summary row.

Until clarified, follow the latest instructor-approved specification and keep the assessed release/version explicit in the submission.
