# Command Pattern - Practice

## Key Concepts
- **Command** — the request, as an object (`execute` / `undo`)
- **ConcreteCommand** — binds a Receiver + parameters
- **Invoker** — triggers commands (button, queue, scheduler)
- **Receiver** — performs the real work
- **Client** — builds and wires commands
- **Macro command** — composite of commands

## Common Command Use Cases
1. **Remote control** — on/off/undo per device
2. **Text editor** — undo/redo typing and formatting
3. **Job/task queue** — enqueue then execute later
4. **Drawing app** — undoable shape operations
5. **Transaction log** — record and replay requests
6. **Job scheduler** — cron-like tasks

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design an Undoable Counter](solutions/Design-Undoable-Counter.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-undoable-counter)

### Medium
- [ ] [Design a Database Transaction](solutions/Design-Database-Transaction.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-database-transaction)

### Hard
- [ ] [Design an Order Fulfillment Saga](solutions/Design-Order-Fulfillment-Saga.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Remote control with undo (light on/off) — [reference code](solutions/Command-Implementations.md)
- [ ] Macro command (execute/undo a batch) — [reference code](solutions/Command-Implementations.md)
- [ ] Thread-safe command queue with workers — [reference code](solutions/Command-Implementations.md)

---

## Tips
- The **Invoker knows only `Command`** — never the Receiver
- Store **just enough state** in the command to `undo()` correctly
- **Cap the undo history** (or use a bounded deque)
- Say it in interviews: "Command = a request as an object → enables undo, queue, log"