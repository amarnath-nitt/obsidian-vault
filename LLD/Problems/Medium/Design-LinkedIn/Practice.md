# Design LinkedIn - Practice

## Key Concepts
- **Edges are mutual ids, degree is BFS** — 2nd degree = friends-of-friends minus directs; nothing stored to rot
- **Publish returns, fan-out follows** — the observer queue is the async boundary
- **Rank on read** — engagement × affinity ÷ age; new likes reorder without rewrites

## Common Moves in LLD
1. **Connection as a directed edge with status** — PENDING → ACCEPTED becomes mutual
2. **Feed inbox per member** — fan-out writes, ranked read sorts a copy
3. **Applications snapshot** — later profile edits can't rewrite history
4. **Recruiter notify on the same event shape** — jobs ride the post/notify pipeline

---

## Problems (self-study)

> No AlgoMaster exercise — implement the solution note below, then extend it.

- [ ] [Design LinkedIn](solutions/Design-LinkedIn.md) — Medium · Observer, Strategy

---

## Extra Practice (self-study)

- [ ] Add 2nd-degree visibility rule — BFS depth 2 over the edge set
- [ ] Add async fan-out queue — `post()` enqueues, a worker drains to inboxes
- [ ] Add skill endorsements — counters on the profile, ranked into search later

## Tips
- Say **"post returns before fan-out finishes"** — the async sentence
- Degree derived, never stored — say it before they ask
- Rank on read with one formula — engagement × affinity ÷ age

---

#lld #machine-coding #linkedin #medium #practice
