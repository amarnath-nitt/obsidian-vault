# Builder Pattern - Practice

## Key Concepts
- **Fluent API** — each setter returns `this`
- **`build()`** — validates and returns the immutable product
- **Static nested builder** — `Product.builder()`
- **Immutability** — final fields, no setters on the product
- **Telescoping constructor** — the anti-pattern Builder removes

## Common Builder Use Cases
1. **HTTP request** — url, method, headers, body, timeout, retries
2. **SQL query** — SELECT / FROM / WHERE / ORDER BY step by step
3. **Pizza / burger** — size, crust, toppings
4. **User / profile** — name, email, address, preferences
5. **Document** — title, sections, theme, output format

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Implement Email Builder](solutions/Implement-Email-Builder.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/implement-builder-email)

### Medium
- [ ] [Implement a Report Builder](solutions/Implement-Report-Builder.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/implement-report-builder)

### Hard
- [ ] [Implement a Pizza Builder and Director](solutions/Implement-Pizza-Builder-And-Director.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] HttpRequest builder (headers + defaults) — [reference code](solutions/Builder-Implementations.md)
- [ ] SqlQuery builder (step-by-step clauses) — [reference code](solutions/Builder-Implementations.md)
- [ ] Immutable value object with `toBuilder()` — [reference code](solutions/Builder-Implementations.md)

---

## Tips
- The **fluent methods return `this`**; only `build()` returns the product
- **Validate in `build()`** — throw `IllegalStateException` for missing required fields
- Keep the **product immutable** (`private final` fields, no setters)
- **Don't reuse** a builder instance across builds — start fresh
- Use `toBuilder()` on an immutable object to create a modified copy