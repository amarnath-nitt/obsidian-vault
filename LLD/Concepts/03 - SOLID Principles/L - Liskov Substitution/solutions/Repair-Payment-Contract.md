# Repair a Payment Contract (Liskov Substitution)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** Liskov Substitution
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/repair-payment-contract)

### Problem

A `RefundablePayment` base class promises that every payment can be refunded. A subclass
(`GiftCardPayment`) throws when `refund()` is called — breaking the base contract. Code that treats
all payments as `RefundablePayment` crashes. Repair the hierarchy so **every subtype is substitutable**.

### The Smell (before)

```java
// ❌ Base promises refund(); a subtype breaks the promise
abstract class RefundablePayment {
    abstract void pay(double amount);
    abstract void refund(double amount);
}

class GiftCardPayment extends RefundablePayment {
    public void pay(double amount) { /* charge the gift card */ }
    public void refund(double amount) {
        throw new UnsupportedOperationException("Gift cards are non-refundable");  // LSP violation!
    }
}

void refundAll(List<RefundablePayment> payments) {
    for (RefundablePayment p : payments) p.refund(10);   // 💥 blows up on a gift card
}
```

### The Fix (after)

Model the **capability** as a separate contract and only promise what every subtype can honour.

```java
interface Payment {
    void pay(double amount);
}

interface Refundable {
    void refund(double amount);
}

class CreditCardPayment implements Payment, Refundable {
    public void pay(double amount)    { /* charge card */ }
    public void refund(double amount) { /* reverse charge */ }   // honours the promise
}

class GiftCardPayment implements Payment {          // simply not Refundable — no false promise
    public void pay(double amount) { /* debit gift card */ }
}

// This method only accepts objects that genuinely support refunding
void refundAll(List<Refundable> payments) {
    for (Refundable p : payments) p.refund(10);      // safe — type system guarantees support
}
```

### Design points
- **No false promises** — `Payment` only declares what every implementer supports.
- **Substitutability** — any `Payment` can stand in wherever a `Payment` is expected.
- **Capability via interfaces** — `Refundable` is a role, not a subclass quirk.
- **Compile-time safety** — the type system now prevents the runtime crash.

### Alternative fix
If refunds *are* fundamentally part of the domain, give the base a **sanctioned no-op/default**
(e.g. `refund()` that does nothing and returns `false`) rather than throwing — but prefer the
interface split above, which expresses the real contract.

**Complexity:** O(1) per operation · Space O(1)

---
#solid #lsp #lld #practice