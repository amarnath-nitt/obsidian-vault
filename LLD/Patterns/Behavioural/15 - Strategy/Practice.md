# Strategy Pattern - Practice

## Key Concepts
- **Strategy** — interface for one algorithm
- **ConcreteStrategy** — an implementation of that algorithm
- **Context** — holds a Strategy and delegates to it
- **Runtime selection** — swap the strategy without touching the context
- **Open/Closed** — add strategies without editing existing code
- **Functional strategies** — lambdas / `Comparator` / `BiFunction`

## Common Strategy Use Cases
1. **Payment methods** — Card / UPI / PayPal / Wallet
2. **Pricing / discount rules** — flat / percentage / tiered
3. **Shipping cost** — standard / express / same-day
4. **Sorting / comparison** — `Comparator` per field
5. **Compression** — zip / gzip / none
6. **Route planning** — fastest / shortest / scenic
7. **Authentication** — password / OAuth / OTP

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design a Discount Calculator](solutions/Design-Discount-Calculator.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-strategy-discount-calculator)
- [ ] [Design a Route Planner](solutions/Design-Route-Planner.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-route-planner)

---

## Extra Practice (self-study)

- [ ] Payment strategies (Card/UPI/PayPal) — [reference code](solutions/Strategy-Implementations.md)
- [ ] Shipping cost strategies (standard/express/same-day) — [reference code](solutions/Strategy-Implementations.md)
- [ ] Strategy selected by a factory — [reference code](solutions/Strategy-Implementations.md)

---

## Tips
- **Name strategies after the rule** — `FlatDiscount`, `TieredPricing`, not `StrategyImpl1`
- Keep strategies **stateless** — safe to share and thread-safe
- **Move selection out of the context** into a factory/registry
- Say it in interviews: "Strategy = interchangeable algorithm; State = self-transitioning behaviour"