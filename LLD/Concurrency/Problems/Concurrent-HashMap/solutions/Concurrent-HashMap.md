# Concurrent HashMap (Thread-safe structure)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Lock striping
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-concurrent-hash-map)

### Problem

```java
class ConcurrentHashMap {
    ConcurrentHashMap(int stripeCount);   // 1..32 independently locked stripes
    void put(int key, int value);
    int  get(int key);                    // value, or -1 when absent
    void remove(int key);
    int  increment(int key, int delta);   // atomically add delta (missing ⇒ 0), return new value
    int  size();                          // key count in a consistent snapshot
}
```

Every op is thread-safe and linearizable. Keys on different stripes must proceed concurrently;
two concurrent `increment`s must never lose an update. Keys in `±1_000_000`, values
non-negative (`-1` = absent), delta `1..1000`, result fits signed 32-bit.

Example: `put(1,10), put(2,20), get(1)→10, put(1,15), get(1)→15, remove(2), get(2)→-1, size→1`
(updating key 1 doesn't change the count).

### The failure, before

```java
// ❌ Two bugs: (1) read-modify-write split across no/partial locking — two increments
// interleave and one update is lost; (2) one global lock — disjoint keys serialise,
// failing the "different stripes proceed concurrently" check.
public int increment(int key, int delta) {
    int cur = map.getOrDefault(key, 0);   // read (unlocked)
    map.put(key, cur + delta);            // write (later) — another thread slipped between
    return cur + delta;
}
```

### The Fix (after)

**One lock per stripe**; single-key ops take one lock, `size()` takes all in index order.

```java
import java.util.HashMap;
import java.util.Map;

public final class ConcurrentHashMap {
    private final Object[] locks;
    private final Map<Integer, Integer>[] table;

    @SuppressWarnings("unchecked")
    public ConcurrentHashMap(int stripeCount) {
        if (stripeCount < 1) throw new IllegalArgumentException("stripeCount >= 1");
        locks = new Object[stripeCount];
        table = new Map[stripeCount];
        for (int i = 0; i < stripeCount; i++) { locks[i] = new Object(); table[i] = new HashMap<>(); }
    }

    private int stripe(int key) { return Math.floorMod(Integer.hashCode(key), locks.length); }

    public void put(int key, int value) {
        int s = stripe(key);
        synchronized (locks[s]) { table[s].put(key, value); }
    }

    public int get(int key) {
        int s = stripe(key);
        synchronized (locks[s]) { return table[s].getOrDefault(key, -1); }
    }

    public void remove(int key) {
        int s = stripe(key);
        synchronized (locks[s]) { table[s].remove(key); }
    }

    public int increment(int key, int delta) {
        int s = stripe(key);
        synchronized (locks[s]) {                       // read-modify-write: ONE critical section
            int next = table[s].getOrDefault(key, 0) + delta;
            table[s].put(key, next);
            return next;
        }
    }

    public int size() {
        for (int i = 0; i < locks.length; i++) { /* acquire locks[0..n-1] in order */ }
        try {
            int total = 0;
            for (Map<Integer, Integer> shard : table) total += shard.size();
            return total;
        } finally { /* release in reverse order */ }
        // Practical form: lock in index order with explicit monitor nesting or a
        // striped ReadWriteLock; the rule is FIXED GLOBAL ORDER, never hash order.
    }
}
```

> **Faithful `size()` implementation** (locks strictly in index order — deadlock-free):
> ```java
> public int sizeOrdered() {
>     // recursive nesting keeps acquisition order 0..n-1 regardless of stripeCount
>     return sizeFrom(0);
> }
> private int sizeFrom(int i) {
>     if (i == locks.length) { int t = 0; for (Map<Integer,Integer> sh : table) t += sh.size(); return t; }
>     synchronized (locks[i]) { return sizeFrom(i + 1); }
> }
> ```

**Usage**
```java
ConcurrentHashMap map = new ConcurrentHashMap(4);
// threads hammer increment(k, d) concurrently — every delta lands exactly once
// keys hashing to different stripes never block each other
```

### Design points
- **Stripe affinity** — a key always lands on the same stripe, so one stripe lock serialises all
  racers on that key; lost update becomes impossible.
- **`increment` is one critical section** — read, add, write, return under the same hold; the
  interleaving that loses updates has nowhere to slip in.
- **Disjoint stripes never share a lock** — the concurrency the statement demands falls out of
  the design, no special-casing.
- **`size()` in fixed index order** — every thread that ever takes multiple stripes uses `0..n-1`,
  so no wait-cycle (deadlock) can form; the sum is a linearizable snapshot.
- **`floorMod`** — negative keys stripe into range; `%` would index out of bounds.

**Complexity:** O(1) amortised per single-key op · `size()` O(stripes + keys) · Space O(keys + stripes).

---
#concurrency #concurrent-hashmap #lld #practice
