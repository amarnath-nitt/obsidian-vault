# Combination Sum (LC 39)

**Difficulty**: Medium  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/combination-sum/

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order. The same number may be chosen from `candidates` an unlimited number of times.

**Example:**
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

## Approach: Backtracking

### Intuition
Standard backtracking template. At each step, we can either include the current candidate (and stay at the same index since we can reuse it) or move to the next candidate (and not include the current one anymore).

### Java Code
```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] candidates, int remain, int start, 
                           List<Integer> current, List<List<Integer>> result) {
        if (remain == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        if (remain < 0) {
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            current.add(candidates[i]);
            // Pass 'i' not 'i+1' because we can reuse the same element
            backtrack(candidates, remain - candidates[i], i, current, result); 
            current.remove(current.size() - 1);
        }
    }
}
```

### Complexity
- **Time**: O(N^(T/M)) where N is number of candidates, T is target, M is min value in candidates.
- **Space**: O(T/M) for recursion path

## Key Takeaways
- "Unlimited reuse" means we pass index `i` to recursive call
- Base cases: target reached (add to result) or exceeded (return)
- Sort candidates early to break early if `current > target` (optimization)
