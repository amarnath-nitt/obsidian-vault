# Memento Pattern - Practice

## Key Concepts
- **Originator** — owns the state; creates/restores mementos
- **Memento** — immutable, opaque snapshot
- **Caretaker** — stores snapshots, never inspects them
- **Encapsulation preserved** — no getters for memento internals
- **History / undo stack** — a `Deque<Memento>` of snapshots

## Common Memento Use Cases
1. **Text editor undo/redo** — snapshot the document
2. **Drawing app** — snapshot the canvas
3. **Game save/load** — checkpoint player state
4. **Transaction rollback** — restore on failure
5. **Versioned documents** — browse history

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Text Editor](solutions/Design-Text-Editor.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-text-editor)
- [ ] [Design a Game Save System](solutions/Design-Game-Save-System.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-game-save-system)

### Hard
- [ ] [Design a Document Version History](solutions/Design-Document-Version-History.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Undo/redo with caretaker stacks — [reference code](solutions/Memento-Implementations.md)
- [ ] Bounded history (cap memory) — [reference code](solutions/Memento-Implementations.md)
- [ ] Memento + Command for precise undo — [reference code](solutions/Memento-Implementations.md)

---

## Tips
- Keep the memento **immutable** and its fields **private** (package-private access for the originator)
- The **caretaker must not read** memento contents — that is the encapsulation guarantee
- **Cap** the history size, or store **deltas**, to avoid memory growth
- Watch for **aliasing** — snapshot copies of mutable fields, not references to them