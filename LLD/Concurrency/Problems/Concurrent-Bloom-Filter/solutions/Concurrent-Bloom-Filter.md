# Concurrent Bloom Filter (Thread-safe structure)

**Source:** AlgoMaster · Concurrency Practice · **medium (premium)** · **Pattern:** Probabilistic set
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-concurrent-bloom-filter)
> ⚠️ Premium-gated: the link resolves to the premium page, not the statement. Contract below is
> the standard concurrent-bloom-filter shape (add / probably-contains), consistent with the
> track's naming and difficulty.

### Problem

```java
class ConcurrentBloomFilter {
    ConcurrentBloomFilter(int bitCount, int hashCount);   // m bits, k hashes
    void add(int x);
    boolean contains(int x);   // false ⇒ definitely absent; true ⇒ present OR false positive
}
```

`add` and `contains` may run concurrently. False negatives are forbidden; false positives must
stay near the theoretical rate for `(m, k)`. No deletion required.

### The failure, before

```java
// ❌ Non-atomic bit-set: two threads read the same word, each ORs its own bit locally,
// one write clobbers the other — a set bit is lost and contains() can lie "absent".
words[idx] |= mask;                       // read-modify-write, unlocked
```

### The Fix (after)

**Atomic OR per word** over an `AtomicLongArray`, positions from double hashing.

```java
import java.util.concurrent.atomic.AtomicLongArray;

public final class ConcurrentBloomFilter {
    private final AtomicLongArray bits;
    private final int bitCount;
    private final int hashCount;

    public ConcurrentBloomFilter(int bitCount, int hashCount) {
        if (bitCount < 1 || hashCount < 1) throw new IllegalArgumentException();
        this.bitCount = bitCount;
        this.hashCount = hashCount;
        this.bits = new AtomicLongArray((bitCount + 63) / 64);
    }

    private int[] positions(int x) {
        int h1 = mix(x), h2 = mix(x ^ 0x9E3779B9) | 1;   // h2 odd ⇒ coprime-ish stride
        int[] pos = new int[hashCount];
        for (int i = 0; i < hashCount; i++)
            pos[i] = Math.floorMod(h1 + i * h2, bitCount);
        return pos;
    }

    private static int mix(int z) {                      // light avalanche mix
        z ^= z >>> 16; z *= 0x7feb352d; z ^= z >>> 15; z *= 0x846ca68b; z ^= z >>> 16;
        return z;
    }

    public void add(int x) {
        for (int p : positions(x))
            bits.getAndAccumulate(p / 64, 1L << (p % 64), (a, b) -> a | b);  // atomic set
    }

    public boolean contains(int x) {
        for (int p : positions(x))
            if ((bits.get(p / 64) & (1L << (p % 64))) == 0) return false;    // proof of absence
        return true;
    }
}
```

**Usage**
```java
ConcurrentBloomFilter bf = new ConcurrentBloomFilter(8192, 5);
// threads: bf.add(id); ... bf.contains(id) → false means "never added", guaranteed
// sizing: m ≈ -(n ln p)/(ln 2)², k ≈ (m/n)·ln 2 for n items at FP rate p
```

### Design points
- **OR commutes, so concurrent adds never lose bits** — atomic OR is lossless without a lock;
  that single fact is the whole thread-safety argument.
- **One zero bit is proof of absence** — `contains` short-circuits; all-set admits the tunable
  false positive honestly.
- **Double hashing** — k well-spread positions from two mixes; `floorMod` keeps negatives in range.
- **No deletion by design** — a bit may belong to several elements; clearing corrupts the rest.
- **Lock-free reads** — `contains` takes no lock; `AtomicLongArray` gives word-level atomicity.

**Complexity:** O(k) per op · Space O(m) bits.

---
#concurrency #bloom-filter #lld #practice
