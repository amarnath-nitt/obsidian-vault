# Design a Paginated Catalog

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Iterator
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

A product catalog is large, so it is browsed **page by page** rather than all at once. Provide an
iterator that yields items and exposes pages of a fixed size, so a client can render one page at a
time without loading the whole catalog into view.

### Approach — Iterator

- `Catalog` hides its storage and offers a `paginate(pageSize)` iterator.
- The iterator walks the collection in chunks and can report the current page and total pages.

### Java Solution

```java
import java.util.*;

final class Product {
    final String name;
    Product(String name) { this.name = name; }
    @Override public String toString() { return name; }
}

class Catalog implements Iterable<Product> {
    private final List<Product> products = new ArrayList<>();

    Catalog add(Product p) { products.add(p); return this; }

    @Override public Iterator<Product> iterator() { return products.iterator(); }

    public int size() { return products.size(); }

    /** A paginated view over the catalog. */
    public Paginator paginate(int pageSize) {
        if (pageSize < 1) throw new IllegalArgumentException("pageSize must be >= 1");
        return new Paginator(products, pageSize);
    }

    static final class Paginator {
        private final List<Product> source;
        private final int pageSize;
        private final int totalPages;
        private int page = 0;                                   // zero-based

        Paginator(List<Product> source, int pageSize) {
            this.source = source;
            this.pageSize = pageSize;
            this.totalPages = (source.size() + pageSize - 1) / pageSize;
        }

        int totalPages() { return totalPages; }
        int currentPage() { return page + 1; }                  // one-based for display
        boolean hasNextPage() { return page < totalPages; }

        /** Advance and return the next page of items. */
        List<Product> nextPage() {
            if (!hasNextPage()) throw new NoSuchElementException("No more pages");
            int from = page * pageSize;
            int to = Math.min(from + pageSize, source.size());
            page++;
            return source.subList(from, to);
        }

        /** Iterate the remaining items across all remaining pages. */
        Iterator<Product> remaining() {
            int start = page * pageSize;
            return source.subList(start, source.size()).iterator();
        }
    }
}
```

**Usage**
```java
Catalog catalog = new Catalog();
for (int i = 1; i <= 7; i++) catalog.add(new Product("Item " + i));

Catalog.Paginator paginator = catalog.paginate(3);
while (paginator.hasNextPage()) {
    System.out.println("Page " + paginator.currentPage() + "/" + paginator.totalPages()
            + " → " + paginator.nextPage());
}
// Page 1/3 → [Item 1, Item 2, Item 3]
// Page 2/3 → [Item 4, Item 5, Item 6]
// Page 3/3 → [Item 7]
```

### Design points
- **Traversal state inside the paginator** — the catalog stays untouched.
- **Fixed-size chunks** — `subList` gives each page without copying the whole list.
- **Remaining-items iterator** — clients can switch from paging to full iteration seamlessly.

**Complexity:** O(pageSize) per page · Space O(1) extra (views into the backing list)

---
#iterator #pagination #lld #practice