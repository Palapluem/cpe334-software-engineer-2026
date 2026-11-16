# PocketLedger: team work plan for PD1, PD2, Labs 5–7 and Final Delivery

**Team:** Wisit Suwannao (Palapluem) · Natthawat Primsirikunawut (N0TAW00D) · **LEB2 group:** 2-Nor · **Product:** PocketLedger, Theme 7: Personal Money and Expense Logging System

**Status checked:** 16 November 2026

This is the shared work plan for the same product, team and product repository across Project Deliverables 1–2, Labs 5–7 and Final Delivery. Use each assessment's official handout as the authority for its rubric and submission requirements. This file maps the dependencies, current status, team work and source paths.

## Schedule and dependency map

These assessments share one product and repository, but they are not six consecutive blocks. Lab 6 preparation and Sprint 2 work overlap with deployment; Lab 7 and PD2 also overlap and share a deadline.

| When / checkpoint | Workstream | Dependency and exit condition |
|---|---|---|
| First: PD1 | **Project Deliverable 1** | Agree the Sprint 1 contract, implement and verify the vertical slice locally, then release it through reviewed PRs to `main`. PD1 is the starting release for the later labs. The saved handout says 8 November 2026, 23:59; the student-reported cutoff was 15 November 2026, 23:30 Asia/Bangkok. Both dates have passed; no extension is verified. |
| Next: Lab 5, original date 15 Nov | **Docker, PR CI and GCP deployment** | Prepare configuration while PD1 work finishes; deploy the accepted Sprint 1 release. Complete the clean-clone/container check, required PR checks and repeatable deployment to GCP. The handout date has passed; no extension is verified. |
| Prepare alongside Lab 5; execute after deployment; due 22 Nov | **Lab 6 UAT** | Arrange the partner team and write executable cases early. Execute both teams' UAT responsibilities against the identified deployed Sprint 1 releases once they are available. Triage findings; fix and independently retest release-blocking defects through the Lab 5 delivery process. |
| After the Sprint 1 baseline; continues during Labs 5–7; due 29 Nov | **Sprint 2 and PD2** | Implement all planned Sprint 2 features with reviewed contracts and tests, define all remaining Sprint 3 contracts, and implement/test at least one meaningful Sprint 3 workflow. PD2 requires a coherent GCP-deployed candidate and reports relevant deployment, UAT and maintenance findings, including honest unresolved status. |
| Work sessions listed 17/19 Nov; due 29 Nov in the available master | **Lab 7 maintenance** | The available master document is marked draft for instructor review, and the Lab 7 folder still has no detailed official handout. Treat these dates and rubric as provisional. Provisionally plan one instructor/TA-approved change to an already implemented behavior, regression-safe delivery and metrics. Run it alongside Sprint 2/PD2; reconcile the details when the official Lab 7 handout arrives. |
| After PD2; final due 13 Dec | **Final Delivery** | Complete Sprint 3, integrate and verify the approved scope, perform final UAT/retests, and deliver the final release, report and demonstration. |

**Immediate order:** finish the accepted PD1 release, then complete the Lab 5 deployment path. Book the Lab 6 partner now and prepare its cases in parallel; its execution depends on a working deployed Sprint 1 release. Continue Sprint 2 while Labs 5 and 6 run. Lab 7 and PD2 both have a 29 November deadline, so coordinate their release/evidence cutoffs; PD2 does not need to wait for a separate later “Lab 7 phase,” but it must report the maintenance finding/status that exists at submission. Keep one product identity, repository and release history throughout.

## Current status snapshot

### Product repository

