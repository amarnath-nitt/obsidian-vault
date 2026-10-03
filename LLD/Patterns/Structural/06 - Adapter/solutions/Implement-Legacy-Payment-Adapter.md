# Implement a Legacy Payment Adapter

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Adapter
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/implement-legacy-payment-adapter)

### Problem

A checkout service is written against a modern `PaymentProcessor` interface (`pay(amount, currency)`
returning a `receiptId`). A **legacy** payment library exposes an older API
(`makePayment(cents, code)` returning a numeric transaction id, or `-1` on failure). Wrap the legacy
library in an adapter so the checkout can use it without knowing it is legacy.

### Approach

- **Target** = `PaymentProcessor` (what checkout expects).
- **Adaptee** = the legacy `LegacyPaymentGateway` (different names **and** units).
- **Adapter** translates: rupees → cents, currency → code, numeric id → string receipt, failure → exception.

### Java Solution

```java
// Target
interface PaymentProcessor {
    String pay(double amount, String currency);   // returns a receipt id
}

// Adaptee — the legacy library (do not modify)
class LegacyPaymentGateway {
    /** amount in cents; code like "USD"/"INR"; returns transaction id or -1 on failure. */
    long makePayment(long cents, String code) {
        if (cents <= 0) return -1;
        return 900_000 + cents;                    // simulate a txn id
    }
}

// Adapter
class LegacyPaymentAdapter implements PaymentProcessor {

    private final LegacyPaymentGateway legacy;

    LegacyPaymentAdapter(LegacyPaymentGateway legacy) { this.legacy = legacy; }

    @Override
    public String pay(double amount, String currency) {
        long cents = Math.round(amount * 100);                  // unit conversion
        long txn = legacy.makePayment(cents, currency.toUpperCase());
        if (txn < 0) throw new IllegalStateException("Legacy payment failed");
        return "LEGACY-" + txn;                                 // shape conversion
    }
}
```

**Client — unchanged, depends only on the Target**
```java
class Checkout {
    private final PaymentProcessor processor;
    Checkout(PaymentProcessor processor) { this.processor = processor; }

    void checkout(double amount, String currency) {
        String receipt = processor.pay(amount, currency);
        System.out.println("Paid " + amount + " " + currency + " → receipt " + receipt);
    }
}

// usage
new Checkout(new LegacyPaymentAdapter(new LegacyPaymentGateway())).checkout(499.99, "INR");
```

### Why it works
- **Translates three things** — method name, **units** (rupees ↔ cents), and return shape (id ↔ receipt).
- **Failures normalised** — the legacy `-1` becomes a clear exception the modern client understands.
- **No legacy type leaks** — `Checkout` never references `LegacyPaymentGateway`.

**Complexity:** O(1) per payment · Space O(1)

---
#adapter #payments #lld #practice