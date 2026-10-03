# Fizz Buzz Multithreaded (Ordering)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Signaling / per-value dispatch
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/fizz-buzz-multithreaded)

### Problem

```java
class FizzBuzz {
    FizzBuzz(int n);
    void fizz(Runnable printFizz);           // i % 3 == 0 && i % 5 != 0
    void buzz(Runnable printBuzz);           // i % 5 == 0 && i % 3 != 0
    void fizzbuzz(Runnable printFizzBuzz);   // i % 15 == 0
    void number(IntConsumer printNumber);    // all remaining values
}
```

Four threads share one instance. Invoke the callbacks so every value 1..n (`1 <= n <= 50`) is
produced exactly once, in order. Each callback is thread-safe and must be called only for its
own values. The judge creates the object, starts all four threads, and calls each method once.

Example: `n = 15` → `[1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]`.

### The failure, before

```java
// ❌ No coordination: all four threads race over 1..n; values double-emit,
// go out of order, or never emit at all
public void fizz(Runnable p) { for (int i = 3; i <= n; i += 3) p.run(); }
// ... three more independent loops, no shared cursor
```

### The Fix (after)

A **shared `current` cursor** + **one predicate per method** + `while` + `notifyAll()`.

```java
public class FizzBuzz {
    private final int n;
    private final Object lock = new Object();
    private int current = 1;                              // next value to emit

    public FizzBuzz(int n) { this.n = n; }

    public void fizz(Runnable printFizz) throws InterruptedException {
        while (true) {
            synchronized (lock) {
                while (current <= n && !isFizz(current)) lock.wait();
                if (current > n) { lock.notifyAll(); return; }  // done — release the rest
                printFizz.run();
                current++;
                lock.notifyAll();
            }
        }
    }

    public void buzz(Runnable printBuzz) throws InterruptedException {
        while (true) {
            synchronized (lock) {
                while (current <= n && !isBuzz(current)) lock.wait();
                if (current > n) { lock.notifyAll(); return; }
                printBuzz.run();
                current++;
                lock.notifyAll();
            }
        }
    }

    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (true) {
            synchronized (lock) {
                while (current <= n && !isFizzBuzz(current)) lock.wait();
                if (current > n) { lock.notifyAll(); return; }
                printFizzBuzz.run();
                current++;
                lock.notifyAll();
            }
        }
    }

    public void number(IntConsumer printNumber) throws InterruptedException {
        while (true) {
            synchronized (lock) {
                while (current <= n && !isNumber(current)) lock.wait();
                if (current > n) { lock.notifyAll(); return; }
                printNumber.accept(current);
                current++;
                lock.notifyAll();
            }
        }
    }

    private static boolean isFizz(int i)     { return i % 3 == 0 && i % 5 != 0; }
    private static boolean isBuzz(int i)     { return i % 5 == 0 && i % 3 != 0; }
    private static boolean isFizzBuzz(int i) { return i % 15 == 0; }
    private static boolean isNumber(int i)   { return i % 3 != 0 && i % 5 != 0; }
}
```

**Usage**
```java
FizzBuzz fb = new FizzBuzz(15);
// four threads call fizz / buzz / fizzbuzz / number; callbacks fire in 1..15 order
```

### Design points
- **Disjoint predicates** — for every `current` exactly one of the four is true, so exactly one
  thread proceeds; double-emit is impossible by construction.
- **`while (true)` + in-lock exit** — no thread knows its own share upfront, so each loops until
  the cursor passes `n`.
- **Notify before every `return`** — the last value's notifier wakes the other three so they can
  observe `current > n` and exit instead of hanging.
- **Advance-then-notify under one lock** — woken threads test their predicate against the new
  cursor atomically.
- **`while`, not `if`** — a spurious wakeup re-parks instead of emitting the wrong value.

**Complexity:** O(n) callbacks total, O(1) work per value · Space O(1).

---
#concurrency #fizzbuzz #lld #practice
