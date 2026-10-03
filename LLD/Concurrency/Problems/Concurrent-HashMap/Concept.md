# Concurrent HashMap — Concept

## What Is It?

A thread-safe integer→integer map with `put / get / remove / increment / size`, where
`increment(key, delta)` is one atomic read-modify-write (missing key starts at 0) and the
constructor's `stripeCount` (1..32) sets the number of **independently locked stripes** — keys on
different stripes must proceed concurrently.

| | |
|---|---|
| **Pattern** | Striped locking (lock striping) over a sharded map |
| **Core** | `stripeCount` locks; key → `stripe = floorMod(hash(key), stripeCount)` |
| **Java** | `Object[]`/`ReentrantLock[]` + per-stripe `HashMap` (or `ConcurrentHashMap` segments) |

---

## When to Use

> **Trigger keywords:** "stripeCount", "different stripes proceed concurrently", "atomic increment"

| Need | Move |
|------|------|
| Whole-map correctness, low contention | single lock (correct but serial) |
| **Concurrent disjoint keys** | **striped locks** — this package |
| Linearizable aggregate (`size`) over stripes | lock stripes in a fixed global order, then sum |

---

## The shape

```java
public final class StripedMap {
    private final Object[] locks;                 // locks[i] guards table[i]
    private final Map<Integer,Integer>[] table;

    @SuppressWarnings("unchecked")
    public StripedMap(int stripeCount) {
        locks = new Object[stripeCount];
        table = new Map[stripeCount];
        for (int i = 0; i < stripeCount; i++) { locks[i] = new Object(); table[i] = new HashMap<>(); }
    }

    private int stripe(int key) { return Math.floorMod(Integer.hashCode(key), locks.length); }

    public void put(int key, int value) {
        synchronized (locks[stripe(key)]) { table[stripe(key)].put(key, value); }
    }

    public int increment(int key, int delta) {
        int s = stripe(key);
        synchronized (locks[s]) {                  // read-modify-write under ONE stripe lock
            int next = table[s].getOrDefault(key, 0) + delta;
            table[s].put(key, next);
            return next;
        }
    }

    public int size() {
        // fixed global order 0..n-1 ⇒ no deadlock; consistent snapshot
        synchronized (locks[0]) { synchronized (locks[1]) { /* … */ return sum; } }
        // (real code: lock all stripes in index order, sum, unlock in reverse)
    }
}
```

**Why it works:** a key always maps to the same stripe, and everything touching that stripe holds
its lock — so two `increment`s on one key serialise (no lost update) while keys on different
stripes never block each other. `size()` takes *all* stripes in index order for a linearizable
snapshot without deadlock.

---

## Notes

- `floorMod`, not `%` — negative keys must still stripe to `0..stripeCount-1`.
- `-1` means "absent" and stored values are non-negative — no sentinel clash.
- `increment` result fits in signed 32-bit; delta in `1..1000`.
- `stripeCount` up to 32: a tiny fixed lock array, not one lock per key.

---

## Common Mistakes

1. Locking the whole map per op — correct but fails the "different stripes proceed" check.
2. Read-modify-write across two acquisitions — two increments interleave and one is lost.
3. `size()` locking stripes in hash order — inconsistent acquisition order risks deadlock.
4. `%` on negative keys → negative stripe index → `ArrayIndexOutOfBounds`.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Concepts/Mutex/Concept|Mutex]] · [[../../Concepts/Coarse-vs-Fine-Grained-Locking/Concept|Coarse vs Fine-grained Locking]]

---

#concurrency #concurrent-hashmap #lld #concept
