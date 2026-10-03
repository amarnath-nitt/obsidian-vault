# Producer-Consumer Pattern — Concept

## What Is It?

One or more threads **produce** items into a bounded buffer; others **consume** them. The buffer
decouples the two rates, applies back-pressure when it's full, and blocks consumers when it's empty.

| | |
|---|---|
| **Pattern** | Producer → bounded queue → Consumer |
| **Core** | two conditions: *not full* and *not empty* |
| **Java** | `BlockingQueue`, or a lock + two `Condition`s |

---

## When to Use

> **Trigger keywords:** "producers and consumers", "back-pressure", "bounded buffer", "rate mismatch", "clean shutdown"

| Need | Move |
|------|------|
| Decouple rates, bound memory | **bounded** queue |
| Producers outpace consumers | block the producer (`notFull.await()`) |
| Consumers outpace producers | block the consumer (`notEmpty.await()`) |
| Graceful end of stream | **close()** the queue — drain what's accepted, reject the rest |

---

## The shape

```java
public final class BoundedQueue<T> {
    private final ArrayDeque<T> items = new ArrayDeque<>();
    private final int capacity;
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition notFull  = lock.newCondition();
    private final Condition notEmpty = lock.newCondition();

    public BoundedQueue(int capacity) { this.capacity = capacity; }

    public void put(T item) throws InterruptedException {
        lock.lock();
        try {
            while (items.size() == capacity) notFull.await();   // back-pressure
            items.addLast(item);
            notEmpty.signal();                                 // wake a consumer
        } finally { lock.unlock(); }
    }

    public T take() throws InterruptedException {
        lock.lock();
        try {
            while (items.isEmpty()) notEmpty.await();           // wait for work
            T item = items.removeFirst();
            notFull.signal();                                  // wake a producer
        } finally { lock.unlock(); }
        return item;
    }
}
```

---

## Closing (the part interviews actually ask about)

```java
// close() must be unambiguous:
//  1. items already accepted stay available, drained in FIFO order
//  2. once drained, take() returns "no item" instead of blocking forever
//  3. a producer blocked in put() wakes and FAILS without adding
//  4. a producer arriving after close() fails immediately
//  5. close() is idempotent — a closed queue never reopens
```

---

## Notes

- **Two conditions, not one** — one lock protecting both `notEmpty` and `notFull` avoids the
  thundering herd on a single predicate.
- **`while`, always** — both sides must re-check after waking.
- **`signal()` vs `signalAll()`** — with distinct predicates, `signal()` is precise; `signalAll()` is
  the safe default.

---

## Common Mistakes**

1. Unbounded queue — "back-pressure" silently becomes an OOM.
2. Forgetting to signal the *other* side after mutating.
3. Blocking a producer forever because `close()` never wakes it.
4. Returning items after close instead of draining, or dropping them instead of draining.

---

## Related

- [[../00 - Index|Concurrency Patterns Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Concepts/Condition-Variables/Concept|Condition Variables]] · [[../../Concepts/Semaphores/Concept|Semaphores]]

---

#concurrency #producer-consumer #lld #concept
