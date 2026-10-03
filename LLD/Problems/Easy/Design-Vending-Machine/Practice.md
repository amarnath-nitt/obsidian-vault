# Design a Vending Machine - Practice

## Key Concepts
- **States own the transitions** — Idle/Selection/Payment/Dispense/OutOfService, each rejecting illegal moves
- **Two ledgers** — inventory (stock) and cash box (money in, change out) updated together
- **Cancel refunds** — every paid-but-undispensed coin returns on cancel

## Common Moves in LLD
1. **Context delegates everything** — `VendingMachine` holds state; states hold the rules
2. **Guard select** — in stock AND affordable, else stay with a reason
3. **Change from the cash box** — dispense fails loudly if exact change impossible
4. **Out-of-service as a state** — not a boolean; it rejects all money operations uniformly

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design a Vending Machine](solutions/Design-Vending-Machine.md) — Easy · State, Singleton

---

## Extra Practice (self-study)

- [ ] Add card payment — a `CardPaymentState` reusing the same interface
- [ ] Add exact-change-only mode — `select` rejected when the box can't make change
- [ ] Add operator refill + cash collection — refill allowed only in Idle/OutOfService

## Tips
- Say **"illegal moves are impossible to express"** — states reject, no scattered ifs
- Cancel path first (refund), then the happy path — interviewers check the refund
- Draw the 5-state machine before coding — it is the whole design

---

#lld #machine-coding #vending-machine #easy #practice
