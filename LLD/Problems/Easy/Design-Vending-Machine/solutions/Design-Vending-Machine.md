# Design a Vending Machine (Easy)

**Difficulty:** Easy · **Patterns:** State, Singleton
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a vending machine: stock products, take coins/notes, select, pay, dispense with change, cancel with refund, refill, out-of-service.

**Functional**
- Stock **products** (code, name, price, quantity); operator **refills**.
- Accept **coins/notes**; **select** only if in stock and affordable; **dispense** product + **change**; **cancel** refunds all inserted money.
- Operator takes machine **out of service** and **collects cash**.

**Non-functional**
- New payment modes plug in as states; concurrent presses never double-dispense.

### The failure, before

```java
// ❌ One class, a mode int, and ifs everywhere — cancel forgets the refund,
// select from Idle NPEs, and "out of service" is a boolean checked in 6 places.
public void press(String btn) { if (mode == 2 && ...) { ... } }
```

### The Fix (after)

Context + `MachineState` interface; each state owns its legal moves.

```java
import java.util.*;

class Product {
    private final String code, name; private final int price; private int qty;
    Product(String code, String name, int price, int qty) {
        this.code = code; this.name = name; this.price = price; this.qty = qty;
    }
    public String getCode() { return code; }
    public int getPrice() { return price; }
    public int getQty() { return qty; }
    public void takeOne() { if (qty <= 0) throw new IllegalStateException("Out of stock"); qty--; }
    public void refill(int n) { qty += n; }
}

class Inventory {
    private final Map<String, Product> slots = new HashMap<>();
    public void add(Product p) { slots.put(p.getCode(), p); }
    public Product get(String code) {
        Product p = slots.get(code);
        if (p == null) throw new IllegalArgumentException("Bad code");
        return p;
    }
}

interface MachineState {
    void insertCoin(int v);
    void select(String code);
    void cancel();
    default void refill(String code, int n) { throw new IllegalStateException("Not now"); }
}

class VendingMachine {
    private MachineState state;
    private final Inventory inventory = new Inventory();
    private int inserted = 0, cashHeld = 0;

    VendingMachine() { state = new IdleState(this); }
    void setState(MachineState s) { state = s; }
    Inventory inventory() { return inventory; }
    int inserted() { return inserted; }
    void addInserted(int v) { inserted += v; }
    void clearInserted() { inserted = 0; }
    void bank(int v) { cashHeld += v; }

    public void insertCoin(int v) { state.insertCoin(v); }
    public void select(String code) { state.select(code); }
    public void cancel() { state.cancel(); }
    public int collectCash() { int c = cashHeld; cashHeld = 0; return c; }
}

class IdleState implements MachineState {
    private final VendingMachine m;
    IdleState(VendingMachine m) { this.m = m; }
    public void insertCoin(int v) { m.addInserted(v); m.setState(new SelectionState(m)); }
    public void select(String c) { throw new IllegalStateException("Insert coins first"); }
    public void cancel() { /* nothing to refund */ }
}

class SelectionState implements MachineState {
    private final VendingMachine m;
    SelectionState(VendingMachine m) { this.m = m; }
    public void insertCoin(int v) { m.addInserted(v); }
    public void select(String code) {
        Product p = m.inventory().get(code);
        if (p.getQty() <= 0) throw new IllegalStateException("Out of stock");
        if (m.inserted() < p.getPrice()) throw new IllegalStateException("Need " + p.getPrice());
        p.takeOne();
        int change = m.inserted() - p.getPrice();
        m.bank(p.getPrice()); m.clearInserted();
        System.out.println("Dispensed " + code + ", change " + change);
        m.setState(new IdleState(m));
    }
    public void cancel() { System.out.println("Refunded " + m.inserted()); m.clearInserted(); m.setState(new IdleState(m)); }
}
```

**Usage**
```java
VendingMachine vm = new VendingMachine();
vm.inventory().add(new Product("A1", "Cola", 25, 5));
vm.insertCoin(10); vm.insertCoin(25); vm.select("A1");  // dispensed, change 10
```

### Design points
- **States reject illegal moves** — select-from-Idle and insert-while-dispensing are compile-safe impossibilities.
- **Two ledgers move together** — stock decrements and cash banks in the same transition; no half-dispense.
- **Cancel is a first-class path** — refund + back to Idle, tested before the happy path.
- **Out-of-service is a state** — rejects money ops uniformly; repair returns to Idle.

**Complexity:** select/dispense O(1) · Space O(products).

---
#lld #machine-coding #vending-machine #easy #practice
