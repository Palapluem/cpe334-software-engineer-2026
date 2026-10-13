# Writing and diagram guide for the CPE334 study pack

## Story from lecture to practice

The notes follow the engineering work in the order a student uses it:

1. Start with a user need and project context.
2. Turn the need into precise requirements and acceptance evidence.
3. Design system behavior and select a diagram that answers a specific question.
4. apply security and ownership rules at the trusted boundary.
5. plan the work with scope, owners, dependencies and dates.
6. deliver a small increment, test it and review evidence.

Each main lecture chapter introduces its concepts once. A later example should add a new artifact, decision or verification step. If it adds none, link back to the first explanation instead of repeating it.

## Language and source labels

- Write short Thai sentences and keep standard engineering terms in English where the course uses them.
- Define a term once in the glossary, then use it consistently.
- Prefer a concrete question over an abstract description: “What must be true for the fourth registration?” is easier to verify than “enforce the limit correctly.”
- Label course facts, the instructor's exam blueprint, applied examples, explanation and assumptions separately.
- Keep unknown values visible. A blank performance threshold, missing RACI assignment or unspecified payment response must not become a claimed course rule.
- A proposed test is not evidence that the software has already passed it.

## Example pattern

A useful worked example follows this sequence:

| Stage | What to show |
|---|---|
| Input | The exact fact or short scenario from the source. |
| Interpretation | Which actor, object, rule, quality or boundary it implies. |
| Artifact | The requirement, diagram, schedule, test or issue that follows. |
| Check | A positive, negative or boundary case that could verify it. |
| Open point | Any missing fact or assumption that must be confirmed. |

Examples may refer back to earlier definitions. Repeat the question and answer only when the second version is deliberate exam practice.

## Diagram rules

### UML and flow diagrams

- Give every diagram one purpose: message order, branching workflow, object lifecycle, actor goals or data structure.
- Match the boxes and arrows to the source behavior. Label guards and outcomes on the path they describe.
- Put text inside its node with enough padding. Keep connector labels out of nodes and arrowheads.
- Route lines through whitespace. Do not run a line through another node or label.
- Show a final outcome only when the scenario supports it; distinguish a proposed assumption from a source-defined state.

### WBS and Gantt

- Draw WBS as a tree: project → milestone or deliverable → task. Place each task once and keep every connector outside node text.
- WBS communicates hierarchy; it does not itself give dates or dependency.
- Gantt communicates working dates, duration, dependency, buffer and milestones. Keep weekends and buffers visually distinct, and explain why a buffer exists.
- Reuse task IDs across WBS, RACI and Gantt so readers can trace the same scope.

### UI wireframes

- Show source of value, editability, requiredness, validation and state.
- Make read-only fields visually distinct from editable inputs. Explain any required-field marker that is a design assumption.
- Leave enough space between controls and labels; do not rely on color alone to signal meaning.

### Git diagrams

- Draw commit ancestry separately from branch pointers.
- Label `HEAD`, local branches and `origin/*` independently. A branch switch moves `HEAD`; it does not update a remote-tracking ref.
- Put commands in the order that changes the graph and state any assumptions about the working tree.

## PDF layout checks

- Use vector drawings for precise diagrams; preserve source image crops only when the crop itself is useful evidence.
- Keep tables within page margins, give columns enough width for the longest label and move long prose below a table when needed.
- Render the final PDF, inspect full-size pages with high-risk diagrams and answer areas, and check that no node, line, label or page edge clips the content.
- Check exported fonts, page count, extracted text and unresolved references after the final build.
