# Design Splitwise (Hard)

**Difficulty:** Hard · **Patterns:** Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design expense sharing: groups, expenses with equal/exact/percent splits, net balances, and a minimal-transfer settle-up.

**Functional**
- Add expenses (payer + split rule); equal, exact, percent splits validated against the total.
- Net balances per member; settle-up produces transfers that zero everyone; observers notified per expense.

**Non-functional**
- Integer money only; balances always net to zero; new split rules plug in.

### The failure, before

```java
// ❌ `double balance` per user updated ad-hoc: floating-point drift, splits that do not
// sum to the bill, and "who owes whom" recomputed with nested loops over everybody.
// balance += amount / n;   // 100/3 three times ≠ 100 — money evaporates.
```

### The Fix (after)

Integer money + `SplitStrategy` (reconciled) + one net-balance map + greedy settle-up.

```java
import java.util.*;

class User {
    final String id, name;
    User(String id, String name) { this.id = id; this.name = name; }
}

record Split(User user, long amount) {}

interface SplitStrategy {
    List<Split> split(long total, List<User> participants);
}

class EqualSplit implements SplitStrategy {                  // first member absorbs the remainder
    public List<Split> split(long total, List<User> participants) {
        long each = total / participants.size();
        List<Split> out = new ArrayList<>();
        for (int i = 0; i < participants.size(); i++)
            out.add(new Split(participants.get(i), i == 0 ? each + total % participants.size() : each));
        return out;
    }
}

class ExactSplit implements SplitStrategy {                  // caller-supplied amounts
    private final List<Long> amounts;
    ExactSplit(List<Long> amounts) { this.amounts = amounts; }
    public List<Split> split(long total, List<User> participants) {
        long sum = amounts.stream().mapToLong(Long::longValue).sum();
        if (sum != total) throw new IllegalArgumentException("Exact splits must sum to " + total);
        List<Split> out = new ArrayList<>();
        for (int i = 0; i < participants.size(); i++) out.add(new Split(participants.get(i), amounts.get(i)));
        return out;
    }
}

class PercentSplit implements SplitStrategy {                // percents sum to 100; last absorbs rounding
    private final List<Integer> percents;
    PercentSplit(List<Integer> percents) { this.percents = percents; }
    public List<Split> split(long total, List<User> participants) {
        if (percents.stream().mapToInt(Integer::intValue).sum() != 100)
            throw new IllegalArgumentException("Percents must sum to 100");
        List<Split> out = new ArrayList<>();
        long allocated = 0;
        for (int i = 0; i < participants.size(); i++) {
            long amt = i == participants.size() - 1 ? total - allocated : total * percents.get(i) / 100;
            allocated += amt;
            out.add(new Split(participants.get(i), amt));
        }
        return out;
    }
}

record Expense(String id, User paidBy, long amount, List<Split> splits) {}

interface ExpenseObserver { void onExpense(Expense expense); }

class Group {
    final String name;
    private final List<User> members = new ArrayList<>();
    private final List<Expense> expenses = new ArrayList<>();
    private final Map<String, Long> net = new HashMap<>();       // +ve = gets back, -ve = owes
    private final List<ExpenseObserver> observers = new ArrayList<>();

    Group(String name) { this.name = name; }
    void join(User u) { members.add(u); net.putIfAbsent(u.id, 0L); }
    void subscribe(ExpenseObserver o) { observers.add(o); }

    void addExpense(User payer, long amount, SplitStrategy rule, List<User> participants) {
        if (amount <= 0) throw new IllegalArgumentException("Amount must be positive");
        List<Split> splits = rule.split(amount, participants);
        long sum = splits.stream().mapToLong(Split::amount).sum();
        if (sum != amount) throw new IllegalStateException("Splits sum to " + sum + ", not " + amount);
        Expense e = new Expense("E" + (expenses.size() + 1), payer, amount, splits);
        expenses.add(e);
        net.merge(payer.id, +amount, Long::sum);                  // payer fronted the money
        splits.forEach(s -> net.merge(s.user().id, -s.amount(), Long::sum));   // each owes their share
        observers.forEach(o -> o.onExpense(e));
    }

    long balanceOf(User u) { return net.getOrDefault(u.id, 0L); }

    List<String> settleUp() {                                     // greedy big-debtor ↔ big-creditor
        List<String> dIds = new ArrayList<>(), cIds = new ArrayList<>();
        List<Long> dAmt = new ArrayList<>(), cAmt = new ArrayList<>();
        net.forEach((id, v) -> {
            if (v < 0) { dIds.add(id); dAmt.add(-v); }
            else if (v > 0) { cIds.add(id); cAmt.add(v); }
        });
        List<String> transfers = new ArrayList<>();
        while (!dAmt.isEmpty() && !cAmt.isEmpty()) {
            int di = indexOfMax(dAmt), ci = indexOfMax(cAmt);
            long amt = Math.min(dAmt.get(di), cAmt.get(ci));
            transfers.add(dIds.get(di) + " pays " + cIds.get(ci) + " " + amt);
            dAmt.set(di, dAmt.get(di) - amt);
            cAmt.set(ci, cAmt.get(ci) - amt);
            if (dAmt.get(di) == 0) { dAmt.remove(di); dIds.remove(di); }
            if (cAmt.get(ci) == 0) { cAmt.remove(ci); cIds.remove(ci); }
        }
        return transfers;
    }
    private static int indexOfMax(List<Long> xs) {
        int best = 0;
        for (int i = 1; i < xs.size(); i++) if (xs.get(i) > xs.get(best)) best = i;
        return best;
    }
}

class Splitwise {                                                 // thin registry facade
    private final Map<String, Group> groups = new LinkedHashMap<>();
    Group newGroup(String name) { Group g = new Group(name); groups.put(name, g); return g; }
    Group group(String name) { return groups.get(name); }
}
```

**Usage**
```java
Splitwise app = new Splitwise();
Group trip = app.newGroup("Goa Trip");
User asha = new User("u1", "Asha"), bharat = new User("u2", "Bharat"), chen = new User("u3", "Chen");
trip.join(asha); trip.join(bharat); trip.join(chen);

trip.addExpense(asha, 300, new EqualSplit(), List.of(asha, bharat, chen));      // 100 each
trip.addExpense(bharat, 500, new PercentSplit(List.of(50, 25, 25)),             // 250/125/125
                                   List.of(asha, bharat, chen));
System.out.println(trip.balanceOf(asha));    // +300 -100 -250 = -50 (owes 50)
System.out.println(trip.settleUp());         // asha pays chen 50 — one clean transfer
```

### Design points
- **One invariant** — the net map always sums to zero; every bug hunt starts there.
- **Strategies reconcile themselves** — exact splits must sum to the bill, percents to 100; `Group` double-checks.
- **Remainders have owners** — equal → first member, percent → last member; no paisa disappears.
- **Settle-up is derived, not stored** — balances persist; the transfer list is recomputed in O(n²) for study sizes.

**Complexity:** addExpense O(participants) · settleUp O(n²) worst case · balances O(1) read.

---
#lld #machine-coding #splitwise #hard #practice