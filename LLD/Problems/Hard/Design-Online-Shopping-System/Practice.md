# Design Online Shopping System like Amazon - Practice

## Key Concepts
- **Available = on-hand − reserved** — the reservation gap is what makes concurrent checkout safe
- **Checkout reserves; payment commits** — two moments, two inventory operations, one story
- **Cancels restore what they took** — release (CREATED) or restock (PAID); SHIPPED is too late

## Common Moves in LLD
1. **All-or-nothing reserve** — check every line, then reserve every line; partial reservations never exist
2. **Guarded transitions** — `advance()` follows the state graph; skipping SHIPPED is impossible
3. **Discounts over subtotal** — pure function of cart lines; coupons/percent/flat compose as strategies
4. **Restock observer** — "back in stock" alerts are a side effect of inventory changes, not a separate scanner

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Online Shopping System like Amazon](solutions/Design-Online-Shopping-System.md) — Hard · State, Strategy, Observer

---

## Extra Practice (self-study)

- [ ] Add cart expiry — reservations time out, releasing stock (reuse the TTL pattern)
- [ ] Add split shipments — one order, several packages, per-line states
- [ ] Add returns — DELIVERED → RETURNED with restock and refund policy

## Tips
- Say **"reserved is the word that makes concurrency work"** — one word, whole answer
- Walk cancel from both CREATED and PAID — they restore differently
- Discount strategies are the warm-up question; have Percent and Flat ready

---

#lld #machine-coding #amazon #hard #practice