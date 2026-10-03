# Template Method Pattern - Practice

## Key Concepts
- **Template Method** — `final` base method defining the algorithm skeleton
- **Primitive operations** — abstract steps subclasses must implement
- **Hooks** — optional steps with default behaviour
- **Hollywood Principle** — "don't call us, we'll call you"
- **Inversion of control** — base class drives, subclass fills in

## Common Template Method Use Cases
1. **Beverage preparation** — boil → brew → pour → add condiments
2. **Data pipeline** — read → parse → transform → write
3. **Report generation** — header → body → footer
4. **Game turn** — collect input → update → render
5. **`JdbcTemplate`** — get connection → execute → map → close
6. **Servlet lifecycle** — `doGet` / `doPost`

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design a Beverage Station](solutions/Design-Beverage-Station.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-beverage-station)
- [ ] [Design a Text Formatter](solutions/Design-Text-Formatter.md) — AlgoMaster · easy (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Medium
- [ ] [Design a Build Pipeline](solutions/Design-Build-Pipeline.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-build-pipeline)
- [ ] [Design an Order Processor](solutions/Design-Order-Processor-Template.md) — AlgoMaster · medium (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Data processing pipeline (CSV/JSON import) — [reference code](solutions/Template-Method-Implementations.md)
- [ ] Game turn sequence (input/update/render) — [reference code](solutions/Template-Method-Implementations.md)
- [ ] Template Method + Factory Method — [reference code](solutions/Template-Method-Implementations.md)

---

## Tips
- Make the **template method `final`** so the sequence is protected
- Use **hooks** for optional steps; use **abstract** for mandatory ones
- Keep the template **small** — 3–5 steps
- Consider **Strategy** if subclasses would only differ by swapping an algorithm