# Allocate Minimum Pages

**Problem:** N books, M students. Allocate books to minimize the maximum pages a student reads. Each student gets contiguous books.

### Approach (Binary Search on Answer)

- Binary search on max pages (answer space: max_single_book to sum_all_books)
- For a given max `mid`, check if M students can read all books
- Minimize valid `mid`

### Java Solution

```java
public int allocatePages(int[] books, int m) {
    if (m > books.length) return -1;
    int lo = Arrays.stream(books).max().getAsInt();
    int hi = Arrays.stream(books).sum();

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (canAllocate(books, m, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

boolean canAllocate(int[] books, int m, int maxPages) {
    int students = 1, pagesRead = 0;
    for (int pages : books) {
        if (pages > maxPages) return false;
        if (pagesRead + pages > maxPages) {
            students++;
            pagesRead = 0;
        }
        pagesRead += pages;
    }
    return students <= m;
}
```

**Complexity:** Time O(n log(sum)) · Space O(1)

---
