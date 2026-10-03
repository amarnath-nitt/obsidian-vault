# DRY - Practice

## Key Concepts
- **One home for each piece of knowledge** — change it in exactly one place
- DRY is about **knowledge**, not identical text
- Prefer the **rule of three** before abstracting

## Common DRY Moves in LLD
1. **Extract a constant** — replace magic numbers with a named value
2. **Extract a method** — one copy of a validation or calculation
3. **Extract a value object / spec** — a single `PriceBook`, `TaxRule`, `PasswordPolicy`
4. **Centralise a lookup** — one map instead of scattered `if (sku == ...)`

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Refactor Account Intake](solutions/Refactor-Account-Intake.md) — AlgoMaster · easy · DRY — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-account-intake)
- [ ] [Refactor Price Book](solutions/Refactor-Price-Book.md) — AlgoMaster · easy · DRY — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-price-book)

---

## Extra Practice (self-study)

- [ ] Find three duplicated rules in your own code and give each one home
- [ ] Replace a scattered magic number with a single named constant

## Tips
- Say **"one source of truth"** — it is the interviewer-friendly phrasing of DRY
- Watch the **over-abstraction trap**: shared text is not always shared knowledge
- DRY is the cure for **Shotgun Surgery**
