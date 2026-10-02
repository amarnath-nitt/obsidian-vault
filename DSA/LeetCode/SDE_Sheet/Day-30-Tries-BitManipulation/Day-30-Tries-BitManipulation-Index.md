# Day 30 — Tries & Bit Manipulation

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Tries (Prefix Trees) & Bit Manipulation
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Implement Trie (Prefix Tree)](Implement-Trie-Prefix-Tree.md) | LeetCode 208 | Medium | [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [ ] [Maximum XOR of Two Numbers in an Array](Maximum-XOR-of-Two-Numbers-in-an-Array.md) | LeetCode 421 | Medium | [LeetCode](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
- [ ] [Maximum XOR with an Element From Array](Maximum-XOR-with-an-Element-From-Array.md) | LeetCode 1707 | Hard | [LeetCode](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)
- [ ] [Power Set (Subset Generation using Bitmasking)](Power-Set-Subset-Generation-using-Bitmasking.md) | LeetCode 78 | Medium | [LeetCode](https://leetcode.com/problems/subsets/)
- [ ] [Single Number III (Two Non-Repeating Numbers)](Single-Number-III-Two-Non-Repeating-Numbers.md) | LeetCode 260 | Medium | [LeetCode](https://leetcode.com/problems/single-number-iii/)
- [ ] [Divide Two Integers](Divide-Two-Integers.md) | LeetCode 29 | Medium | [LeetCode](https://leetcode.com/problems/divide-two-integers/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Implement Trie | Store all words in a list and scan for search/prefix. O(N*L). | HashSet for exact search plus prefix set for startsWith. | Trie nodes by character. O(L) search/insert/prefix. |
| Maximum XOR of Two Numbers | Check every pair. O(n^2). | Greedy prefix-set bit building. O(31*n). | Binary trie choosing opposite bits. O(31*n). |
| Maximum XOR with an Element From Array | For each query, scan all nums <= mi. O(n*q). | Sort nums and filter eligible range per query. Still costly. | Offline sort queries by mi and insert eligible nums into trie. |
| Power Set | Recursive include/exclude generation. O(n*2^n). | Bitmask from 0 to 2^n - 1. | Output-bound; bitmask/backtracking both are optimal. |
| Single Number III | Frequency map counts every number. O(n) space. | Sort and scan singles. O(n log n). | XOR all, split by rightmost set bit, XOR groups. O(n), O(1). |
| Divide Two Integers | Repeated subtraction. O(quotient). | Exponential subtraction by doubling divisor. O(log quotient). | Check high-to-low bit shifts and subtract. O(log dividend), O(1). |

---

## Bitwise Reference Cheatsheet

```
  Operation             Code                     Use Case
---------------------------------------------------------------------------------
  Get lowest set bit    `x & -x`                 Isolate rightmost set bit
  Clear lowest set bit  `x & (x - 1)`            Check power of 2, count set bits
  Toggle bit            `x ^ (1 << i)`           Toggle i-th bit from right
  Subset Check          `(mask & (1 << i)) != 0` Check if i-th element is in subset
```

#sde-sheet #tries #bit-manipulation #day30
