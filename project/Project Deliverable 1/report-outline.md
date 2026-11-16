# Project Deliverable 1 — Report map and verification record

This file indexes the self-contained PDF; it is not a substitute for the report or an LMS receipt.

- **PDF:** [CPE334_PD1_PocketLedger.pdf](CPE334_PD1_PocketLedger.pdf)
- **Source:** Project Deliverable 1 tab in the shared Google Doc
- **Print export:** 17 November 2026, 01:34 (+07)
- **Pages:** 58 A4
- **SHA-256:** `3e2d11638c5d920b67219b065aee9875a555de290cc54b7f887fc663ecb7300b`
- **Accepted product release:** `main` at `bbf7c4a168b6b3585c4e973bb78faf7f233fd11b`

## Rubric and page map

| Part | Points | Contents | PDF pages |
|---|---:|---|---:|
| A | 10 | Whole-product SRS, scope, functional/business/non-functional requirements and decisions | 3–13 |
| B | 10 | Feature inventory, dependencies and requirement-to-feature-to-sprint traceability | 14–23 |
| C | 15 | System-Level SDS: architecture, data, UI/API, roles, authentication and delivery design | 24–29 |
| D | 5 | Goals, dependencies and completion outcomes for all three sprints | 30–33 |
| E | 20 | Sprint 1 feature contracts, acceptance criteria, STS and DoD | 34–45 |
| F | 20 | Working increment, reproduction, demonstrations, verification, review and contributions | 46–58 |

## Part F evidence locations

| Evidence | PDF pages |
|---|---:|
| Release/test summary and demonstration matrix | 46–48 |
| Application screenshots, Figures F.1–F.5 | 49–53 |
| Build, test counts, exact tested versions and AC-to-test results | 54–55 |
| Red/green evidence, selected test excerpts, reviews, board status, contributions, AI-use statement and limitations | 56–58 |

## Version and result notes

The accepted release is `main` at `bbf7c4a168b6b3585c4e973bb78faf7f233fd11b`; its tree matches reviewed PR #28’s tested head `922adfc70a26a7c8371628a64c168e17805210bf`. Main CI run [43911059795](https://github.com/Palapluem/pocket-ledger/actions/runs/43911059795) passed 125 PostgreSQL-backed server tests, 11 browser E2E tests, type checks, Biome, web build and production-image build. Manual TEST-27 remains attributed to `53c20ff`.

The report does not claim a live GCP deployment. Deploy run [43911059895](https://github.com/Palapluem/pocket-ledger/actions/runs/43911059895) is waiting at the `production` gate: N0TAW00D triggered the run and is its only configured reviewer, while self-review is disabled. Another authorized reviewer or a team-approved environment-rule change is needed for Lab 5. Repository secrets are not set; the workflow uses OIDC and GCP Secret Manager, whose secret state and IAM access remain unverified.

The PDF has 58 A4 pages, a complete A–F navigation table, and no blank final page. It was visually checked at the cover, navigation, Part F demonstrations and final page. The repository does not establish whether the PDF was uploaded to the LMS or whether an extension was granted.
