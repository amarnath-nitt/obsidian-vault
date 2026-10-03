# Thread-Safe Blocking Queue (Thread-safe structure)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Producer-Consumer / bounded buffer
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-bounded-blocking-queue)

### Problem

```java
class BoundedBlockingQueue {
    BoundedBlockingQueue(int capacity);   // 1..1000
    void enqueue(int element);            // block while full until space appears
    int  dequeue();                       // block while empty until an element arrives
    int  size();                          // current element count
}
```

FIFO order, never more than `capacity` elements, no busy-waiting. Multiple producers/consumers
share one instance; all three methods may run concurrently. The judge supplies balanced finite
op streams. Elements in `1..1_000_000`.

Example: `capacity = 2; enqueue(1), enqueue(2), dequeue() → 1, dequeue() → 2`.

### The failure, before

```java
// ❌ Two bugs: (1) busy-wait burns CPU and the statement forbids it;
// (2) check-then-act is unlocked — count can change between the test and the insert.
public void enqueue(int e) { while (count == cap) {} buf[tail++] = e; count++; }
```

### The Fix (after)

A **circular buffer** + **one lock, two conditions**.

```java
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public final class BoundedBlockingQueue {
    private final int[] buf;
    private int head = 0, count = 0;
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition notFull  = lock.newCondition();
    private final Condition notEmpty = lock.newCondition();

    public BoundedBlockingQueue(int capacity) {
        if (capacity < 1) throw new IllegalArgumentException("capacity >= 1");
        buf = new int[capacity];
    }

    public void enqueue(int element) throws InterruptedException {
        lock.lock();
        try {
            while (count == buf.length) notFull.await();        // full → park, zero CPU
            buf[(head + count) % buf.length] = element;
            count++;
            notEmpty.signal();                                  // an element exists now
        } finally { lock.unlock(); }
    }

    public int dequeue() throws InterruptedException {
        lock.lock();
        try {
            while (count == 0) notEmpty.await();                // empty → park
            int v = buf[head];
            head = (head + 1) % buf.length;
            count--;
            notFull.signal();                                   // space exists now
            return v;
        } finally { lock.unlock(); }
    }

    public int size() {
        lock.lock();
        try { return count; } finally { lock.unlock(); }
    }
}
```

**Usage**
```java
BoundedBlockingQueue q = new BoundedBlockingQueue(2);
// producers: q.enqueue(1); q.enqueue(2); q.enqueue(3); // third parks until a dequeue
// consumers: q.dequeue(); // → 1, 2, 3 in FIFO order, unparking producers as it goes
```

### Design points
- **Park, don't spin** — `await()` releases the lock and sleeps; `signal()` wakes exactly the
  side whose predicate just became true.
- **`while`, not `if`** — several dequeuers can wake for one element; losers must re-park, and
  spurious wakeups must never consume from an empty queue.
- **Signal under the same lock, after the mutation** — the woken thread observes the fresh
  `count`; no missed wake-up.
- **Circular indexing** — `(head + count) % length` inserts at the tail in O(1) with no shifts;
  `head` advances on dequeue.
- **`size()` locked** — the count is only ever valid under the lock; an unlocked read tears.

**Complexity:** O(1) per op · Space O(capacity).

---
#concurrency #blocking-queue #lld #practice
