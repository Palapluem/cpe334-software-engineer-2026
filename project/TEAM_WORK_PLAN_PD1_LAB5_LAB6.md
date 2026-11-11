# PocketLedger: team work plan for PD1, Lab 5 and Lab 6

**For:** Wisit Suwannao (Palapluem) and Natthawat Primsirikunawut (N0TAW00D)

**Group:** 2-Nor · **Product:** PocketLedger · **Theme 7:** Personal Money and Expense Logging System

**Status checked:** 11 November 2026
**Purpose:** one practical handoff showing the work order, ownership, source files and evidence for the next checkpoints. This guide supplements the official handouts; it does not replace them or approve a proposed product decision.

## Read this first

The work is one connected product, not three separate projects:

1. **Project Deliverable 1 (PD1):** agree the product baseline and Sprint 1 contracts, build and test a useful working increment, review it, and release it on `main`.
2. **Lab 5:** take that accepted Sprint 1 release, package it, add required CI and deploy it to GCP with persistent data and a repeatable release pipeline.
3. **Lab 6:** provide Sprint 1 UAT cases to another team, independently test that team's release, triage findings on PocketLedger, fix and release blocking defects, and obtain an independent retest decision.
4. **Project Deliverable 2 and Final Delivery:** continue the same product, repository, release history and traceability through Sprint 2, Sprint 3 and final verification.

The reports must describe real work on the PocketLedger repository and the exact version tested. A planned task, drafted test, screenshot of TokTickIT, or green check from an older commit does not prove the current product works.

## Current status snapshot

### PocketLedger product repository

