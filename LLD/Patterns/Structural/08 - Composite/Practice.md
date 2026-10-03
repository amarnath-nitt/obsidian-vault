# Composite Pattern - Practice

## Key Concepts
- **Component** — common interface for leaves and composites
- **Leaf** — a terminal element with no children
- **Composite** — holds children and aggregates over them
- **Recursion** — operations recurse down the tree
- **Transparent vs Safe** — where `add/remove` live

## Common Composite Use Cases
1. **File system** — File + Folder, total size
2. **Menus** — MenuItem + sub-Menu
3. **Org chart** — Developer + Manager, total cost
4. **UI widget tree** — Panel containing widgets
5. **Parking lot** — Lot → Floor → Spot aggregation
6. **Arithmetic expressions** — Number + Add/Multiply nodes

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Menu System](solutions/Design-Menu-System.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-menu-system)
- [ ] [Design a File Tree](solutions/Design-File-Tree.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-file-tree)

### Hard
- [ ] [Design an HTML Element Tree](solutions/Design-HTML-Element-Tree.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Organization compensation (Manager's team cost) — [reference code](solutions/Composite-Implementations.md)
- [ ] Arithmetic expression tree (`evaluate()`) — [reference code](solutions/Composite-Implementations.md)
- [ ] Composite + Visitor for multiple operations — [reference code](solutions/Composite-Implementations.md)

---

## Tips
- **Notice the word "group"/"folder"/"and its children"** — that is Composite
- Prefer the **Safe** variant (child ops only on Composite)
- Every aggregate method should **recurse** into children
- **Guard against cycles** if the tree can be mutated arbitrarily