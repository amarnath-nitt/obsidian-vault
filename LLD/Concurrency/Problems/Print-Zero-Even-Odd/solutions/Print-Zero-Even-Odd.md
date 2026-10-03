# Print Zero Even Odd (Ordering)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Pattern:** Signaling over a shared counter
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/print-zero-even-odd)

### Problem

```java
class ZeroEvenOdd {
    ZeroEvenOdd(int n);
    void zero(IntConsumer printNumber);   // may output only 0
    void even(IntConsumer printNumber);   // may output only even numbers
    void odd(IntConsumer printNumber);    // may output only odd numbers
}
```

Three threads share one instance. Coordinate them so the callback sequence is
`0,1,0,2,0,3,…,0,n` (`1 <= n <= 1000`). The judge creates the object, starts all three
threads, and calls each method once — you coordinate, you don't create threads.

Example: `n = 2` → `0102`.

### The failure, before

```java
// ❌ No coordination: three threads race; zeros clump, numbers repeat or skip,
// and even may print odd's value
public void zero(IntConsumer p) { for (int i = 1; i <= n; i++) p.accept(0); }
public void even(IntConsumer p) { for (int i = 2; i <= n; i += 2) p.accept(i); }
public void odd(IntConsumer p)  { for (int i = 1; i <= n; i += 2) p.accept(i); }
```

### The Fix (after)

A **`zeroTurn` flag + `current` cursor** + `while` + `notifyAll()`, all under one lock.

```java
public class ZeroEvenOdd {
    private final int n;
    private final Object lock = new Object();
    private int current = 1;                 // next number to emit
    private boolean zeroTurn = true;         // zero prints before every number

    public ZeroEvenOdd(int n) { this.n = n; }

    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i++) {
            synchronized (lock) {
                while (!zeroTurn) lock.wait();
                printNumber.accept(0);
                zeroTurn = false;            // hand over to the number side
                lock.notifyAll();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            synchronized (lock) {
                while (zeroTurn || current % 2 != 0) lock.wait();  // my turn AND my parity
                printNumber.accept(current++);
                zeroTurn = true;             // hand back to zero
                lock.notifyAll();
            }
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            synchronized (lock) {
                while (zeroTurn || current % 2 == 0) lock.wait();  // my turn AND my parity
                printNumber.accept(current++);
                zeroTurn = true;
                lock.notifyAll();
            }
        }
    }
}
```

**Usage**
```java
ZeroEvenOdd z = new ZeroEvenOdd(2);
// Thread A: z.zero(print); Thread B: z.even(print); Thread C: z.odd(print);
// callback sequence: 0,1,0,2
```

### Design points
- **Two-clause predicates** — `zeroTurn` gates *whose side*, `current % 2` gates *which thread*
  on the number side. Drop either clause and the wrong thread prints.
- **Only the number side advances `current`** — `zero` flips the flag but never the cursor.
- **Loop bounds are the contract** — even iterates `2,4,…≤n`, odd iterates `1,3,…≤n`; with odd
  `n` the even thread simply runs fewer times and exits.
- **`while`, not `if`** — a spurious wakeup must re-park, not emit out of sequence.
- **Flip both fields before `notifyAll()`, under the same lock** — woken threads see the new
  `(zeroTurn, current)` pair atomically.

**Complexity:** O(n) callbacks total, O(1) per callback · Space O(1).

---
#concurrency #zero-even-odd #lld #practice
