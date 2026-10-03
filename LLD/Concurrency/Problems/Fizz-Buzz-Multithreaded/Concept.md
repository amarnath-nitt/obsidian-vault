# Fizz Buzz Multithreaded — Concept

## What Is It?

Four threads share one `FizzBuzz` instance and produce the FizzBuzz sequence 1..n: thread A
(`fizz`) outputs `fizz` for numbers divisible by 3 but not 5; thread B (`buzz`) for 5 but not 3;
thread C (`fizzbuzz`) for both; thread D (`number`) for the rest. Synchronize the four methods
so every value 1..n is produced exactly once, in order.

| | |
|---|---|
| **Pattern** | Signaling / per-value dispatch over a shared cursor |
| **Core** | one `int current` cursor + a predicate per method + `notifyAll()` |
| **Java** | `synchronized`, `wait/notifyAll` |

---

## When to Use

> **Trigger keywords:** "four threads", "each value exactly once", "only this method may handle X"

| Need | Move |
|------|------|
| Two parties alternate | boolean flag (see FooBar) |
| N parties over a counter with parity roles | cursor + flag (see Zero Even Odd) |
| **N parties with disjoint value sets** | **cursor + one predicate per method** — this package |

---

## The shape

```java
public final class FizzBuzz {
    private final int n;
    private final Object lock = new Object();
    private int current = 1;                        // next value to emit, 1..n

    public FizzBuzz(int n) { this.n = n; }

    public void fizz(Runnable printFizz) throws InterruptedException {
        while (true) {
            synchronized (lock) {
                while (current <= n && !isFizz(current)) lock.wait();  // wait for MY values
                if (current > n) { lock.notifyAll(); return; }        // done — release others
                printFizz.run();
                current++;                          // advance the shared cursor
                lock.notifyAll();                   // everyone re-checks
            }
        }
    }
    // buzz / fizzbuzz / number: same loop, only the predicate differs.

    private static boolean isFizz(int i)     { return i % 3 == 0 && i % 5 != 0; }
    private static boolean isBuzz(int i)     { return i % 5 == 0 && i % 3 != 0; }
    private static boolean isFizzBuzz(int i) { return i % 15 == 0; }
}
```

**Why it works:** `current` is the single source of truth — at any moment exactly one of the
four predicates is true, so exactly one thread proceeds while the other three park. The thread
that prints advances the cursor, handing the turn to whoever owns the next value.

---

## Notes

- The loop is `while (true)` with an **exit check inside the lock** — a fixed `for` bound can't
  work because no thread knows in advance how many of the `n` values are its own.
- **Every exit path must `notifyAll()` first** — otherwise the remaining threads sleep forever
  after the last value is emitted.
- `number`'s predicate is the negation of the other three: not divisible by 3 nor 5.
- `n ≤ 50`, so throughput is irrelevant — clarity of the predicate is what gets marked.

---

## Common Mistakes

1. `for` loop with a guessed count → a thread exits early and its values never print.
2. Returning without notifying → the other three threads hang after the last value.
3. Checking the predicate outside the lock → two threads both see "mine" and double-emit.
4. `if` instead of `while` → spurious wakeup emits the wrong value.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Print-Zero-Even-Odd/Concept|Zero Even Odd]] · [[../../Patterns/Signaling-Pattern/Concept|Signaling Pattern]]

---

#concurrency #fizzbuzz #lld #concept
