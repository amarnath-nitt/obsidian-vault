# State Pattern - Practice

## Key Concepts
- **Context** — holds the current state, delegates behaviour
- **State** — interface of behaviour per state
- **ConcreteState** — behaviour + transition logic
- **Transition** — moving the context to a new state
- **Illegal transition** — throw or ignore, per requirement
- **Stateless states** — safe to share/reuse

## Common State Use Cases
1. **Order lifecycle** — New / Paid / Shipped / Delivered / Cancelled
2. **Vending machine** — Idle / HasMoney / Dispensing / OutOfStock
3. **ATM** — Idle / HasCard / Authenticated / Dispensing
4. **Traffic light** — Red / Green / Yellow
5. **Media player** — Playing / Paused / Stopped
6. **Document workflow** — Draft / Moderation / Published
7. **Elevator** — Idle / Moving / DoorOpen

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design a Traffic Light](solutions/Design-State-Traffic-Light.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-state-traffic-light)

### Medium
- [ ] [Design an ATM Machine](solutions/Design-ATM-Machine.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-atm-machine)
- [ ] [Design an Order Processor](solutions/Design-Order-Processor-State.md) — AlgoMaster · medium (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Media player states (playing/paused/stopped) — [reference code](solutions/State-Implementations.md)
- [ ] Order lifecycle (pay/ship/deliver/cancel) — [reference code](solutions/State-Implementations.md)
- [ ] Table-driven state machine — [reference code](solutions/State-Implementations.md)

---

## Tips
- Expose **intent methods** (`pay()`, `ship()`), not a `setState("PAID")`.
- Put **transition logic inside the state**, not in the context.
- Keep states **stateless** so they can be shared/singletons.
- Never leave the context pointing at a state that can't handle a legal event.