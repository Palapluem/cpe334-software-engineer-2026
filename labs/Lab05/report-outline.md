# Lab 5: Cloud Deployment and CI/CD Pipeline on GCP

> Evidence-index template. Fill blank cells with actual verified evidence; do not mark a planned check as passing. Keep the exact Answer Part 0–4 order. The final PDF filename is `lab5_sec<section>_<group name>.pdf`, using the confirmed section and team name.

## Answer Part 0: Team and Evidence Index

| Field | Actual submission value |
| --- | --- |
| Team name / number / section | |
| Topic and product name | PocketLedger · Personal Money and Expense Logging System |
| Student | Wisit Suwannao · 67070501042 · Palapluem |
| Student | Natthawat Primsirikunawut · 67070501027 · N0TAW00D |
| Public product repository | https://github.com/Palapluem/pocket-ledger |
| Submitted immutable tag / full commit | |
| Public URL and served commit | |

| Student | Requirements / tests / supervision | Implementation / deployment | Specific reviews | Issue / PR evidence |
| --- | --- | --- | --- | --- |
| Wisit Suwannao | | | | |
| Natthawat Primsirikunawut | | | | |

| Rubric part | Artifact / direct link | Check / requirement / version | Actual verification result |
| --- | --- | --- | --- |
| 1. CI and Quality Gate | | C-01 / C-02; R-05 / R-06 | |
| 2. Docker and Reproducible Configuration | | C-03; R-01 / R-02 | |
| 3. GCP Deployment and Persistence | | C-04 / C-05; R-03 / R-04 | |
| 4. Repeatable Release Pipeline | | C-06; R-07–R-10 | |

Use direct links and one or two sentences explaining each artifact. Identify public visibility and participation evidence for R-11/R-12 as well.

## Answer Part 1: CI and Quality Gate

Link the actual CI workflow and a normal passing PR/run. State the executed suites and build results with counts and tested version. Show that integration and release PRs run the relevant checks.

Link the required-check configuration and the temporary failing PR. Include a readable capture showing the required failed check and blocked merge. State that the proof PR was not merged and the released application remained functional.

| Check | PR / run / configuration | Tested commit | Result |
| --- | --- | --- | --- |
| C-01 | | | |
| C-02 | | | |

## Answer Part 2: Docker and Reproducible Configuration

Link Dockerfile, `.dockerignore`, applicable compose configuration, `.env.example` and the environment table in `docs/labs/lab-05/deployment.md`. Include clean-clone commands/output and the observed working container with its database (C-03). State the stack and relevant deviations from the reference.

## Answer Part 3: GCP Deployment and Persistence

Provide the public URL, GCP service/database evidence and the live domain journey through UI/API/database (C-04). Demonstrate a rule rejection or access restriction with synthetic data; keep the URL visible in the relevant captures.

For C-05, show the same record and relevant values before restart, after actual application restart and after redeploy. Identify each event and its release/revision. Do not substitute two similar screenshots without documenting the events.

| Event | Source commit / revision | Synthetic record identifier | Observed persisted result | Evidence |
| --- | --- | --- | --- | --- |
| Before restart | | | | |
| After restart | | | | |
| After redeploy | | | | |

## Answer Part 4: Repeatable Release Pipeline

Trace one labelled change from Issue → feature PR into staging → specific teammate review → integration → reviewed release PR into main → CI/deploy run → running revision. Link the repeatable release procedure and identify the source commit/image/running version (C-06).

| Issue / feature PR | Review / staging integration | Release PR / main commit | Pipeline | Image / running revision | Observed live change |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Assembly checks before producing the final PDF

- Every rubric part has direct evidence and an actual result; unexecuted or failed checks remain explicit.
- Use screenshots only where a link does not establish the claim, such as a blocked merge, console setting or persistence before/after.
- Each numbered caption identifies the check/requirement and source commit/run/URL. Crop at complete field/row/section boundaries; keep IDs and text readable at 100%.
- Keep only one current evidence sequence per topic. Remove stale captures, repeated source-file dumps, editor notes and placeholder guidance from the final report.
- Use Sarabun prose, Consolas commands/code, justified paragraphs and the student's established blue italic captions. Keep tables/code aligned for readability, with clear boxes for command output.
- Check that no credential, connection string, key or token appears in any image/log/text. Keep the public service available through grading.
- Print/export only when the release and report content are verified and the student authorizes the output; inspect the actual printed page count, images and final page before submission.
