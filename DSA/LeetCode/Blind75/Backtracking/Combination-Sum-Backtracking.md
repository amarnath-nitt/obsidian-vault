# Combination Sum (Backtracking)

**Difficulty:** Medium  
**Category:** Backtracking  
**LeetCode Link:** [Combination Sum](https://leetcode.com/problems/combination-sum/)

---

## Problem Statement

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

**Example:**
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

**Constraints:**
- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

---

## Intuition

Use backtracking to explore all possible combinations. For each number, we can either include it (possibly multiple times) or skip it.

---

## Approach: Backtracking

### Algorithm
1. Sort candidates (optional, helps with optimization)
2. Use backtracking with current combination and remaining target
3. For each candidate, try including it and recurse
4. If target becomes 0, add combination to result
5. If target < 0, backtrack

### Java Code
```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);  // Optional optimization
        backtrack(candidates, target, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] candidates, int target, int start, 
                          List<Integer> current, List<List<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        if (target < 0) {
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            // Include current candidate
            current.add(candidates[i]);
            
            // Recurse with same start index (can reuse same number)
            backtrack(candidates, target - candidates[i], i, current, result);
            
            // Backtrack
            current.remove(current.size() - 1);
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(N^(T/M)) where N = candidates, T = target, M = min candidate
- **Space Complexity:** O(T/M) - Recursion depth

---

## Key Takeaways

1. **Pattern:** Backtracking with repeated elements allowed
2. **Reuse:** Same index in recursion allows reusing numbers
3. **Pruning:** Sorting enables early termination
4. **State:** Track current combination and remaining target

---

## Tags
#backtracking #recursion #combinations #medium #blind75