Repository: [Palapluem/pocket-ledger](https://github.com/Palapluem/pocket-ledger)

| Item | Verified status on 11 November 2026 |
|---|---|
| `main` | `a4cced2` — documentation/bootstrap baseline; no accepted Sprint 1 release |
| `sprint-1-staging` | `ff2143a` — PR #4's documentation changes are merged here |
| PR #4 | Merged by N0TAW00D on 8 November 2026; the PR added documentation, not application code or test results |
| Open PRs | None at the check time |
| Open Issues | #1 financial rules and Sprint 1 slice; #2 team/runtime/authentication decisions; #3 English baseline and Sprint 1 contracts |
| Application source/tests | Not present in the tracked product tree at the check time |
| Decisions | D-01 is partial; D-02–D-07 remain proposals/open decisions in `docs/decisions.md` |

**This makes the schedule high risk.** The next task is not to wait for another PR to review. Both students need to resolve the blocking decisions, agree bounded features, and start implementation through Issues and reviewed PRs. Do not treat the proposals in `docs/decisions.md` as team-approved until both students agree and record them.

### Report documents

The four links point to separate tabs in the same Google Doc:

| Assessment | Google Docs tab | State last compared |
|---|---|---|
| PD1 | [Project Deliverable 1](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.241qhfcdhce3) | The report must match the accepted Sprint 1 release and actual evidence. |
| Lab 5 | [Lab 5](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.s9umabyrevqi) | Separate Lab 5 evidence index. |
| Lab 6 | [Lab 6](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.uhs47dish96h) | On 10 Nov, the body matched the Lab 5 tab except for its title. Rebuild this tab for Lab 6; it is not a Lab 6 report yet. |
| PD2 | [Project Deliverable 2](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.amnwb9uwd0u0) | On 10 Nov, the body matched the PD1 tab except for its title. Replace it with the PD2 requirements and evidence; it is not a PD2 report yet. |

Do not copy forward claims, screenshots, test results, release SHAs or dates from one assessment into another unless they actually apply to the tested version.

## Deadlines and the immediate risk

| Work | Date in the handout | Current note |
|---|---|---|
| PD1 | 8 Nov 2026, 23:59 | Wisit reports that the deadline moved to **14 Nov**. Confirm the announcement with the instructor/TA; the local handout still shows 8 Nov. |
| Lab 5 | 15 Nov 2026, 23:59 | The Lab 5 handout still gives this date. Confirm whether it also moved; do not assume it did. |
| Lab 6 | 22 Nov 2026, 23:59 | Arrange the independent partner team now. |
| PD2 | 29 Nov 2026, 23:59 | Sprint 2 completion plus real Sprint 3 progress. |
| Final Delivery | 13 Dec 2026, 23:59 | Final release, full verification and presentation video. |

Because PD1 and Lab 5 are one day apart in the available instructions, contact the TA **today** if the product has not yet begun implementation or if the Lab 5 deadline is unchanged. Ask for the applicable dates and the required recovery plan. Do not hide missing work or claim a deployment that has not happened.

## What both students do together

Both members must participate in requirements, design, tests, implementation, AI-agent supervision, review and release. A temporary owner split is fine; permanent “one writes docs, one writes code” roles are not. Each person must understand the behavior and be able to explain sampled steps.

### Step 1 — Hold a short team decision session

Open [Issue #1](https://github.com/Palapluem/pocket-ledger/issues/1), [Issue #2](https://github.com/Palapluem/pocket-ledger/issues/2), [Issue #3](https://github.com/Palapluem/pocket-ledger/issues/3), and `docs/decisions.md` on `sprint-1-staging`.

Agree and record the decisions that affect Sprint 1 behavior before implementing them:

- product scope and the smallest complete Sprint 1 user journey;
- stack/runtime and reproducible local setup;
- money representation, balance signs, allocation rules, dates and correction boundaries;
- authentication, current-user behavior, roles and ownership/privacy rules;
- public UI/API/data interfaces and how each acceptance criterion will be tested.

Use the team's actual answers. If an answer is not known, record it as open and ask the instructor/TA; do not convert a proposed value into a fact.

### Step 2 — Give each student a bounded feature Issue

Agree on a vertical slice only after Step 1. A possible split to discuss is one identity/access slice and one financial transaction/persistence slice. This is a proposal, not an approved feature assignment.

For each Issue, record the linked requirement/feature/AC IDs, owner, expected behavior, test evidence and completion conditions. The implementer creates a branch from `sprint-1-staging`; the other student reviews the PR and merges only after the contract, diff, tests and results check out. Then swap roles on the next Issue.

Use the product board sequence:

`Backlog → Specified → Started → PR Review → Fixing → Done`

Move an Issue to Done only when its acceptance criteria are satisfied. A Done card by itself does not prove that the release is on `main` or deployed.

## PD1: deliver an accepted Sprint 1 release

Official source: [`Project Deliverable 1` handout](Project%20Deliverable%201/project_deliverable_1_v1.pdf), [preparation guide](Project%20Deliverable%201/README.md), [report outline](Project%20Deliverable%201/report-outline.md), and [feature contract template](Project%20Deliverable%201/feature-contract-template.md).

| Part | What must be completed | Where the canonical product material lives |
|---|---|---|
| A — SRS and scope (10) | Stakeholder/problem, actors, scope/exclusions, stable FR/BR/NFR IDs, measurable NFR checks, assumptions and decisions | `docs/srs.md`, `docs/decisions.md` |
| B — Feature inventory and traceability (10) | Every baseline requirement linked to a feature/responsibility, sprint and verification; expose gaps and approved changes | `docs/features.md`, `docs/traceability.md`, `docs/sprints/plan.md` |
| C — System-Level SDS (15) | UI/API/database architecture, data model, role/permission matrix, auth/session, configuration and deployment design | `docs/system-sds.md` |
| D — Three-sprint plan (5) | Goals, feature IDs, dependencies and completion outcomes for Sprints 1–3 | `docs/sprints/plan.md` |
| E — Sprint 1 contracts (20) | Feature design, UI/API/data details, validation/permissions, stable AC, STS, DoD and visible contract history before implementation | `docs/sprints/sprint-1/contract.md`, `docs/sprints/sprint-1/tests.md` and feature contract files added through reviewed work |
| F — Working increment and verification (20) | UI→API→database domain journey and retrieval; real login/logout/current identity; at least two roles; meaningful rule rejection; persistence/access tests; reviewed staging integration and release to `main` | Application source, tests, migrations, README, Issues/PRs and release records in the product repository |

PD1 must release a working Sprint 1 increment to `main`. It must have a complete domain journey, authentication and permissions enforced by the backend, meaningful business-rule validation, persisted data, and tests for rules, persistence and access. Seeded test accounts are sufficient. Docker, completed CI/CD and GCP deployment belong to Lab 5, not PD1.

The PD1 PDF must be self-contained and include Parts A–F, page navigation, selected program evidence, actual build/test results and tested commit, AC-to-test results, two short test excerpts, meaningful red/green history, two completed Issue/PR samples, contributions from both students, truthful AI-use and known limitations. A repository link does not replace the required material in the PDF.

### Immediate PD1 exit checks

- [ ] Both students have resolved or explicitly escalated the decisions needed for the selected Sprint 1 scope.
- [ ] Every Sprint 1 feature has a reviewed contract, AC and planned tests before implementation.
- [ ] The implemented flow works through UI, API and database; saved data can be retrieved.
- [ ] Login/logout, current identity, two roles, business-rule rejection and backend access denial are verified.
- [ ] The tests and build run on the release commit; failures/skips and actual counts are recorded.
- [ ] Feature PRs enter staging with substantive teammate review; a reviewed release PR reaches `main`.
- [ ] The PDF points to that exact release and contains the required evidence, not placeholders presented as results.

## Lab 5: package and deploy the PD1 release

Official sources: [`Lab 5` handout](../labs/Lab05/01_SE_Lab_5_updated.pdf), [Student Guide V1.1](../labs/Lab05/03_Student-Guide-GCP-Deployment-and%20CI%20CD-V1_1.pdf), [course deployment template](../labs/Lab05/deployment-template.md), and the reference kit in `../labs/Lab05/toktickit-lab5-starter/`. The starter kit is an example; do not copy TokTickIT application source into PocketLedger.

The team starts Lab 5 from the accepted PD1 release and keeps the same app, GCP project and pipeline for later work.

| Requirement group | Work and proof |
|---|---|
| R-01–R-02: Docker/config | A clean clone builds and runs; settings come from environment variables; `.env.example` contains placeholders only; no real secrets enter Git, image, logs or PDF. |
| R-03–R-04: GCP/data | A public URL runs the real UI/API/database workflow; data persists outside the container and survives restart and redeploy. |
| R-05–R-06: CI gate | Relevant PRs run meaningful build/tests; configure a required check and prove a temporary failing PR is blocked. Never merge the failing proof PR. |
| R-07–R-08: repeatable release | Reviewed changes flow through CI and merge to `main`, then deploy through the same pipeline; identify the running commit/tag/revision and document the repeatable release procedure. |
| R-09–R-12: team/repository | Use Issues, feature branches, reviewed staging PRs and reviewed release PRs; label Lab 5 work; preserve history; record both members' contributions; keep the product repository public and secret-free. |

Create or update `Dockerfile`, `.dockerignore`, `.env.example`, workflow files, and `docs/labs/lab-05/deployment.md` in the **PocketLedger repo**. The deployment document must list actual environment variables and their sources, safe commands, GCP project/region/resource names and release procedure. Use the Lab 5 report's Answer Part 0–4 evidence index; keep it concise, link directly to actual artifacts/runs, and add screenshots only where a link cannot prove the result.

Record the six required checks against the tested commit: **C-01** passing normal PR build/tests; **C-02** failing temporary PR blocked by the required check; **C-03** clean-clone build/run; **C-04** live public workflow; **C-05** data after restart and redeploy; **C-06** reviewed staging-to-main release, CI/deployment and running revision matching the release commit. The failing proof PR must stay unmerged. Submit one team PDF to LEB2 named `lab5_sec<section>_<group name>.pdf`.

GCP setup requires care. Set an alerts-only budget before resources, never commit service keys or connection strings, do not pay prepayment or click Upgrade as part of the prescribed free-trial flow, and review every IAM/billing/database change. Ask the student and TA before a material cloud change; an agent must not change billing, IAM or databases on its own.

### Immediate Lab 5 exit checks

- [ ] Clean-clone build and container run work with documented environment configuration.
- [ ] CI runs for PRs into staging and main; a failing required check demonstrably blocks merge.
- [ ] The public URL serves the reviewed `main` release and the business workflow works.
- [ ] Data remains after an application restart and after a redeploy.
- [ ] A release run identifies the exact running commit/revision.
- [ ] `deployment.md` and the Answer Part 0–4 evidence index are complete and truthful.

## Lab 6: independent UAT and defect handling

Official source: [`Lab 6` handout](../labs/Lab06/Lab_6_Sprint_1_UAT.pdf), [course preparation guide](../labs/Lab06/README.md), and [report outline](../labs/Lab06/report-outline.md). The new [Lab 6 Google Docs tab](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.uhs47dish96h) needs Lab 6 content; as last checked, it was still a copy of Lab 5.

Both two-person teams take both roles:

| Role | What PocketLedger's team must do |
|---|---|
| Product Team | Prepare executable Sprint 1 cases, safe accounts, deployed version/URL and instructions; review every finding; fix accepted critical/major defects; run regression; deploy and provide a corrected version for independent retest. |
| UAT Team | Independently execute another team's cases against its identified Sprint 1 release; record actual results and reproducible findings; retest fixes; make the evidence-based acceptance decision. |

Find the other team and agree UAT, defect review and retest times now. Do not use a teammate's own developer tests as independent UAT. If the partner team is unavailable or the service cannot be accessed, notify the instructor/TA promptly and retain the notice.

Prepare at least four executable cases, each with stable ID, linked Sprint 1 requirement/AC, role, preconditions, synthetic inputs, numbered steps and specific expected result:

1. Normal finance workflow with explicit expected money movement/balances.
2. Business-rule or boundary rejection; verify no partial transaction or balance change.
3. Forbidden role/ownership access, including another user's records and Administrator denial of financial data.
4. State/history/persistence behavior in the implemented Sprint 1 scope.

Four is a minimum; add cases to cover important implemented Sprint 1 criteria. Record expected and actual separately, with tester, date/time, tested version and PASS/FAIL/BLOCKED. Triage every real finding against the contract. Critical/major defects must be fixed and independently retested. If there is no natural defect, ask the TA for an isolated controlled exercise; never invent a defect or break the accepted release to create one.

The Lab 6 PDF has Parts A–D: **A UAT preparation/handoff (20), B independent execution (25), C defect reporting/triage (20), D resolution and independent retest (35)**. Embed cases, selected actual evidence, all finding dispositions, red/green fix evidence, CI/release/retest and the final independent acceptance decision in one PDF.

## Later project checkpoints

The same PocketLedger repo and released history continue. Do not start these as separate products or overwrite the accepted Sprint 1 baseline.

| Checkpoint | Required next outcome | Source |
|---|---|---|
| PD2, 29 Nov | Sprint 1 continuity; all planned Sprint 2 features complete/reviewed/tested; all Sprint 3 contracts plus at least one meaningful Sprint 3 workflow/rule implemented and tested; updated traceability; integrated deployed candidate and dated remaining-work plan. | [`PD2 handout`](Project%20Deliverable%202/project_deliverable_2_v1.pdf), [`PD2 README`](Project%20Deliverable%202/README.md), [`PD2 outline`](Project%20Deliverable%202/report-outline.md) |
| Lab 7 | Approved maintenance/change exercise, measurement and regression on the same release history. Wait for/use the Lab 7 handout and instructor approval before changing implemented behavior. | `../labs/Lab07/` and product `docs/labs/lab-07/change-and-metrics.md` |
| Final Delivery, 13 Dec | Final integrated release; all requirements/contracts/tests traceable to final behavior; final regression/UAT and deployment evidence; final report and app demonstration by both members. | [`Final Delivery handout`](Final%20Delivery/project_final_delivery_v1.pdf), [`Final README`](Final%20Delivery/README.md), [`Final outline`](Final%20Delivery/report-outline.md) |

The Final handout gives different video limits in two sections (10 minutes and 4 minutes). Ask the instructor/TA which limit controls before recording.

## Canonical file map

### Course repository: instructions, preparation and submitted PDFs

- `project/README.md` — project map and repository boundary.
- `project/Project Deliverable 1/` — PD1 PDF, preparation guide, feature-contract template and report outline.
- `labs/Lab05/` — Lab 5 handout, Student Guide, deployment template, report outline and reference Starter Kit.
- `labs/Lab06/` — Lab 6 handout, preparation guide and report outline.
- `project/Project Deliverable 2/` — PD2 handout, preparation guide and report outline.
- `project/Final Delivery/` — Final handout, preparation guide and report outline.
- `project/group_work_specs_v1.pdf` — master product/theme requirements; use each assessment handout for its submission details.

### PocketLedger product repository: source of truth for the product

Use [the product repository](https://github.com/Palapluem/pocket-ledger) for code and canonical engineering documents. The reviewed baseline is currently on `sprint-1-staging`, not on `main`.

| Path in product repository | Purpose |
|---|---|
| `AGENTS.md`, `CONTRIBUTING.md`, `COORDINATION.md` | Product rules, branch/review workflow and safe task handoff. Read before work. |
| `docs/decisions.md` | Single register for team decisions. Update only after agreement. |
| `docs/srs.md` | Whole-product requirements and scope. |
| `docs/features.md`, `docs/traceability.md` | Feature inventory and requirement verification map. |
| `docs/system-sds.md` | System architecture, data, UI/API, access and deployment design. |
| `docs/sprints/plan.md` | Goals, features and dependencies for three sprints. |
| `docs/sprints/sprint-1/contract.md`, `docs/sprints/sprint-1/tests.md` | Sprint 1 contract, AC, STS and DoD baseline. |
| `docs/labs/lab-05/deployment.md` | Lab 5 deployment draft; fill with actual stack, variables, resources and results. |
| `docs/labs/lab-06/uat.md` | Lab 6 UAT preparation draft; execution fields remain unverified until performed. |
| `docs/labs/lab-07/change-and-metrics.md` | Lab 7 preparation draft; follow the actual handout and approval gate. |
| `docs/assessment-plan.md`, `docs/releases.md` | Evidence mapping and immutable release history. |

The course repository and product repository are separate Git roots. Never copy PocketLedger source into the course repository or stage files from both roots in one Git operation. Product work follows Issue → branch from `sprint-1-staging` → reviewed PR → integration → reviewed release PR to `main`. The author does not approve their own PR; preserve pushed history and do not open a PR merely to record a previous merge.

## Message to send the teammate

> เราต้องเร่งเริ่ม PocketLedger แล้วนะ ตอนนี้ PR #4 merge เข้า `sprint-1-staging` แล้ว แต่เป็นเอกสาร ยังไม่มีโค้ดแอป ไม่มี PR เปิดอยู่ และ Issue #1–#3 ยังเปิดอยู่
>
> วันนี้ช่วยนัดคุยกันเพื่อปิด decision ที่กระทบ Sprint 1 ใน Issue #1/#2 และเลือก vertical slice ที่ทำจบได้ก่อนนะ จากนั้นแบ่ง Issue ให้เราสองคนรับคนละส่วน ทำ contract/AC/test plan ก่อน implementation แล้วเปิด PR เข้า `sprint-1-staging` ให้กัน review และสลับบทบาทในงานถัดไป เป้าหมายแรกคือมี journey ที่ใช้ได้จริงผ่าน UI/API/database พร้อม login, role/ownership, rule rejection, persistence และ tests แล้วค่อย release ที่ผ่าน review ไป `main` สำหรับ PD1
>
> หลังได้ release ของ PD1 ค่อยทำ Lab 5 ต่อจาก version เดียวกัน: Docker/env, CI required check, GCP public deployment, persistence หลัง restart/redeploy และ release pipeline ส่วน Lab 6 เราต้องหาอีกทีมมาเป็น independent UAT partner ตอนนี้เลย เพราะทีมเราทดสอบ PocketLedger เองแทนเขาไม่ได้
>
> เราเข้าใจว่า PD1 เลื่อนเป็น 14 พ.ย. แต่ handout Lab 5 ยังระบุ 15 พ.ย. ขอให้เราถาม TA วันนี้ว่า Lab 5 เลื่อนด้วยไหม และยืนยันแผน/เวลาที่แต่ละคนทำได้ เพราะตอนนี้ timeline เสี่ยงมาก

## Sources and status discipline

The requirements above come from the local assessment PDFs linked in each section. Where a user-reported extension conflicts with a saved PDF, record both and verify the official announcement. Mark planned items as planned; only record PASS, accepted, deployed, reviewed or complete after the named evidence exists for the identified version.
