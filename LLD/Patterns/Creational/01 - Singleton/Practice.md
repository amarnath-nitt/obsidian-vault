# Singleton Pattern - Practice

## Key Concepts
- **Private constructor** — blocks external `new`
- **Static instance** — the single stored object
- **Static accessor** — `getInstance()` global point of access
- **Thread safety** — the crux of the discussion
- **`volatile` + double-checked locking** — lazy + safe

## Common Singleton Use Cases
1. **Logger / Audit** — one sink for the whole app
2. **Config / Registry** — global settings
3. **Connection Pool** — one shared pool of connections
4. **Thread Pool / Executor** — one executor service
5. **Cache Manager** — a single in-memory cache owner

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design an Application Config](solutions/Design-Application-Config.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-application-config)
- [ ] [Design a Shared Counter](solutions/Design-Shared-Counter.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-shared-counter)

### Medium
- [ ] [Design an ID Generator](solutions/Design-ID-Generator.md) — AlgoMaster · medium (premium) — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-id-generator)

---

## Extra Practice (self-study)

- [ ] Eager / Lazy (DCL) / Bill Pugh / Enum variants — [reference code](solutions/Singleton-Implementations.md)
- [ ] Break & harden a Singleton (reflection, serialisation) — [reference code](solutions/Singleton-Implementations.md)
- [ ] Thread-safe connection pool as a Singleton — [reference code](solutions/Singleton-Implementations.md)

---

## Tips
- **Default to Bill Pugh or Enum** — covers ~90% of interview expectations
- **Mention `volatile`** whenever you say "double-checked locking"
- **Mention DI** as the testable alternative when you discuss downsides
- **Say "per JVM"** — a Singleton is not global across machines