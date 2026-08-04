# CPE334 Course Workspace — Lab 1 Alignment Context

Outer workspace repo for CPE334 Software Engineering. Hosts private course materials, planning/grill artifacts, and the nested graded product repo `labs/toktickit_cpe334/` (independent Git repository, tracked separately — see repository-boundary rules in `TokTickIT_Lab1_Master_Prompt.md`, which is itself excluded from both repos).

## Language

**Vertical slice**:
A thin feature that runs through every layer (React UI → Express API → Prisma → PostgreSQL) to prove the whole stack works together. Lab 1's entire deliverable is one vertical slice: Check System → health + categories.
_Avoid_: MVP, prototype (those imply broader scope than a single proven path).

**Engineering contract**:
The specification plus the evidence (tests, acceptance criteria, Definition of Done) required to prove an Issue is complete. Distinct from a bare specification, which only describes behavior.

**lab1-staging**:
The Lab 1 integration branch. All four feature branches are created from it and merge back into it via PR; it merges into `main` once via a single release PR after all four are Done.
_Avoid_: dev, develop, staging (use the exact literal branch name).

**Individual Sprint**:
Lab 1 is completed independently per student — each student owns a separate `toktickit_cpe334` repository. Peer review is cross-repository (Collaborator access both ways), not a shared team repo with both partners committing to the same branches.
