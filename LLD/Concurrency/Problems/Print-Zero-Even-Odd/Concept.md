# Print Zero Even Odd — Concept

## What Is It?

Three threads share one `ZeroEvenOdd` instance: thread A calls `zero` (may output only `0`),
thread B calls `even` (only even numbers), thread C calls `odd` (only odd numbers). Coordinate
them so the sequence is `0, 1, 0, 2, 0, 3, …` through `n` — every number 1..n preceded by a zero.

| | |
|---|---|
| **Pattern** | Signaling / turn alternation over a shared counter |
| **Core** | one `int current` cursor + `while` wait loop + `notifyAll()` |
| **Java** | `synchronized`, `wait/notifyAll` |

---

## When to Use

> **Trigger keywords:** "three threads", "each number preceded by", "only this thread may output X"

| Need | Move |
|------|------|
| Two parties alternate | boolean flag (see FooBar) |
| N parties take turns over a counter | **integer cursor** — each method's predicate is a function of it |
| Four fixed roles over 1..n | per-value dispatch (see FizzBuzz) |

---

## The shape

```java
public final class ZeroEvenOdd {
    private final int n;
    private final Object lock = new Object();
    private int current = 1;                // next number to emit (1..n); even/odd decided by it
    private boolean zeroTurn = true;        // durable state: zero prints before every number

    public ZeroEvenOdd(int n) { this.n = n; }

    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i++) {
            synchronized (lock) {
                while (!zeroTurn) lock.wait();
                printNumber.accept(0);
                zeroTurn = false;           // hand over to whichever number is next
                lock.notifyAll();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            synchronized (lock) {
                while (zeroTurn || current % 2 != 0) lock.wait();  // wait for MY even value
                printNumber.accept(current++);
                zeroTurn = true;            // hand back to zero
                lock.notifyAll();
            }
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            synchronized (lock) {
                while (zeroTurn || current % 2 == 0) lock.wait();  // wait for MY odd value
                printNumber.accept(current++);
                zeroTurn = true;
                lock.notifyAll();
            }
        }
    }
}
```

**Why it works:** `zeroTurn` forces the `0` before every number; `current` tells *which* number
side may go, and its parity picks even vs odd. Each method loops exactly as many times as it
must print (`n` zeros, `n/2` evens, `ceil(n/2)` odds).

---

## Notes

- The predicate has **two clauses**: "is it the number side's turn?" AND "is the cursor mine?".
- `current` only advances on the number side — `zero` never touches it.
- Loop bounds matter: `even` iterates `2,4,6…≤n`, `odd` iterates `1,3,5…≤n`.
- Same rule as FooBar: the judge supplies the threads; you coordinate the three methods.

---

## Common Mistakes

1. Single-clause predicate (`while (zeroTurn)`) — even prints odd's number and vice versa.
2. Letting `zero` advance the cursor — numbers get skipped or duplicated.
3. Wrong loop bounds — printing evens up to `n` when `n` is odd emits a phantom number.
4. `if` instead of `while` → spurious wakeup breaks the `0102…` sequence.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../Print-FooBar-Alternately/Concept|FooBar]] · [[../../Patterns/Signaling-Pattern/Concept|Signaling Pattern]]

---

#concurrency #zero-even-odd #lld #concept
