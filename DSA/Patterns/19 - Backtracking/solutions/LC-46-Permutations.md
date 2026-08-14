# Permutations (LC 46)

**Difficulty**: Medium  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/permutations/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Backtracking/Permutations.md)

## Problem Statement
Given an array `nums` of distinct integers, return all possible permutations.

**Example:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

## Approach 1: Iterative (Build Permutations)

### Java Code
```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        
        for (int num : nums) {
            List<List<Integer>> newResult = new ArrayList<>();
            for (List<Integer> perm : result) {
                for (int i = 0; i <= perm.size(); i++) {
                    List<Integer> newPerm = new ArrayList<>(perm);
                    newPerm.add(i, num);
                    newResult.add(newPerm);
                }
            }
            result = newResult;
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(n! × n²)
- **Space**: O(n!)

## Approach 2: Backtracking (Optimized)

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
            if (current.contains(num)) continue; // Skip if already used
            
            current.add(num); // Choose
            backtrack(nums, current, result); // Explore
            current.remove(current.size() - 1); // Unchoose
        }
    }
}
```

### Complexity
- **Time**: O(n! × n)
- **Space**: O(n) - Recursion depth

## Key Takeaways
- Classic backtracking: choose, explore, unchoose
- Track used elements with contains() or boolean array
- Base case: when current size equals input size
