# Refactor Expense Importer (Separation of Concerns)

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Principle:** Separation of Concerns
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-expense-importer)

### Problem

An `ExpenseImporter` reads a CSV, parses each row, validates and converts the values, and writes the
results — all in one method. Reading, parsing, validating, converting, and persisting are distinct
concerns. Apply **Separation of Concerns**.

### The Smell (before)

```java
// ❌ File I/O + parsing + validation + conversion + persistence interleaved
class ExpenseImporter {
    void importFile(String path) throws java.io.IOException {
        var lines = java.nio.file.Files.readAllLines(java.nio.file.Path.of(path));   // I/O
        for (int i = 1; i < lines.size(); i++) {                                     // skip header
            String[] c = lines.get(i).split(",");                                    // parsing
            if (c.length != 3) { System.out.println("bad row " + i); continue; }     // validation
            String vendor = c[0].trim();                                             // conversion
            double amount = Double.parseDouble(c[1].trim());
            String currency = c[2].trim().toUpperCase();
            System.out.println("Insert " + vendor + " " + amount + " " + currency);  // persistence
        }
    }
}
```

### The Fix (after)

```java
import java.util.*;
import java.nio.file.*;

record Expense(String vendor, double amount, String currency) {}
record RawRow(int lineNumber, String[] columns) {}

// Concern 1: file I/O
class ExpenseFileReader {
    List<String> readLines(String path) throws java.io.IOException {
        return Files.readAllLines(Path.of(path));
    }
}

// Concern 2: parsing text → raw rows (no validation here)
class ExpenseCsvParser {
    List<RawRow> parse(List<String> lines) {
        List<RawRow> rows = new ArrayList<>();
        for (int i = 1; i < lines.size(); i++) {           // skip header
            rows.add(new RawRow(i + 1, lines.get(i).split(",")));
        }
        return rows;
    }
}

// Concern 3: validating + converting raw rows → domain objects
class ExpenseMapper {
    List<Expense> map(List<RawRow> rows) {
        List<Expense> expenses = new ArrayList<>();
        for (RawRow row : rows) {
            if (row.columns().length != 3) continue;                 // tolerate bad rows
            expenses.add(new Expense(
                    row.columns()[0].trim(),
                    Double.parseDouble(row.columns()[1].trim()),
                    row.columns()[2].trim().toUpperCase()));
        }
        return expenses;
    }
}

// Concern 4: persistence
interface ExpenseRepository { void save(Expense expense); }
class ConsoleExpenseRepository implements ExpenseRepository {
    public void save(Expense e) {
        System.out.println("Insert " + e.vendor() + " " + e.amount() + " " + e.currency());
    }
}

// Coordinator — depends on interfaces (also DIP)
class ExpenseImporter {
    private final ExpenseFileReader reader;
    private final ExpenseCsvParser parser;
    private final ExpenseMapper mapper;
    private final ExpenseRepository repository;

    ExpenseImporter(ExpenseFileReader reader, ExpenseCsvParser parser,
                    ExpenseMapper mapper, ExpenseRepository repository) {
        this.reader = reader; this.parser = parser; this.mapper = mapper; this.repository = repository;
    }

    int importFile(String path) throws java.io.IOException {
        List<Expense> expenses = mapper.map(parser.parse(reader.readLines(path)));
        expenses.forEach(repository::save);
        return expenses.size();
    }
}
```

### Design points
- **I/O isolated** — swapping to S3/HTTP touches only `ExpenseFileReader`.
- **Parsing vs mapping split** — syntax and semantics are separate concerns.
- **Persistence behind an interface** — the importer does not know the storage details.
- **Testable stages** — parse, map, and save can each be tested independently.

**Complexity:** O(rows) per import · Space O(expenses)

---
#design-principles #separation-of-concerns #lld #practice