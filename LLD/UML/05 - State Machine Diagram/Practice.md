# State Machine Diagram - Practice

## Key Concepts
- **One object, many states** — states + `event [guard] / action` transitions + initial `●` / final `◉`
- **Guards make illegal moves unrepresentable** — transition table beats scattered ifs
- **States as enum, not booleans** — `isPaid + isShipped + isCancelled` explodes combinatorially

## Common Triggers in Interviews
| Trigger | Response |
|---------|----------|
| "status" / "lifecycle" / "cancel" / "expire" | state machine for that object |
| states × events getting unreviewable | draw states + guard every transition |
| "can X happen from state Y?" | answer from the diagram, then encode as a transition table |

---

## Exercises (self-study)

> UML has no AlgoMaster exercise — the state machine is how you tame stateful objects. Work these on paper, whiteboard, or Mermaid.

- [ ] **Order lifecycle** — EMPTY → PENDING → PAID → DISPATCHED plus CANCELLED with `place / pay [amount > 0] / cancel / ship` and initial + final
- [ ] **Guard the cancel** — cancel is legal from PENDING only: show the guard and name what happens from DISPATCHED (rejected)
- [ ] **Elevator drill** — IDLE / MOVING / DOORS_OPEN with `call, arrive, open, close, timeout` events and guards
- [ ] **Mermaid drill** — reproduce the order `stateDiagram-v2` from Concept.md without looking

---

## Extra Practice

- [ ] Replace a boolean-flag cluster (`isPaid, isShipped, isCancelled`) with one enum + transition table
- [ ] For any stateful Medium-problem object, list all illegal transitions explicitly

## Tips
- **One diagram per stateful object** — not per system
- Say *"illegal transitions are impossible to express"* — that sentence sells the transition table
- Self-transitions (event, same state) are legal modelling — don't force a new state
