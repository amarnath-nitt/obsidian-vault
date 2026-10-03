# Design ATM - Practice

## Key Concepts
- **Screens are states** — Idle/CardInserted/Authenticated/OutOfService; illegal moves rejected by the state
- **Transactions are a chain** — validate → authorize → execute; withdraw/deposit/balance plug in as handlers
- **Two ledgers move together** — account balance + cassette cash commit atomically

## Common Moves in LLD
1. **PIN tries bounded** — 3 failures retain the card and eject to Idle
2. **Withdraw checks both** — account balance AND cassette denominations before dispensing
3. **Dispense is greedy** — largest notes first; fail loudly if exact mix impossible
4. **Out-of-service as a state** — rejects card ops uniformly; refill allowed only there/Idle

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design ATM](solutions/Design-ATM.md) — Medium · State, Chain of Responsibility, Singleton

---

## Extra Practice (self-study)

- [ ] Add mini-statement — last 5 ledger entries per account
- [ ] Add PIN change — old-PIN verify + new-PIN policy, one handler
- [ ] Add inter-bank fee — a decorator on the withdraw handler

## Tips
- Say **"two ledgers, one commit"** — balance and cassette never diverge
- PIN flow first (retain on 3rd failure), then withdraw — interviewers check both
- Draw the 4-state screen flow before coding — it is the whole design

---

#lld #machine-coding #atm #medium #practice
