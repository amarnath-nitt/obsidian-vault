# Design a Closable Bounded Queue (Producer-Consumer)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Producer-Consumer
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-closable-bounded-queue)

### Problem

```java
class ClosableBoundedQueue {
    ClosableBoundedQueue(int capacity);
    void put(int item) throws IllegalStateException;   // blocks while full
    Integer take();                                    // blocks while empty; null when drained+closed
    void close();                                      // permanent
}
```

**The five closing rules (Java):**
1. Items accepted **before** `close()` remain available and are returned in **FIFO** order
2. Once the closed queue is **empty**, `take()` returns `null` instead of waiting
3. A `put()` **blocked** when the queue closes must wake and **fail without adding** its item
4. Any `put()` **started after** closure **fails immediately** (throws `IllegalStateException`)
5. `close()` is **idempotent**; a closed queue never reopens

Plus: no busy-waiting; don't create worker threads inside the queue.

### The failure, before

```java
// ❌ close() sets a flag but never wakes anyone → blocked producers/consumers hang forever
void close() { closed = true; }
void put(int item) {
    while (full && !closed) lock.wait();    // wakes only if someone signals
    if (closed) throw new IllegalStateException();
    items.add(item);                        // and after close+drain, take() still waits
}
```

### The Fix (after)

```java
import java.util.ArrayDeque;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public final class ClosableBoundedQueue {
    private final ArrayDeque<Integer> items = new ArrayDeque<>();
    private final int capacity;
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition notFull  = lock.newCondition();
    private final Condition notEmpty = lock.newCondition();
    private boolean closed = false;

    public ClosableBoundedQueue(int capacity) {
        if (capacity < 1) throw new IllegalArgumentException("capacity >= 1");
        this.capacity = capacity;
    }

    public void put(int item) {
        lock.lock();
        try {
            // Rule 4: started after closure → fail immediately
            // Rule 3: blocked when closure happened → wake, fail, add nothing
            while (!closed && items.size() == capacity) notFull.awaitUninterruptibly();
            if (closed) throw new IllegalStateException("queue is closed");

            items.addLast(item);            // FIFO
            notEmpty.signal();              // wake a consumer
        } finally {
            lock.unlock();
        }
    }

    public Integer take() {
        lock.lock();
        try {
            while (items.isEmpty() && !closed) notEmpty.awaitUninterruptibly();
            if (items.isEmpty()) return null;      // Rule 2: closed AND drained → no item
            Integer item = items.removeFirst();    // Rule 1: drain accepted items in FIFO order
            notFull.signal();                      // wake a blocked producer
            return item;
        } finally {
            lock.unlock();
        }
    }

    public void close() {
        lock.lock();
        try {
            closed = true;                 // Rule 5: idempotent, never reopens
            notEmpty.signalAll();          // Rule 2 & 3: wake consumers AND blocked producers
            notFull.signalAll();
        } finally {
            lock.unlock();
        }
    }
}
```

**Usage**
```java
ClosableBoundedQueue q = new ClosableBoundedQueue(2);
q.put(10); q.put(20);
q.close();
q.take();   // 10  (drained in order)
q.take();   // 20
q.take();   // null — closed and empty, does not block
q.put(30);  // throws IllegalStateException — started after close
q.close();  // safe to call again
```

### Design points
- **One lock, two conditions** — `notFull`/`notEmpty` target their own predicates precisely.
- **`closed` is checked inside the wait loop** — a blocked producer re-evaluates after `close()` wakes
  it, so rule 3 falls out naturally (the `throw` is after the loop, before any `add`).
- **Close signals both conditions** — otherwise blocked producers hang forever.
- **`take()` checks `items.isEmpty()` before `closed` ordering** — items already accepted are drained
  first (rule 1), and only an empty+closed queue returns `null` (rule 2).
- **No busy-waiting** — everything parks on a `Condition`.
- **Idempotent close** — it just sets a flag and wakes; calling twice is harmless.

**Complexity:** O(1) per operation · Space O(capacity).

---
#concurrency #producer-consumer #lld #practice
