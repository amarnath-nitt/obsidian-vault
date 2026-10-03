# Flyweight Pattern - Practice

## Key Concepts
- **Intrinsic state** — shared, immutable, stored in the flyweight
- **Extrinsic state** — per-object, passed in by the client
- **FlyweightFactory** — caches flyweights by key
- **Memory reduction** — many objects → few shared types
- **Immutability** — a flyweight must never change

## Common Flyweight Use Cases
1. **Forest / game world** — millions of trees or particles
2. **Text editor** — glyph styles shared per font/size/colour
3. **Chess pieces** — piece *types* shared, positions extrinsic
4. **Bullet hell** — bullet sprites shared, trajectories extrinsic
5. **JDK examples** — `Integer` cache, `String` pool

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design Board Game Pieces](solutions/Design-Board-Game-Pieces.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-board-game-pieces)
- [ ] [Design a Terrain Map](solutions/Design-Terrain-Map.md) — AlgoMaster · medium (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Forest with shared TreeTypes — [reference code](solutions/Flyweight-Implementations.md)
- [ ] Text glyph styles (shared font/size/colour) — [reference code](solutions/Flyweight-Implementations.md)
- [ ] JDK examples: `Integer` cache, `String` pool — [reference code](solutions/Flyweight-Implementations.md)

---

## Tips
- Ask: **"does this field change per object?"** — if no, it's intrinsic (share it)
- Make flyweights **immutable** (`final` fields / records)
- **Always cache** through a factory keyed by intrinsic state
- Mention the JDK **Integer cache / String pool** as real examples