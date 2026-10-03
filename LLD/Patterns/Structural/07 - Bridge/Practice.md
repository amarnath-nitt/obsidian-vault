# Bridge Pattern - Practice

## Key Concepts
- **Abstraction** — high-level type, holds an Implementor reference (the bridge)
- **Implementor** — low-level interface that varies independently
- **RefinedAbstraction / ConcreteImplementor** — the two concrete hierarchies
- **Class explosion avoided** — N × M becomes N + M
- **Composition over inheritance** — the bridge is a field, not an `extends`

## Common Bridge Use Cases
1. **Shapes × Renderers** — Vector / Raster drawing
2. **Remotes × Devices** — Basic/Advanced remote controlling TV/Radio
3. **Reports × Formats** — Sales/Inventory report in PDF/HTML/CSV
4. **Messages × Channels** — Text/Alert message via Email/SMS/Push
5. **Persistence × Backend** — Repository abstraction over SQL/NoSQL

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Shape Renderer](solutions/Design-Shape-Renderer.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-shape-renderer)

### Hard
- [ ] [Design a Remote Control](solutions/Design-Remote-Control.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Message × Channel bridge (Text/Alert × Email/SMS) — [reference code](solutions/Bridge-Implementations.md)
- [ ] Report × Format bridge (PDF/HTML/CSV) — [reference code](solutions/Bridge-Implementations.md)
- [ ] Bridge + Abstract Factory family — [reference code](solutions/Bridge-Implementations.md)

---

## Tips
- **Find the two dimensions** first — the "X × Y" in the requirement is the giveaway
- The **abstraction holds the implementor** as a field (`protected`/constructor-injected)
- Say it in interviews: "Bridge separates two hierarchies; Strategy swaps one algorithm"
- **Count the classes** to justify Bridge: without it, `N × M` classes; with it, `N + M`