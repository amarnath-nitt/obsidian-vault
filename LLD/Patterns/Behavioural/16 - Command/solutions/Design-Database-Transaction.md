# Design a Database Transaction

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Command
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-database-transaction)

### Problem

A transaction groups several operations (insert/update/delete). Either **all** operations are applied
on commit, or **all** are rolled back. Model each operation as a command so the transaction can
apply and reverse them.

### Approach — Command

- **Receiver** = `Table` (the in-memory data store).
- **Command** = `DbCommand` with `execute()` / `undo()`.
- **Invoker** = `Transaction` — queues commands, applies or reverses them per commit/rollback.

### Java Solution

```java
import java.util.*;

interface DbCommand {
    void execute();
    void undo();
}

class Table {                                             // Receiver
    private final Map<String, String> rows = new LinkedHashMap<>();
    void put(String key, String value) { rows.put(key, value); }
    void remove(String key)            { rows.remove(key); }
    String get(String key)             { return rows.get(key); }
    Map<String, String> snapshot()     { return new LinkedHashMap<>(rows); }
    void restore(Map<String, String> s) { rows.clear(); rows.putAll(s); }
}

class InsertCommand implements DbCommand {
    private final Table table; private final String key, value;
    InsertCommand(Table t, String k, String v) { table = t; key = k; value = v; }
    public void execute() { table.put(key, value); }
    public void undo()    { table.remove(key); }          // inverse of insert
}
class DeleteCommand implements DbCommand {
    private final Table table; private final String key;
    private String removed;
    DeleteCommand(Table t, String k) { table = t; key = k; }
    public void execute() { removed = table.get(key); table.remove(key); }
    public void undo()    { if (removed != null) table.put(key, removed); }
}
class UpdateCommand implements DbCommand {
    private final Table table; private final String key, newValue;
    private String oldValue;
    UpdateCommand(Table t, String k, String v) { table = t; key = k; newValue = v; }
    public void execute() { oldValue = table.get(key); table.put(key, newValue); }
    public void undo()    { if (oldValue != null) table.put(key, oldValue); else table.remove(key); }
}

class Transaction {                                       // Invoker
    private final Deque<DbCommand> applied = new ArrayDeque<>();

    public void add(DbCommand command) { command.execute(); applied.push(command); }

    public void commit() {                                     // keep the effects
        System.out.println("Committed " + applied.size() + " operation(s)");
        applied.clear();
    }
    public void rollback() {                                   // reverse in LIFO order
        while (!applied.isEmpty()) applied.pop().undo();
        System.out.println("Rolled back");
    }
}
```

**Usage**
```java
Table table = new Table();
Transaction tx = new Transaction();

tx.add(new InsertCommand(table, "id", "1"));
tx.add(new UpdateCommand(table, "id", "2"));
tx.commit();                       // table.id == "2"

Transaction tx2 = new Transaction();
tx2.add(new InsertCommand(table, "temp", "x"));
tx2.add(new DeleteCommand(table, "id"));
tx2.rollback();                    // undoes in reverse: id restored, temp removed
```

### Design points
- **Atomicity via commands** — a transaction is a list of reversible operations.
- **LIFO rollback** — commands are undone in reverse order of execution.
- **Single responsibility** — each command knows only its own forward and inverse action.

**Complexity:** O(operations) per commit/rollback · Space O(operations)

---
#command #transactions #lld #practice