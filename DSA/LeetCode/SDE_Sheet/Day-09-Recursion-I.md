# Day 9 — Recursion & Backtracking I

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Recursion · Backtracking — Subsets, Permutations, Combinations
**Difficulty Mix:** Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Subsets]] | 78 | Medium | ⬜ |
| 2 | [[#Subsets II (with duplicates)]] | 90 | Medium | ⬜ |
| 3 | [[#Combination Sum I]] | 39 | Medium | ⬜ |
| 4 | [[#Combination Sum II]] | 40 | Medium | ⬜ |
| 5 | [[#Permutations]] | 46 | Medium | ⬜ |
| 6 | [[#Permutations II (with duplicates)]] | 47 | Medium | ⬜ |

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

## Subsets

**LeetCode 78** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/subsets/)

### Problem
Given an array of unique integers, return all possible subsets (power set).

### Approach

- At each index, we have 2 choices: **include** or **exclude** the element
- Recurse with `start+1` to avoid revisiting elements

### Java Solution

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, int start, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current)); // add at every node

        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);           // choose
            backtrack(nums, i + 1, current, result);
            current.remove(current.size() - 1); // unchoose
        }
    }
}
```

**Complexity:** Time O(n × 2ⁿ) · Space O(n × 2ⁿ)

---

## Subsets II (with duplicates)

**LeetCode 90** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/subsets-ii/)

### Problem
Same as Subsets, but array may contain duplicates. Return unique subsets.

### Approach

- **Sort** first to group duplicates
- At the same recursion level, skip duplicate values (not the first occurrence)

### Java Solution

```java
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, int start, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current));

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i-1]) continue; // skip dup at same level
            current.add(nums[i]);
            backtrack(nums, i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
}
```

**Complexity:** Time O(n × 2ⁿ) · Space O(n × 2ⁿ)

---

## Combination Sum I

**LeetCode 39** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/combination-sum/)

### Problem
Find all combinations that sum to target. Numbers can be reused.

### Approach

- Can reuse elements → don't advance `start` when recursing with same element
- Prune: if remaining < 0, stop

### Java Solution

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, 0, target, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int start, int remain,
                           List<Integer> current, List<List<Integer>> result) {
        if (remain == 0) { result.add(new ArrayList<>(current)); return; }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remain) break; // pruning (sorted array)
            current.add(candidates[i]);
            backtrack(candidates, i, remain - candidates[i], current, result); // i not i+1 (reuse)
            current.remove(current.size() - 1);
        }
    }
}
```

**Complexity:** Time O(n^(T/M)) where T=target, M=min candidate · Space O(T/M)

---

## Combination Sum II

**LeetCode 40** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/combination-sum-ii/)

### Problem
Each number may only be used **once**. Array may have duplicates. Return unique combinations.

### Approach

- Sort + skip duplicates at same level (same as Subsets II)
- Advance `i+1` in recursion (no reuse)

### Java Solution

```java
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, 0, target, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] candidates, int start, int remain,
                           List<Integer> current, List<List<Integer>> result) {
        if (remain == 0) { result.add(new ArrayList<>(current)); return; }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remain) break;
            if (i > start && candidates[i] == candidates[i-1]) continue; // skip dup
            current.add(candidates[i]);
            backtrack(candidates, i + 1, remain - candidates[i], current, result);
            current.remove(current.size() - 1);
        }
    }
}
```

---

## Permutations

**LeetCode 46** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/permutations/)

### Problem
Return all possible permutations of unique integers.

### Approach (Swap-based)

- Swap `nums[start]` with each element from `start` to `end`
- Recurse with `start+1`
- Swap back (backtrack)

### Java Solution

```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, result);
        return result;
    }

    private void backtrack(int[] nums, int start, List<List<Integer>> result) {
        if (start == nums.length) {
            List<Integer> perm = new ArrayList<>();
            for (int n : nums) perm.add(n);
            result.add(perm);
            return;
        }
        for (int i = start; i < nums.length; i++) {
            swap(nums, start, i);
            backtrack(nums, start + 1, result);
            swap(nums, start, i); // backtrack
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
    }
}
```

**Complexity:** Time O(n × n!) · Space O(n!)

---

## Permutations II (with duplicates)

**LeetCode 47** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/permutations-ii/)

### Problem
Return all unique permutations. Array may contain duplicates.

### Approach

- Sort first
- Use a `used[]` boolean array
- At each level, skip if `nums[i] == nums[i-1] && !used[i-1]` (skip dup in same position)

### Java Solution

```java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, used, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, boolean[] used,
                           List<Integer> current, List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current)); return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            if (i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue; // skip dup
            used[i] = true;
            current.add(nums[i]);
            backtrack(nums, used, current, result);
            current.remove(current.size() - 1);
            used[i] = false;
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
