# Subsets

**Difficulty:** Medium
**Category:** Backtracking
**LeetCode Link:** [Subsets](https://leetcode.com/problems/subsets/)

---

## Problem Statement

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

**Example:**
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

---

## Intuition

At each step of backtracking, we add the current subset to the result (every partial state is valid). Then we try including each remaining element one at a time, recurse, and backtrack by removing it.

---

## Approach: Backtracking

### Algorithm
1. Add current `current` list to result at every call (not just at leaf)
2. For each index from `start` to end:
   - Add `nums[i]` to current
   - Recurse with `start = i + 1`
   - Remove last element (backtrack)

### Java Code
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int[] nums, int start, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current)); // Every state is a valid subset

        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);
            backtrack(nums, i + 1, current, result);
            current.remove(current.size() - 1); // Backtrack
        }
    }
}
```

### Step-by-Step Example
`nums = [1,2,3]`:
```
call(start=0): add [] → try 1
  call(start=1): add [1] → try 2
    call(start=2): add [1,2] → try 3
      call(start=3): add [1,2,3]
    backtrack → [1,2]
  backtrack → [1] → try 3
    call(start=3): add [1,3]
  backtrack → [1]
backtrack → [] → try 2 ...
```

### Complexity Analysis
- **Time Complexity:** O(2^n × n) — 2^n subsets, each takes O(n) to copy
- **Space Complexity:** O(n) — recursion depth

---

## Key Takeaways

1. **Add at every node:** Unlike permutations/combinations, collect result at every recursive call
2. **`start` index:** Prevents duplicates by only moving forward
3. **Backtrack:** Remove last element after recursion to restore state

---

## Tags
#backtracking #medium #blind75
