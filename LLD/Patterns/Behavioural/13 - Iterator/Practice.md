# Iterator Pattern - Practice

## Key Concepts
- **Iterator** — `hasNext()` + `next()`
- **Aggregate** — `iterator()` factory method
- **External vs internal** — client-driven vs collection-driven
- **Encapsulation** — the internal structure stays hidden
- **Fail-fast vs fail-safe** — behaviour under concurrent modification
- **Java `Iterable`** — enables `for-each`

## Common Iterator Use Cases
1. **Playlist** — iterate songs
2. **Tree traversal** — in-order / pre-order / level-order
3. **Social feed** — paginated friends/posts
4. **Custom collection** — ring buffer, LRU list
5. **Inventory / catalogue** — iterate items by some order

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design a Playlist Iterator](solutions/Design-Playlist-Iterator.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-playlist-iterator)

### Medium
- [ ] [Design a Music Library Iterator](solutions/Design-Music-Library-Iterator.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-music-library-iterator)

### Hard
- [ ] [Design a Paginated Catalog](solutions/Design-Paginated-Catalog.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Binary tree in-order iterator (stack-based, lazy) — [reference code](solutions/Iterator-Implementations.md)
- [ ] Filtered / round-robin iterators — [reference code](solutions/Iterator-Implementations.md)
- [ ] Fail-fast iterator with a modification counter — [reference code](solutions/Iterator-Implementations.md)

---

## Tips
- Implement **`Iterable<T>`** so your class works with `for-each`
- Keep **traversal state inside the iterator**, not the collection
- Never **expose the internal list** — return an iterator instead
- Watch out for **`ConcurrentModificationException`**; document fail-fast behaviour