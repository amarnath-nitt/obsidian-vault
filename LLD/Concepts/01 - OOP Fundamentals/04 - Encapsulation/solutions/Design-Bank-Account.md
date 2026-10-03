# Design Bank Account (Encapsulation)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Encapsulation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-bank-account)

### Problem

Design a `BankAccount` with a balance that can only change through **valid** operations. Callers may
deposit and withdraw, but must never be able to set the balance directly or drive it negative. The
class enforces its own invariants.

### Approach

- Keep `balance` **private** — no public setter.
- Expose `deposit` / `withdraw` that validate inputs and update state.
- Reject invalid operations rather than silently corrupting state.

### Java Solution

```java
public class BankAccount {

    private final String owner;
    private double balance;                    // private — never exposed for writing

    public BankAccount(String owner, double openingBalance) {
        if (owner == null || owner.isBlank()) throw new IllegalArgumentException("owner required");
        if (openingBalance < 0) throw new IllegalArgumentException("opening balance must be >= 0");
        this.owner = owner;
        this.balance = openingBalance;
    }

    public void deposit(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("deposit must be > 0");
        balance += amount;
    }

    /** Returns true if the withdrawal succeeded. */
    public boolean withdraw(double amount) {
        if (amount <= 0 || amount > balance) return false;   // invariant: never negative
        balance -= amount;
        return true;
    }

    public double balance() { return balance; }              // read-only access
}
```

**Usage**
```java
BankAccount acc = new BankAccount("Alice", 100);
acc.deposit(50);          // balance 150
acc.withdraw(30);         // true, balance 120
acc.withdraw(999);        // false — insufficient, balance unchanged
acc.balance();            // 120
```

### Design points
- **No public setter** — `balance` cannot be assigned from outside.
- **Invariants enforced** — deposits must be positive; withdrawals cannot overdraw.
- **Controlled failure** — invalid input throws; an over-draw simply returns `false`.

**Complexity:** O(1) per operation · Space O(1)

---
#oop #encapsulation #lld #practice