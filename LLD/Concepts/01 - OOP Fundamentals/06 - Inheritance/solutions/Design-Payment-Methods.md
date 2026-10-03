# Design Payment Methods (Inheritance)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Inheritance
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-payment-methods)

### Problem

Design a set of payment methods that share common behaviour but differ in how they charge. Use
**inheritance** to put the shared workflow in a base class and let each method supply the parts that
differ.

### Approach — Template Method via inheritance

- `PaymentMethod` (abstract) holds shared fields + a `final` `process()` skeleton.
- Subclasses implement the abstract `authorize()` / `charge()` steps.

### Java Solution

```java
// Base class — shared state and workflow (is-a)
public abstract class PaymentMethod {

    protected final String id;

    protected PaymentMethod(String id) { this.id = id; }

    /** Fixed workflow shared by all payment methods. */
    public final String process(double amount) {
        validate(amount);                       // common step
        authorize();                            // subclass step
        charge(amount);                         // subclass step
        return receipt(amount);                 // common step
    }

    private void validate(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("amount must be > 0");
    }
    private String receipt(double amount) {
        return id + " charged " + amount;
    }

    protected abstract void authorize();
    protected abstract void charge(double amount);
}

class CreditCard extends PaymentMethod {
    private final String last4;
    CreditCard(String last4) { super("card-" + last4); this.last4 = last4; }
    protected void authorize()          { System.out.println("Authorizing card " + last4); }
    protected void charge(double amt)   { System.out.println("Charging card " + last4 + " " + amt); }
}

class Upi extends PaymentMethod {
    private final String handle;
    Upi(String handle) { super("upi-" + handle); this.handle = handle; }
    protected void authorize()          { System.out.println("Authorizing UPI " + handle); }
    protected void charge(double amt)   { System.out.println("Charging UPI " + handle + " " + amt); }
}
```

**Usage**
```java
PaymentMethod card = new CreditCard("4242");
card.process(499.0);   // shared validate → authorize → charge → receipt

PaymentMethod upi = new Upi("alice@bank");
upi.process(120.0);
```

### Design points
- **Shared code in the base** — validation and receipt live in `PaymentMethod`.
- **Varying steps abstract** — `authorize`/`charge` differ per method.
- **`final process`** — subclasses cannot break the workflow order.
- **Appropriate use of is-a** — a `CreditCard` *is-a* `PaymentMethod`.

**Complexity:** O(1) per payment · Space O(1)

---
#oop #inheritance #lld #practice