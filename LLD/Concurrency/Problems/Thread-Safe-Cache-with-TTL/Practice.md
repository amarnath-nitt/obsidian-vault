# Thread-Safe Cache with TTL - Practice

## Key Concepts
- **Lazy expiry over a logical clock** — no timers, no background threads, no system clock
- Expiry is **per-entry data** (`expiry = clock() + ttl`), replaced atomically with the value
- One lock makes every check-and-act (`get`'s read-then-purge, `size`'s sweep-then-count) atomic

## Common Moves in LLD
1. **Entry holds value + expiry** — a single `map.put` installs both
2. **`get` purges on sight** — expired entry is removed and reported as `-1`
3. **`size` sweeps with one timestamp** — single `now` for the whole pass, then count
4. **Expired ⟺ `now >= expiry`** — boundary-inclusive, exactly as the statement defines

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Thread-Safe Cache with TTL](solutions/Thread-Safe-Cache-with-TTL.md) — AlgoMaster · medium · Thread-safe structure — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-thread-safe-cache-with-ttl)

---

## Extra Practice (self-study)

- [ ] Upgrade to `ReentrantReadWriteLock`: reads under the read lock, purge-upgrade path under write
- [ ] Trace the replacement trap: `put(7,…,expiry 15)` then `put(7,…,expiry 100)` at time 20 — prove the old deadline can't kill the new entry

## Tips
- Say **"lazy expiry against the supplied clock"** first — it rules out the background-thread design instantly
- The replacement trap is the marked edge case: expiry must travel *with* the entry
- One timestamp per `size()` sweep — reading the clock per entry is a subtle inconsistency
