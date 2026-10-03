# Decorator Pattern - Practice

## Key Concepts
- **Component** — the shared interface
- **ConcreteComponent** — base object
- **Decorator** — abstract wrapper that *holds* a Component
- **ConcreteDecorator** — adds behaviour, then delegates
- **Stacking** — decorators compose by nesting
- **Order matters** — the nesting order changes the result

## Common Decorator Use Cases
1. **Coffee / Pizza** — condiments / toppings with prices
2. **Java I/O** — `BufferedReader(new FileReader(...))`
3. **HTTP middleware** — auth → logging → retry → handler
4. **UI components** — borders, scrollbars, shadows on a view
5. **Pricing add-ons** — insurance, gift wrap, express shipping

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Implement Pizza Topping Decorators](solutions/Implement-Pizza-Topping-Decorators.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/implement-pizza-topping-decorators)

### Medium
- [ ] [Implement Character Abilities Decorator](solutions/Implement-Character-Abilities-Decorator.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/implement-character-abilities-decorator)
- [ ] [Implement Log Formatter Decorators](solutions/Implement-Log-Formatter-Decorators.md) — AlgoMaster · medium (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] HTTP middleware chain (auth + logging + retry) — [reference code](solutions/Decorator-Implementations.md)
- [ ] Java I/O style encoding decorator — [reference code](solutions/Decorator-Implementations.md)
- [ ] Order-sensitive pricing engine (discount before/after tax) — [reference code](solutions/Decorator-Implementations.md)

---

## Tips
- The **decorator implements the same interface** as what it wraps
- **Delegate first, then add** (or add, then delegate) — be explicit about order
- Keep each decorator **single-purpose** and small
- In interviews, contrast with **Proxy** (access control) and **Adapter** (changes interface)