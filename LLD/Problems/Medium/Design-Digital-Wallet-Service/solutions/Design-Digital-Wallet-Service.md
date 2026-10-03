# Design a Digital Wallet Service (Medium)

**Difficulty:** Medium · **Patterns:** State, Command, Strategy
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a wallet service: create wallets, top up, transfer between wallets atomically, freeze/close, statements — with retry-safe transfers.

**Functional**
- Create wallets; top up, pay, transfer; balance + statement; freeze/unfreeze/close.
- Every movement writes two immutable ledger entries under one transfer reference; duplicate keys apply once.

**Non-functional**
- No double-spend, no half-applied transfer, no deadlock under opposed concurrent transfers.

### The failure, before

```java
// ❌ Two independent updates with no atomicity and no idempotency:
// a crash between the two lines loses money; a client retry charges twice.
// from.balance -= amount;
// to.balance += amount;   ← crash between these two → money vanished; retry → charged again
```

### The Fix (after)

Guarded wallets + one atomic transfer section + an idempotency set + a double-entry ledger.

```java
import java.util.*;

enum WalletStatus { ACTIVE, FROZEN, CLOSED }

class Wallet {
    final String id;
    private long balance;
    private WalletStatus status = WalletStatus.ACTIVE;

    Wallet(String id, long balance) { this.id = id; this.balance = balance; }

    void debit(long amount) {
        if (status != WalletStatus.ACTIVE) throw new IllegalStateException(id + " is " + status);
        if (balance < amount) throw new IllegalStateException("Insufficient balance in " + id);
        balance -= amount;
    }
    void credit(long amount) {
        if (status == WalletStatus.CLOSED) throw new IllegalStateException(id + " is closed");
        balance += amount;
    }
    void freeze() { status = WalletStatus.FROZEN; }
    void activate() { status = WalletStatus.ACTIVE; }
    void close() {
        if (balance != 0) throw new IllegalStateException("Move the balance out first");
        status = WalletStatus.CLOSED;
    }
    long balance() { return balance; }
    WalletStatus status() { return status; }
}

record LedgerEntry(String wallet, long delta, String ref, long at) {}

interface FeeStrategy { long fee(long amount); }

class WalletService {
    private final Map<String, Wallet> wallets = new HashMap<>();
    private final List<LedgerEntry> ledger = new ArrayList<>();
    private final Set<String> applied = new HashSet<>();     // idempotency keys
    private FeeStrategy fees = amount -> 0;
    private long clock = 0;

    void open(String id, long initial) { wallets.put(id, new Wallet(id, initial)); }
    void setFees(FeeStrategy f) { fees = f; }
    void freeze(String id) { wallets.get(id).freeze(); }
    void activate(String id) { wallets.get(id).activate(); }
    long balance(String id) { return wallets.get(id).balance(); }
    List<LedgerEntry> statement(String id) {
        return ledger.stream().filter(e -> e.wallet().equals(id)).toList();
    }

    synchronized void topUp(String id, long amount) {
        Wallet w = wallets.get(id);
        w.credit(amount);
        ledger.add(new LedgerEntry(id, +amount, "TOPUP-" + (++clock), clock));
    }

    synchronized void transfer(String fromId, String toId, long amount, String idemKey) {
        if (applied.contains(idemKey)) return;               // retry-safe: money moves once
        if (amount <= 0) throw new IllegalArgumentException("Amount must be positive");
        Wallet from = wallets.get(fromId), to = wallets.get(toId);
        if (from == null || to == null) throw new IllegalArgumentException("Unknown wallet");

        long fee = fees.fee(amount);
        from.debit(amount + fee);                            // throws → nothing applied yet
        to.credit(amount);

        long at = ++clock;
        ledger.add(new LedgerEntry(fromId, -(amount + fee), idemKey, at));
        ledger.add(new LedgerEntry(toId,   +amount,         idemKey, at));
        applied.add(idemKey);                                // only after both writes
    }
}
```

**Usage**
```java
WalletService svc = new WalletService();
svc.open("alice", 1_000);
svc.open("bob", 0);
svc.transfer("alice", "bob", 400, "tx-1");
svc.transfer("alice", "bob", 400, "tx-1");   // retry: ignored, no double charge
System.out.println(svc.statement("alice").size());   // 1 entry: -400
```

### Design points
- **Debit is self-guarding** — frozen or short wallets throw inside `Wallet`; no call site can skip the rule.
- **Idempotency checked first, recorded last** — a failed transfer stays retryable; a completed one applies exactly once.
- **Double-entry pairs** — both entries share the transfer key, so statements reconcile by reference.
- **One lock for the slice; order locks when sharding** — a global section is correct here; production locks per-wallet in id order to survive A→B / B→A deadlocks.

**Complexity:** transfer O(1) · statement O(ledger) (index per wallet to make it O(entries)).

---
#lld #machine-coding #wallet #medium #practice