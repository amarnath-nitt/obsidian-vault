# Readers-Writers Problem (Reader-Writer)

**Source:** AlgoMaster · Concurrency Practice · **hard** · **Pattern:** Readers-Writers
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/readers-writers-problem)

### Problem

```java
class ReadersWriters {
    ReadersWriters();
    void read(Runnable readAction) throws InterruptedException;
    void write(Runnable writeAction) throws InterruptedException;
}
```

**Guarantees:** any number of readers run simultaneously; a writer runs **alone** (no other writer,
no readers); access lasts for the **entire callback**; callbacks are invoked exactly once; the class
only **coordinates** — it must not create worker threads. `read`/`write` declare
`throws InterruptedException` because `Condition.await()` is a checked, cancellable park.

**The hard part — writer preference:**

> *Use writer preference to prevent writer starvation. Once at least one writer is waiting, readers
> that arrive later must wait until the queued writers have had an opportunity to proceed. Readers
> that were already active may finish normally.*

### The failure, before

```java
// ❌ Reader-preference: under a steady stream of readers, writers starve forever
public void read(Runnable r) throws InterruptedException {
    lock.lock();
    while (writerActive) canRead.await();
    activeReaders++;                       // new readers keep arriving → waitingWriters never matters
    lock.unlock();
    r.run();
    // ...
}
```

### The Fix (after)

Track **waiting writers** and gate late readers on it.

```java
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public final class ReadersWriters {
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition canRead  = lock.newCondition();
    private final Condition canWrite = lock.newCondition();

    private int  activeReaders  = 0;
    private int  waitingWriters = 0;
    private boolean writerActive = false;

    public void read(Runnable readAction) throws InterruptedException {
        lock.lock();
        try {
            // READER PREFERENCE is deliberately broken here:
            // wait if a writer is active OR any writer is already queued
            while (writerActive || waitingWriters > 0) canRead.await();
            activeReaders++;                         // readers that passed go together
        } finally { lock.unlock(); }

        try {
            readAction.run();                        // OUTSIDE the lock — reads overlap
        } finally {
            lock.lock();
            try {
                activeReaders--;
                if (activeReaders == 0) canWrite.signal();   // last reader frees the writers
            } finally { lock.unlock(); }
        }
    }

    public void write(Runnable writeAction) throws InterruptedException {
        lock.lock();
        try {
            waitingWriters++;                        // ← queue position: blocks later readers
            try {
                while (writerActive || activeReaders > 0) canWrite.await();
                writerActive = true;                 // exclusive
            } finally {
                waitingWriters--;                    // we are no longer merely waiting
            }
        } finally { lock.unlock(); }

        try {
            writeAction.run();
        } finally {
            lock.lock();
            try {
                writerActive = false;
                canWrite.signal();                   // next queued writer first (FIFO-ish)
                canRead.signalAll();                 // then release readers that were held back
            } finally { lock.unlock(); }
        }
    }
}
```

**Usage**
```java
ReadersWriters rw = new ReadersWriters();
rw.read(readA); rw.read(readB);   // may run together
rw.write(writeC);                 // runs alone, after both finish
// lateRead, arriving while writeC is queued → must WAIT (writer preference)
```

### Design points
- **`waitingWriters > 0` in the readers' predicate** is the whole anti-starvation mechanism: a reader
  arriving *after* a writer queued must step aside, while readers already active finish normally.
- **`waitingWriters--` before `writerActive = true`** — the writer transitions from *queued* to
  *active* atomically with the grant, so no reader slips in between.
- **Callbacks run outside the lock** — otherwise readers would serialise, defeating the pattern.
- **Access held for the whole callback** — released only in `finally`, so a throwing callback can't
  leave a phantom writer/reader.
- **Signal order on write-finish** — the next writer first, then `signalAll()` to readers, preserving
  the writer-preference guarantee.

**Complexity:** O(1) per call (amortised) · Space O(1).

---
#concurrency #reader-writer #lld #practice
