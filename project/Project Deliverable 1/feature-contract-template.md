# Feature engineering contract

> Working template. Copy one contract per bounded feature into the team product repository and replace the guidance with agreed content before implementation. Blank results are unverified, not passing. Do not copy this preparation template into the submission as a completed contract.

## Identity and history

Start with a clear DRAFT / REVIEWED / ACCEPTED status. Link any unresolved decision IDs and list which behavior is blocked by them. A prepared document does not establish team agreement, test execution or implementation completion.

| Field | Agreed value |
| --- | --- |
| Feature ID and name | |
| Sprint and scope | |
| Linked FR / BR / NFR | |
| Dependencies | |
| Issue and branch | |
| Implementation owner / teammate reviewer | |
| Contract version and review date | |
| Contract commit before implementation | |

| Revision | Reason and changed behavior | Impact on AC / STS / data / compatibility | Version |
| --- | --- | --- | --- |
| | | | |

## Feature-Level SDS

State the user goal, actors, preconditions, normal workflow, postconditions and persisted result. Specify validation, domain rules, boundary/failure cases and permitted records for each role. State explicit exclusions and unresolved decisions.

For a money-changing feature, define the affected account types, amount/date rules, balance effects, allocation compatibility, atomicity and the expected result of a rejected request. Use the agreed financial vocabulary; distinguish user accounts from financial accounts.

## UI specification, where applicable

| Screen / action | Role and ownership | Inputs and validation | Loading / empty / failure / success | Navigation and persisted result |
| --- | --- | --- | --- | --- |
| | | | | |

Include relevant layouts/diagrams and field behavior. If this feature has no UI change, state that and identify the interface that demonstrates it.

## API specification, where applicable

| Method and path | Authentication / permission | Request | Success response | Validation / access / failure response |
| --- | --- | --- | --- | --- |
| | | | | |

Specify the actual request/response shapes, precedence of relevant checks, safe errors and record ownership. Do not invent endpoints or reuse TokTickIT error rules without an explicit design decision.

## Data specification, where applicable

| Entity / field | Meaning and type | Ownership / relationship | Constraint | Migration / seed effect |
| --- | --- | --- | --- | --- |
| | | | | |

Describe transaction boundaries, reads after writes, rollback on failure and safe setup/seed behavior. State when this feature needs no schema change.

## Acceptance criteria

| AC ID | Preconditions / role | Action | Observable expected outcome | Linked requirement |
| --- | --- | --- | --- | --- |
| | | | | |

Include the relevant normal, invalid/boundary, unauthenticated, forbidden-role and cross-owner outcomes. Keep IDs stable when the wording evolves.

## Software Test Specification

| TEST ID | AC IDs | Level and public interface | Preconditions / input | Action | Expected result | Planned file / test name |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

Map every Sprint 1 AC. Use important logic tests, real API/database integration tests and selected UI/end-to-end journeys. Agree the public interfaces before writing executable tests. Check retrieved behavior rather than private helper calls, and use independent expected values.

## Red / green and verification record

| Behavior / test | Red version and command | Observed intended failure | Green version and command | Actual result / output |
| --- | --- | --- | --- | --- |
| | | | | |

| AC | TEST ID | Actual file / test name | Command or CI run | Tested commit | Result, including failures/skips |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Label manual checks separately. Leave execution cells empty until the check has actually run.

## Definition of Done and release evidence

- Required behavior and backend rules are implemented; the agreed AC/STS has meaningful passing evidence.
- Setup, migrations, seed and required configuration are reproducible without real secrets in Git.
- The teammate inspected behavior, assertions and diff and recorded a specific review.
- Sprint integration/system checks pass and the accepted release is recorded by immutable SHA/tag.
- Documents, actual test paths, remaining work and failed/skipped results are current.

| Issue / PR | Contract-before-code evidence | Review and resolution | Staging integration | Main release |
| --- | --- | --- | --- | --- |
| | | | | |

## Known gaps and decisions still required

| Gap / decision | Affected requirement or AC | Owner | Resolution / status |
| --- | --- | --- | --- |
| | | | |
