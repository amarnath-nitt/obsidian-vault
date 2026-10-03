# Abstract Factory Pattern - Practice

## Key Concepts
- **AbstractFactory** — declares a `create*()` per product type
- **ConcreteFactory** — one per family/variant (Light, Dark, AWS, GCP)
- **AbstractProduct / ConcreteProduct** — the individual items in the family
- **Consistency guarantee** — one factory produces a matching set
- **Client** — chooses a factory once, then builds the family

## Common Abstract Factory Use Cases
1. **UI themes** — Light vs Dark (Button + Checkbox + TextField)
2. **Cross-platform UI** — Windows vs Mac vs Linux widgets
3. **Repository suites** — SQL vs NoSQL (UserRepo + OrderRepo + PaymentRepo)
4. **Cloud SDKs** — AWS vs GCP (Storage + Queue + Compute)
5. **Furniture kits** — Modern vs Victorian (Chair + Sofa + Table)

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design Theme Factory](solutions/Design-Theme-Factory.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-factory-theme)

### Hard
- [ ] [Design Cloud Provider Factory](solutions/Design-Cloud-Provider-Factory.md) — AlgoMaster · hard — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-cloud-provider-factory)

---

## Extra Practice (self-study)

- [ ] Furniture kit factory (Chair/Sofa/Table) — [reference code](solutions/Abstract-Factory-Implementations.md)
- [ ] Repository suite (SQL vs NoSQL) — [reference code](solutions/Abstract-Factory-Implementations.md)
- [ ] Factory-of-factories registry — [reference code](solutions/Abstract-Factory-Implementations.md)

---

## Tips
- **Think "family" first** — if the products must match, reach for Abstract Factory
- **Expose only abstract products** from every `create*()` method
- **Choose the factory once** at start-up, then reuse it
- **Call out the trade-off**: adding a *product* is hard, adding a *family* is easy