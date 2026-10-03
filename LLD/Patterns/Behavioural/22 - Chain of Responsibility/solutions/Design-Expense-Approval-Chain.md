# Design an Expense Approval Chain

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Chain of Responsibility
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-expense-approval-chain)

### Problem

Expenses are approved by escalating authority: a **team lead** approves small amounts, a **manager**
larger ones, a **director** even larger, and anything beyond that goes to the **CFO**. Each approver
handles what it is allowed to and forwards the rest up the chain.

### Approach — Chain of Responsibility

- **Handler** = `Approver` with a `next` link and a limit.
- **ConcreteHandlers** = `TeamLead`, `Manager`, `Director`, `Cfo`.
- Each approver either approves or forwards; the CFO is the terminal handler.

### Java Solution

```java
abstract class Approver {
    protected Approver next;
    protected final String title;
    protected final double limit;

    protected Approver(String title, double limit) { this.title = title; this.limit = limit; }

    Approver setNext(Approver next) { this.next = next; return next; }

    /** Approve if within limit, otherwise escalate. */
    final void approve(String expense, double amount) {
        if (amount <= limit) {
            System.out.println(title + " approved \"" + expense + "\" (" + amount + ")");
        } else if (next != null) {
            next.approve(expense, amount);
        } else {
            System.out.println("No approver can handle " + amount);
        }
    }
}

class TeamLead extends Approver { protected TeamLead() { super("Team Lead", 1_000); } }
class Manager  extends Approver { protected Manager()  { super("Manager", 10_000); } }
class Director extends Approver { protected Director() { super("Director", 100_000); } }
class Cfo      extends Approver { protected Cfo()      { super("CFO", Double.MAX_VALUE); } }   // terminal
```

**Usage**
```java
Approver chain = new TeamLead();
chain.setNext(new Manager()).setNext(new Director()).setNext(new Cfo());

chain.approve("Team lunch", 200);       // Team Lead approved
chain.approve("Laptop", 2_500);         // Manager approved
chain.approve("Conference", 50_000);    // Director approved
chain.approve("Acquisition", 5_000_000);// CFO approved
```

### Design points
- **Escalation** — each approver narrows the problem until one can handle it.
- **Decoupled sender** — the caller submits to the head and does not know who approves.
- **Terminal handler** — the CFO guarantees a decision, so requests are never dropped.

**Complexity:** O(chain length) worst case · Space O(chain)

---
#chain-of-responsibility #lld #practice