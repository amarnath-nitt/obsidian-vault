# Mediator Pattern - Practice

## Key Concepts
- **Mediator** — central coordination point
- **Colleague** — participant that talks only to the mediator
- **Star topology** — O(n) links instead of O(n²)
- **Encapsulated interaction** — the *how they interact* lives in the mediator
- **Decoupling** — colleagues don't know each other

## Common Mediator Use Cases
1. **Chat room** — users ↔ room mediator
2. **Air traffic control** — planes ↔ tower
3. **UI dialog** — widgets coordinate through the dialog
4. **Smart home hub** — devices ↔ hub
5. **Event bus / message broker** — services ↔ bus
6. **Stock exchange matching engine**

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Chat Room](solutions/Design-Chat-Room.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-chat-room)

### Hard
- [ ] [Design a Turn-Based Game Lobby](solutions/Design-Turn-Based-Game-Lobby.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Air traffic control (planes ↔ tower) — [reference code](solutions/Mediator-Implementations.md)
- [ ] UI dialog coordination (widgets via dialog) — [reference code](solutions/Mediator-Implementations.md)
- [ ] Event bus as mediator (topic-based) — [reference code](solutions/Mediator-Implementations.md)

---

## Tips
- Keep the mediator **focused** — if it grows huge, split it by domain
- Colleagues hold **one** reference (the mediator), never peers
- Say it in interviews: "Mediator = coordinate peers; Facade = simplify an API; Observer = broadcast changes"
- An **event bus** is the modern, decoupled mediator