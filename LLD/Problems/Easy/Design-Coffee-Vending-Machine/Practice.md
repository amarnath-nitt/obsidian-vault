# Design Coffee Vending Machine - Practice

## Key Concepts
- **Recipes are factory products** — code → ingredient map + price; new drink = one registration
- **Ingredients checked before money moves** — availability gates payment, not the reverse
- **Atomic brew** — all ingredients deducted together or the sale is refused

## Common Moves in LLD
1. **Factory owns recipes** — brewer asks for a recipe, never news one up
2. **Containers are bounded ledgers** — `take` fails loudly below zero; `low()` warns early
3. **State reuses the vending skeleton** — Idle/Selection/Payment/Brewing/Dispense
4. **Refill is operator-only** — allowed in Idle, resets levels, logs the event

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design Coffee Vending Machine](solutions/Design-Coffee-Vending-Machine.md) — Easy · Factory, State

---

## Extra Practice (self-study)

- [ ] Add mocha (chocolate + espresso) — factory registration only
- [ ] Add large/small sizes — portion multiplier on the ingredient map
- [ ] Add low-ingredient alert — observer on containers below threshold

## Tips
- Say **"ingredients gate payment"** — check stock before taking money
- Atomic deduct: validate all, then take all — no half-brewed cup
- Factory + State is the whole answer — name both in the first minute

---

#lld #machine-coding #coffee-machine #easy #practice
