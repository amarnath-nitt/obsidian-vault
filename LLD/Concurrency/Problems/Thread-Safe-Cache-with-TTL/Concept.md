# Thread-Safe Cache with TTL — Concept

## What Is It?

A cache whose entries expire after a time-to-live. The constructor receives a `clock()` function
returning logical milliseconds (judge-controlled — never the system clock, no background threads).
`put(key, value, ttl)` expires at `clock() + ttl`; `get` returns the value or `-1` on
miss/expiry; `size` purges expired entries and counts live ones. All three may run concurrently.

| | |
|---|---|
| **Pattern** | Thread-safe map + lazy expiry (expiry checked on access, not by a sweeper) |
| **Core** | `HashMap` + per-entry `expiry` + one lock; expired ⟺ `now >= expiry` |
| **Java** | `synchronized` / `ReentrantLock` (or `ReentrantReadWriteLock` for read-heavy use) |

---

## When to Use

> **Trigger keywords:** "expire after", "TTL", "logical clock", "purge on access"

| Need | Move |
|------|------|
| Expiry without a cleaner thread | **lazy expiry** — check `now >= expiry` on every `get`/`size` |
| Replacement must not be killed by the old TTL | **store expiry per entry**, overwrite both on `put` |
| Read-heavy cache | `ReentrantReadWriteLock`: shared read lock, exclusive write lock |

---

## The shape

```java
public final class TTLCache {
    private static final class Entry { int value; long expiry; }

    private final LongSupplier clock;          // judge-controlled logical time
    private final Object lock = new Object();
    private final Map<Integer, Entry> map = new HashMap<>();

    public TTLCache(LongSupplier clock) { this.clock = clock; }

    public void put(int key, int value, long ttlMillis) {
        synchronized (lock) {
            Entry e = new Entry();
            e.value = value;
            e.expiry = clock.getAsLong() + ttlMillis;   // expiry travels WITH the entry
            map.put(key, e);                            // replace installs a fresh expiry
        }
    }

    public int get(int key) {
        synchronized (lock) {
            Entry e = map.get(key);
            if (e == null) return -1;
            if (clock.getAsLong() >= e.expiry) { map.remove(key); return -1; }  // lazy purge
            return e.value;
        }
    }

    public int size() {
        synchronized (lock) {
            long now = clock.getAsLong();               // ONE timestamp for the whole sweep
            map.entrySet().removeIf(en -> now >= en.getValue().expiry);
            return map.size();
        }
    }
}
```

**Why it works:** expiry is *data* (a per-entry timestamp), not a timer — so no background thread
can race the judge's clock, and replacing a key atomically replaces its deadline. One lock makes
check-and-act (`get`'s read-then-maybe-remove, `size`'s sweep-then-count) atomic.

---

## Notes

- `expired ⟺ now >= expiry` — live at 149, expired at 150 for `put` at 100 with TTL 50.
- Read the clock **once per method** (`size`) — a second read mid-sweep could disagree.
- `-1` is reserved for miss, so stored values are non-negative — no sentinel clash.
- At most ~1,000 live entries: a full `size()` sweep is cheap; no expiry heap needed.

---

## Common Mistakes

1. System clock / background cleaner — fights the judge's logical clock, flaky verdicts.
2. Separate `expiry` map keyed apart from values — replacement updates one and not the other.
3. Check-then-act across two lock acquisitions — an expiry can slip between them.
4. `get` returning the value but leaving the corpse — `size()` then overcounts.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Concepts/Mutex/Concept|Mutex]] · [[../../Patterns/Reader-Writer-Pattern/Concept|Reader-Writer Pattern]]

---

#concurrency #ttl-cache #lld #concept
