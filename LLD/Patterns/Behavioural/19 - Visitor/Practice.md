# Visitor Pattern - Practice

## Key Concepts
- **Visitor** — one `visit(elementType)` method per type
- **Element** — `accept(Visitor)`; calls back `visitor.visitX(this)`
- **Double dispatch** — behaviour depends on element type **and** visitor type
- **Open for operations** — new operation = new Visitor, no element changes
- **Closed for types** — new element type = edit every Visitor

## Common Visitor Use Cases
1. **Shapes** — area, perimeter, export-to-XML
2. **Expression AST** — evaluate, print, optimise
3. **File tree** — total size, search, report
4. **Cart items** — tax, discount, shipping per type
5. **Compiler / interpreter** — multiple passes over an AST

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Message Inbox Visitor](solutions/Design-Message-Inbox-Visitor.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-message-inbox-visitor)

### Hard
- [ ] [Design a Document Visitor](solutions/Design-Document-Visitor.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Shape area/export visitor — [reference code](solutions/Visitor-Implementations.md)
- [ ] Expression AST evaluator + printer — [reference code](solutions/Visitor-Implementations.md)
- [ ] File-tree size visitor (composite + visitor) — [reference code](solutions/Visitor-Implementations.md)

---

## Tips
- Say it in interviews: "Visitor adds **operations**, not types; new element types are costly"
- The element's `accept()` should be a **one-liner**: `visitor.visitX(this)`
- Keep visitors **stateless** when possible
- Use it only when the **type set is stable** and operations change often