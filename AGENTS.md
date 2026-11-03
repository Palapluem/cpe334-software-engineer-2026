# CPE334 workspace rules

## Repository boundaries

This directory is the course-material repository:
`/Users/wisitsuwannao/Documents/Workspace/cpe334-software-engineer-2026`

Two independent product repositories may live inside the workspace:

- `labs/toktickit_cpe334/`: completed individual Labs 1–4.
- `project/pocket-ledger/`: the PocketLedger team product for Deliverables 1–2, Labs 5–7 and Final Delivery.

Both paths are ignored by the course repository. They are not submodules. Never force-add either path, its `.git` directory, a gitlink, or copied application source to the course repository.

Before staging, committing or pushing, run `git -C <intended-root> rev-parse --show-toplevel`, `git -C <intended-root> remote -v` and `git -C <intended-root> status --short --branch`. Use the explicit root for subsequent Git commands.

## What belongs where

- Course repository: supplied lecture/assessment PDFs, study notes, preparation guides, report templates and the final submitted reports.
- PocketLedger: authoritative product requirements/design/contracts, application code, tests, migrations, configuration, workflows and release/test records.
- Local-only evidence and scratch work: `_private/pocket-ledger/` in this course workspace. Create dated/versioned evidence folders only when needed; do not publish credentials, raw database exports or temporary renders.
- Keep the supplied Lab 5 starter kit as reference in `labs/Lab05/toktickit-lab5-starter/`; adapt selected files in the product repository rather than modifying the reference or copying the old TokTickIT application.

## Updates and review

Course-material updates may be committed together when they form one coherent change. Stage explicit paths and inspect the staged diff. Do not create product PRs for course-report-only changes.

For PocketLedger, read its own `AGENTS.md` and `CONTRIBUTING.md`. After the initial documentation-only repository bootstrap, changes go through an Issue, a feature/fix/docs branch, teammate review into sprint staging, integration checks and a reviewed release PR to `main`. The reviewer merges. Keep related docs with their feature and do not open a follow-up PR just to record the previous merge SHA.

Do not rewrite pushed history. Do not add AI-credit lines, AI authors or `Co-Authored-By` trailers to commits, PRs, Issues or comments. Required assessment AI-use declarations must remain brief and truthful; they are tool-use records, not contributor credits.

## Evidence and unfinished work

Read the actual handout before claiming an assessment requirement. The Lab 6/7 folders may exist before their detailed handouts arrive; label preparation based on the master specification accordingly.

Use professional English for product/report prose and Thai for discussion with the student. Never invent test counts, release SHAs, reviewers, cloud resources, approvals, UAT findings or completion status. Leave unexecuted results explicitly unverified.

Respect the student's report style: Sarabun prose, Consolas commands/code, justified paragraphs and consistent blue italic captions. The handout controls completeness: project PDFs are self-contained; Lab 5 uses a concise evidence index. Print final reports only when authorized and inspect the actual output.
