# Permutations

**Difficulty:** Medium
**Category:** Backtracking
**LeetCode Link:** [Permutations](https://leetcode.com/problems/permutations/)

---

## Problem Statement

Given an array `nums` of distinct integers, return all possible permutations.

**Example:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

---

## Intuition

For permutations, every element can appear at every position. At each step, try adding each unused element. When the current list has all elements, we have a complete permutation. Use `contains` check (or a visited array) to avoid reusing elements.

---

## Approach: Backtracking

### Algorithm
1. If `current.size() == nums.length` → add to result
2. For each number in `nums`:
   - Skip if already in `current`
   - Add to current, recurse, remove (backtrack)

### Java Code
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, List<Integer> current, List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int num : nums) {
            if (current.contains(num)) continue;
            current.add(num);
            backtrack(nums, current, result);
            current.remove(current.size() - 1);
        }
    }
}
```

### Optimized with Boolean Visited Array
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, new boolean[nums.length], new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, boolean[] used, List<Integer> current, List<List<Integer>> result) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.add(nums[i]);
            backtrack(nums, used, current, result);
            current.remove(current.size() - 1);
            used[i] = false;
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n! × n) — n! permutations, each takes O(n) to copy
- **Space Complexity:** O(n) — recursion depth

---

## Key Takeaways

1. **Collect at leaf:** Only add to result when list is full (unlike Subsets)
2. **No `start` index:** Every element can go in every position — iterate all each time
3. **Visited array:** More efficient than `contains` — O(1) vs O(n) per check

---

## Tags
#backtracking #medium #blind75
