# Chain of Responsibility Pattern - Practice

## Key Concepts
- **Handler** — `handle()` + a `next` link
- **ConcreteHandler** — handles or forwards
- **Chain** — built by the client, head to tail
- **Decoupling** — sender doesn't know the receiver
- **Terminal handler** — the default that always handles
- **Pure vs impure** — one handler vs middleware chain

## Common Chain Use Cases
1. **Logging levels** — DEBUG → INFO → WARN → ERROR
2. **Approval workflow** — Manager → Director → CEO
3. **Middleware** — auth → rate limit → validation → handler
4. **ATM cash dispensing** — 2000 → 500 → 100 notes
5. **Support ticket escalation**
6. **Servlet filters / interceptors**

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Logging Framework](solutions/Design-Logging-Framework.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-logging-framework)
- [ ] [Design an Expense Approval Chain](solutions/Design-Expense-Approval-Chain.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-expense-approval-chain)

### Hard
- [ ] [Design a Support Ticket Router](solutions/Design-Support-Ticket-Router.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] ATM cash dispensing (2000 → 500 → 100 notes) — [reference code](solutions/Chain-of-Responsibility-Implementations.md)
- [ ] Middleware pipeline (auth/rate-limit/validation) — [reference code](solutions/Chain-of-Responsibility-Implementations.md)
- [ ] Configurable chain order — [reference code](solutions/Chain-of-Responsibility-Implementations.md)

---

## Tips
- Always add a **terminal/default handler** so requests are never silently dropped
- **Link the chain in the client**, not inside the handlers
- Say it in interviews: "CoR = one handler (may stop); Decorator = every wrapper adds"
- Keep chains **short** and order them intentionally (security first, logging last)