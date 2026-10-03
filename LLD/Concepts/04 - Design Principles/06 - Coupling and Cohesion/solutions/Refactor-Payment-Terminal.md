# Refactor Payment Terminal (Coupling & Cohesion)

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Principle:** Coupling & Cohesion
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-payment-terminal)

### Problem

A payment terminal is tightly coupled to concrete gateway classes — it `new`s a specific gateway,
duplicating retry/logging logic per gateway — and mixes payment orchestration with gateway-specific
details. Apply **low coupling, high cohesion**.

### The Smell (before)

```java
// ❌ Terminal is glued to concrete gateways and repeats cross-cutting logic
class PaymentTerminal {
    boolean charge(String provider, double amount) {
        if (provider.equals("stripe")) {
            var gateway = new StripeGateway();
            System.out.println("log: stripe " + amount);      // logging duplicated
            return gateway.charge(amount);
        } else if (provider.equals("paypal")) {
            var gateway = new PayPalGateway();
            System.out.println("log: paypal " + amount);      // logging duplicated
            return gateway.charge(amount);
        }
        throw new IllegalArgumentException("unknown provider");
    }
}
class StripeGateway { boolean charge(double amount) { return true; } }
class PayPalGateway { boolean charge(double amount) { return true; } }
```

### The Fix (after)

```java
import java.util.*;

// Low coupling: the terminal depends on this abstraction
interface PaymentGateway {
    String provider();
    boolean charge(double amount);
}

class StripeGateway implements PaymentGateway {
    public String provider() { return "stripe"; }
    public boolean charge(double amount) { System.out.println("Stripe charge " + amount); return true; }
}
class PayPalGateway implements PaymentGateway {
    public String provider() { return "paypal"; }
    public boolean charge(double amount) { System.out.println("PayPal charge " + amount); return true; }
}

// High cohesion: this class only orchestrates a charge with retry + logging
class PaymentTerminal {
    private static final int MAX_ATTEMPTS = 3;
    private final Map<String, PaymentGateway> gateways = new HashMap<>();

    void register(PaymentGateway gateway) { gateways.put(gateway.provider(), gateway); }

    boolean charge(String provider, double amount) {
        PaymentGateway gateway = gateways.get(provider);
        if (gateway == null) throw new IllegalArgumentException("Unknown provider: " + provider);

        for (int attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
            System.out.println("log: " + provider + " attempt " + attempt + " amount " + amount);
            if (gateway.charge(amount)) return true;           // single place for retry/logging
        }
        return false;
    }
}
```

**Usage**
```java
PaymentTerminal terminal = new PaymentTerminal();
terminal.register(new StripeGateway());
terminal.register(new PayPalGateway());

terminal.charge("stripe", 49.99);
```

### Design points
- **Low coupling** — the terminal knows only `PaymentGateway`.
- **High cohesion** — retry + logging lives in one place, not duplicated per provider.
- **No `switch`/`if-else`** — a new gateway registers itself (OCP).
- **Testable** — a stub gateway can simulate failures to exercise the retry loop.

**Complexity:** O(attempts) per charge · Space O(gateways)

---
#design-principles #coupling #cohesion #lld #practice