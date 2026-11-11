# Lab 6: Cross-team UAT and defect management

**Due:** 22 November 2026, 23:59 · **100 lab points (5%)**

**Product:** PocketLedger · **Team:** Wisit Suwannao and Natthawat Primsirikunawut

Use the actual [Lab 6 UAT handout](Lab_6_Sprint_1_UAT.pdf) as the authority. This guide and the [report outline](report-outline.md) help organise the work; neither substitutes for the handout.

## Assessment goal

Test another team's deployed Sprint 1 release independently, provide executable UAT cases for PocketLedger, classify every real finding, resolve release-blocking defects, and obtain an evidence-based independent acceptance decision. Lab 6 assesses the delivered Sprint 1 scope, not unfinished Sprint 2 or Sprint 3 features.

Both teams have two roles. As **Product Team**, prepare and hand off PocketLedger's cases and test access, assess findings, fix accepted defects, and provide corrected releases. As **UAT Team**, execute the partner team's cases, report reproducible findings, independently retest fixes, and decide whether the tested Sprint 1 release is acceptable. Wisit and Natthawat are one product team; one cannot substitute for an external UAT partner.

| Part | Points | Required outcome |
|---|---:|---|
| A. UAT preparation and handoff | 20 | Another team can execute the Sprint 1 cases against the identified scope/version using the written instructions and safe accounts. |
| B. Independent execution | 25 | Record actual outcomes for the partner's UAT cases, with testers, tested release and supporting evidence. |
| C. Defect reporting and triage | 20 | Report reproducible findings and give every received finding a reasoned classification, severity, owner and disposition. |
| D. Resolution and independent retest | 35 | Correct release-blocking defects through the reviewed release process and obtain a partner retest/acceptance decision for the identified version. |

## Work in order

1. **Agree on the partner team and dates.** Schedule initial UAT, finding review and retest early. If the team is unavailable or its app cannot be accessed, notify the instructor/TA promptly and retain the notice. Do not replace independent UAT with your own developer testing.
2. **Prepare cases for PocketLedger.** Include at least four executable cases, each with a stable ID, linked Sprint 1 requirement/AC, role, purpose, preconditions, synthetic input, numbered steps and specific expected results. Four is a minimum; cover important implemented AC as well.
3. **Hand off a precise version and safe test access.** Record Sprint 1 tag/commit, deployed revision and URL, accepted scope, roles/account labels, data setup/reset and cleanup. Send credentials privately; never place secrets in the PDF or public repo.
4. **Test the partner product independently.** Record actual results separately from expected results, with tester, date/time, input, tested version and PASS/FAIL/BLOCKED. BLOCKED is not PASS. Show that rejected actions did not disclose or partially change protected state.
5. **Triage findings against the contract.** Classify each as accepted defect, duplicate, not-defect or enhancement, with a reason, severity, owner and status. Reproduce and clarify a failure before dismissing it; do not label a failed requirement as an enhancement.
6. **Fix and retest accepted blocking defects.** Add a meaningful regression test and show RED against the defective version, fix to GREEN, run related regression checks, obtain substantive peer review, pass CI, release and deploy. Give the independent UAT team the corrected release and original reproduction steps for retest.
7. **Record one final decision.** State Accepted, Accepted with documented minor limitations, or Not Accepted, with the exact tested version, independent tester, date and rationale. Only the independent UAT team can confirm acceptance.

### Minimum PocketLedger case categories

- Normal finance journey with expected money movement and balances calculated from the approved Sprint 1 contract.
- Business-rule or boundary rejection; verify that no partial transaction/allocation/balance change remains.
- Forbidden access, including User B attempting to read User A's records and an Administrator being denied financial records/summaries.
- State/history/persistence behavior in the implemented Sprint 1 scope.

Use synthetic accounts and data. Derive amounts and expected values from the approved contract; do not invent values or record planned outcomes as test results.

## If UAT finds no legitimate defect

A sound release is not penalised for having no natural defect. Complete the partner UAT and obtain its acceptance decision. Ask the instructor/TA for a controlled exercise on an isolated version/branch to demonstrate defect correction. Keep that exercise separate from the accepted release. Do not fabricate a finding, substitute a feature request, or deliberately break the live release.

## What the team submits

Submit one self-contained PDF per team through LEB2 by the deadline. The PDF contains Parts A–D, page navigation, identity/theme/repository, Sprint 1 scope and exact tested/deployed version. Embed the relevant cases, results, findings/dispositions, test excerpts and execution evidence; external links alone do not replace the assessed material.

| Report part | Include |
|---|---|
| A | PocketLedger UAT cases/handoff and the partner team's identity, release, actual case execution, tester/date and selected evidence. |
| B | Outgoing defect reports, all findings received and each triage/disposition, including accepted minor limitations or “none” where true. |
| C | Correction/retest evidence for release-blocking defects or approved controlled exercise, red/green results, review/CI/redeployment and the independent Sprint 1 decision. |
| D | PocketLedger's own accepted-defect chain, with regression excerpt/results, relevant diff, reviewed release/deployed fix and independent partner retest/closure. |

Keep full application source out of the PDF. Include contributions, truthful AI-use and limitations; identify tested versions for every claim. Use [`report-outline.md`](report-outline.md) to assemble the PDF and reconcile page references after printing.

## Record locations

- Course handout: `labs/Lab06/Lab_6_Sprint_1_UAT.pdf`
- Course report outline: `labs/Lab06/report-outline.md`
- Product preparation record: [`docs/labs/lab-06/uat.md`](https://github.com/Palapluem/pocket-ledger/blob/sprint-1-staging/docs/labs/lab-06/uat.md)
- Product defect Issues, regression tests, reviewed PRs, CI and release records: `Palapluem/pocket-ledger`
- Private credentials/raw evidence: use a private course handoff or `_private/pocket-ledger/` when needed; do not commit secrets.

Carry relevant UAT findings, accepted changes and independent retests into PD2 Part A and Final verification. An old PASS does not establish that a later release remains correct.
