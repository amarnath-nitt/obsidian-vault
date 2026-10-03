# Design a Thread-Safe Inventory (Race Conditions)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Topic:** Race Conditions and Critical Sections
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-thread-safe-inventory)

### Problem

Design a reusable inventory supporting concurrent purchases and restocking without overselling or
losing updates.

```java
class ThreadSafeInventory {
    ThreadSafeInventory(int initialStock);
    boolean tryPurchase(int quantity, Runnable onPurchased);  // atomic check + subtract
    void   restock(int quantity);                             // never loses stock
    int    available();                                       // thread-safe snapshot
}
```

**Guarantees the judge checks:**
- `tryPurchase` atomically checks `stock >= quantity` and subtracts — no overselling, never negative
- `onPurchased` runs **exactly once** on success, **never** on rejection
- The stock is already decremented **when the callback begins**
- The callback must run **without holding the inventory lock** (so other operations progress)
- The method returns only after its own callback finishes
- All operations on one instance are **linearizable**

### The race, before

```java
// ❌ check-then-act, and the callback inside the lock
public boolean tryPurchase(int qty, Runnable onPurchased) {
    if (stock >= qty) {          // ← thread A and B both pass this
        stock -= qty;            // ← both subtract → oversell / negative
        onPurchased.run();       // ← callback under lock: blocks everyone
        return true;
    }
    return false;
}
```

Two threads read `stock = 5`, both see `5 >= 3`, both subtract → `stock = -1`.

### The Fix (after)

The **decision** and the **subtraction** are one critical section; the **callback** runs after the
lock is released but before the method returns.

```java
import java.util.concurrent.locks.ReentrantLock;

public final class ThreadSafeInventory {
    private final ReentrantLock lock = new ReentrantLock();
    private int stock;

    public ThreadSafeInventory(int initialStock) { this.stock = initialStock; }

    public boolean tryPurchase(int quantity, Runnable onPurchased) {
        lock.lock();
        boolean ok;
        try {
            ok = stock >= quantity;      // check  ┐ ONE critical section
            if (ok) stock -= quantity;   // act    ┘
        } finally {
            lock.unlock();               // release BEFORE the callback
        }

        if (!ok) return false;           // callback never runs on rejection
        try {
            onPurchased.run();           // stock already decremented
        } finally {
            // nothing to undo: the purchase is committed
        }
        return true;                     // returns only after its own callback
    }

    public void restock(int quantity) {
        lock.lock();
        try { stock += quantity; } finally { lock.unlock(); }
    }

    public int available() {
        lock.lock();
        try { return stock; } finally { lock.unlock(); }
    }
}
```

**Usage**
```java
ThreadSafeInventory inv = new ThreadSafeInventory(10);
inv.tryPurchase(3, () -> System.out.println("sold"));  // true
inv.tryPurchase(8, () -> System.out.println("sold"));  // false — no callback
inv.restock(5);
inv.available();                                        // 12
```

### Design points
- **Atomic check-then-act** — one lock acquisition covers both; no oversell.
- **Callback outside the lock** — other threads can purchase/restock while it runs, yet it still runs
  exactly once because the decision was already committed.
- **`finally` releases the lock** — an exception in the callback can't leave it held.
- **`try/finally` around the lock** — the original failure propagates after cleanup.
- **Linearizable** — every operation behaves as if it happened at one instant.

**Complexity:** O(1) per operation · Space O(1) — lock contention is the real cost, so the
critical section is kept to two integer operations.

---
#concurrency #race-condition #lld #practice
