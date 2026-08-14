# Multithreading — Code Snippet Practice

Practice these "What does this code print?" questions for Java Multithreading and Concurrency. Attempt each snippet before revealing the answer.

Related theory: [Core Java Interview Questions](Java Core/Core-Java-Interview-Questions.mdCore-Java-Interview-Questions.md) and [Modern Java Interview Questions](Java Core/Core-Java-Interview-Questions.mdModern-Java-Interview-Questions.md)

---

## Snippet 1 — run() vs start() 🟢

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(() -> {
            System.out.println("Thread: " + Thread.currentThread().getName());
        });

        System.out.println("Before: " + Thread.currentThread().getName());
        t.run();   // not t.start()
        System.out.println("After: " + Thread.currentThread().getName());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Before: main
Thread: main
After: main
```

**Explanation:**
- `t.run()` does NOT create a new thread. It simply calls the `run()` method as a **normal method call** on the current thread (`main`).
- That's why `Thread.currentThread().getName()` inside the Runnable shows `"main"`.
- To actually run in a new thread, you must call `t.start()`, which would show a name like `"Thread-0"`.
- This is one of the most common threading bugs.

**Common wrong answer:** "Thread: Thread-0" — confusing `run()` with `start()`.

**Interview Tip:** "`run()` executes synchronously on the calling thread. `start()` creates a new OS thread and invokes `run()` on it. Never call `run()` directly if you want concurrency."

</details>

---

## Snippet 2 — Thread Ordering Is Non-Deterministic 🟡

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) {
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 3; i++) System.out.print("A");
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 3; i++) System.out.print("B");
        });

        t1.start();
        t2.start();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Non-deterministic. Could be any interleaving:
AAABBB
BBBAAA
ABABAB
AABBBA
BAABAB
... etc.
```

**Explanation:**
- Thread scheduling is managed by the OS. There is **no guarantee** on execution order.
- `t1.start()` being called before `t2.start()` does NOT mean `t1` will execute first or finish first.
- Even calling `start()` first only means the thread is scheduled — the OS decides when it actually runs.
- If you need ordering, use synchronization, `join()`, `CountDownLatch`, or other coordination primitives.

**Interview Tip:** "Thread execution order is non-deterministic. Never assume one thread will run before another without explicit synchronization."

</details>

---

## Snippet 3 — Volatile Flag Visibility 🟡

**What problem does this code have?**

```java
public class Main {
    static boolean running = true;

    public static void main(String[] args) throws InterruptedException {
        Thread worker = new Thread(() -> {
            int count = 0;
            while (running) {
                count++;
            }
            System.out.println("Stopped after " + count);
        });

        worker.start();
        Thread.sleep(100);
        running = false;
        System.out.println("Set running to false");
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
May print:
Set running to false
(worker thread may NEVER stop — infinite loop)

Or with volatile:
Set running to false
Stopped after <some number>
```

**Explanation:**
- Without `volatile`, the worker thread may **cache** the `running` variable in its CPU register or local memory.
- The main thread sets `running = false`, but the worker thread may never see this change — it keeps reading its cached `true`.
- This is a **visibility problem** in the Java Memory Model.
- **Fix:** Declare `static volatile boolean running = true;`
- `volatile` guarantees that writes by one thread are immediately visible to other threads.
- In practice, JIT optimizations (like hoisting the field read out of the loop) can make this bug very real.

**Common wrong answer:** "Worker always stops" — not understanding visibility without volatile.

**Interview Tip:** "`volatile` guarantees visibility across threads. Without it, the JVM may cache the variable, and another thread's write may never be seen."

</details>

---

## Snippet 4 — Race Condition on count++ 🟡

**What does this code print?**

```java
public class Main {
    static int count = 0;

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) count++;
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) count++;
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Count: " + count);
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Count: (some number ≤ 20000, rarely exactly 20000)
Example: Count: 15823
```

**Explanation:**
- `count++` is NOT atomic. It involves three steps: read, increment, write.
- Two threads can read the same value simultaneously, increment it, and write the same result — losing one increment.
- This is a **race condition** (also called a "lost update").
- **Fixes:**
  1. Use `synchronized`: `synchronized(Main.class) { count++; }`
  2. Use `AtomicInteger`: `AtomicInteger count = new AtomicInteger(); count.incrementAndGet();`
  3. Use `LongAdder` for high-contention counting.

