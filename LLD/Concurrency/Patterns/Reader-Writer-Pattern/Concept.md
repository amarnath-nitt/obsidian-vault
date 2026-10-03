# Reader-Writer Pattern — Concept

## What Is It?

Many threads may **read** a shared resource concurrently; a **writer** must have it **exclusively**.
The pattern exploits the fact that reads don't conflict with each other.

| | Readers | Writers |
|---|---|---|
| **vs readers** | may run together | must wait |
| **vs writers** | must wait | must run alone |

| Variant | Rule |
|---------|------|
| **Reader-preference** | readers never wait for readers — writers can **starve** |
| **Writer-preference** | once a writer waits, new readers queue — prevents writer starvation |
| **Fair** | strict arrival order |

---

## When to Use

> **Trigger keywords:** "many readers, few writes", "read-heavy", "cache", "shared config", "concurrent reads"

| Need | Move |
|------|------|
| Frequent reads, rare writes | **reader-writer lock** |
| Strict write ordering / no writer starvation | **writer preference** |
| Simple and uncontended | a plain mutex (readers then serialize — slower but simpler) |

---

## The shape (writer-preference)

```java
public final class ReadersWriters {
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition canRead  = lock.newCondition();
    private final Condition canWrite = lock.newCondition();
    private int activeReaders  = 0;
    private int waitingWriters = 0;
    private boolean writerActive = false;

    public void read(Runnable action) throws InterruptedException {
        lock.lock();
        try {
            // writer preference: wait if a writer is active OR waiting
            while (writerActive || waitingWriters > 0) canRead.await();
            activeReaders++;                        // shared access
        } finally { lock.unlock(); }

        try { action.run(); }                       // OUTSIDE the lock
        finally {
            lock.lock();
            try {
                activeReaders--;
                if (activeReaders == 0) canWrite.signal();   // last reader lets a writer in
            } finally { lock.unlock(); }
        }
    }

    public void write(Runnable action) throws InterruptedException {
        lock.lock();
        try {
            waitingWriters++;                       // block later readers (anti-starvation)
            try {
                while (writerActive || activeReaders > 0) canWrite.await();
                writerActive = true;                // exclusive
            } finally { waitingWriters--; }
        } finally { lock.unlock(); }

        try { action.run(); }
        finally {
            lock.lock();
            try {
                writerActive = false;
                canWrite.signal();                  // next writer
                canRead.signalAll();                // release queued readers
            } finally { lock.unlock(); }
        }
    }
}
```

---

## Notes

- **Run the callback outside the lock** — otherwise readers serialise each other and you've thrown
  away the entire benefit.
- **`signal()` for the writer, `signalAll()` for readers** — many readers may go at once.
- The `waitingWriters` counter is what stops readers from starving writers.

---

## Common Mistakes**

1. Holding the lock while running the read/write action → readers block each other.
2. Reader-preference and then wondering why writers never run.
3. Forgetting to signal `canWrite` when the last reader leaves.
4. Not re-checking predicates after every wakeup.

---

## Related

- [[../00 - Index|Concurrency Patterns Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Concepts/Condition-Variables/Concept|Condition Variables]] · [[../../Concepts/Mutex/Concept|Mutex]]

---

#concurrency #reader-writer #lld #concept
