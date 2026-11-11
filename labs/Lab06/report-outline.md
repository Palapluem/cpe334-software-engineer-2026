# CPE334 Lab 6: Independent UAT and defect management

> Assembly outline based on the actual [Lab 6 handout](Lab_6_Sprint_1_UAT.pdf). Submit one self-contained PDF per team through LEB2 by **22 November 2026 at 23:59**. The PDF must identify the tested Sprint 1 version and the independent UAT decision. Blank execution fields are unverified.

## Team and version information

| Field | Actual value |
|---|---|
| LEB2 group / section | 2-Nor / [confirm section] |
| Product / assigned theme | PocketLedger / Theme 7: Personal Money and Expense Logging System |
| Product Team | Wisit Suwannao · 67070501042 · Palapluem; Natthawat Primsirikunawut · 67070501027 · N0TAW00D |
| Product repository | https://github.com/Palapluem/pocket-ledger |
| Sprint 1 scope and accepted release tag/full SHA | [actual scope and immutable SHA] |
| PocketLedger public URL / served revision | [actual URL and deployed revision] |
| Independent UAT partner team and testers | [actual team and student names] |
| Partner product / tested Sprint 1 version / URL | [actual product, release and URL] |
| UAT, triage and retest dates | [actual dates and times] |
| Private access handoff reference | [reference only; never include credentials] |

## PDF navigation

| Part | Actual PDF pages | Case/finding/evidence IDs |
|---|---|---|
| A. Cases and independent execution | | |
| B. Findings and triage | | |
| C. Resolution and acceptance | | |
| D. PocketLedger correction chain | | |

## Part A — UAT preparation, handoff and independent execution

### A1. PocketLedger cases handed to the partner team

Include executable cases covering implemented Sprint 1 acceptance criteria. At least four are required; add cases for important criteria not covered by the minimum categories. Use synthetic data and derive expected values from the approved product contract.

| UAT ID / linked requirement and AC | User role / purpose | Preconditions and synthetic inputs | Numbered actions | Specific expected result |
|---|---|---|---|---|
| | | | | |

The minimum categories are: a normal finance journey with calculated expected balances; a business-rule/boundary rejection with no partial state change; forbidden access including cross-user records and Administrator denial of financial data; and a state/history/persistence case.

Document the accepted scope, tested release, deployed revision/URL, roles and account labels, setup/reset/cleanup, case order and private credential handoff. Never print credentials, tokens or production secrets.

### A2. Results from testing the partner team's product

These results belong to PocketLedger's team as the independent UAT Team. Do not copy expected results into the actual-result column.

| Partner UAT ID | Tester / date and time | Tested release / URL | Input and actual result | PASS / FAIL / BLOCKED | Evidence / finding ID |
|---|---|---|---|---|---|
| | | | | | |

For each failure, show the expected result, actual result, reproduction details and whether protected data/state was exposed or changed. BLOCKED is not PASS. Include selected readable evidence with case ID, action and tested version.

## Part B — Findings, reports and triage

List outgoing reports to the partner team and **every finding received** about PocketLedger, including “none” if none occurred. Distinguish behavior defects against the Sprint 1 contract from duplicate reports, not-defects and enhancement requests.

| Finding / linked UAT ID and requirement | Reporter / tested version | Preconditions and reproduction | Expected vs actual / impact | Severity | Triage decision and contract-based reason | Owner / status |
|---|---|---|---|---|---|---|
| | | | | | | |

Reproduce and clarify a finding before dismissing it. Critical and major accepted defects block Sprint 1 acceptance. Fix minor defects or obtain explicit independent UAT acceptance as a documented limitation. Do not relabel a failing requirement as an enhancement.

## Part C — Resolution, independent retest and acceptance

For every accepted release-blocking defect, identify the regression test, defective version, fix, review/CI, corrected deployment and independent retest. If no natural defect occurred, identify the TA-approved controlled exercise and its isolated version; do not fabricate a finding or break the accepted release.

| Finding / AC | Regression test and RED result/version | Fix PR / review / CI | Corrected release and deployed version | Partner tester / date | Retest actual result / evidence | Closed or reopened |
|---|---|---|---|---|---|---|
| | | | | | | |

### Final independent Sprint 1 decision

| Decision field | Actual value |
|---|---|
| Decision | Accepted / Accepted with documented minor limitations / Not Accepted |
| Independent UAT team and decision-maker | |
| Exact tested release/deployed revision | |
| Decision date | |
| Reasons, conditions and unresolved blockers | |

Only the independent UAT Team makes this decision. Do not record Accepted while critical/major defects remain unresolved or required tests are blocked.

## Part D — PocketLedger's own defect-correction chain

Include the accepted defect chain for PocketLedger: linked Issue and requirement/AC; meaningful test that fails against the defective version; fix diff; the same test passing; relevant regression results; teammate review; CI; staging integration; reviewed release to `main`; deployed version; independent partner retest and closure. If no legitimate defect occurred, include only an instructor/TA-approved isolated exercise and identify it as such.

| Issue / requirement / AC | Defective release | RED test and actual output | Fix commit/PR and review | GREEN/regression output | Deployed fix version | Independent retest and closure |
|---|---|---|---|---|---|---|
| | | | | | | |

## Contributions, limitations and evidence references

| Student | Product Team work / Issues / PRs | Independent UAT work / cases | Other verified contribution |
|---|---|---|---|
| Wisit Suwannao | | | |
| Natthawat Primsirikunawut | | | |

Include a brief truthful AI-use declaration, known limitations, partner/access delays and remaining actions. Link evidence to its case/finding and release version. Embed the necessary UAT cases, finding records, selected output, test excerpts, review text and acceptance record in this PDF; external links alone do not replace the assessed material. Do not include the whole application source or unchanged SRS.

## Final assembly checks

- [ ] Both teams and their roles are identified; PocketLedger's team tested the partner app and prepared PocketLedger for independent testing.
- [ ] Cases are executable, linked to Sprint 1 requirement/AC and include safe setup and expected results.
- [ ] Actual results identify tester, date, input and exact tested release; BLOCKED items are not reported as PASS.
- [ ] Every received finding has a justified disposition; accepted blocking fixes have regression RED/GREEN and independent retest evidence.
- [ ] The final acceptance decision names the independent UAT team and exact deployed version.
- [ ] PDF Parts A–D, page navigation, contributions, limitations and evidence IDs are complete and readable.
- [ ] No password, token, private user data or production secret is included.