**Common wrong answer:** "Count: 20000" — assuming `++` is atomic.

**Interview Tip:** "`i++` is not atomic — it's read-modify-write. Use `AtomicInteger.incrementAndGet()` or `synchronized` for thread-safe increments."

</details>

---

## Snippet 5 — Deadlock Example 🔴

**What happens when this code runs?**

```java
public class Main {
    static final Object lockA = new Object();
    static final Object lockB = new Object();

    public static void main(String[] args) {
        Thread t1 = new Thread(() -> {
            synchronized (lockA) {
                System.out.println("T1: holding lockA");
                try { Thread.sleep(50); } catch (InterruptedException e) {}
                synchronized (lockB) {
                    System.out.println("T1: holding lockA and lockB");
                }
            }
        });

        Thread t2 = new Thread(() -> {
            synchronized (lockB) {
                System.out.println("T2: holding lockB");
                try { Thread.sleep(50); } catch (InterruptedException e) {}
                synchronized (lockA) {
                    System.out.println("T2: holding lockB and lockA");
                }
            }
        });

        t1.start();
        t2.start();
    }
}
```

<details>
<summary>Answer</summary>

**Output (most likely):**
```
T1: holding lockA
T2: holding lockB
(program hangs — DEADLOCK)
```

**Explanation:**
- T1 acquires `lockA` and sleeps. T2 acquires `lockB` and sleeps.
- T1 wakes up and tries to acquire `lockB` — blocked because T2 holds it.
- T2 wakes up and tries to acquire `lockA` — blocked because T1 holds it.
- Both threads are waiting for each other → **deadlock**.
- Deadlock conditions (all four must be present): mutual exclusion, hold-and-wait, no preemption, circular wait.
- **Fix:** Always acquire locks in the **same order** (e.g., always `lockA` before `lockB`).

```java
// Fix: Both threads acquire lockA first, then lockB
synchronized (lockA) {
    synchronized (lockB) { ... }
}
```

**Interview Tip:** "Deadlock occurs when threads acquire locks in different orders. Fix by establishing a global lock ordering. Use `tryLock()` with timeout for graceful recovery."

</details>

---

## Snippet 6 — synchronized on Wrong Object 🟡

**Is this code thread-safe?**

```java
public class Counter {
    private int count = 0;

    public void increment() {
        synchronized (new Object()) {
            count++;
        }
    }

    public int getCount() {
        return count;
    }
}
```

<details>
<summary>Answer</summary>

**Answer: NO — this is NOT thread-safe.**

**Explanation:**
- `synchronized (new Object())` creates a **new lock object** on every call.
- Each thread synchronizes on a different object → no mutual exclusion.
- This is equivalent to having no synchronization at all.
- **Fix:** Synchronize on a shared, stable object:

```java
private final Object lock = new Object();

public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

- Or use `synchronized` on `this`:
```java
public synchronized void increment() {
    count++;
}
```

**Common wrong answer:** "Yes, it's thread-safe because of synchronized" — not examining WHAT object is being locked on.

**Interview Tip:** "Synchronization is only effective when threads lock on the SAME object. Locking on `new Object()` is useless — each thread gets its own lock."

</details>

---

## Snippet 7 — wait() Outside synchronized 🟢

**What happens when this code runs?**

```java
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Object monitor = new Object();
        monitor.wait();
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Exception in thread "main" java.lang.IllegalMonitorStateException
```

**Explanation:**
- `wait()` must be called from within a `synchronized` block on the same object.
- The thread must own the object's monitor (lock) before calling `wait()`.
- `wait()` releases the monitor, allowing other threads to acquire it and call `notify()`.
- Without `synchronized`, the thread doesn't own the monitor → `IllegalMonitorStateException`.
- **Correct usage:**

```java
synchronized (monitor) {
    while (!condition) {
        monitor.wait();    // releases monitor, waits for notify
    }
}
```

**Interview Tip:** "`wait()`, `notify()`, and `notifyAll()` must be called inside a `synchronized` block on the same object. Always use `wait()` inside a `while` loop to guard against spurious wakeups."

</details>

---

## Snippet 8 — Thread.join() Behavior 🟡

**What does this code print?**

```java
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(() -> {
            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {}
            System.out.println("Thread finished");
        });

        t.start();
        System.out.println("Before join");
        t.join();
        System.out.println("After join");
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Before join
Thread finished
After join
```

**Explanation:**
- `t.start()` starts the thread (which sleeps for 200ms).
- "Before join" prints immediately (main thread).
- `t.join()` blocks the main thread until thread `t` completes.
- After `t` finishes (printing "Thread finished"), `join()` returns.
- "After join" prints last.
- `join()` is the simplest way to wait for a thread to complete.

**Key point:** "After join" will ALWAYS print after "Thread finished" because `join()` guarantees this ordering.

**Interview Tip:** "`join()` blocks the calling thread until the target thread completes. It establishes a happens-before relationship."

</details>

---

## Snippet 9 — AtomicInteger vs synchronized int 🟡

**What does this code print?**

```java
import java.util.concurrent.atomic.AtomicInteger;

