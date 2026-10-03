# Design a Read-Write Coordinator (Reader-Writer)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Read-Write Lock
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-read-write-coordinator)

### Problem

```java
class ReadWriteCoordinator {
    ReadWriteCoordinator();
    void read(Runnable readTask);
    void write(Runnable writeTask);
}
```

**Guarantees:** **any number of reads** may execute simultaneously; a **write executes alone** — it
cannot overlap another writer **or any reader**; access lasts for the callback's **entire**
execution; if a callback throws, access is released and the failure propagates; instances are
independent; no specific fairness/reader-writer ordering required (unlike the hard variant).

### The failure, before

```java
// ❌ one lock for everything: correct, but reads serialise — the whole point is lost
public void read(Runnable r)  { synchronized (lock) { r.run(); } }
public void write(Runnable w) { synchronized (lock) { w.run(); } }
```

Also wrong: allowing a writer in while a reader is active, or running the callback *outside* the
granted access.

### The Fix (after)

```java
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public final class ReadWriteCoordinator {
    private final ReentrantLock lock = new ReentrantLock();
    private final Condition canRead  = lock.newCondition();
    private final Condition canWrite = lock.newCondition();
    private int  activeReaders  = 0;
    private boolean writerActive = false;

    public void read(Runnable readTask) {
        lock.lock();
        try {
            while (writerActive) canRead.awaitUninterruptibly();   // wait for exclusive writer
            activeReaders++;                                       // shared access granted
        } finally { lock.unlock(); }

        try {
            readTask.run();                                        // OUTSIDE the lock:
        } finally {                                                // many reads overlap
            lock.lock();
            try {
                activeReaders--;
                if (activeReaders == 0) canWrite.signal();         // last reader → let a writer in
            } finally { lock.unlock(); }
        }
    }

    public void write(Runnable writeTask) {
        lock.lock();
        try {
            while (writerActive || activeReaders > 0) canWrite.awaitUninterruptibly();
            writerActive = true;                                   // exclusive
        } finally { lock.unlock(); }

        try {
            writeTask.run();
        } finally {
            lock.lock();
            try {
                writerActive = false;
                canWrite.signal();                                 // next writer
                canRead.signalAll();                               // release every queued reader
            } finally { lock.unlock(); }
        }
    }
}
```

**Usage**
```java
ReadWriteCoordinator c = new ReadWriteCoordinator();
// c.read(readA); c.read(readB);   → readA and readB may run at the same time
// c.write(writeC);                 → runs only after both finish, alone
```

### Design points
- **Grant access, then release the lock before the callback** — that's why `readA` and `readB` can
  overlap while the lock itself is free.
- **Access spans the callback** — `activeReaders`/`writerActive` are only released in the callback's
  `finally`, so a writer can't slip in mid-read even if the reader throws.
- **Two conditions** — readers wait on `canRead`, writers on `canWrite`; each predicate is targeted.
- **Last reader signals the writer** — without this, a writer waits forever after the readers finish.
- **Writer out signals all readers** — several may be released at once.
- **Exceptions release access** — `finally` guarantees the invariant survives a throwing callback.

**Complexity:** O(1) per call (amortised) · Space O(1).

---
#concurrency #reader-writer #lld #practice
