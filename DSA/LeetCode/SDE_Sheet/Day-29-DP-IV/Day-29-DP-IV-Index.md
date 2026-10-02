# Day 29 — Dynamic Programming IV (String DP, Partition DP)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** DP — Strings, Partitioning, Stock Trading, Advanced Optimization
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Best Time to Buy and Sell Stock (DP Suite)](Best-Time-to-Buy-and-Sell-Stock-DP-Suite.md) | LeetCode 122/123 | Medium / Hard | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
- [ ] [Word Break](Word-Break.md) | LeetCode 139 | Medium | [LeetCode](https://leetcode.com/problems/word-break/)
- [ ] [Palindrome Partitioning II (Min Cuts)](Palindrome-Partitioning-II-Min-Cuts.md) | LeetCode 132 | Hard | [LeetCode](https://leetcode.com/problems/palindrome-partitioning-ii/)
- [ ] [Maximum Sum Increasing Subsequence](Maximum-Sum-Increasing-Subsequence.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Maximum+Sum+Increasing+Subsequence)
- [ ] [Rod Cutting](Rod-Cutting.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Rod+Cutting)
- [ ] [Maximum Profit in Job Scheduling](Maximum-Profit-in-Job-Scheduling.md) | LeetCode 1235 | Hard | [LeetCode](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Best Time to Buy and Sell Stock (DP Suite) | Try every buy/sell sequence. Exponential. | DP over day, hold state, and remaining transactions. | Space-compressed state variables/tables. O(n*k) or O(n) for fixed k. |
| Word Break | Try all split combinations recursively. Exponential. | Memoized DFS by start index. O(n^2). | Bottom-up DP with HashSet/trie pruning. O(n^2). |
| Palindrome Partitioning II | Generate every palindrome partition. Exponential. | Palindrome table plus cut DP. O(n^2). | Center expansion updates min cuts with O(n) space. |
| Maximum Sum Increasing Subsequence | Enumerate all increasing subsequences. Exponential. | DP best sum ending at each index. O(n^2). | Fenwick/segment tree after coordinate compression. O(n log n). |
| Rod Cutting | Try every way to cut the rod. Exponential. | Unbounded knapsack DP. O(n^2). | 1D DP over rod lengths. O(n^2), O(n) space. |
| Maximum Profit in Job Scheduling | Try every subset of compatible jobs. Exponential. | Sort by end/start and DP with binary search. O(n log n). | Bottom-up or memoized DP over sorted jobs with next-compatible lookup. |

---

## Summary of Advanced DP Techniques

```
  Technique              Primary Application               Optimization Method
---------------------------------------------------------------------------------
  Interval DP            MCM, Palindrome Partitioning      O(N³) or O(N²) Matrix
  State Machine DP       Stock Trading, Game Theory        State compression, O(1) space
  DP + Binary Search     Weighted Job Scheduling, LIS      Replace O(N²) scan with O(log N)
```

#sde-sheet #dynamic-programming #day29
