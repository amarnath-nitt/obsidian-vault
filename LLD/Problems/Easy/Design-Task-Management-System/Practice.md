# Design a Task Management System - Practice

## Key Concepts
- **Composite work items** — `Task` and `TaskList` share `progress()`; nesting is free
- **Status is a linear flow** — TODO → IN_PROGRESS → DONE (+ BLOCKED); moves validated
- **Events fan out to observers** — assign/move/comment/overdue → notify, audit, remind

## Common Moves in LLD
1. **Roll-up progress** — list progress = mean of children; recursion does the work
2. **Filter as Strategy** — one interface, many predicates; combine with AND
3. **Watchers + assignee notified** — task owns its subscriber set
4. **Overdue as derived query** — due date + status, never a stored flag

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design a Task Management System](solutions/Design-Task-Management-System.md) — Easy · Composite, Observer

---

## Extra Practice (self-study)

- [ ] Add subtasks (nest tasks inside tasks) — Composite already allows it
- [ ] Add due-date reminders — a scheduled observer over overdue query
- [ ] Add activity log — an observer appending every event

## Tips
- Say **"lists roll up, tasks report"** — the Composite sentence
- Status moves validated in one method — no teleporting TODO → DONE past BLOCKED rules you set
- Filters compose — show an AND of assignee + overdue

---

#lld #machine-coding #task-management #easy #practice
