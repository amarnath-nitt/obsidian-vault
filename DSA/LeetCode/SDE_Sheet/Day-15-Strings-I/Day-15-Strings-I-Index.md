# Day 15 — Strings I

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** String Algorithms — Anagram, KMP, Hashing
**Difficulty Mix:** Easy / Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Valid Anagram](Valid-Anagram.md) | LeetCode 242 | Easy | [LeetCode](https://leetcode.com/problems/valid-anagram/)
- [ ] [Group Anagrams](Group-Anagrams.md) | LeetCode 49 | Medium | [LeetCode](https://leetcode.com/problems/group-anagrams/)
- [ ] [Longest Palindromic Substring](Longest-Palindromic-Substring.md) | LeetCode 5 | Medium | [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)
- [ ] [Count and Say](Count-and-Say.md) | LeetCode 38 | Medium | [LeetCode](https://leetcode.com/problems/count-and-say/)
- [ ] [KMP — Find Pattern in String](KMP-Find-Pattern-in-String.md) | LeetCode 28 | Medium | [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
- [ ] [Rabin-Karp String Hashing](Rabin-Karp-String-Hashing.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Rabin-Karp+String+Hashing)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Valid Anagram | Sort both strings and compare. O(n log n). | Frequency HashMap. O(n) space. | Fixed-size count array. O(n), O(1) for bounded alphabet. |
| Group Anagrams | Compare each word against existing groups. O(n^2*k). | Sort each word as the key. O(n*k log k). | Character-count signature as key. O(n*k). |
| Longest Palindromic Substring | Check every substring. O(n^3). | DP palindrome table. O(n^2) space. | Expand around centers. O(n^2) time, O(1) space. |
| Count and Say | Recompute previous terms recursively. Repeated work. | Iteratively run-length encode the previous term. | StringBuilder per row; total work is proportional to generated output. |
| KMP - Find Pattern in String | Try every start and compare pattern. O(n*m). | Rolling hash / Rabin-Karp average O(n+m). | KMP LPS table avoids rechecking characters. O(n+m). |
| Rabin-Karp String Hashing | Compare every substring directly. O(n*m). | Rolling hash for O(1) window hash updates. | Double hash or verify matches to control collisions. |

---

## String Algorithm Comparison

| Algorithm | Time | Space | Use When |
|-----------|------|-------|----------|
| Brute Force | O(nm) | O(1) | Short strings |
| KMP | O(n+m) | O(m) | Pattern search, guaranteed linear |
| Rabin-Karp | O(n+m) avg | O(1) | Multiple pattern search |
| Z-Algorithm | O(n+m) | O(n+m) | Pattern + string properties |

#sde-sheet #strings #kmp #day15
