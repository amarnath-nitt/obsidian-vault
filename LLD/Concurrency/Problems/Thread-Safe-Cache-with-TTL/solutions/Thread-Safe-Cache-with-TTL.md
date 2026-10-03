# Thread-Safe Cache with TTL (Thread-safe structure)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Lazy-expiry map
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-thread-safe-cache-with-ttl)

### Problem

```java
class TTLCache {
    TTLCache(LongSupplier clock);              // judge-controlled logical millis
    void put(int key, int value, long ttl);    // expiry = clock() + ttl
    int  get(int key);                         // value, or -1 on miss/expiry (purges corpse)
    int  size();                               // purges expired, returns live count
}
```

Expired ⟺ `now >= expiry`. All three methods may run concurrently. Never read the system clock
or spawn cleanup threads — the judge drives `clock()`. Keys/values in `0..1_000_000`, `-1`
reserved for miss; ≤1,000 live entries, ≤20,000 calls.

Example: `put(1,42,50)` at `t=100` → expires at 150 → `get` at 149 returns `42`, at 150
returns `-1`. Replacement `put(7,…,expiry 15)` then `put(7,…,expiry 100)`: at `t=20` the key
must still be live — the old deadline dies with the old entry.

### The failure, before

```java
// ❌ Two races: (1) check-then-act outside a lock — get can return a value that
// expires before it is read; (2) expiry stored apart from the entry — a replace
// updates the value but the stale deadline kills it early.
Integer v = map.get(key);
if (v != null && !isExpired(key)) return v;   // expiry checked later, unlocked
```

### The Fix (after)

**Per-entry expiry + one lock + lazy purge**, single clock read per method.

```java
import java.util.HashMap;
import java.util.Map;
import java.util.function.LongSupplier;

public final class TTLCache {
    private static final class Entry { int value; long expiry; }

    private final LongSupplier clock;
    private final Object lock = new Object();
    private final Map<Integer, Entry> map = new HashMap<>();

    public TTLCache(LongSupplier clock) { this.clock = clock; }

    public void put(int key, int value, long ttlMillis) {
        synchronized (lock) {
            Entry e = new Entry();
            e.value = value;
            e.expiry = clock.getAsLong() + ttlMillis;   // deadline travels WITH the value
            map.put(key, e);                            // replace ⇒ fresh deadline
        }
    }

    public int get(int key) {
        synchronized (lock) {
            Entry e = map.get(key);
            if (e == null) return -1;
            if (clock.getAsLong() >= e.expiry) { map.remove(key); return -1; }
            return e.value;
        }
    }

    public int size() {
        synchronized (lock) {
            long now = clock.getAsLong();               // ONE timestamp for the sweep
            map.entrySet().removeIf(en -> now >= en.getValue().expiry);
            return map.size();
        }
    }
}
```

**Usage**
```java
// t=100: put(1, 42, 50) → expiry 150
// t=149: get(1) → 42 (live) · t=150: get(1) → -1 (expired, corpse removed)
// size() purges all corpses, then counts
```

### Design points
- **Lazy expiry** — no sweeper thread to race the logical clock; corpses die when observed.
- **Expiry inside the entry** — `put` replaces value+deadline atomically, so the old TTL can
  never kill its replacement (the marked trap).
- **One lock** — `get`'s read-check-remove and `size`'s sweep-count are each atomic; no
  check-then-act window for a concurrent `put` to slip through.
- **Single `now` per `size()`** — every entry judged against the same instant; consistent snap.
- **`>=` boundary** — entry live at 149, dead at 150 for expiry 150, exactly per spec.

**Complexity:** O(1) put/get · O(live) size sweep · Space O(live).

---
#concurrency #ttl-cache #lld #practice