public class Main {
    static AtomicInteger count = new AtomicInteger(0);

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) count.incrementAndGet();
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) count.incrementAndGet();
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Count: " + count.get());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Count: 20000
```

**Explanation:**
- `AtomicInteger.incrementAndGet()` is an **atomic** operation using CAS (Compare-And-Swap) at the hardware level.
- Unlike `count++`, there is no read-modify-write race condition.
- Both threads increment safely, and the final result is always `20000`.
- `AtomicInteger` is faster than `synchronized` for simple atomic operations because it avoids lock overhead.

| Approach | Thread-Safe | Performance |
|---|---|---|
| `int count; count++` | ❌ | Fastest but wrong |
| `synchronized { count++ }` | ✅ | Lock overhead |
| `AtomicInteger.incrementAndGet()` | ✅ | CAS, lock-free |
| `LongAdder.increment()` | ✅ | Best for high contention |

**Interview Tip:** "`AtomicInteger` uses CAS (lock-free) for atomic operations. It's more efficient than `synchronized` for single-variable atomicity. For high contention, use `LongAdder`."

</details>

---

## Snippet 10 — CompletableFuture Exception 🔴

**What does this code print?**

```java
import java.util.concurrent.CompletableFuture;

public class Main {
    public static void main(String[] args) {
        CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
            throw new RuntimeException("Oops");
        });

        CompletableFuture<String> handled = future
            .thenApply(val -> val.toUpperCase())
            .exceptionally(ex -> "Recovered: " + ex.getMessage());

        System.out.println(handled.join());
    }
}
```

<details>
<summary>Answer</summary>

**Output:**
```
Recovered: java.lang.RuntimeException: Oops
```

**Explanation:**
- `supplyAsync` throws a `RuntimeException`. The future completes exceptionally.
- `thenApply` is **skipped** because the input future completed with an exception.
- `exceptionally` catches the exception and provides a fallback value.
- Note: The exception message includes the full exception class name because `exceptionally` receives a `CompletionException` wrapping the original cause. `getMessage()` includes the wrapped exception's `toString()`.
- **Chain behavior:** If the upstream future fails, `thenApply`/`thenCompose` stages are skipped, and the exception propagates until `exceptionally` or `handle` catches it.

**Interview Tip:** "`thenApply` is skipped on exception, `exceptionally` recovers. Use `handle(val, ex)` to process both success and failure in one callback."

</details>

---

## Quick Review Table

| # | Concept Tested | Key Rule |
|---|---|---|
| 1 | run() vs start() | `run()` = normal call, `start()` = new thread |
| 2 | Thread ordering | Non-deterministic, never assume order |
| 3 | volatile visibility | Without volatile, writes may not be visible across threads |
| 4 | count++ race condition | Read-modify-write is not atomic |
| 5 | Deadlock | Different lock ordering → deadlock |
| 6 | synchronized on new Object | Each call gets a different lock — no protection |
| 7 | wait() without synchronized | IllegalMonitorStateException |
| 8 | Thread.join() | Blocks until target thread completes |
| 9 | AtomicInteger | Lock-free CAS-based atomic operations |
| 10 | CompletableFuture exception | `thenApply` skipped, `exceptionally` recovers |
