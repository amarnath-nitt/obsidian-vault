# Day 27 — Dynamic Programming II (2D DP, Grid, LCS)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** DP — 2D Grid, Subsequences
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Unique Paths II (with obstacles)](Unique-Paths-II-with-obstacles.md) | LeetCode 63 | Medium | [LeetCode](https://leetcode.com/problems/unique-paths-ii/)
- [ ] [Minimum Path Sum](Minimum-Path-Sum.md) | LeetCode 64 | Medium | [LeetCode](https://leetcode.com/problems/minimum-path-sum/)
- [ ] [Longest Common Subsequence (LCS)](Longest-Common-Subsequence-LCS.md) | LeetCode 1143 | Medium | [LeetCode](https://leetcode.com/problems/longest-common-subsequence/)
- [ ] [Longest Increasing Subsequence (LIS)](Longest-Increasing-Subsequence-LIS.md) | LeetCode 300 | Medium | [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)
- [ ] [Edit Distance](Edit-Distance.md) | LeetCode 72 | Hard | [LeetCode](https://leetcode.com/problems/edit-distance/)
- [ ] [Matrix Chain Multiplication](Matrix-Chain-Multiplication.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Matrix+Chain+Multiplication)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Unique Paths II | Recursively try right/down paths around obstacles. Exponential. | 2D DP table. O(m*n). | 1D DP over columns. O(m*n) time, O(n) space. |
| Minimum Path Sum | Recursively try every right/down path. Exponential. | 2D DP table. O(m*n). | In-place grid update or 1D DP. O(m*n) time, O(n) or O(1) extra. |
| Longest Common Subsequence | Recursive take/skip both strings. Exponential. | 2D memo/DP. O(n*m). | Two-row DP when only length is needed. O(min(n,m)) space. |
| Longest Increasing Subsequence | Generate all subsequences. O(2^n). | DP ending at each index. O(n^2). | Patience sorting / tails array with binary search. O(n log n). |
| Edit Distance | Recursive insert/delete/replace choices. Exponential. | 2D memo/DP. O(n*m). | Rolling rows. O(n*m) time, O(min(n,m)) space. |
| Matrix Chain Multiplication | Try all parenthesizations recursively. Exponential. | Memoized interval DP. O(n^3). | Bottom-up interval DP. O(n^3), O(n^2) space. |

---

## 2D DP Summary

```
State          Meaning                     Recurrence
dp[i][j]       s1[0..i] and s2[0..j]      LCS, Edit Distance
dp[i][j]       grid[0..i][0..j]           Min/Max path in grid
dp[i][j]       interval [i..j]            Matrix chain, Palindrome partition
```

#sde-sheet #dynamic-programming #day27
