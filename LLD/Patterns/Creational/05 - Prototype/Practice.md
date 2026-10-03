# Prototype Pattern - Practice

## Key Concepts
- **Prototype** — the instance you copy from
- **`clone()`** — produces a new object without calling a constructor
- **Shallow copy** — references are shared
- **Deep copy** — nested objects are cloned too
- **Prototype registry** — named templates cloned on demand
- **Copy constructor** — idiomatic Java alternative to `Cloneable`

## Common Prototype Use Cases
1. **Game enemies / NPCs** — clone a base mob, tweak stats
2. **Document templates** — clone a formatted template
3. **Configuration objects** — clone a loaded config and override fields
4. **Expensive graphs** — clone a pre-built object graph
5. **Undo / snapshots** — keep a copy before mutating

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design an Enemy Spawner](solutions/Design-Enemy-Spawner.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-enemy-spawner)

### Medium
- [ ] [Design a Widget Palette](solutions/Design-Widget-Palette.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-widget-palette)

---

## Extra Practice (self-study)

- [ ] Deep copy of an `Order` with items — [reference code](solutions/Prototype-Implementations.md)
- [ ] `Cloneable` + `clone()` for a `Shape` — [reference code](solutions/Prototype-Implementations.md)
- [ ] Prototype registry of templates — [reference code](solutions/Prototype-Implementations.md)

---

## Tips
- **Deep copy** the moment your object holds a `List`, `Map`, or another mutable class
- Prefer a **copy constructor** over `Cloneable` in modern Java
- **`super.clone()`** returns a shallow copy — then fix the mutable fields manually
- A **registry** of prototypes avoids rebuilding expensive templates