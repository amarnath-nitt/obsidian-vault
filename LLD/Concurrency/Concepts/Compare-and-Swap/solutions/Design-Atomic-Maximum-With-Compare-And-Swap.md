# Design an Atomic Maximum With Compare-and-Swap (CAS)

**Source:** AlgoMaster · Concurrency Practice · **medium (premium)** · **Topic:** Compare-and-Swap (CAS)
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-atomic-maximum-with-compare-and-swap)

### Problem

Implement an **atomic maximum**: concurrent callers each propose a candidate, and the stored value
must end up as the largest candidate seen — with **no lock** and **no lost update**.

**Guarantees (as the judge checks):**
- The stored value is **linearizable** — every successful update is observed in some total order
- Concurrent `accumulate` calls **never lose** a larger candidate
- No blocking: a slow thread must not hold others up

### The race, before

```java
// ❌ read → compare → write is three steps; two threads interleave
void accumulate(int candidate) {
    if (candidate > max) {     // A and B both read max = 10
        max = candidate;       // A writes 20, B writes 15 → 15 wins, 20 LOST
    }
}
```

### The Fix (after)

The whole *compare-and-update* is one atomic instruction, wrapped in a **retry loop**.

```java
import java.util.concurrent.atomic.AtomicInteger;

public final class AtomicMaximum {
    // initialise below any legal candidate so the first CAS always has a baseline
    private final AtomicInteger max = new AtomicInteger(Integer.MIN_VALUE);

    public void accumulate(int candidate) {
        while (true) {
            int current = max.get();                          // 1. read
            if (current >= candidate) return;                 // 2. already big enough
            if (max.compareAndSet(current, candidate)) {      // 3. swap ONLY if unchanged
                return;                                       //    we won
            }
            // 4. else another thread changed it between read and CAS → retry
        }
    }

    public int get() { return max.get(); }
}
```

**Usage**
```java
AtomicMaximum m = new AtomicMaximum();
// thread A: m.accumulate(20);
// thread B: m.accumulate(15);
m.get();   // 20 — never 15, no matter the interleaving
```

### Design points
- **CAS is the atomicity** — "if it's still what I read, write; otherwise retry" is one CPU
  instruction, so no other thread can slip between the compare and the swap.
- **The loop is mandatory** — `compareAndSet` returning `false` means someone else won; you must
  re-read and retry, not give up.
- **Early exit on `current >= candidate`** — avoids pointless CAS attempts (and reduces collisions).
- **Linearizable** — each successful CAS takes effect at a single instant.
- **No lock, no blocking** — a stalled thread never prevents others from progressing.
- **Baseline initialised to `MIN_VALUE`** — so the very first candidate always succeeds without a
  null/absent special case.

> **Follow-ups to expect:** *ABA* (fix with a version stamp), *why not just use a lock?* (CAS wins
> only while the critical section is this short), *live-lock* (two threads can keep colliding).

**Complexity:** O(k) retries where k = contention · Space O(1).

---
#concurrency #cas #lock-free #lld #practice
