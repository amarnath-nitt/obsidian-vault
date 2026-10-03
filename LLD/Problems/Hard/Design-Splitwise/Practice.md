# Design Splitwise - Practice

## Key Concepts
- **Balances are net deltas** — payer gets +amount, every participant gets −share; the map always sums to zero
- **Split strategies must reconcile** — equal/exact/percent all end with `Σ splits == amount`, or they throw
- **Settle-up is a graph reduction** — greedy match the biggest debtor with the biggest creditor until clean

## Common Moves in LLD
1. **Integer money** — rupees/paise as `long`; never floating point for balances
2. **Validate at the boundary** — the split rule owns its own check (sums to total, percents to 100)
3. **Rounding remainder has an owner** — equal splits give the first member the odd paisa; percent gives it to the last
4. **Settle-up result is presentation** — balances stay; the transfer list is recomputed on demand

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Splitwise](solutions/Design-Splitwise.md) — Hard · Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add multi-payer expenses — several users front parts of one bill
- [ ] Add "simplify" toggling — minimal transfers vs direct who-paid-whom history
- [ ] Add currency — balances per currency, settle-up never crosses currencies

## Tips
- Say **"the balances map sums to zero — that invariant is the whole model"**
- Reconcile one equal split with ₹100 / 3 people out loud — remainder handling is the checkpoint
- Greedy settle-up is not provably minimal in general — say so; interviewers respect the caveat

---

#lld #machine-coding #splitwise #hard #practice