# Concurrent Bloom Filter - Practice

## Key Concepts
- **Probabilistic set** — exact negatives, tunable false positives, no false negatives
- Bit-set must be **atomic OR** — monotonic updates commute, so lock-free works
- `m` bits + `k` hashes sized from `(n, p)`; double hashing derives k positions from 2 hashes

## Common Moves in LLD
1. **`AtomicLongArray` bit array** — `getAndAccumulate(word, mask, OR)` per position
2. **Double hashing** — `h1 + i*h2`, `floorMod m` (never `%` on raw hashes)
3. **`contains` short-circuits on first zero bit** — one zero is proof of absence
4. **No deletion** — clearing a bit may erase another element's membership

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.
>
> ⚠️ The AlgoMaster statement for this one is premium-gated, so the URL below resolves to the
> premium page rather than the problem text. The solution note reconstructs the standard
> contract (add / contains over a striped or lock-free bit array) faithfully.

### Medium (premium)
- [ ] [Concurrent Bloom Filter](solutions/Concurrent-Bloom-Filter.md) — AlgoMaster · medium (premium) · Thread-safe structure — [🔗 AlgoMaster](https://algomaster.io/practice/concurrency/design-concurrent-bloom-filter)

---

## Extra Practice (self-study)

- [ ] Size a filter for `n = 1M, p = 1%` — compute `m` and `k`, then verify against the formulas
- [ ] Reimplement with striped locks over `long[]` and compare contention with the lock-free form

## Tips
- Say **"atomic OR is lossless because bit-sets commute"** — the concurrency argument in one line
- Never promise zero false positives — the trade-off *is* the answer
- `floorMod` on hashes — `%` on a negative hash is the silent crash
