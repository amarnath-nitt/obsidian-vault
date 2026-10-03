# Design a Thread Pool (Thread Pool)

**Source:** AlgoMaster · Concurrency Practice · **hard** · **Pattern:** Thread Pool
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-thread-pool)

### Problem

```java
class ThreadPool {
    ThreadPool(int workerCount);        // starts exactly workerCount workers
    boolean submit(Runnable task);      // true if accepted; false after shutdown
    void shutdown();                    // stop intake, run everything accepted, join workers
}
```

**Guarantees:** an accepted task executes **exactly once** on a worker; after `shutdown()` begins,
`submit` returns **`false`** and the task never runs; `shutdown()` is **idempotent** and every caller
waits until all accepted tasks finish; callbacks run **outside the pool's internal lock** (a callback
may `submit()` another task); a task is **never run inline** by the calling thread.

### The failures, before

```java
// ❌ 1) runs the task in submit() — the caller executes it, violating "never inline"
// ❌ 2) holds a lock while running it — a callback that submits() deadlocks
public synchronized boolean submit(Runnable task) {
    if (!running) return false;
    task.run();                       // inline + under lock
    return true;
}

// ❌ 3) workers exit as soon as the queue is empty → accepted tasks are dropped
while (tasks.isEmpty()) { /* exit */ }
```

### The Fix (after)

```java
import java.util.*;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

public final class ThreadPool {
    private final BlockingQueue<Runnable> tasks = new LinkedBlockingQueue<>();
    private final List<Thread> workers = new ArrayList<>();
    private volatile boolean running = true;     // published to every worker

    public ThreadPool(int workerCount) {
        if (workerCount < 1) throw new IllegalArgumentException("workerCount >= 1");
        for (int i = 0; i < workerCount; i++) {
            Thread worker = new Thread(() -> {
                while (running || !tasks.isEmpty()) {        // keep draining after shutdown
                    try {
                        Runnable task = tasks.poll(5, TimeUnit.MILLISECONDS);
                        if (task != null) task.run();        // OUTSIDE any pool lock
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        return;
                    }
                }
            });
            worker.start();
            workers.add(worker);
        }
    }

    /** Accepts only — never executes the task on the caller's thread. */
    public synchronized boolean submit(Runnable task) {
        if (!running) return false;               // rejected after shutdown begins
        return tasks.offer(task);                 // offer() == true → accepted exactly once
    }

    /** Idempotent: stop accepting, drain accepted work, join all workers. */
    public void shutdown() {
        running = false;                          // stop intake (idempotent)
        for (Thread worker : workers) {
            try { worker.join(); }                // wait for the drain to finish
            catch (InterruptedException e) { Thread.currentThread().interrupt(); return; }
        }
    }
}
```

**Usage**
```java
ThreadPool pool = new ThreadPool(2);
pool.submit(() -> System.out.print("A"));   // true
pool.submit(() -> System.out.print("B"));   // true
pool.shutdown();                            // waits until A and B have both run
pool.submit(() -> {});                      // false — never runs
pool.shutdown();                            // safe to call again
```

### Design points
- **`offer()` is the acceptance point** — `true` means *exactly once* will happen; `false` after
  shutdown means *never*.
- **Tasks run in the worker loop, not in `submit()`** — satisfies "never inline" and keeps the caller
  fast.
- **No lock held while running a task** — a callback that calls `submit()` can acquire the
  `synchronized` method, so no self-deadlock.
- **`while (running || !tasks.isEmpty())`** — workers don't exit on a momentarily empty queue, so
  accepted tasks are never dropped.
- **`volatile running`** — workers see the shutdown flag promptly.
- **`join()` in `shutdown()`** — every caller returns only after all accepted tasks finished, making
  repeated calls idempotent and safe.

**Complexity:** O(1) per submit · Space O(workerCount + queued tasks).

---
#concurrency #thread-pool #lld #practice
