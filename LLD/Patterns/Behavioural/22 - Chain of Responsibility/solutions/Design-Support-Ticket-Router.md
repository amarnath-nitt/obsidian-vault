# Design a Support Ticket Router

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Chain of Responsibility
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

Support tickets are routed to the **first team that can handle them**: a general **triage** desk,
then **billing**, **technical**, and finally **escalation**. Each tier either resolves the ticket or
forwards it. New tiers must be insertable without editing existing ones.

### Approach — Chain of Responsibility

- **Handler** = `TicketHandler` with a `next` link and a `canHandle(ticket)` predicate.
- **ConcreteHandlers** = `TriageDesk`, `BillingDesk`, `TechnicalDesk`, `EscalationDesk`.
- The first handler whose predicate matches resolves the ticket (pure chain).

### Java Solution

```java
enum Category { GENERAL, BILLING, TECHNICAL, UNKNOWN }

final class Ticket {
    final String id;
    final Category category;
    final int priority;          // 1 = low … 5 = critical
    Ticket(String id, Category category, int priority) {
        this.id = id; this.category = category; this.priority = priority;
    }
}

abstract class TicketHandler {
    protected TicketHandler next;
    TicketHandler setNext(TicketHandler next) { this.next = next; return this; }

    protected final String title;
    protected TicketHandler(String title) { this.title = title; }

    final void route(Ticket ticket) {
        if (canHandle(ticket)) resolve(ticket);
        else if (next != null) next.route(ticket);
        else System.out.println(ticket.id + " could not be routed");
    }

    protected abstract boolean canHandle(Ticket ticket);
    protected abstract void resolve(Ticket ticket);
}

class TriageDesk extends TicketHandler {
    TriageDesk() { super("Triage"); }
    protected boolean canHandle(Ticket t) { return t.category == Category.GENERAL; }
    protected void resolve(Ticket t)      { System.out.println("Triage resolved " + t.id); }
}
class BillingDesk extends TicketHandler {
    BillingDesk() { super("Billing"); }
    protected boolean canHandle(Ticket t) { return t.category == Category.BILLING; }
    protected void resolve(Ticket t)      { System.out.println("Billing resolved " + t.id); }
}
class TechnicalDesk extends TicketHandler {
    TechnicalDesk() { super("Technical"); }
    protected boolean canHandle(Ticket t) { return t.category == Category.TECHNICAL && t.priority < 5; }
    protected void resolve(Ticket t)      { System.out.println("Technical resolved " + t.id); }
}
class EscalationDesk extends TicketHandler {          // terminal — anything left
    EscalationDesk() { super("Escalation"); }
    protected boolean canHandle(Ticket t) { return true; }
    protected void resolve(Ticket t)      { System.out.println("⚠ Escalated " + t.id + " (priority " + t.priority + ")"); }
}
```

**Usage**
```java
TicketHandler chain = new TriageDesk();
chain.setNext(new BillingDesk()).setNext(new TechnicalDesk()).setNext(new EscalationDesk());

chain.route(new Ticket("T-1", Category.GENERAL, 2));    // Triage
chain.route(new Ticket("T-2", Category.BILLING, 3));    // Billing
chain.route(new Ticket("T-3", Category.TECHNICAL, 4));  // Technical
chain.route(new Ticket("T-4", Category.TECHNICAL, 5));  // critical → Escalation
chain.route(new Ticket("T-5", Category.UNKNOWN, 2));    // Escalation
```

### Design points
- **First-matching-handler (pure chain)** — exactly one tier resolves each ticket.
- **Configurable order** — insert a new desk by re-linking the chain; existing desks are untouched.
- **Terminal handler** — escalation guarantees every ticket is resolved.

**Complexity:** O(chain length) per ticket · Space O(chain)

---
#chain-of-responsibility #lld #practice