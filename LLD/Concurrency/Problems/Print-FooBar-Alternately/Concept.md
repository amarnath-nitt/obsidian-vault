# Print FooBar Alternately — Concept

## What Is It?

Two threads share one `FooBar` instance: thread A calls `foo(printFoo)`, thread B calls
`bar(printBar)`. Coordinate them so the output is `foobar` repeated exactly `n` times.

| | |
|---|---|
| **Pattern** | Signaling / turn alternation — a *two-state* version of Print in Order |
| **Core** | one boolean turn flag + `while` wait loop + `notifyAll()` |
| **Java** | `synchronized`, `wait/notifyAll` (or `Semaphore(0,1)` pair, `Lock`+`Condition`) |

---

## When to Use

> **Trigger keywords:** "alternately", "take turns", "A then B then A", "exactly n times each"

| Need | Move |
|------|------|
| Two parties strictly alternate | boolean turn flag (`fooTurn`) |
| More than two parties / ordered chain | integer `step` counter (see Signaling Pattern) |
| Over a shared counter 1..n | per-method turn predicate on `i` (see Zero Even Odd) |

---

## The shape

```java
public final class FooBar {
    private final int n;
    private final Object lock = new Object();
    private boolean fooTurn = true;             // durable state: whose turn is it?

    public FooBar(int n) { this.n = n; }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            synchronized (lock) {
                while (!fooTurn) lock.wait();   // WAIT until it is foo's turn
                printFoo.run();                 // "foo"
                fooTurn = false;                // hand over
                lock.notifyAll();               // wake bar — it re-checks its predicate
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            synchronized (lock) {
                while (fooTurn) lock.wait();    // WAIT until it is bar's turn
                printBar.run();                 // "bar"
                fooTurn = true;                 // hand back
                lock.notifyAll();
            }
        }
    }
}
```

**Why it works:** `fooTurn` is *state*, so whichever thread arrives first simply parks until the
other hands over. Each loop iteration is one rendezvous; `n` iterations give `foobar × n`.

---

## Notes

- The wait/notify must be **inside the per-iteration loop** — one handover per printed pair.
- `notifyAll()` (not `notify()`) — with only two waiters either works, but `notifyAll()` is the
  safe default when predicates differ.
- Alternative: two semaphores — `fooSem(1)`, `barSem(0)`; `foo` acquires `fooSem`, prints,
  releases `barSem`, and vice versa. Same alternation, no explicit flag.
- `n` iterations also bound the judge: each callback runs **exactly** `n` times.

---

## Common Mistakes

1. Waiting once outside the loop → only the first pair alternates, then chaos.
2. `if` instead of `while` → spurious wakeup prints out of turn.
3. Forgetting to flip the flag before notifying → the same side runs twice.
4. Creating threads inside the class — the judge supplies the threads; you coordinate the calls.

---

## Related

- [[../00 - Index|Concurrency Problems Index]]
- [[../../00 - Index|Concurrency Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../../Patterns/Signaling-Pattern/Concept|Signaling Pattern]] · [[../../Concepts/Condition-Variables/Concept|Condition Variables]]

---

#concurrency #foobar #lld #concept
