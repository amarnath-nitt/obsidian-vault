# Sequence Diagram - Practice

## Key Concepts
- **Lifelines + time** — participants across the top, time runs down; initiator left, dependencies right
- **Sync call `──▶` + dashed return `╌╌▶`** — every call that waits needs its reply drawn
- **`alt` / `loop` / `opt` fragments** — branches, repetition, and optional messages

## Common Triggers in Interviews
| Trigger | Response |
|---------|----------|
| "show the flow" / "walk through" | pick **one** key workflow, draw its sequence |
| "what happens when…" / "order of calls" | lifelines + ordered messages, top to bottom |
| branching / retry logic in the flow | `alt` / `loop` fragment with a label |

---

## Exercises (self-study)

> UML has no AlgoMaster exercise — the sequence diagram is how you *defend* a workflow in interviews and reviews. Work these by hand (or Mermaid).

- [ ] **Order the calls** — draw placeOrder → pay → confirm for Client / OrderService / PaymentService with returns
- [ ] **Add the branch** — extend a login flow with an `alt` fragment (valid → token, invalid → 401)
- [ ] **Add the loop** — draw a retry loop (`loop` fragment) around a payment call with max 3 attempts
- [ ] **Mermaid drill** — reproduce the placeOrder Mermaid diagram from Concept.md without looking

---

## Extra Practice

- [ ] Take any Medium problem and draw the sequence for its single most complex workflow
- [ ] Review a diagram and check: every sync call has a return, every fragment has a label

## Tips
- **One diagram per workflow** — modelling every method buries the flow
- Say *"who calls whom, in what order"* — that sentence is the whole diagram
- Returns are not optional — a missing dashed arrow hides half the design
