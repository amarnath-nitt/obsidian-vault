# Day 1 — Arrays I

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Arrays — Fundamentals
**Difficulty Mix:** Easy / Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Set Matrix Zeroes](Set-Matrix-Zeroes.md) | LeetCode 73 | Medium | [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)
- [ ] [Pascal's Triangle](Pascal-s-Triangle.md) | LeetCode 118 | Easy | [LeetCode](https://leetcode.com/problems/pascals-triangle/)
- [ ] [Next Permutation](Next-Permutation.md) | LeetCode 31 | Medium | [LeetCode](https://leetcode.com/problems/next-permutation/)
- [ ] [Kadane's Algorithm — Maximum Subarray](Kadane-s-Algorithm-Maximum-Subarray.md) | LeetCode 53 | Medium | [LeetCode](https://leetcode.com/problems/maximum-subarray/)
- [ ] [Sort an Array of 0s 1s 2s (Dutch National Flag)](Sort-an-Array-of-0s-1s-2s-Dutch-National-Flag.md) | LeetCode 75 | Medium | [LeetCode](https://leetcode.com/problems/sort-colors/)
- [ ] [Best Time to Buy and Sell Stock](Best-Time-to-Buy-and-Sell-Stock.md) | LeetCode 121 | Easy | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Set Matrix Zeroes | For every zero, scan its full row and column. O(m*n*(m+n)) time. | Keep row and column marker arrays. O(m*n) time, O(m+n) space. | Use first row and first column as markers. O(m*n) time, O(1) space. |
| Pascal's Triangle | Compute every value independently with combinations. Costly repeated work. | Build each row from the previous row. O(n^2) time. | Same output-bound DP; for a single row use rolling nCr values. |
| Next Permutation | Generate all permutations, sort them, pick the next one. O(n!*n). | Find pivot, swap, then sort the suffix. O(n log n). | Find pivot, swap with next greater from suffix, reverse suffix. O(n), O(1). |
| Kadane's Algorithm | Try every subarray and sum it. O(n^3). | Use prefix sums or two loops. O(n^2). | Kadane: keep best subarray ending here. O(n), O(1). |
| Sort 0s 1s 2s | Use library sort. O(n log n). | Count 0s, 1s, 2s, then overwrite. O(n), two passes. | Dutch National Flag with low/mid/high. O(n), one pass, O(1). |
| Best Time to Buy and Sell Stock | Try every buy/sell pair. O(n^2). | Precompute best future selling price. O(n) time, O(n) space. | Track minimum price so far and best profit. O(n), O(1). |

---

## Interview Tips for Arrays

> 💡 **Always clarify:** Can we modify the array? Is there extra space allowed?
> 💡 **Common tricks:** Two pointers, prefix sums, frequency maps, in-place markers
> 💡 **Edge cases:** Empty array, single element, all same elements, all zeros

#sde-sheet #arrays #day1
