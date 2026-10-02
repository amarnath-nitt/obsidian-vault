# Combination Sum I

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
