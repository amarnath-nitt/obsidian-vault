# Subsets (LC 78)

**Difficulty**: Medium  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/subsets/

## Problem Statement
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**Example:**
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

## Approach 1: Cascading (Iterative)

### Intuition
Start with `[[]]`. For each number in `nums`, add it to all existing subsets to create new ones.
Start: `[[]]`
Add 1: `[[]]` + `[[1]]` -> `[[], [1]]`
Add 2: `[[], [1]]` + `[[2], [1,2]]` -> `[[], [1], [2], [1,2]]`

### Java Code
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        
        for (int num : nums) {
            int size = result.size();
            for (int i = 0; i < size; i++) {
                List<Integer> newSubset = new ArrayList<>(result.get(i));
                newSubset.add(num);
                result.add(newSubset);
            }
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(N × 2^N)
- **Space**: O(N × 2^N)

## Approach 2: Backtracking

### Intuition
For each index, we make a choice: either include `nums[i]` in the current subset, or don't.

### Java Code
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] nums, int start, List<Integer> current, List<List<Integer>> result) {
        // Add every valid subset generated
        result.add(new ArrayList<>(current));
        
        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);
            backtrack(nums, i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
}
```

## Key Takeaways
- Power set has 2^N elements
- Iterative approach is clean but backtracking is more generic
- For "Subsets II" (duplicates), we would sort and skip
