# Design an Order Fulfillment Saga

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Command
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

Fulfilling an order is a multi-step process — charge payment, reserve inventory, schedule shipping,
send confirmation. In a distributed setting each step can fail, so the whole flow must be **compensable**:
if a later step fails, the earlier steps are **undone** in reverse order. This is the **Saga** pattern,
built on commands.

### Approach — Command (+ Saga orchestration)

- Each step is a `Step` command with `execute()` and `compensate()`.
- A `Saga` runs the steps in order; on failure it compensates the completed steps in reverse.
- Steps are idempotent and independently reversible.

### Java Solution

```java
import java.util.*;

interface Step {
    String name();
    void execute();
    void compensate();     // the "undo" for a saga step
}

class PaymentStep implements Step {
    private final String orderId; private boolean charged;
    PaymentStep(String orderId) { this.orderId = orderId; }
    public String name() { return "charge payment"; }
    public void execute() { charged = true; System.out.println("Charged payment for " + orderId); }
    public void compensate() { if (charged) { System.out.println("Refunded " + orderId); charged = false; } }
}
class InventoryStep implements Step {
    private final String orderId; private boolean reserved;
    InventoryStep(String orderId) { this.orderId = orderId; }
    public String name() { return "reserve inventory"; }
    public void execute() { reserved = true; System.out.println("Reserved inventory for " + orderId); }
    public void compensate() { if (reserved) { System.out.println("Released inventory for " + orderId); reserved = false; } }
}
class ShippingStep implements Step {
    private final String orderId; private final boolean fail;
    ShippingStep(String orderId, boolean fail) { this.orderId = orderId; this.fail = fail; }
    public String name() { return "schedule shipping"; }
    public void execute() {
        if (fail) throw new IllegalStateException("Shipping unavailable");
        System.out.println("Scheduled shipping for " + orderId);
    }
    public void compensate() { System.out.println("Cancelled shipping for " + orderId); }
}

class Saga {
    private final List<Step> steps;
    Saga(List<Step> steps) { this.steps = steps; }

    /** Run all steps; on any failure, compensate the completed ones in reverse. */
    public boolean run() {
        Deque<Step> completed = new ArrayDeque<>();
        try {
            for (Step step : steps) {
                step.execute();
                completed.push(step);
            }
            System.out.println("Saga completed ✔");
            return true;
        } catch (RuntimeException e) {
            System.out.println("Saga failed at step: " + e.getMessage());
            while (!completed.isEmpty()) completed.pop().compensate();   // reverse order
            return false;
        }
    }
}
```

**Usage**
```java
Saga ok = new Saga(List.of(
        new PaymentStep("ORD-1"),
        new InventoryStep("ORD-1"),
        new ShippingStep("ORD-1", false)));
ok.run();    // all steps succeed

Saga failing = new Saga(List.of(
        new PaymentStep("ORD-2"),
        new InventoryStep("ORD-2"),
        new ShippingStep("ORD-2", true)));   // shipping fails
failing.run();  // refunds payment + releases inventory
```

### Design points
- **Compensating actions** — each step can undo its effect (a saga has no global rollback).
- **Reverse-order compensation** — completed steps are undone last-in-first-out.
- **Orchestration vs choreography** — here a central `Saga` orchestrates; a choreographed version
  would let services react to events instead.

**Complexity:** O(steps) per run · Space O(completed steps)

---
#command #saga #lld #practice