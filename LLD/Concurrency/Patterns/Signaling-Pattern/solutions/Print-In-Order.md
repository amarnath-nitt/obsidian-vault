# Print in Order (Signaling)

**Source:** AlgoMaster · Concurrency Practice · **easy** · **Pattern:** Signaling
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/print-in-order)

### Problem

```java
class Foo {
    void first(Runnable printFirst);    // prints "first"
    void second(Runnable printSecond);  // prints "second"
    void third(Runnable printThird);    // prints "third"
}
```

Three threads call the three methods **in any order**. The callbacks must run in the order
`first → second → third`, each exactly once. The judge starts the threads; you coordinate them, you
don't create them. Waiting must not busy-wait, and an interrupted wait must exit **without**
invoking its callback.

### The failure, before

```java
// ❌ One-shot flag: if first() runs before second() starts waiting, the signal is lost
private boolean firstDone = false;
void second(Runnable r) {
    while (!firstDone) { /* spin or wait with no persistent state */ }
    r.run();
}
```

### The Fix (after)

A **durable turn counter** + `while` + `notifyAll()`, all under one lock.

```java
public class Foo {
    private final Object lock = new Object();
    private int turn = 0;                       // 0 → wait for first, 1 → for second, 2 → for third

    public void first(Runnable printFirst) throws InterruptedException {
        synchronized (lock) {
            while (turn != 0) lock.wait();      // our turn is not yet
            printFirst.run();                   // "first"
            turn = 1;                           // advance durable state
            lock.notifyAll();                   // wake everyone; each re-checks its own turn
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        synchronized (lock) {
            while (turn != 1) lock.wait();
            printSecond.run();                  // "second"
            turn = 2;
            lock.notifyAll();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        synchronized (lock) {
            while (turn != 2) lock.wait();
            printThird.run();                   // "third"
            turn = 3;
            lock.notifyAll();                   // unblocks nothing further, but keeps the invariant
        }
    }
}
```

**Usage**
```java
Foo foo = new Foo();
// Thread A: foo.first(() -> print("first"));
// Thread B: foo.second(() -> print("second"));
// Thread C: foo.third(() -> print("third"));
// arrivalOrder = [3,1,2]  →  output: firstsecondthird
```

### Design points
- **State, not events** — `turn` records progress, so a signal that fired before a waiter arrived is
  never lost.
- **`while`, not `if`** — a wakeup whose `turn` isn't mine yet must park again.
- **Advance and notify under the same lock** — a waiter can't wake between the two and see stale state.
- **`notifyAll()`** — all three threads may be parked; each re-checks its own predicate.
- **No busy-wait** — `lock.wait()` parks the thread.
- **Interruption** — propagates out of `wait()`; the method exits before invoking its callback, so the
  sequence is never partially advanced.

**Complexity:** O(1) per method · Space O(1).

---
#concurrency #signaling #lld #practice
