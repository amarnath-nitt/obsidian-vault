# Print FooBar Alternately (Ordering)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Signaling / turn alternation
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/print-foobar-alternately)

### Problem

```java
class FooBar {
    FooBar(int n);
    void foo(Runnable printFoo);   // prints "foo"
    void bar(Runnable printBar);   // prints "bar"
}
```

Two threads share one instance: thread A calls `foo`, thread B calls `bar`. Produce `foobar`
exactly `n` times (`1 <= n <= 1000`). Each callback is thread-safe and must be invoked exactly
`n` times. The judge creates the object, starts both threads, and calls each method once — you
coordinate the calls, you don't create threads.

Example: `n = 1` → `foobar`.

### The failure, before

```java
// ❌ No coordination: whichever thread the scheduler prefers runs first
public void foo(Runnable printFoo) { for (int i = 0; i < n; i++) printFoo.run(); }
public void bar(Runnable printBar) { for (int i = 0; i < n; i++) printBar.run(); }
// output could be "foofoobarbar..." — interleaving decides, not you
```

### The Fix (after)

A **boolean turn flag** + `while` + `notifyAll()` **inside** the per-iteration loop.

```java
public class FooBar {
    private final int n;
    private final Object lock = new Object();
    private boolean fooTurn = true;                    // durable state: whose turn?

    public FooBar(int n) { this.n = n; }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            synchronized (lock) {
                while (!fooTurn) lock.wait();          // not my turn → park
                printFoo.run();                        // "foo"
                fooTurn = false;                       // hand over to bar
                lock.notifyAll();                      // wake bar; it re-checks
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            synchronized (lock) {
                while (fooTurn) lock.wait();           // not my turn → park
                printBar.run();                        // "bar"
                fooTurn = true;                        // hand back to foo
                lock.notifyAll();
            }
        }
    }
}
```

**Usage**
```java
FooBar fb = new FooBar(2);
// Thread A: fb.foo(() -> print("foo"));   Thread B: fb.bar(() -> print("bar"));
// output: foobarfoobar (each callback ran exactly 2 times)
```

### Design points
- **State, not events** — `fooTurn` survives early arrival; whoever comes first just waits.
- **Wait inside the loop** — one rendezvous per pair; waiting once outside breaks after pair #1.
- **`while`, not `if`** — a spurious wakeup must re-park, not print out of turn.
- **Flip before notify, under the same lock** — the woken thread observes the new turn.
- **`notifyAll()`** — safe default when the two waiters hold different predicates.
- **No threads created** — the judge owns the threads; the class only holds the flag.

**Complexity:** O(1) per callback · Space O(1).

---
#concurrency #foobar #lld #practice
