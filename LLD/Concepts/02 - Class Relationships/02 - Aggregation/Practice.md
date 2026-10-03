# Aggregation - Practice

## Key Concepts
- **Weak "has-a"** — the whole shares parts it did not create and does not own
- **Lifetime test:** if the whole dies, the part survives → aggregation
- Parts are **passed in** (constructor/setter), not created internally

## Common Aggregation Moves in LLD
1. **Inject the parts** — `Library(List<Playlist>)` rather than `new`-ing them inside
2. **Copy defensively** — `List.copyOf(...)` so ownership stays clear
3. **Reuse parts across wholes** — one `Playlist` can belong to several libraries
4. **Draw the hollow diamond** ◇ on the whole side of the diagram

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Playlist Library](solutions/Design-Playlist-Library.md) — AlgoMaster · easy · Aggregation — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-playlist-library)

### Medium
- [ ] [Design Team Directory](solutions/Design-Team-Directory.md) — AlgoMaster · medium · Aggregation — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-team-directory)

### Hard
- [ ] [Design Music Catalog](solutions/Design-Music-Catalog.md) — AlgoMaster · hard · Aggregation — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-music-catalog)

---

## Extra Practice (self-study)

- [ ] Model `Team ◇── Player` and explain why the players outlive the team
- [ ] Take a composed relationship and decide whether it should be aggregation

## Tips
- Answer with the **lifetime question** — it's the fastest way to show you know the difference
- "Parts are **passed in**" is the Java-level giveaway
- Aggregation is the default when parts are **reusable**
