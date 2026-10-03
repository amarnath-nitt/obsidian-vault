# Design Library Book Class

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Topic:** Classes and Objects
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-library-book)

### Problem

Design a `Book` class for a library. A book has a title and author (fixed), and an availability
state that changes as members borrow and return it. The class must **encapsulate** the borrowing
rules — callers ask to borrow and the book decides whether that is allowed.

### Approach

- Identity (`title`, `author`) is `final`; availability is private mutable state.
- Borrow/return are transactional: they return whether the action succeeded.

### Java Solution

```java
public class Book {

    private final String title;
    private final String author;
    private boolean borrowed;                 // private state

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    /** Returns true if the book was available and is now borrowed. */
    public boolean borrow() {
        if (borrowed) return false;
        borrowed = true;
        return true;
    }

    /** Returns true if the book was on loan and is now returned. */
    public boolean returnBook() {
        if (!borrowed) return false;
        borrowed = false;
        return true;
    }

    public boolean isAvailable() { return !borrowed; }

    public String describe() {
        return "\"" + title + "\" by " + author + (borrowed ? " (borrowed)" : " (available)");
    }
}
```

**Usage**
```java
Book book = new Book("Clean Code", "Robert Martin");
book.isAvailable();   // true
book.borrow();        // true
book.borrow();        // false  ← already borrowed
book.returnBook();    // true
book.describe();      // "Clean Code" by Robert Martin (available)
```

### Design points
- **Encapsulation** — `borrowed` is private; callers cannot set it directly.
- **Rules live in the object** — the book rejects a second borrow.
- **Boolean results** — the caller learns whether the operation was allowed.

**Complexity:** O(1) per operation · Space O(1)

---
#oop #encapsulation #lld #practice