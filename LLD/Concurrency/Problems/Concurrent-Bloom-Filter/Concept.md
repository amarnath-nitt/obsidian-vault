# Concurrent Bloom Filter — Concept

## What Is It?

A space-efficient **probabilistic set**: `add(x)` inserts, `contains(x)` answers "definitely not"
or "probably yes". False negatives are impossible; false positives are tunable via size and hash
count. The concurrent version must keep both guarantees under multi-threaded `add`/`contains`.

| | |
|---|---|
| **Pattern** | Lock-free / striped bit array with k independent hashes |
| **Core** | `m`-bit array + `k` hash functions; element ⇒ k bit positions |
| **Java** | `AtomicLongArray` (lock-free) or striped locks over `long[]` |

---

## When to Use

> **Trigger keywords:** "probabilistic", "may contain", "definitely not present", "memory-efficient set"

| Need | Move |
|------|------|
| Exact membership, small set | `HashSet` (+ a lock) |
| **Exact-negative / probable-positive at scale** | **bloom filter** — this package |
| Exact membership at scale, deletions needed | concurrent hash set / Cuckoo filter |

---

## The shape

```java
public final class ConcurrentBloomFilter {
    private final AtomicLongArray bits;         // lock-free bit array
    private final int bitCount;                 // m
    private final int hashCount;                // k

    public ConcurrentBloomFilter(int bitCount, int hashCount) {
        this.bitCount = bitCount;
        this.hashCount = hashCount;
        this.bits = new AtomicLongArray((bitCount + 63) / 64);
    }

    private int[] positions(int x) {
        // double hashing: h1 + i*h2 gives k positions from 2 hashes
        int h1 = mix(x), h2 = mix(x ^ 0x9E3779B9);
        int[] pos = new int[hashCount];
        for (int i = 0; i < hashCount; i++)
            pos[i] = Math.floorMod(h1 + i * h2, bitCount);
        return pos;
    }

    public void add(int x) {
        for (int p : positions(x)) {
            long mask = 1L << (p % 64);
            bits.getAndAccumulate(p / 64, mask, (a, b) -> a | b);  // atomic bit-set
        }
    }

    public boolean contains(int x) {
        for (int p : positions(x)) {
            if ((bits.get(p / 64) & (1L << (p % 64))) == 0) return false;  // one zero ⇒ absent
        }
        return true;                              // all set ⇒ present OR false positive
    }
}
```

**Why it works:** setting bits is a monotonic OR — concurrent `add`s commute, so no update is
ever lost even lock-free. `contains` returns `false` the moment any of the k bits is zero (exact
negative); all-set means present *or* an unlucky collision (tunable false positive).

---

## Notes

- Sizing: `m ≈ -(n ln p) / (ln 2)²`, `k ≈ (m/n) ln 2` for `n` items and false-positive rate `p`.
- Bit-set must be **atomic OR** (`getAndAccumulate`, striped lock, or `synchronized`) — a plain
  read-modify-write loses concurrent sets.
- No deletion in a classic bloom filter — clearing a bit could erase another element's hash.
- `contains` needs no lock on `AtomicLongArray` — a torn read can't produce a false *negative*
  beyond the inherent raciness of concurrent add (documented linearizability caveat).

---

## Common Mistakes

1. Non-atomic bit-set (`bits[i] |= mask`) → concurrent adds lose bits → false negatives.
2. One hash reused k times without mixing → correlated positions → far higher FP rate.
3. `%` on negative hashes → negative index; use `floorMod`.
4. Promising "no false positives" — the structure *guarantees* the opposite trade-off.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Concurrent-HashMap/Concept|Concurrent HashMap]] · [[../../Concepts/Compare-and-Swap/Concept|Compare-and-Swap]]

---

#concurrency #bloom-filter #lld #concept
