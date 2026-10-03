# Design an ATM Machine

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** State
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-atm-machine)

### Problem

An ATM moves through a well-defined lifecycle: idle → card inserted → authenticated → dispensing
cash, with a "no cash / out of service" state as well. Which operations are legal depends on the
current state (e.g. you cannot withdraw before authenticating). Model the ATM as a **state machine**.

### Approach — State

- **Context** = `Atm` — holds the current state and delegates operations to it.
- **States** = `Idle`, `HasCard`, `Authenticated`, `Dispensing`, `OutOfService`.
- Each state implements the legal behaviour and the transitions.

### Java Solution

```java
interface AtmState {
    void insertCard(Atm atm);
    void enterPin(Atm atm, int pin);
    void withdraw(Atm atm, int amount);
    void ejectCard(Atm atm);
}

class Atm {
    private AtmState state = new IdleState();
    private final int correctPin = 1234;
    private int balance = 1000;

    void setState(AtmState state) { this.state = state; System.out.println("→ " + state.getClass().getSimpleName()); }

    public void insertCard()      { state.insertCard(this); }
    public void enterPin(int pin) { state.enterPin(this, pin); }
    public void withdraw(int amt) { state.withdraw(this, amt); }
    public void ejectCard()       { state.ejectCard(this); }

    int balance() { return balance; }
    int correctPin() { return correctPin; }
    void debit(int amount) { balance -= amount; }
}

class IdleState implements AtmState {
    public void insertCard(Atm atm)      { atm.setState(new HasCardState()); }
    public void enterPin(Atm atm, int p) { System.out.println("Insert a card first"); }
    public void withdraw(Atm atm, int a) { System.out.println("Insert a card first"); }
    public void ejectCard(Atm atm)       { System.out.println("No card inserted"); }
}
class HasCardState implements AtmState {
    public void insertCard(Atm atm)      { System.out.println("Card already inserted"); }
    public void enterPin(Atm atm, int pin) {
        if (pin == atm.correctPin()) atm.setState(new AuthenticatedState());
        else { System.out.println("Wrong PIN"); atm.setState(new IdleState()); }
    }
    public void withdraw(Atm atm, int a) { System.out.println("Enter your PIN first"); }
    public void ejectCard(Atm atm)       { atm.setState(new IdleState()); }
}
class AuthenticatedState implements AtmState {
    public void insertCard(Atm atm)      { System.out.println("Card already inserted"); }
    public void enterPin(Atm atm, int p) { System.out.println("Already authenticated"); }
    public void withdraw(Atm atm, int amount) {
        if (amount > atm.balance()) { System.out.println("Insufficient funds"); return; }
        atm.setState(new DispensingState());
        atm.debit(amount);
        System.out.println("Dispensing " + amount);
        atm.setState(new AuthenticatedState());
    }
    public void ejectCard(Atm atm)       { atm.setState(new IdleState()); }
}
class DispensingState implements AtmState {
    public void insertCard(Atm atm)      { System.out.println("Please wait"); }
    public void enterPin(Atm atm, int p) { System.out.println("Please wait"); }
    public void withdraw(Atm atm, int a) { System.out.println("Please wait"); }
    public void ejectCard(Atm atm)       { System.out.println("Please wait"); }
}
```

**Usage**
```java
Atm atm = new Atm();
atm.withdraw(100);        // "Insert a card first"
atm.insertCard();         // → HasCardState
atm.enterPin(1234);       // → AuthenticatedState
atm.withdraw(300);        // → DispensingState → "Dispensing 300" → back to Authenticated
```

### Design points
- **Behaviour depends on state** — illegal actions are rejected by the current state, not by `if`s in the ATM.
- **Transitions inside states** — each state decides what comes next.
- **Intent methods** — the API is `insertCard`/`enterPin`/`withdraw`, never `setState(...)`.

**Complexity:** O(1) per operation · Space O(1)

---
#state #lld #practice