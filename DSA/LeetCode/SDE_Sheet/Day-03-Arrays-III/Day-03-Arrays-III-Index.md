# Day 3 — Arrays III

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Arrays — Advanced
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Search in a 2D Matrix](Search-in-a-2D-Matrix.md) | LeetCode 74 | Medium | [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)
- [ ] [Pow(x, n)](Pow-x-n.md) | LeetCode 50 | Medium | [LeetCode](https://leetcode.com/problems/powx-n/)
- [ ] [Majority Element (n/2 times)](Majority-Element-n-2-times.md) | LeetCode 169 | Easy | [LeetCode](https://leetcode.com/problems/majority-element/)
- [ ] [Majority Element II (n/3 times)](Majority-Element-II-n-3-times.md) | LeetCode 229 | Medium | [LeetCode](https://leetcode.com/problems/majority-element-ii/)
- [ ] [Grid Unique Paths](Grid-Unique-Paths.md) | LeetCode 62 | Medium | [LeetCode](https://leetcode.com/problems/unique-paths/)
- [ ] [Reverse Pairs](Reverse-Pairs.md) | LeetCode 493 | Hard | [LeetCode](https://leetcode.com/problems/reverse-pairs/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Search in a 2D Matrix | Scan every cell. O(m*n). | Binary search each row. O(m log n). | Treat matrix as a sorted 1D array. O(log(m*n)). |
| Pow(x, n) | Multiply x by itself abs(n) times. O(n). | Recursive divide-and-conquer exponentiation. O(log n). | Iterative binary exponentiation with negative exponent handling. O(log n), O(1). |
| Majority Element | Count every candidate by scanning. O(n^2). | Use a frequency map. O(n) time, O(n) space. | Boyer-Moore voting. O(n) time, O(1) space. |
| Majority Element II | Count every candidate by scanning. O(n^2). | Use a frequency map. O(n) space. | Extended Boyer-Moore with two candidates plus verification. O(n), O(1). |
| Grid Unique Paths | Recursively try right/down paths. Exponential. | DP table over cells. O(m*n). | Combinatorics: choose moves. O(min(m,n)) time, O(1) space. |
| Reverse Pairs | Check every pair. O(n^2). | Fenwick tree with coordinate compression. O(n log n). | Modified merge sort counts cross pairs. O(n log n). |

---

## Interview Tips for Arrays III

> 💡 **2D Matrix → Flatten to 1D** for binary search
> 💡 **Boyer-Moore** works for n/k majority: need k-1 candidates
> 💡 **Merge Sort** solves inversion-type problems in O(n log n)

#sde-sheet #arrays #day3
