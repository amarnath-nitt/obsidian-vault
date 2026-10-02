# Day 28 — Dynamic Programming III (Knapsack Variants)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** DP — Knapsack, Subsets, Coin Change
**Difficulty Mix:** Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [0/1 Knapsack](0-1-Knapsack.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=0%2F1+Knapsack)
- [ ] [Subset Sum](Subset-Sum.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Subset+Sum)
- [ ] [Partition Equal Subset Sum](Partition-Equal-Subset-Sum.md) | LeetCode 416 | Medium | [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/)
- [ ] [Coin Change (Min Coins)](Coin-Change-Min-Coins.md) | LeetCode 322 | Medium | [LeetCode](https://leetcode.com/problems/coin-change/)
- [ ] [Coin Change II (Total Ways)](Coin-Change-II-Total-Ways.md) | LeetCode 518 | Medium | [LeetCode](https://leetcode.com/problems/coin-change-ii/)
- [ ] [Target Sum](Target-Sum.md) | LeetCode 494 | Medium | [LeetCode](https://leetcode.com/problems/target-sum/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| 0/1 Knapsack | Include/exclude every item. O(2^n). | 2D DP by item and capacity. O(n*W). | 1D DP over capacity in reverse. O(W) space. |
| Subset Sum | Enumerate all subsets. O(2^n). | 2D boolean DP. O(n*sum). | 1D boolean DP in reverse. O(sum) space. |
| Partition Equal Subset Sum | Enumerate subsets and check half sum. O(2^n). | Reduce to subset sum target total/2. | 1D DP or bitset subset-sum. O(sum) space. |
| Coin Change (Min Coins) | Try all coin combinations recursively. Exponential. | Memoized recursion by amount. | Bottom-up 1D DP for min coins. O(amount*coins). |
| Coin Change II (Total Ways) | Recursively count all combinations. Exponential. | 2D DP by coin index and amount. | 1D combinations DP with coins as outer loop. |
| Target Sum | Assign plus/minus to every number. O(2^n). | Memoize index and current sum. | Transform to subset-count DP. O(n*target). |

---

## Knapsack Decision Tree

```
                      Knapsack Problems
                             |
         -----------------------------------------
        |                                         |
   Bounded (0/1)                              Unbounded
(Use each item max 1 time)               (Use each item inf times)
  - Backwards iteration                    - Forwards iteration
  - `w` from `W` down to `cost`            - `w` from `cost` up to `W`
  - Examples: 0/1 Knapsack,                 - Examples: Coin Change I/II,
    Subset Sum, Target Sum                   Rod Cutting
```

#sde-sheet #dynamic-programming #day28
