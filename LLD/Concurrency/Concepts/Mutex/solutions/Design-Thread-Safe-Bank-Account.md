# Design a Thread-Safe Bank Account (Mutex)

**Source:** AlgoMaster · Concurrency Practice · **medium** · **Topic:** Mutex (Mutual Exclusion)
🔗 [AlgoMaster problem](https://algomaster.io/practice/concurrency/design-thread-safe-bank-account)

### Problem

```java
class BankAccount {
    BankAccount(long initialBalance);
    void   deposit(long amount);
    boolean withdraw(long amount);   // returns false + leaves balance unchanged if insufficient
    long   getBalance();
}
```

**Guarantees:** every operation is **thread-safe and linearizable**; checking the balance and
subtracting a withdrawal must be **one atomic operation**; concurrent withdrawals must never make
the balance negative; different `BankAccount` instances must synchronize **independently**.

### The race, before

```java
// ❌ check-then-act across two calls
public synchronized boolean withdraw(long amount) {
    if (balance < amount) return false;   // looks safe — but balance is read again below?
    balance -= amount;
    return true;
}

// Worse, if written without synchronization:
if (balance >= amount) {        // A and B both see balance = 100, amount = 100
    balance -= amount;          // both subtract → balance = -100  ❌
    return true;
}
```

Two threads each read `balance = 100`, both pass `balance >= 100`, both subtract → `-100`.

### The Fix (after)

```java
public final class BankAccount {
    // Per-instance private monitor → different accounts never contend
    private final Object lock = new Object();
    private long balance;

    public BankAccount(long initialBalance) { this.balance = initialBalance; }

    public void deposit(long amount) {
        if (amount <= 0) throw new IllegalArgumentException("amount > 0");
        synchronized (lock) {
            balance += amount;
        }
    }

    public boolean withdraw(long amount) {
        if (amount <= 0) throw new IllegalArgumentException("amount > 0");
        synchronized (lock) {                 // ONE critical section:
            if (balance < amount) {           //   check
                return false;                 //   (no mutation on rejection)
            }
            balance -= amount;                //   act
            return true;
        }                                     // released on exit, including exceptions
    }

    public long getBalance() {
        synchronized (lock) {                 // reads are locked too — they must be consistent
            return balance;
        }
    }
}
```

**Usage**
```java
BankAccount account = new BankAccount(100);
account.deposit(50);        // balance = 150
account.withdraw(30);       // true  → 120
account.withdraw(150);      // false → still 120
account.getBalance();       // 120
```

### Design points
- **One atomic step** — the balance check and subtraction share a single critical section, so the
  balance can never go negative.
- **`private final Object lock` per instance** — accounts are independent; no false contention
  between two customers' accounts (and callers can't lock your monitor from outside).
- **`synchronized` block, not method** — makes explicit *which* state is protected; method-level
  `synchronized` would lock `this`, exposing the monitor to callers.
- **`getBalance()` is locked too** — an unlocked read could observe a torn/inconsistent value.
- **Linearizable** — every call appears to take effect at one instant.

**Complexity:** O(1) per operation · Space O(1) — cost is lock contention; the section is two
primitive operations wide.

---
#concurrency #mutex #lld #practice
