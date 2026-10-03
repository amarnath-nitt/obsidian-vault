# Coarse vs Fine-grained Locking - Practice

## Key Concepts
- **Coarse** = one lock covers a lot → simple, but a throughput ceiling
- **Fine** = per-key/per-shard → parallel, but ordering bugs and deadlocks
- **Start coarse, measure, split only where contention actually is**

## Common Moves in LLD
1. **Per-key locks** — one lock per bucket, unrelated keys run in parallel
2. **Striping** — hash into N locks when a per-key table is too big
3. **Shard** — partition the whole structure across independent lock domains
4. **Re-check the invariant** — after splitting, the operation must still be atomic across the parts it touches

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Design a Keyed Task Executor](solutions/Design-Keyed-Task-Executor.md) — AlgoMaster · medium · Coarse vs Fine-grained Locking — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-keyed-task-executor)

---

## Extra Practice (self-study)

- [ ] Take a single-lock map and convert it to striped locking
- [ ] Profile a contended lock and identify whether splitting it would actually help

## Tips
- The contract to quote: **"same key never overlaps; different keys run concurrently"**
- Say **"I'd start coarse and split on measured contention"** — it shows engineering judgement
- Fine-grained locking is the direct route to **deadlock** risk — mention the ordering rule
