# Project Deliverable 1 — PocketLedger

**Assessment:** Engineering baseline and working Sprint 1 · 80 points (8%)
**Handout deadline:** 8 November 2026, 23:59. Any later extension is not verified here.

## Submission file

The final report was exported from the Project Deliverable 1 Google Docs tab using Print on 17 November 2026 at 01:34 (+07).

- **PDF:** [CPE334_PD1_PocketLedger.pdf](CPE334_PD1_PocketLedger.pdf)
- **Format:** 58 A4 pages
- **SHA-256:** `3e2d11638c5d920b67219b065aee9875a555de290cc54b7f887fc663ecb7300b`
- **LMS status:** The file is prepared; an upload receipt was not checked.

The PDF is self-contained and follows the handout’s six-part order. The page ranges below are from the saved PDF.

| Part | Content | PDF pages |
|---|---|---:|
| A / 10 | SRS, scope and decisions | 3–13 |
| B / 10 | Feature inventory and traceability | 14–23 |
| C / 15 | System-Level SDS | 24–29 |
| D / 5 | Three-sprint plan | 30–33 |
| E / 20 | Sprint 1 contracts, acceptance criteria and STS | 34–45 |
| F / 20 | Working Sprint 1 and verification | 46–58 |

Part F contains the working journey and role-denial captures (Figures F.1–F.5, pp. 49–53), accepted-main test/build evidence, selected test excerpts, TDD evidence, peer-reviewed integration, contribution records, AI-use disclosure and known limits.

## Accepted product release

- **Product:** PocketLedger — Personal Money and Expense Logging System
- **Team:** 2-Nor — Wisit Suwannao (67070501042) and Natthawat Primsirikunawut (67070501027)
- **Repository:** [Palapluem/pocket-ledger](https://github.com/Palapluem/pocket-ledger)
- **Accepted `main`:** `bbf7c4a168b6b3585c4e973bb78faf7f233fd11b`
- **Release PR:** #28, reviewed and merged by N0TAW00D
- **Main CI:** run [43911059795](https://github.com/Palapluem/pocket-ledger/actions/runs/43911059795) passed on the accepted commit: 125 PostgreSQL-backed server tests, 11 browser E2E tests, type checks, Biome, web build and production-image build.
- **Manual TEST-27:** passed on `53c20ff`; the report keeps that result tied to its actual tested commit.

## Deployment status — separate Lab 5 work

The handout places Docker, completed CI/CD and GCP deployment in Lab 5, so PD1 does not claim a live deployment.

Deploy run [43911059895](https://github.com/Palapluem/pocket-ledger/actions/runs/43911059895) is **waiting** at the `production` approval gate. N0TAW00D triggered the run and is the only configured reviewer; self-review is disabled, so that reviewer cannot approve this run. The job has not started. A different authorized reviewer or a team-approved environment-rule change is needed for Lab 5; do not bypass the gate for PD1.

All ten GitHub Actions repository variables referenced by the workflow are set. No repository Actions secrets are configured, which is expected: the workflow uses GitHub OIDC rather than a service-account key, then reads runtime values from GCP Secret Manager. The required GCP secret versions and IAM access were not verified. Do not add made-up values or bypass the environment approval.

PR #29 is separate Lab 5 documentation. PR #24 is a separate D-05 policy proposal. Neither is required for the PD1 report.

## Next action

Upload the PDF to the course submission site if that has not already been done, and retain the receipt. The report file is ready; an LMS submission or late-submission extension is not verified by this repository record.
