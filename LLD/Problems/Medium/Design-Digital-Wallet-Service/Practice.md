# Design a Digital Wallet Service - Practice

## Key Concepts
- **Double-entry ledger** — every transfer writes a −amount and +amount entry sharing one reference; the ledger is the truth
- **One transfer boundary** — validate → debit → credit → record happens atomically; failures leave nothing half-way
- **Idempotency keys** — the same request id applies once; retries are free

## Common Moves in LLD
1. **Guarded debit** — `Wallet.debit` itself refuses when frozen or short; callers cannot bypass the rules
2. **Fee before debit** — the source pays amount + fee; the destination receives amount
3. **Lock ordering** — when sharding, lock wallets in id order to avoid deadlock between A→B and B→A
4. **Freeze as a state** — rejected uniformly by the wallet, not by every call site

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design a Digital Wallet Service](solutions/Design-Digital-Wallet-Service.md) — Medium · State, Command, Strategy

---

## Extra Practice (self-study)

- [ ] Add a statement query — ledger entries for a wallet in time order
- [ ] Add a daily transfer limit — policy checked before the debit
- [ ] Add a compensating reversal — a refund writes an opposite pair, never edits history

## Tips
- Say **"the ledger is append-only; balances are just the fastest projection"** — it is the sharpest answer you can give
- Retries with the same key must not move money twice — show the check *before* the debit
- Walk one failed transfer end-to-end: where does compensation happen? Nowhere — it never started

---

#lld #machine-coding #wallet #medium #practice