# Combination Sum II

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
