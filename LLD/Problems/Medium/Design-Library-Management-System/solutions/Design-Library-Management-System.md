# Design a Library Management System (Medium)

**Difficulty:** Medium · **Patterns:** State, Strategy, Observer
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a library: books as multiple copies, borrow/return/renew with due dates, fines for lateness, and FIFO reservations.

**Functional**
- Catalogue with search (title/author/ISBN); borrow with member limits; return with fines; renew.
- Reserve when all copies are out; notify the first waiter when a copy returns.

**Non-functional**
- No copy is double-loaned; waitlist order is stable; fine rules are swappable.

### The failure, before

```java
// ❌ One `Book` with `boolean available` and `int copies`:
// counters drift from reality, waitlists do not exist, fines are ifs in three places.
// if (book.available) { book.available = false; loan(member); }
```

### The Fix (after)

`Book` metadata + `BookItem` copies with their own status machine + fine strategy + FIFO waitlist.

```java
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.*;

enum CopyStatus { AVAILABLE, LOANED, RESERVED, LOST }

class Book {
    final String isbn, title, author;
    final List<BookItem> copies = new ArrayList<>();
    Book(String isbn, String title, String author) { this.isbn = isbn; this.title = title; this.author = author; }
    void addCopy(String barcode) { copies.add(new BookItem(barcode, this)); }
}

class BookItem {
    final String barcode; final Book book; CopyStatus status = CopyStatus.AVAILABLE;
    BookItem(String barcode, Book book) { this.barcode = barcode; this.book = book; }
}

class Member {
    final String id, name; final int limit = 5;
    Member(String id, String name) { this.id = id; this.name = name; }
}

class Loan {
    final BookItem item; final Member member; final LocalDate dueAt;
    LocalDate returnedAt;
    Loan(BookItem item, Member member, LocalDate dueAt) { this.item = item; this.member = member; this.dueAt = dueAt; }
    boolean overdue(LocalDate on) { return on.isAfter(dueAt); }
}

interface FineStrategy { long fine(Loan loan, LocalDate returnedOn); }

class DailyFine implements FineStrategy {                   // ₹5 per overdue day, ₹200 cap
    public long fine(Loan loan, LocalDate returnedOn) {
        long days = ChronoUnit.DAYS.between(loan.dueAt, returnedOn);
        return days <= 0 ? 0 : Math.min(days * 5, 200);
    }
}

interface NotificationService { void onAvailable(String memberId, Book book); }

class Library {
    private final Map<String, Book> catalogue = new LinkedHashMap<>();   // isbn → book
    private final Map<String, Member> members = new LinkedHashMap<>();
    private final Map<String, Loan> loansByBarcode = new HashMap<>();
    private final Map<Book, Deque<String>> waitlists = new HashMap<>();  // book → member ids (FIFO)
    private FineStrategy fines = new DailyFine();
    private final List<NotificationService> notifications = new ArrayList<>();
    private long clock = 0;                                              // days since epoch, test-friendly

    void register(Member m) { members.put(m.id, m); }
    void addBook(Book b) { catalogue.put(b.isbn, b); }
    void setFineStrategy(FineStrategy s) { fines = s; }
    void subscribe(NotificationService n) { notifications.add(n); }

    List<Book> search(String q) {
        String needle = q.toLowerCase();
        return catalogue.values().stream()
                .filter(b -> b.isbn.equals(q) || b.title.toLowerCase().contains(needle)
                          || b.author.toLowerCase().contains(needle))
                .toList();
    }

    BookItem borrow(String memberId, String isbn, LocalDate today) {
        Member m = members.get(memberId);
        long held = loansByBarcode.values().stream().filter(l -> l.member == m && l.returnedAt == null).count();
        if (held >= m.limit) throw new IllegalStateException("Borrow limit reached");
        Book book = catalogue.get(isbn);
        BookItem copy = book.copies.stream().filter(c -> c.status == CopyStatus.AVAILABLE).findFirst()
                .orElseThrow(() -> new IllegalStateException("All copies out — reserve instead"));
        copy.status = CopyStatus.LOANED;
        loansByBarcode.put(copy.barcode, new Loan(copy, m, today.plusDays(14)));
        return copy;
    }

    long returnItem(String barcode, LocalDate today) {
        Loan loan = loansByBarcode.get(barcode);
        if (loan == null || loan.returnedAt != null) throw new IllegalStateException("Not on loan");
        long fine = fines.fine(loan, today);
        loan.returnedAt = today;
        Deque<String> queue = waitlists.get(loan.item.book);
        if (queue != null && !queue.isEmpty()) {
            loan.item.status = CopyStatus.RESERVED;             // hold for the next waiter
            String next = queue.poll();
            notifications.forEach(n -> n.onAvailable(next, loan.item.book));
        } else {
            loan.item.status = CopyStatus.AVAILABLE;
        }
        return fine;
    }

    void reserve(String memberId, String isbn) {
        waitlists.computeIfAbsent(catalogue.get(isbn), k -> new ArrayDeque<>()).add(memberId);
    }

    boolean renew(String barcode, LocalDate today) {
        Loan loan = loansByBarcode.get(barcode);
        Deque<String> queue = waitlists.get(loan.item.book);
        if (queue != null && !queue.isEmpty()) return false;     // waiters first
        loansByBarcode.put(barcode, new Loan(loan.item, loan.member, today.plusDays(14)));
        return true;
    }
}
```

**Usage**
```java
Library lib = new Library();
Book dune = new Book("978-0441013593", "Dune", "Frank Herbert");
dune.addCopy("CP-001"); dune.addCopy("CP-002");
lib.addBook(dune);
lib.register(new Member("m1", "Asha"));
lib.subscribe((memberId, book) -> System.out.println(memberId + ": " + book.title + " is ready"));

BookItem copy = lib.borrow("m1", dune.isbn, LocalDate.of(2026, 10, 3));   // due Oct 17
lib.reserve("m2", dune.isbn);
lib.returnItem(copy.barcode, LocalDate.of(2026, 10, 20));                 // ₹15 fine; m2 notified
```

### Design points
- **Copies are the inventory** — availability never lives on `Book`; each `BookItem` carries its own status.
- **Return is a cascade** — fine → release → waitlist promotion → notify, in one deterministic method.
- **Fine is a pure function** — daily-rate, grace, and cap all hide behind `FineStrategy`.
- **Renew respects waiters** — a queued reservation blocks renewal; the queue is the fairness contract.

**Complexity:** search O(books) · borrow O(copies) · return O(1) + O(waiters).

---
#lld #machine-coding #library #medium #practice