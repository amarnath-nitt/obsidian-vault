# Observer Pattern - Practice

## Key Concepts
- **Subject / Publisher** — attach, detach, notify
- **Observer / Subscriber** — `update()` callback
- **One-to-many** — one change, many reactions
- **Push vs Pull** — payload in the callback vs query the subject
- **Loose coupling** — subject knows only the observer interface
- **Async dispatch / weak refs** — robustness at scale

## Common Observer Use Cases
1. **Stock ticker** — price → investors / displays
2. **Event bus** — service events → handlers
3. **Order lifecycle** — status change → email, inventory, analytics
4. **UI listeners** — button click → multiple handlers
5. **Chat rooms** — message → all members
6. **Social feed** — new post → followers

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design a Newsletter Publisher](solutions/Design-Newsletter-Publisher.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-newsletter-publisher)

### Medium
- [ ] [Design Stock Price Alerts](solutions/Design-Stock-Price-Alerts.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-stock-alerts)
- [ ] [Design a Weather Station](solutions/Design-Weather-Station.md) — AlgoMaster · medium (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Order event bus (email + inventory + analytics) — [reference code](solutions/Observer-Implementations.md)
- [ ] Async observer dispatch / safe iteration — [reference code](solutions/Observer-Implementations.md)
- [ ] Topic-based pub-sub — [reference code](solutions/Observer-Implementations.md)

---

## Tips
- Name the two roles clearly: **Subject (publisher)** and **Observer (subscriber)**
- Always provide **detach** — and mention **memory leaks**
- Iterate over a **snapshot** during `notify()` to avoid `ConcurrentModificationException`
- For scale, dispatch notifications **asynchronously**