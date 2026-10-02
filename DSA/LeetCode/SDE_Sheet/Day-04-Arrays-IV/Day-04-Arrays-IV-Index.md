# Day 4 — Arrays IV (Hard Problems)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Arrays — Hard Hitters
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Two Sum](Two-Sum.md) | LeetCode 1 | Easy | [LeetCode](https://leetcode.com/problems/two-sum/)
- [ ] [4-Sum](4-Sum.md) | LeetCode 18 | Medium | [LeetCode](https://leetcode.com/problems/4sum/)
- [ ] [Longest Consecutive Sequence](Longest-Consecutive-Sequence.md) | LeetCode 128 | Medium | [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)
- [ ] [Largest Subarray with Zero Sum](Largest-Subarray-with-Zero-Sum.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Largest+Subarray+with+Zero+Sum)
- [ ] [Count Subarrays with XOR = k](Count-Subarrays-with-XOR-k.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Count+Subarrays+with+XOR+%3D+k)
- [ ] [Longest Subarray with Sum K](Longest-Subarray-with-Sum-K.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Longest+Subarray+with+Sum+K)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Two Sum | Try every pair. O(n^2). | Sort and use two pointers, preserving original indexes. O(n log n). | HashMap complement lookup in one pass. O(n), O(n) space. |
| 4-Sum | Use four nested loops. O(n^4). | Store pair sums in a map. O(n^2) space. | Sort, fix two numbers, then two pointers with duplicate skipping. O(n^3). |
| Longest Consecutive Sequence | For each number, search for the next values repeatedly. O(n^2) or worse. | Sort and count streaks. O(n log n). | HashSet; start counting only at sequence starts. O(n). |
| Largest Subarray with Zero Sum | Check all subarrays and compute sums. O(n^2) to O(n^3). | Use prefix sums. | Store first index of each prefix sum in a HashMap. O(n). |
| Count Subarrays with XOR = k | Compute XOR for every subarray. O(n^2). | Keep prefix XORs and compare pairs. O(n^2). | Prefix XOR frequency map using x ^ k. O(n). |
| Longest Subarray with Sum K | Try every subarray. O(n^2). | Sliding window works only for non-negative arrays. O(n). | Prefix sum first-index map works with negative numbers too. O(n). |

---

## The Prefix Sum Pattern — Master Template

```
Problem type         → Technique
─────────────────────────────────────────────
Sum = k              → prefixSum + HashMap
XOR = k              → prefixXOR + HashMap
Zero sum subarray    → prefixSum + HashMap (first occurrence)
Max length subarray  → prefixSum + HashMap (first occurrence)
Count subarrays      → prefixSum + HashMap (frequency count)
```

---

## Interview Tips for Arrays IV

> 💡 **Prefix Sum + HashMap** solves a huge class of subarray problems
> 💡 **Always handle long for 4-sum** to avoid integer overflow
> 💡 **HashSet start-detection trick** enables O(n) consecutive sequence

#sde-sheet #arrays #day4 #prefix-sum #hashmap
