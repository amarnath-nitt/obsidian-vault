# Thread Pool Pattern — Concept

## What Is It?

Create a **fixed set of long-lived worker threads** once, and feed them tasks from a queue — instead
of spawning (and destroying) a thread per task.

| | Thread-per-task | Thread pool |
|---|---|---|
| **Cost** | create/destroy per task | amortised |
| **Bound** | unbounded (can exhaust memory/OS) | **bounded** by `workerCount` |
| **Reuse** | no | yes — workers loop |
| **Shutdown** | hard to drain | explicit `shutdown()` |

---

## When to Use

> **Trigger keywords:** "bounded number of threads", "reuse workers", "submit tasks", "shutdown"

| Need | Move |
|------|------|
| Many short tasks, limited cores | thread pool |
| Bound resource usage | fixed pool size |
| Graceful drain on close | `shutdown()` that stops intake, then joins |
| Need a result per task | `ExecutorService.submit()` returning a `Future` |

---

## The shape

```java
public final class ThreadPool {
    private final BlockingQueue<Runnable> tasks = new LinkedBlockingQueue<>();
    private final List<Thread> workers = new ArrayList<>();
    private volatile boolean running = true;   // published to all workers

    public ThreadPool(int workerCount) {
        for (int i = 0; i < workerCount; i++) {
            Thread t = new Thread(() -> {
                while (running || !tasks.isEmpty()) {     // drain before exiting
                    Runnable task = tasks.poll(10, TimeUnit.MILLISECONDS);
                    if (task != null) task.run();         // OUTSIDE the queue's lock
                }
            });
            t.start();
            workers.add(t);
        }
    }

    public synchronized boolean submit(Runnable task) {
        if (!running) return false;                       // rejected after shutdown
        return tasks.offer(task);                         // accepted exactly once
    }

    public void shutdown() {
        running = false;                                  // stop accepting
        for (Thread t : workers) {
            try { t.join(); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }
    }
}
```

---

## Rules that matter

1. **Run callbacks outside the pool's internal lock** — otherwise a task can't `submit()` another
   task (self-deadlock) and long tasks block intake.
2. **Never run inline in `submit()`** — the caller must not execute the task itself; `submit` must
   return fast.
3. **`shutdown()` is idempotent and drains** — accept nothing new, run everything already accepted,
   then join all workers.
4. **Every accepted task runs exactly once** — `offer` returning `true` is the acceptance point.
5. **Workers block on a queue, not spin** — no busy-waiting.

---

## Notes

- `Executors.newFixedThreadPool(n)` is this pattern — but beware its **unbounded** queue.
- `volatile`/proper publication is essential: workers must see `running == false`.
- A worker loop must **drain** (`!tasks.isEmpty()`) after shutdown, or accepted tasks are dropped.

---

## Common Mistakes

1. Running the task inside `submit()` while holding a pool lock.
2. Workers exiting when the queue is momentarily empty, dropping accepted tasks.
3. Non-idempotent `shutdown()` — second call hangs or double-joins.
4. Unbounded queue with a bounded pool — you've only moved the problem.

---

## Related

- [[../00 - Index|Concurrency Patterns Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Concepts/Semaphores/Concept|Semaphores]] · [[../../Concepts/Race-Conditions/Concept|Race Conditions]]

---

#concurrency #thread-pool #lld #concept
