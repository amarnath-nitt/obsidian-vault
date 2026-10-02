# Day 2 — Arrays II

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Arrays — Intermediate
**Difficulty Mix:** Easy / Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Rotate Matrix (Image)](Rotate-Matrix-Image.md) | LeetCode 48 | Medium | [LeetCode](https://leetcode.com/problems/rotate-image/)
- [ ] [Merge Overlapping Intervals](Merge-Overlapping-Intervals.md) | LeetCode 56 | Medium | [LeetCode](https://leetcode.com/problems/merge-intervals/)
- [ ] [Merge Two Sorted Arrays Without Extra Space](Merge-Two-Sorted-Arrays-Without-Extra-Space.md) | LeetCode 88 | Medium | [LeetCode](https://leetcode.com/problems/merge-sorted-array/)
- [ ] [Find Duplicate in Array](Find-Duplicate-in-Array.md) | LeetCode 287 | Medium | [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)
- [ ] [Repeat and Missing Number](Repeat-and-Missing-Number.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Repeat+and+Missing+Number)
- [ ] [Count Inversions in Array](Count-Inversions-in-Array.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Count+Inversions+in+Array)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Rotate Matrix | Copy each cell to its rotated position in another matrix. O(n^2) space. | Rotate layer by layer using 4-way swaps. O(1) space. | Transpose, then reverse every row. O(n^2) time, O(1) space. |
| Merge Overlapping Intervals | Repeatedly compare and merge overlapping pairs. O(n^2). | Sort by start and merge in one pass. O(n log n). | Same sorted merge, reusing output list/in-place where possible. |
| Merge Two Sorted Arrays | Combine both arrays and sort. O((m+n) log(m+n)). | Use an extra merged array. O(m+n) space. | Fill from the back of nums1 with three pointers. O(m+n), O(1). |
| Find Duplicate in Array | Compare every pair. O(n^2). | Use sorting or a frequency set. O(n log n) or O(n) extra space. | Floyd cycle detection on index-to-value links. O(n), O(1). |
| Repeat and Missing Number | Count each number by scanning the array. O(n^2). | Use a frequency array. O(n) time, O(n) space. | Use math equations or XOR. O(n) time, O(1) space. |
| Count Inversions in Array | Check every pair. O(n^2). | Use Fenwick tree with coordinate compression. O(n log n). | Count during merge sort. O(n log n), O(n) space. |

---

## Interview Tips for Arrays II

> 💡 **Rotate = Transpose + Reverse** (remember this forever)
> 💡 **Inversions → Modified Merge Sort** (classic divide and conquer)
> 💡 **Floyd's Cycle** works whenever you can model the problem as a linked list

#sde-sheet #arrays #day2
