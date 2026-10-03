# Activity Diagram - Practice

## Key Concepts
- **Control flow, not call order** — steps + decisions + fork/join; sequence diagrams handle who-calls-whom
- **Decision diamonds need guards** — every outgoing arrow labelled `[condition]`
- **Fork needs its join; swimlanes need owners** — parallel paths merge back; every step has an actor

## Common Triggers in Interviews
| Trigger | Response |
|---------|----------|
| "workflow" / "approval process" / "steps" | activity diagram with start `●` → steps → end `◉` |
| branching-heavy logic | decision diamonds with guards, not nested sequence fragments |
| parallel paths ("while also…") | fork/join bars + swimlanes per owner |

---

## Exercises (self-study)

> UML has no AlgoMaster exercise — the activity diagram is your branching-logic tool. Work these on paper, whiteboard, or Mermaid.

- [ ] **Guard the diamond** — draw Validate → `valid?` → Pay / Reject with `[valid]` / `[invalid]` guards plus start and end
- [ ] **Fork and join** — after payment, Receipt-by-email and Update-ledger run in parallel then join: draw the bars
- [ ] **Add swimlanes** — split Park → Pay → Validate → Open-barrier into Driver vs System lanes
- [ ] **Mermaid drill** — reproduce the Validate / valid? / Pay / Reject flowchart from Concept.md without looking

---

## Extra Practice

- [ ] Take a workflow with 3+ branches from any Medium problem and model it as an activity before coding
- [ ] Review rule: sequence for call order, activity for control flow, state machine for lifecycle — classify three flows

## Tips
- **One diagram per process** — modelling the whole system buries the logic
- Say *"guards on every arrow out of the diamond"* — unlabelled branches hide decisions
- Swimlanes turn a flowchart into a design: who does what
