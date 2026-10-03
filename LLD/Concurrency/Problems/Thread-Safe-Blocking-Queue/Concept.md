# Thread-Safe Blocking Queue — Concept

## What Is It?

A fixed-capacity FIFO queue shared by producer and consumer threads: `enqueue` blocks when full
until space appears; `dequeue` blocks when empty until an element arrives; `size` reports the
current count. No busy-waiting — parked threads sleep on conditions.

| | |
|---|---|
| **Pattern** | Producer-Consumer / bounded buffer |
| **Core** | circular array (or linked list) + `notFull` / `notEmpty` conditions on one lock |
| **Java** | `ReentrantLock` + two `Condition`s (or `synchronized` + `wait/notifyAll`) |

---

## When to Use

> **Trigger keywords:** "fixed capacity", "blocks when full/empty", "FIFO", "without busy-waiting"

| Need | Move |
|------|------|
| Unbounded hand-off | `LinkedBlockingQueue` without bound (see Producer-Consumer Pattern) |
| **Bounded hand-off with backpressure** | **blocking queue** — this package |
| Many producers/consumers, high throughput | two-lock queue (separate put/take locks) |

---

## The shape

```java
public final class BoundedBlockingQueue {
    private final int[] buf;                        // circular buffer
    private int head = 0, count = 0;
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition notFull  = lock.newCondition();
    private final Condition notEmpty = lock.newCondition();

    public BoundedBlockingQueue(int capacity) { buf = new int[capacity]; }

    public void enqueue(int element) throws InterruptedException {
        lock.lock();
        try {
            while (count == buf.length) notFull.await();       // full → park (no spin)
            buf[(head + count) % buf.length] = element;
            count++;
            notEmpty.signal();                                 // wake one parked dequeuer
        } finally { lock.unlock(); }
    }

    public int dequeue() throws InterruptedException {
        lock.lock();
        try {
            while (count == 0) notEmpty.await();               // empty → park
            int v = buf[head];
            head = (head + 1) % buf.length;
            count--;
            notFull.signal();                                  // wake one parked enqueuer
            return v;
        } finally { lock.unlock(); }
    }

    public int size() {
        lock.lock();
        try { return count; } finally { lock.unlock(); }       // under lock: no torn read
    }
}
```

**Why it works:** each condition is the *negation of a wait predicate* — `notFull` means "space
exists", `notEmpty` means "an element exists". Every state change signals exactly the side it
unblocks, so no thread sleeps through its wake-up and none ever spins.

---

## Notes

- `while`, not `if` — a woken thread must re-check; another consumer may have taken the element.
- `signal()` suffices (one waiter per side makes progress), `signalAll()` is the safe default.
- `size()` under the lock — otherwise a concurrent enqueue/dequeue tears the read.
- Capacity `1..1000`, elements `1..1_000_000`; the judge uses balanced finite op streams.

---

## Common Mistakes

1. Spinning on `while (full) {}` — burns CPU; the statement forbids busy-waiting.
2. `if` instead of `while` → two woken dequeuers, one element, one crash.
3. Signalling the wrong condition (or none) → threads sleep forever despite available work/space.
4. Returning from `size()` outside the lock → torn count under concurrency.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Patterns/Producer-Consumer-Pattern/Concept|Producer-Consumer Pattern]] · [[../../Concepts/Condition-Variables/Concept|Condition Variables]]

---

#concurrency #blocking-queue #lld #concept
