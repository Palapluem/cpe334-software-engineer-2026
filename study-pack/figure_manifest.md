# Figure manifest — final 91-page reading book and mock

## Vector figures

| Figure | Where used | What it clarifies |
|---|---|---|
| DormFix WBS tree | Study Chapter 6 | Project → milestones → each task once; separates hierarchy from dates. |
| DormFix Gantt | Study visual atlas; scaled answer version in mock | Working days, dependencies, approval buffers, weekends and milestones. |
| Security boundary path | Study visual atlas | Untrusted browser input, server checks, private storage and authorized read. |
| POS decline-to-cash sequence | Study visual atlas and mock solution | Provider decline, customer decision, cash path and successful sale evidence. |
| Hotel payment activity | Study visual atlas and mock solution | Separate denied/cancel path from accepted-payment booking path. |
| Ticket Use Case, State and UI | Study visual atlas and mock solutions | Human goals, lifecycle transitions and read-only/editable fields. |
| KU Registration sequence, activity, UI, Use Case and State | Study worked case and mock solutions | Source-led registration flow; uncertain payment states are marked as assumptions. |
| KU Class diagram | Study worked case | Class relationships and source multiplicities with caveats. |
| Git graphs | Study Git reference and mock | `HEAD`, local refs, remote-tracking refs, ancestry and merge effects. |
| Grades State | Mock solution | Separate submission states from registration state. |

All current redraws are editable TikZ. Labels are placed with clearance from boxes, arrows and boundaries; arrows are routed around node text. The WBS in the notes is an actual parent–child diagram, not a text-only list.

## Raster source crops

Three small crops from Kaching SDS pages 5, 8 and 11 are retained inside the Kaching example because those pages are themselves source artifacts. The compiled book does not include the 25-page low-resolution L4 slide screenshot appendix. Its old editable source file is excluded from the delivery source bundle.

## Visual QA

The rendered PDF was inspected at full page size for the WBS tree, Gantt, requirement traceability tables, security boundary, POS sequence, KU diagrams, mock answer canvases and answer diagrams. See `qa_checklist.md` for page-level checks.
