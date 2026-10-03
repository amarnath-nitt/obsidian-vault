# Design ATM (Medium)

**Difficulty:** Medium · **Patterns:** State, Chain of Responsibility, Singleton
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design an ATM: card + PIN auth, balance/withdraw/deposit/PIN-change, cash dispenser with denominations, operator refill.

**Functional**
- Authenticate by **card + PIN** (3 tries → card retained); support **balance**, **withdraw**, **deposit**, **PIN change**.
- Withdrawal checks **account balance** AND **cassette cash**; dispenses in denominations.
- Operator **refills cash** and takes the machine **out of service**.

**Non-functional**
- New transaction types plug in as handlers; concurrent ATMs on one account must not double-spend.

### The failure, before

```java
// ❌ One class, a screen int, and ifs — withdraw checks balance but not cassette,
// deposit credits before the envelope arrives, out-of-service is a boolean in 6 places.
public void press(String btn) { if (screen == 3 && ...) { balance -= amt; /* cash later? */ } }
```

### The Fix (after)

Context + `ATMState` screens + bank ledger + cassette dispenser.

```java
import java.util.*;

class Account {
    private final String no; private int pin; private long balance;
    Account(String no, int pin, long balance) { this.no = no; this.pin = pin; this.balance = balance; }
    public boolean checkPin(int p) { return pin == p; }
    public long balance() { return balance; }
    public void debit(long a) {
        if (balance < a) throw new IllegalStateException("Insufficient funds");
        balance -= a;
    }
    public void credit(long a) { balance += a; }
}

class CashDispenser {
    private final Map<Integer, Integer> notes = new TreeMap<>(Comparator.reverseOrder());
    CashDispenser() { notes.put(2000, 10); notes.put(500, 20); notes.put(100, 50); }
    public boolean canDispense(long amt) {
        long rest = amt;
        for (var e : notes.entrySet()) rest -= Math.min(rest / e.getKey(), e.getValue()) * e.getKey();
        return rest == 0;
    }
    public Map<Integer, Integer> dispense(long amt) {
        if (!canDispense(amt)) throw new IllegalStateException("Cannot dispense " + amt);
        Map<Integer, Integer> out = new LinkedHashMap<>();
        for (var e : notes.entrySet()) {
            long use = Math.min(amt / e.getKey(), e.getValue());
            if (use > 0) { out.put(e.getKey(), (int) use); e.setValue(e.getValue() - (int) use); amt -= use * e.getKey(); }
        }
        return out;
    }
    public void refill(int denom, int n) { notes.merge(denom, n, Integer::sum); }
}

interface ATMState {
    void insertCard(String card);
    void enterPin(int pin);
    void eject();
}

class IdleState implements ATMState {
    private final ATM atm;
    IdleState(ATM atm) { this.atm = atm; }
    public void insertCard(String card) { atm.setCard(card); atm.setState(new CardInserted(atm, atm.bank())); }
    public void enterPin(int pin) { throw new IllegalStateException("Insert a card first"); }
    public void eject() { /* nothing to eject */ }
}

class CardInserted implements ATMState {
    private final ATM atm; private final Map<String, Account> bank; private int tries = 0;
    CardInserted(ATM atm, Map<String, Account> bank) { this.atm = atm; this.bank = bank; }
    public void insertCard(String card) { throw new IllegalStateException("Card already inserted"); }
    public void enterPin(int pin) {
        Account acc = bank.get(atm.card());
        if (acc == null || !acc.checkPin(pin)) {
            if (++tries == 3) { System.out.println("Card retained"); atm.setCard(null); atm.setState(atm.idle()); }
            else System.out.println("Wrong PIN — tries left: " + (3 - tries));
            return;
        }
        atm.setAccount(acc);
        atm.setState(atm.authenticated());
    }
    public void eject() { atm.setCard(null); atm.setState(atm.idle()); }
}

class Authenticated implements ATMState {
    private final ATM atm;
    Authenticated(ATM atm) { this.atm = atm; }
    public void insertCard(String card) { throw new IllegalStateException("Session already active"); }
    public void enterPin(int pin) { throw new IllegalStateException("Already authenticated"); }
    public void eject() { atm.setCard(null); atm.setAccount(null); atm.setState(atm.idle()); }
}

class OutOfService implements ATMState {
    private final ATM atm;
    OutOfService(ATM atm) { this.atm = atm; }
    public void insertCard(String card) { throw new IllegalStateException("Out of service"); }
    public void enterPin(int pin) { throw new IllegalStateException("Out of service"); }
    public void eject() { /* nothing to eject */ }
    void refill(int denom, int n) { atm.dispenser().refill(denom, n); atm.setState(atm.idle()); }
}

abstract class Transaction {                       // chain: validate → execute
    protected final Account account;
    Transaction(Account account) { this.account = account; }
    final void run() { validate(); execute(); }
    protected abstract void validate();
    protected abstract void execute();
}

class WithdrawTx extends Transaction {
    private final CashDispenser dispenser; private final long amount;
    WithdrawTx(Account account, CashDispenser dispenser, long amount) {
        super(account); this.dispenser = dispenser; this.amount = amount;
    }
    protected void validate() {
        if (account.balance() < amount) throw new IllegalStateException("Insufficient funds");
        if (!dispenser.canDispense(amount)) throw new IllegalStateException("ATM cannot dispense " + amount);
    }
    protected void execute() {
        account.debit(amount);
        try { System.out.println("Dispensed: " + dispenser.dispense(amount)); }
        catch (RuntimeException e) { account.credit(amount); throw e; }   // compensate
    }
}

class DepositTx extends Transaction {
    private final long amount;
    DepositTx(Account account, long amount) { super(account); this.amount = amount; }
    protected void validate() { if (amount <= 0) throw new IllegalArgumentException("Amount must be positive"); }
    protected void execute() { account.credit(amount); }
}

class ATM {
    private final Map<String, Account> bank; private final CashDispenser dispenser = new CashDispenser();
    private ATMState state = new IdleState(this);
    private String card; private Account account;

    ATM(Map<String, Account> bank) { this.bank = bank; }

    void insertCard(String c) { state.insertCard(c); }
    void enterPin(int pin) { state.enterPin(pin); }
    void eject() { state.eject(); }
    void withdraw(long amount) { requireSession(); new WithdrawTx(account, dispenser, amount).run(); }
    void deposit(long amount) { requireSession(); new DepositTx(account, amount).run(); }
    long balance() { requireSession(); return account.balance(); }

    private void requireSession() {
        if (!(state instanceof Authenticated)) throw new IllegalStateException("Not authenticated");
    }
    Map<String, Account> bank() { return bank; }
    CashDispenser dispenser() { return dispenser; }
    String card() { return card; }
    void setCard(String c) { card = c; }
    void setAccount(Account a) { account = a; }
    void setState(ATMState s) { state = s; }
    ATMState idle() { return new IdleState(this); }
    ATMState authenticated() { return new Authenticated(this); }
}
```

**Usage**
```java
Map<String, Account> bank = new HashMap<>();
bank.put("4111-1111", new Account("ACC-1", 1234, 5_000));
ATM atm = new ATM(bank);
atm.insertCard("4111-1111");
atm.enterPin(1234);
atm.deposit(2_000);
atm.withdraw(2_500);                    // dispenses 2000 + 500 — both ledgers move together
System.out.println(atm.balance());      // 4500
```

### Design points
- **Three tries, then retained** — the PIN counter lives in `CardInserted`; the third failure retains the card and drops to Idle.
- **Two ledgers, one boundary** — withdraw validates balance **and** cassette, then debits and dispenses with a compensating credit on failure.
- **Screens are states** — an operation illegal for the current screen is rejected structurally, not by scattered `if`s.
- **Transactions are chain steps** — `validate → execute` in the base class; new operation types extend, the ATM never changes.

**Complexity:** every operation O(1) — greedy dispense over a fixed denomination set.

---
#lld #machine-coding #atm #medium #practice
