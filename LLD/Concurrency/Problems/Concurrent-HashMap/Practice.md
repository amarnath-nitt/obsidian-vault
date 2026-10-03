# Concurrent HashMap - Practice

## Key Concepts
- **Lock striping** — `stripeCount` independent locks; a key always maps to the same stripe
- `increment` is **one atomic read-modify-write** under its stripe lock (missing key reads as 0)
- `size()` locks **all stripes in fixed index order** — linearizable snapshot, no deadlock

## Common Moves in LLD
1. **Stripe function** — `floorMod(hash(key), stripeCount)` (handles negative keys)
2. **Single-stripe ops** — `put/get/remove/increment` each take exactly one stripe lock
3. **All-stripes op** — `size()` acquires every lock in `0..n-1` order, sums, releases in reverse
4. **`-1` = absent** — stored values are non-negative, so the sentinel is unambiguous

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Concurrent HashMap](solutions/Concurrent-HashMap.md) — AlgoMaster · medium · Thread-safe structure — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-concurrent-hash-map)

---

## Extra Practice (self-study)

- [ ] Prove two `increment`s on the same key can't lose an update — draw the serialised interleaving
- [ ] Prove two `put`s on different stripes never block — trace the lock sets

## Tips
- Say **"striped locks; increment is read-modify-write under one stripe"** — the whole answer in a line
- The `size()` follow-up is the deadlock trap: fixed global order is the sentence they want
- `floorMod` for negative keys — `%` is the silent `ArrayIndexOutOfBounds` bug
