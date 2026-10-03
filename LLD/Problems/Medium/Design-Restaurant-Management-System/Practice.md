# Design Restaurant Management System - Practice

## Key Concepts
- **Two machines** — table status (FREE/OCCUPIED) and order state (PLACED…PAID) advance at different moments
- **Snapshot prices** — order lines copy the menu price; menu edits never rewrite history
- **Kitchen is an Observer** — the floor places orders; the kitchen just hears about them

## Common Moves in LLD
1. **`advance()` validates the transition** — switch on current state, throw on skips
2. **One open order per table** — placing checks the table has none; paying frees the table
3. **Bill is a fold** — subtotal from lines; tax/tip are pure functions layered on top
4. **Observer list, not a kitchen reference** — print-kitchen today, KDS tomorrow, same interface

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Restaurant Management System](solutions/Design-Restaurant-Management-System.md) — Medium · State, Observer, Strategy

---

## Extra Practice (self-study)

- [ ] Add per-item prep time — READY when the slowest line completes
- [ ] Add table reservation — a time-slot ledger like Hotel
- [ ] Add split bills — divide lines across payers, one payment record each

## Tips
- Say **"orders and tables are different state machines"** — it is the classic trip-up here
- Snapshot the price — "menu changed mid-dinner" is a favourite follow-up
- Pay is the only transition that frees the table; keep it that way

---

#lld #machine-coding #restaurant #medium #practice