# Day 9 — Recursion & Backtracking I

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Recursion · Backtracking — Subsets, Permutations, Combinations
**Difficulty Mix:** Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Subsets](Subsets.md) | LeetCode 78 | Medium | [LeetCode](https://leetcode.com/problems/subsets/)
- [ ] [Subsets II (with duplicates)](Subsets-II-with-duplicates.md) | LeetCode 90 | Medium | [LeetCode](https://leetcode.com/problems/subsets-ii/)
- [ ] [Combination Sum I](Combination-Sum-I.md) | LeetCode 39 | Medium | [LeetCode](https://leetcode.com/problems/combination-sum/)
- [ ] [Combination Sum II](Combination-Sum-II.md) | LeetCode 40 | Medium | [LeetCode](https://leetcode.com/problems/combination-sum-ii/)
- [ ] [Permutations](Permutations.md) | LeetCode 46 | Medium | [LeetCode](https://leetcode.com/problems/permutations/)
- [ ] [Permutations II (with duplicates)](Permutations-II-with-duplicates.md) | LeetCode 47 | Medium | [LeetCode](https://leetcode.com/problems/permutations-ii/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Subsets | Generate all bitmasks. O(n*2^n). | Include/exclude recursion. Output-bound. | Backtracking with incremental path. O(n*2^n). |
| Subsets II | Generate all subsets, then remove duplicates with a set. | Sort first and skip duplicate choices during recursion. | Same sorted backtracking, avoiding duplicate branches early. |
| Combination Sum I | Generate many sequences and filter by target. Exponential. | Sort and prune when sum exceeds target. | Backtrack with same index for reuse and candidate pruning. |
| Combination Sum II | Generate all subsets, then dedupe. Exponential. | Sort and skip equal values at the same depth. | Backtrack each element once with early break when target is exceeded. |
| Permutations | Generate all arrangements by trying unused values. O(n!*n). | Use a used array/list. O(n) extra space. | Swap-based backtracking. O(n!*n), O(1) extra aside from recursion/output. |
| Permutations II | Generate all permutations, then use a set. | Sort and skip duplicate choices with used array. | Frequency-map backtracking creates only unique permutations. |

---

## Backtracking Template

```
void backtrack(state, choices) {
    if (base_case) {
        result.add(copy_of_state);
        return;
    }
    for (choice in choices) {
        if (is_valid(choice)) {
            make_choice(choice);       // choose
            backtrack(state, choices); // explore
            undo_choice(choice);       // unchoose
        }
    }
}
```

---

## Pattern Comparison

| Problem | Reuse? | Duplicates? | Dedup Strategy |
|---------|--------|-------------|----------------|
| Subsets | No | No | Start from `i+1` |
| Subsets II | No | Yes | Sort + skip `nums[i]==nums[i-1]` at same level |
| Combo Sum I | Yes | No | Start from `i` (same index) |
| Combo Sum II | No | Yes | Sort + skip dup + start from `i+1` |
| Permutations | N/A | No | Swap-based |
| Permutations II | N/A | Yes | `used[]` + skip dup with `!used[i-1]` |

#sde-sheet #recursion #backtracking #day9
