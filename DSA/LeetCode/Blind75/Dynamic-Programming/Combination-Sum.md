# Combination Sum

**Difficulty:** Medium  
**Category:** Dynamic Programming  
**LeetCode Link:** [Combination Sum](https://leetcode.com/problems/combination-sum/)

---

## Approach: Backtracking

### Java Code
```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] candidates, int target, int start, 
                          List<Integer> current, List<List<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        if (target < 0) return;
        
        for (int i = start; i < candidates.length; i++) {
            current.add(candidates[i]);
            backtrack(candidates, target - candidates[i], i, current, result);
            current.remove(current.size() - 1);
        }
    }
}
```

### Complexity
- **Time:** O(N^(T/M))
- **Space:** O(T/M)

---

## Tags
#dynamic-programming #backtracking #medium #blind75
