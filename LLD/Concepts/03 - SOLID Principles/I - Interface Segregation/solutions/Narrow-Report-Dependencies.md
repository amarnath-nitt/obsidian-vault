# Narrow Report Dependencies (Interface Segregation)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Principle:** Interface Segregation
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/narrow-report-dependencies)

### Problem

A `ReportBuilder` needs only two things from its data source — fetch rows and fetch the column
headers. But it is handed a large `Database` interface that also exposes `executeUpdate`, `beginTxn`,
`commit`, `rollback`, etc. The report is coupled to operations it never uses (and could never safely
call). Narrow the dependency.

### The Smell (before)

```java
// ❌ ReportBuilder depends on a huge interface it barely uses
interface Database {
    List<String> columns();
    List<List<String>> rows();
    void executeUpdate(String sql);   // never used by ReportBuilder
    void beginTransaction();          // never used
    void commit();                    // never used
    void rollback();                  // never used
    void close();                     // never used
}

class ReportBuilder {
    private final Database db;
    ReportBuilder(Database db) { this.db = db; }

    String build() {
        // only needs db.columns() and db.rows()
        ...
    }
}
```

### The Fix (after)

Define a **role interface** with just the methods the report needs, and make the database fulfil it.

```java
// The narrow contract ReportBuilder actually needs
interface ReadOnlyTable {
    List<String> columns();
    List<List<String>> rows();
}

// The full database implements the narrow role (among others)
class SqlDatabase implements ReadOnlyTable {
    public List<String> columns()      { return List.of("id", "name"); }
    public List<List<String>> rows()   { return List.of(List.of("1", "Alice")); }

    // ...unrelated operations stay here, not forced on the report
    public void executeUpdate(String sql) { /* ... */ }
    public void beginTransaction()        { /* ... */ }
    public void commit()                  { /* ... */ }
}

class ReportBuilder {
    private final ReadOnlyTable table;                 // depends only on what it uses
    ReportBuilder(ReadOnlyTable table) { this.table = table; }

    String build() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.join(" | ", table.columns())).append("\n");
        for (List<String> row : table.rows()) sb.append(String.join(" | ", row)).append("\n");
        return sb.toString();
    }
}
```

**Usage**
```java
String report = new ReportBuilder(new SqlDatabase()).build();
System.out.println(report);
// id | name
// 1 | Alice
```

### Design points
- **Narrow dependency** — `ReportBuilder` sees only `columns()` and `rows()`.
- **Easier testing** — a tiny fake `ReadOnlyTable` replaces the whole database in tests.
- **Safe** — the report cannot accidentally mutate the database.
- **Realised by the full type** — `SqlDatabase` implements the role without losing its other abilities.

**Complexity:** O(rows × columns) per report · Space O(report)

---
#solid #isp #lld #practice