Repository: [Palapluem/pocket-ledger](https://github.com/Palapluem/pocket-ledger)

| Item | Verified status on 16 November 2026 |
|---|---|
| `main` | `a4cced2` — bootstrap/documentation baseline; no accepted Sprint 1 release. |
| `sprint-1-staging` | `922adfc` — current integrated candidate; PR #27 is the latest merge. |
| PR #18 | Merged into staging at `8cefcaf`; identity/administration UI and browser identity journey. |
| PR #19 | Merged into staging at `a77d324`; Lab 5 container/deployment pipeline. This merge is not evidence of a GCP deployment. |
| PRs #22 and #23 | Merged into staging at `7d8be8e` and `6048593`; F-05/F-06 and shared financial schema. |
| PR #25 | Merged into staging at `53c20ff` after N0TAW00D approved head `420c6bd`; F-03/F-04. CI #59 passed on the PR head (125 server tests / 518 assertions, 11 browser E2E, type checks, Biome, web build and Docker image build). Issue #20 is closed; Issue and PR cards are Done. |
| PR #27 | Docs-only reconciliation merged into staging at `922adfc`; N0TAW00D approved head `13b90a2`, and CI #62 passed. Issue #26 is closed and its Project card is Done. |
| PR #28 | Single release PR from `sprint-1-staging` to `main`; open, CI #64 passed, and no conflict. N0TAW00D's formal approval is pending confirmation of GCP preflight. The merge triggers Lab 5's deploy workflow. |
| PR #24 | Open docs-only D-05 Origin/CSRF proposal. The policy remains deferred; it is separate from PR #25 and is not a PD1 feature blocker. |
| Open Issues / PRs | Issues #2 (team metadata/runtime/authentication) and #17 (Lab 5) remain open. PR #24 is the separate D-05 Origin/CSRF docs proposal; PR #28 is the release PR; PR #29 is a Lab 5 Cloud SQL/secret setup docs PR with CI passed and review requested from Palapluem. Issues #20, #21 and #26 are closed; their completed Project cards are Done. |
| Application source and tests | F-01/F-02, F-03/F-04 and F-05/F-06 are integrated in staging. PR #25's exact-head CI #59 passed; clean-checkout TEST-27 passed on `53c20ff`. Repeat release-level verification on the accepted `main` commit. |
| Decisions | D-01–D-07 were accepted by both students through PR #15 at `98afb3b`. PR #27 reconciled the staging evidence; Issue #26 is complete. |

PD1 is still incomplete: `main` is still the bootstrap commit `a4cced2`, with no accepted Sprint 1 release. PR #28 is the release PR; CI #64 passed and the diff is conflict-free, but formal teammate approval awaits GCP preflight. The 10 GitHub Actions variables and `production` environment are configured. Separate Lab 5 docs PR #29 is open against staging with CI passed and review requested from Palapluem; its author reports Cloud SQL role checks, but they are not independently verified here. Secret Manager, WIF/IAM readiness and live deployment remain unverified. If #29 merges before #28, it advances staging and requires fresh release CI/review; keep it separate from the PD1 release unless the team deliberately chooses to include it. After #28 is accepted, repeat TEST-27 and acceptance checks on the exact `main` SHA, then complete Part F evidence, a dated board screenshot, A–F page ranges and the self-contained PDF. GCP deployment is not a separate PD1 rubric item, but merging #28 triggers the Lab 5 deployment workflow. The reported PD1 cutoff has passed; an extension is not verified.

### Google Docs tabs

The four report links are tabs in one Google Doc:

| Assessment | Tab |
|---|---|
| PD1 | [Project Deliverable 1](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.241qhfcdhce3) |
| Lab 5 | [Lab 5](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.s9umabyrevqi) |
| Lab 6 | [Lab 6](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.uhs47dish96h) |
| PD2 | [Project Deliverable 2](https://docs.google.com/document/d/1LvDrVanne23Pgj6LH7AoiacwpgOu-sGl7Hyr6pycZCo/edit?tab=t.amnwb9uwd0u0) |

**Last content comparison: 10 November.** The Lab 6 tab matched Lab 5 except for its title; the PD2 tab matched PD1 except for its title. Treat both as placeholders until the correct assignment content is built and checked. Never carry over screenshots, results, release IDs or claims unless they apply to the assessed version.

## Deadlines and deadline confirmation

| Assessment | Date in the available handout/schedule | Current status |
|---|---|---|
| PD1 | Original handout: 8 November 2026, 23:59 | Later cutoff reported by Wisit: **15 November 2026, 23:30 Asia/Bangkok**; passed. No extension is verified. |
| Lab 5 | 15 November 2026, 23:59 in the handout | Date has passed; no extension is verified. Do not infer one from the PD1 cutoff. |
| Lab 6 | 22 November 2026, 23:59 in the Lab 6 handout | Identify and schedule the independent UAT partner now. |
| Lab 7 | 29 November 2026, 23:59 in the available master draft | The Lab 7 folder has a preparation guide, not a detailed Lab 7 handout; treat the date as provisional and confirm the final submission instructions when the handout or announcement is available. |
| PD2 | 29 November 2026, 23:59 in the handout | Sprint 2 completion and tested Sprint 3 progress. |
| Final Delivery | 13 December 2026, 23:59 in the handout | Complete integrated release and final verification. |

The reported PD1 cutoff passed on 15 November; no extension is verified. The financial features and PR #27 documentation reconciliation are integrated in `sprint-1-staging` at `922adfc`, but there is no accepted `main` release. PR #28 is open with CI #64 passed. Separate Lab 5 docs PR #29 is open against staging with CI passed and review requested from Palapluem; its Cloud SQL check is author-reported and not independently verified here. GCP deployment evidence has not been verified.

## Team ownership and product workflow

Both students must participate in requirements, design, testing, implementation, AI-agent supervision, review and release. Assign bounded work and rotate implementer/reviewer responsibilities. Equal commit counts are not required. A member must be able to explain the feature and its tests, not just the report section they prepared.

### First joint working session

Use Issues [#1](https://github.com/Palapluem/pocket-ledger/issues/1), [#2](https://github.com/Palapluem/pocket-ledger/issues/2), [#3](https://github.com/Palapluem/pocket-ledger/issues/3), and `docs/decisions.md` on `sprint-1-staging`.

Agree and record the decisions that control Sprint 1 behavior:

- smallest complete domain journey and included/excluded scope;
- stack/runtime and reproducible local setup;
- financial amounts, allocation, balance signs, dates, correction and boundary rules;
- authentication, current-user identity, roles, ownership and Administrator privacy boundary;
- UI/API/data interfaces, stable acceptance criteria and how each criterion will be checked.

Do not silently adopt proposals in `docs/decisions.md`. If a decision cannot be made from the assignment, record the question and ask the instructor/TA.

### Bounded Issues, branches and review

After agreeing the scope, create or take one bounded feature Issue per implementation slice. A possible split to discuss is identity/access and financial transaction/persistence; it is only a proposal until both students approve the boundaries.

For each Issue, record feature/requirement/AC IDs, owner, expected behavior, tests and completion evidence. The owner creates a feature branch from the current `sprint-1-staging`, implements against the versioned contract and opens one PR back to staging. The other student checks the contract, behavior, assertions, diff and actual test results, gives a substantive review and merges after approval. Swap roles on the next Issue.

Board flow: `Backlog → Specified → Started → PR Review → Fixing → Done`. A card reaches Done only when its AC are met. Staging integration is followed by one reviewed release PR to `main`; a Done card is not a release or deployment record. Do not create a PR just to record that another PR merged.

## Project Deliverable 1 — establish and release Sprint 1

**Cutoff:** the student-reported 15 November 2026, 23:30 Asia/Bangkok cutoff has passed; the saved handout says 8 November · **Score:** 80 points (8%). No later extension is verified.

**Official source:** [PD1 handout](Project%20Deliverable%201/project_deliverable_1_v1.pdf), [preparation guide](Project%20Deliverable%201/README.md), [report outline](Project%20Deliverable%201/report-outline.md), and [feature-contract template](Project%20Deliverable%201/feature-contract-template.md).

PD1 covers whole-product planning in Parts A–D and Sprint 1 specification/implementation in Parts E–F. By the checkpoint, release a useful working Sprint 1 increment on `main`. Docker, completed CI/CD and GCP deployment are Lab 5 work, not PD1 requirements.

| Part | Points | Complete this | Canonical product paths |
|---|---:|---|---|
| A. SRS and product scope | 10 | Stakeholder problem, actors, scope/exclusions, stable FR/BR/NFR IDs, measurable NFR targets/checks, assumptions and decisions. | `docs/srs.md`, `docs/decisions.md` |
| B. Feature inventory and traceability | 10 | Map baseline requirements to features/responsibilities, sprint allocation and verification; disclose uncovered requirements and approved changes. | `docs/features.md`, `docs/traceability.md`, `docs/sprints/plan.md` |
| C. System-Level SDS | 15 | Architecture and component roles; data/entities/constraints/ownership; main UI/API conventions; permission matrix; authentication/session/logout; configuration and deployment design. | `docs/system-sds.md` |
| D. Three-sprint plan | 5 | Each sprint's goal, feature IDs, dependencies and completion outcome; all baseline scope allocated. | `docs/sprints/plan.md` |
| E. Sprint 1 contracts | 20 | Every Sprint 1 feature has design, applicable UI/API/data details, validations/permissions, stable AC, STS and DoD before implementation; preserve justified revisions and test-design history. | `docs/sprints/sprint-1/contract.md`, `docs/sprints/sprint-1/tests.md`, feature contract files |
| F. Working increment and verification | 20 | Complete UI→API→database journey and retrieval; real login/logout/current identity; at least two roles; meaningful rule rejection; persistence/access tests; reviewed integration/release and contribution evidence. | Application source/tests/migrations, README, Issues/PRs and release record |

### PD1 build order

1. Resolve the decisions that affect Sprint 1 and update the decision register only after both students agree.
2. Select bounded features from the baseline and finish their contract, AC and STS before writing implementation.
3. Implement one vertical slice at a time. Include domain rules in the backend; do not rely on a hidden UI button for access control.
4. Test normal, invalid/boundary and forbidden-access cases, including persistence through the database. Run build/tests on the candidate release and record actual counts, failures/skips and commit.
5. Merge feature PRs into staging after peer review. Run integration/acceptance checks and merge a peer-reviewed release PR to `main`.
6. Assemble the PD1 PDF from actual evidence. It is self-contained: Parts A–F, page navigation, selected demos, actual build/test output and commit, AC-to-test results, two short test excerpts, meaningful red/green history, two completed Issue/PR samples, both contributions, truthful AI-use and limitations. A link to the repo does not replace the required PDF content.

**PD1 release gate:** the submitted commit on `main` must run the whole documented domain journey and retrieve persisted data. It must include authentication, backend permissions, meaningful business validation and relevant automated tests. Seeded accounts are sufficient; self-registration, password recovery and advanced administration are not required at this checkpoint.

## Lab 5 — make the accepted Sprint 1 release reproducible and deploy it

**Due:** 15 November 2026, 23:59 in the handout; confirm whether the instructor changed it · **Score:** 100 lab points (5%).

**Official sources:** [Lab 5 handout](../labs/Lab05/01_SE_Lab_5_updated.pdf), [Student Guide V1.1](../labs/Lab05/03_Student-Guide-GCP-Deployment-and%20CI%20CD-V1_1.pdf), [deployment template](../labs/Lab05/deployment-template.md), and `../labs/Lab05/toktickit-lab5-starter/` as a reference only.

Start the assessed deployment from the accepted PD1 Sprint 1 release. Keep the same product, repository, GCP project and pipeline for later labs. Do not copy TokTickIT application source into PocketLedger.

### Where the work runs — keep these stages distinct

“CI/CD on GCP” does **not** mean that development, every test, the CI runner and the application must all run on a GCP virtual machine. The handouts separate local development, pull-request checks and deployment:

| Stage | Where it runs | What the requirement means |
|---|---|---|
| PD1 development and verification | On the team's computers | Build and test the Sprint 1 candidate locally; record the results against its release commit. PD1 explicitly says completed Docker, CI/CD and GCP deployment are Lab 5 work. |
| Docker readiness | Docker on a developer machine or another suitable build environment | Keep the Docker files in the product repo and prove a clean-clone build. The Student Guide recommends running the container locally before cloud deployment; it does not require a development VM. |
| CI for pull requests | A GitHub Actions runner, or an equivalent CI service | Run the required build and automated tests for relevant PRs. The required check must block a failing merge. GitHub Actions is the guide's reference; the runner does not have to be a VM in GCP. |
| CD and live application | The deployment workflow sends the accepted release to GCP; the app runs on the selected GCP service | After the reviewed release reaches `main`, deploy it repeatably and identify the running commit. The recommended stack uses Cloud Run for the app, Cloud SQL for PostgreSQL for persistent data, Artifact Registry for images, Secret Manager for runtime secrets and GitHub Actions for CI/CD. |
| Initial cloud setup | GCP Console or the documented setup commands (the guide's first-deploy example uses Cloud Shell) | Create and configure the actual GCP resources safely. Track manual setup changes in Issues and record the real project, region and resource names. |

The handout requires the outcomes above, not Compute Engine or a GCP-hosted runner. Cloud Build, a self-hosted runner and a VM are possible alternatives only if the team chooses and documents them; they are not extra requirements. Follow the Lab 5 handout if a guide or starter-kit detail conflicts with it.

**Current PocketLedger checkpoint (16 November 2026):** `main` remains at bootstrap `a4cced2`; `sprint-1-staging` is at `922adfc`. PR #18 merged at `8cefcaf`, PR #19 at `a77d324`, PR #22 at `7d8be8e`, PR #23 at `6048593`, PR #25 at `53c20ff`, and docs-only PR #27 at `922adfc`. CI #59 passed on #25 head `420c6bd`; CI #62 passed on #27 head `13b90a2`; release PR #28 CI #64 passed on exact staging head `922adfc`. Issue #26 is closed and its board card is Done; PR #28 is on the board in PR Review. PR #24 remains open as a separate docs-only D-05 proposal; Origin/CSRF remains deferred. PR #28 is open pending formal teammate approval after GCP preflight. Separate Lab 5 docs PR #29 is open against staging with CI passed and review requested from Palapluem; its author reports Cloud SQL role checks, not independently verified here. If #29 merges first, #28's head and CI must be rechecked. The GitHub Actions variables and protected `production` environment are configured; Secret Manager, WIF/IAM readiness and live deployment remain unverified. The merged Lab 5 pipeline is not proof of a GCP deployment; verify actual deployment/revision evidence separately.

| Requirements | Work and evidence |
|---|---|
| R-01–R-02 | Docker clean-clone build/run; all settings from environment; `.env.example` documents placeholders; no secret in Git, image, logs, screenshots or PDF. |
| R-03–R-04 | Public GCP URL works through UI/API/database; durable data survives both application restart and redeploy. |
| R-05–R-06 | Relevant PRs run meaningful build/tests; a required check blocks a failing merge; show a temporary failing PR and leave it unmerged. |
| R-07–R-08 | Reviewed change goes through CI and `main`, then deploys repeatably; identify the commit/tag and running revision; document the release procedure. |
| R-09–R-12 | Issues/board, feature/fix branch, reviewed staging PR and reviewed release PR; `lab5` labels; preserved history; both students' contributions; public repository and no committed secrets. |

Record the required checks against their tested versions: **C-01** passing normal PR CI; **C-02** failing temporary PR blocked; **C-03** clean-clone build/run; **C-04** public live workflow; **C-05** data after restart and redeploy; **C-06** reviewed staging-to-main release, deployment and served revision matching its commit.

Product repo paths: `Dockerfile`, `.dockerignore`, `.env.example`, `.github/workflows/`, and `docs/labs/lab-05/deployment.md`. `deployment.md` must describe the real stack, every environment variable and its source, commands, GCP project/region/resources, and repeatable release steps. Submit one concise evidence-index PDF to LEB2, named `lab5_sec<section>_<group name>.pdf`, using Answer Parts 0–4. Link to artifacts/runs and add screenshots only where a link cannot establish a fact. The failing proof PR must not be merged.

Set an alerts-only budget before creating GCP resources. Never commit a password, key or connection string. Do not pay prepayment or click Upgrade in the prescribed Free Trial flow. Review billing, IAM and database changes with the student/TA; an agent must not make those changes on its own.

## Lab 6 — cross-team UAT and defect management

**Due:** 22 November 2026, 23:59 · **Score:** 100 lab points (5%).

**Official source:** [Lab 6 UAT handout](../labs/Lab06/Lab_6_Sprint_1_UAT.pdf), [preparation guide](../labs/Lab06/README.md), and [report outline](../labs/Lab06/report-outline.md).

Each two-person team performs both roles. As **Product Team**, prepare executable Sprint 1 cases, safe test accounts, a deployed release/version and instructions, review received findings, fix release-blocking defects and provide corrected releases. As **UAT Team**, independently execute another team's cases, record actual outcomes/findings, retest fixes and make the independent acceptance decision. The project partner Natthawat is not an external UAT team; find another project team and schedule sessions now. If unavailable, contact the TA promptly and retain the notice.

| Lab 6 part | Points | Required work |
|---|---:|---|
| A. UAT preparation and handoff | 20 | Executable Sprint 1 cases tied to requirements/AC; tested scope/version, setup, safe accounts and partner instructions. |
| B. Independent execution | 25 | Execute the other team's cases; record tester, date, release, input, expected and actual result, PASS/FAIL/BLOCKED and selected evidence. |
| C. Defect reporting and triage | 20 | Record every real finding; link reproduction, impact/severity and requirement; classify received findings with rationale and owner/status. |
| D. Resolution and independent retest | 35 | Fix/retest release-blocking defects through regression test, reviewed PR/CI/deploy and independent partner retest; state the final acceptance decision and version. |

Prepare at least four cases: normal finance journey with explicit expected balances; rule/boundary rejection with no partial state change; forbidden ownership/role access including cross-user records and Administrator denial of financial records; and state/history/persistence. Four is a minimum, not a complete coverage target. Add cases for the implemented Sprint 1 AC. Use synthetic data; send credentials privately and never include them in the report.

If no legitimate defect occurs, do not invent one or break the assessed release. Ask the TA for an isolated controlled exercise. Only the independent UAT Team can accept the tested Sprint 1 release. The one-team PDF must include the assigned cases, actual execution, all finding dispositions, red/green correction evidence where applicable, review/CI/deployment, independent retest, contributions and limitations.

Product path: `docs/labs/lab-06/uat.md` is a preparation draft; its execution/results are not complete until actually performed. Course report path: `labs/Lab06/`. The Lab 6 Google Docs tab was still a copy of Lab 5 in the 10 November comparison, so rebuild that tab from the Lab 6 handout before preparing its PDF.

## Lab 7 — provisional preparation for maintenance and metrics

**Provisional timing:** 29 November 2026, 23:59 in the available master document, which is marked draft for instructor review. The Lab 7 folder has no detailed Lab 7 handout yet; the preparation guide is based on Group Work Specification §10 and must be reconciled with the detailed handout or instructor announcement when it arrives. Do not treat the draft guide as a substitute for that handout. **Provisional rubric:** 100 points (5%) in the available master: impact analysis and updated contract (25), implementation and regression-safe delivery (50), objective engineering metrics (15), and readiness/retrospective (10).

**Sources:** [Lab 7 preparation guide](../labs/Lab07/README.md) and [report outline](../labs/Lab07/report-outline.md).

Lab 7 is a controlled change to a behavior the team has already implemented. It is not a shortcut for finishing a missing baseline feature. Before implementation, obtain instructor/TA approval for the proposed old-to-new behavior and record its impact on requirements, features, SDS, AC, tests, data/migrations, compatibility and other workflows.

| Step | Work | Evidence to retain |
|---|---|---|
| 1. Select and approve | Choose one implemented behavior/business rule; record old behavior, proposed change, reason, scope and approval. | Approved change request and immutable starting version. |
| 2. Analyse impact | Trace affected requirement, feature, architecture/data, permissions, interfaces, AC and regression scope. | Reviewed impact analysis and updated contract. |
| 3. Test first | Add a behavior test that fails because the requested behavior is absent, not because setup is broken. | RED output tied to the defective/start version. |
| 4. Implement and regress | Implement the approved change; keep prior behavior working where it is still required. | GREEN output, relevant regression results and code review. |
| 5. Release | Integrate through the required reviewed branch/PR workflow and deploy if the handout requires it. | CI, release commit and deployed version, if applicable. |
| 6. Measure and reflect | Report the five required metrics with time window, timestamp and source; interpret them in no more than 100 words; complete readiness checks and the short retrospective. | Reproducible metric sources, readiness record and retrospective. |

Do not fabricate a defect or claim an unapproved change. Preserve the old rule and its history. The current guide lists the metric sources as Issue close dates, merged PRs, passing test output, UAT defect records and CI runs; use one consistent measurement window and explain what each number means.

## Project Deliverable 2 — complete Sprint 2 and show tested Sprint 3 progress

**Due:** 29 November 2026, 23:59 · **Score:** 70 points (7%).

**Official sources:** [PD2 handout](Project%20Deliverable%202/project_deliverable_2_v1.pdf), [preparation guide](Project%20Deliverable%202/README.md), and [report outline](Project%20Deliverable%202/report-outline.md).

PD2 is a distinct project checkpoint, not a renamed PD1 report. It uses the same PocketLedger repository and approved baseline changes. By the checkpoint:

- all planned Sprint 2 features are complete, reviewed, integrated and verified against contracts;
- every remaining baseline feature has a Sprint 3 contract, and at least one meaningful Sprint 3 workflow/rule is implemented and tested;
- `main` contains a coherent candidate with Sprint 1, Sprint 2 and implemented Sprint 3 work, deployed through the Lab 5 pipeline;
- original authentication, backend authorization and ownership still work; and
- a dated plan lists exact remaining features/AC, defects, owners, dependencies, next actions and targets through 13 December.

| Part | Points | What the PD2 PDF must contain |
|---|---:|---|
| A. Sprint 1 continuity and change status | 5 | Identify the accepted Sprint 1 release; demonstrate its critical journey on the candidate; track approved baseline changes and relevant Lab 5–7 deployment/UAT/maintenance findings, affected IDs, disposition, fix version and retest. |
| B. Sprint 2 contracts and working increment | 25 | Every Sprint 2 feature contract with linked requirements, feature design, UI/API/data, validations/permissions, AC, STS and DoD; complete feature status table; actual workflows/tests; reviewed integration/release. All planned Sprint 2 features must be complete. |
| C. Sprint 3 contracts and working progress | 15 | Contracts/AC/STS for all remaining Sprint 3 features; at least one meaningful implemented and tested workflow/rule; precise remaining-work table with owner/dependency/action/date. |
| D. Updated requirements and test traceability | 10 | Complete current SRS, feature inventory and System-Level SDS; requirement → feature/responsibility → sprint → AC/NFR target → planned test → actual file/test/measurement → result/version; show gaps and approved changes. |
| E. Integrated release candidate | 15 | Candidate on `main` and GCP; Sprint 1 continuity plus selected Sprint 2/Sprint 3 behavior; rule rejection, persisted retrieval and access evidence; actual build/test/CI/deploy output; two test excerpts, red/green evidence, two Issue/PR chains, setup and finish plan. |

Keep the full required engineering documents and selected evidence inside one self-contained PDF; repository links do not replace them. Identify the immutable submitted commit, deployed URL/version and internal page references. Keep test counts and behavior tied to that candidate. Do not move an unfinished planned Sprint 2 feature into Sprint 3 without an approved scope revision.

Product paths: update `docs/srs.md`, `docs/features.md`, `docs/traceability.md`, `docs/system-sds.md`, `docs/sprints/plan.md`, and all Sprint 2/3 contracts and tests through reviewed product work. Use `docs/assessment-plan.md` and `docs/releases.md` to keep the evidence and release history connected. The PD2 Google Docs tab matched PD1 except for its title in the 10 November comparison; rebuild it as a distinct A–E report.

**Dependency:** findings and retest status from Lab 5, Lab 6 and Lab 7 feed PD2 Part A. Only record a real finding, approved disposition, tested fix and version. Do not claim Lab 6 acceptance before an external UAT team has independently tested the recorded release.

## Final Delivery — finish and verify the complete product

**Due:** 13 December 2026, 23:59 · **100 points (10%).**

**Official sources:** [Final Delivery handout](Final%20Delivery/project_final_delivery_v1.pdf), [preparation guide](Final%20Delivery/README.md), and [report outline](Final%20Delivery/report-outline.md).

The final checkpoint requires the complete approved scope across three sprints on a final `main` release, deployed on GCP at the same version. Re-run final regression and relevant independent UAT/retests, verify workflows, calculations, error handling, persistence, authentication and backend access, and account for every requirement/feature with final test/result/version. Submit one self-contained PDF with Parts A–E, plus the actual product demonstration video. The Final handout states 10 minutes in §2 and 4 minutes in §3.5; ask the instructor which limit controls before recording.

## Source folders and files

### Course repository

| Path | Use |
|---|---|
| `project/Project Deliverable 1/` | PD1 handout, preparation guide, contract template and A–F report outline. |
| `labs/Lab05/` | Lab 5 handout, Student Guide V1.1, deployment template, report outline and reference Starter Kit. |
| `labs/Lab06/` | Lab 6 UAT handout, preparation guide and report outline. |
| `labs/Lab07/` | Lab 7 preparation guide and report outline; check for a detailed handout/announcement before relying on final submission requirements. |
| `project/Project Deliverable 2/` | PD2 handout, preparation guide and A–E report outline. |
| `project/Final Delivery/` | Final handout, preparation guide and report outline. |
| `project/group_work_specs_v1.pdf` | Master product/theme requirements; use the assessment handout for that assessment's submission instructions. |
| `project/pocketledger-team-work-plan.md` | This operational sequence, current status snapshot and team workflow for PD1, Labs 5–7, PD2 and Final Delivery. |

### PocketLedger product repository

Application source and canonical engineering documents belong only in [Palapluem/pocket-ledger](https://github.com/Palapluem/pocket-ledger), a separate Git root ignored by the course repository. Read its `AGENTS.md`, `CONTRIBUTING.md` and `COORDINATION.md` before changing product files.

| Product-repository path | Use |
|---|---|
| `docs/decisions.md` | One record of decisions, with proposals kept separate from agreed rules. |
| `docs/srs.md` | Whole-product scope and FR/BR/NFR. |
| `docs/features.md`, `docs/traceability.md` | Feature inventory and requirement verification map. |
| `docs/system-sds.md` | Architecture, data, UI/API, role/access, auth and deployment design. |
| `docs/sprints/plan.md` | Three-sprint allocation and outcomes. |
| `docs/sprints/sprint-1/contract.md`, `docs/sprints/sprint-1/tests.md` | Current Sprint 1 contract, AC, STS and DoD baseline. |
| `docs/labs/lab-05/deployment.md` | Lab 5 configuration/deployment record; fill with actual commands/resources/results. |
| `docs/labs/lab-06/uat.md` | Lab 6 UAT preparation; execution fields are not results until tested. |
| `docs/labs/lab-07/change-and-metrics.md` | Lab 7 preparation; follow its actual handout and approval gate. |
| `docs/assessment-plan.md`, `docs/releases.md` | Assessment traceability and immutable release history. |

### Repository workflow and safety

Keep course files and product source in their own Git roots. Never force-add or copy PocketLedger source into the CPE334 course repo. Product workflow: Issue → branch from current `sprint-1-staging` → contract/tests/implementation → substantive peer-reviewed PR to staging → integration checks → one peer-reviewed release PR to `main` → deploy when Lab 5 is active. The author does not approve their own PR; preserve pushed history; do not create a PR just to record a previous merge.

Both repositories are public coursework. Never publish credentials, tokens, real account data or production secrets. Record actual evidence and version; mark unrun work as NOT RUN/BLOCKED rather than PASS. Keep report prose in the established style and export reports through Print only after the assessed content is ready.

## Immediate actions for both students

1. Ask the instructor/TA about late-submission handling; the student-reported PD1 cutoff has passed and no extension is verified.
2. PR #27 and Issue #26 are complete; do not open another PD1 documentation PR. Release PR #28 is open, CI #64 passed, and N0TAW00D's formal approval awaits GCP preflight.
3. PR #29 is a separate Lab 5 docs PR, open against staging with CI passed and review requested from Palapluem. Review it separately; merging it before #28 moves the release head and requires fresh CI/review. Keep it out of the PD1 release unless both students choose to include it.
4. Confirm the GCP-owned resources/secrets and WIF/IAM preflight with the project owner; the repo's 10 Actions variables and `production` approval environment are configured. PR #29's Cloud SQL role results are author-reported pending review. Only the owner can verify remaining cloud state; merging #28 triggers deployment, so do not merge until deployment readiness is confirmed.
5. After the teammate approves and merges #28, rerun TEST-27 and required acceptance checks on the exact `main` release, then capture final Part F and dated board evidence, fill A–F page ranges and complete the self-contained PDF.
6. Record Lab 5's deployment, URL, running revision and persistence separately; do not infer a live deployment from merged PR #19 or the release PR alone.
7. Identify and schedule the independent Lab 6 UAT partner; prepare cases now, but do not claim acceptance before an external team tests the recorded deployed release.
8. Keep PD2 and provisional Lab 7 planning tied to the same Sprint 2/Sprint 3 baseline; confirm Lab 7 requirements when its detailed handout arrives.
