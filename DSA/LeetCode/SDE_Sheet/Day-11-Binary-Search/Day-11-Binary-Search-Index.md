# Day 11 — Binary Search

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Binary Search — on arrays & on answers
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Binary Search](Binary-Search.md) | LeetCode 704 | Easy | [LeetCode](https://leetcode.com/problems/binary-search/)
- [ ] [Search in Rotated Sorted Array](Search-in-Rotated-Sorted-Array.md) | LeetCode 33 | Medium | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [ ] [Find Minimum in Rotated Sorted Array](Find-Minimum-in-Rotated-Sorted-Array.md) | LeetCode 153 | Medium | [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [ ] [Kth Missing Positive Number](Kth-Missing-Positive-Number.md) | LeetCode 1539 | Easy | [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/)
- [ ] [Aggressive Cows](Aggressive-Cows.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Aggressive+Cows)
- [ ] [Allocate Minimum Pages](Allocate-Minimum-Pages.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Allocate+Minimum+Pages)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Binary Search | Linear scan. O(n). | Recursive binary search. O(log n) time, O(log n) stack. | Iterative binary search. O(log n), O(1). |
| Search in Rotated Sorted Array | Linear scan. O(n). | Find pivot, then binary search the correct half. O(log n). | One-pass modified binary search by identifying sorted half. O(log n). |
| Find Minimum in Rotated Sorted Array | Scan all elements. O(n). | Find pivot with binary search. O(log n). | Binary search by comparing mid with right boundary. O(log n). |
| Kth Missing Positive Number | Simulate positive integers until kth missing. O(n+k). | Walk array and count gaps. O(n). | Binary search on missing count before index. O(log n). |
| Aggressive Cows | Try all cow placements. Exponential. | Binary search distance and greedily check feasibility. O(n log range). | Same after sorting stalls; this is the standard optimal pattern. |
| Allocate Minimum Pages | Try every partition among students. Exponential. | DP over books/students. O(n^2*k). | Binary search max pages with greedy feasibility. O(n log sum). |

---

## Binary Search Templates

```java
// Standard - find exact target
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}

// Find first true in monotonic predicate
int lo = 0, hi = n;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (predicate(mid)) hi = mid;  // could be answer
    else lo = mid + 1;
}
// answer is lo

// Binary search on answer (feasibility)
int lo = minPossible, hi = maxPossible;
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (canAchieve(mid)) hi = mid;
    else lo = mid + 1;
}
```

---

## Binary Search on Answer — Identify the Pattern

```
Key signals:
[x] "Minimize the maximum" → BS on answer, check feasibility
[x] "Maximize the minimum" → BS on answer, check feasibility
[x] "Can you achieve X with constraint Y?" → feasibility check function

Template:
  lo = minimum possible answer
  hi = maximum possible answer
  Binary search → find the boundary
```

#sde-sheet #binary-search #day11
