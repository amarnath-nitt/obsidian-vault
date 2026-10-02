# Day 16 — Strings II

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** String — DP, Wildcards, Advanced
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Palindrome Partitioning II (Min Cuts)](Palindrome-Partitioning-II-Min-Cuts.md) | LeetCode 132 | Hard | [LeetCode](https://leetcode.com/problems/palindrome-partitioning-ii/)
- [ ] [Word Break](Word-Break.md) | LeetCode 139 | Medium | [LeetCode](https://leetcode.com/problems/word-break/)
- [ ] [Wildcard Matching](Wildcard-Matching.md) | LeetCode 44 | Hard | [LeetCode](https://leetcode.com/problems/wildcard-matching/)
- [ ] [Regular Expression Matching](Regular-Expression-Matching.md) | LeetCode 10 | Hard | [LeetCode](https://leetcode.com/problems/regular-expression-matching/)
- [ ] [String to Integer (atoi)](String-to-Integer-atoi.md) | LeetCode 8 | Medium | [LeetCode](https://leetcode.com/problems/string-to-integer-atoi/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Palindrome Partitioning II | Generate every partition and count cuts. Exponential. | Precompute palindrome table and DP cuts. O(n^2). | Center expansion updates cuts with O(n) space. O(n^2). |
| Word Break | Try all split combinations recursively. Exponential. | Memoized DFS by start index. O(n^2). | Bottom-up DP with HashSet/trie pruning. O(n^2). |
| Wildcard Matching | Recursive branching on star. Exponential. | DP over pattern/string. O(n*m). | Greedy two-pointer with last star fallback. O(n+m), O(1). |
| Regular Expression Matching | Recursive branching for star. Exponential. | Memoized recursion. O(n*m). | Bottom-up or rolling DP. O(n*m). |
| String to Integer (atoi) | Use parsing/library conversion and clamp after; overflow risk. | Manual scan with long accumulator. O(n). | Manual scan with pre-overflow checks. O(n), O(1). |

---

## String DP Patterns

```
Problem                      → DP State
───────────────────────────────────────────────
Word Break                   → dp[i] = can segment s[0..i]
Palindrome min cuts          → dp[i] = min cuts for s[0..i]
Wildcard matching            → dp[i][j] = s[0..i] matches p[0..j]
Regex matching               → dp[i][j] = s[0..i] matches p[0..j]
Longest Palindromic Subseq   → dp[i][j] = LPS of s[i..j]
Edit Distance                → dp[i][j] = min ops to convert s[0..i] to t[0..j]
```

#sde-sheet #strings #dp #day16
