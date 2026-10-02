---
solved: false
difficulty: Medium
pattern: Backtracking
lc_number: 47
date_solved: 
tags:
  - dsa
  - backtracking
  - medium
---
# Permutations II (LC 47)

**Difficulty**: Medium  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/permutations-ii/

## Problem Statement
Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations.

**Example:**
```
Input: nums = [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
```

## Approach: Sort + Skip Duplicates

### Intuition
Sort `nums` to group duplicates.
Use boolean `used` array.
When simpler `nums[i] == nums[i-1]`, we can only use `nums[i]` if `nums[i-1]` was used in the current recursive stack (or vice-versa, depending on logic).
Common logic: `if (i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue;`. This forces us to use the first instance of a duplicate before the second, avoiding duplicate permutations.

### Java Code
```java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(result, new ArrayList<>(), nums, new boolean[nums.length]);
        return result;
    }
    
    private void backtrack(List<List<Integer>> result, List<Integer> current, int[] nums, boolean[] used) {
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1])) {
                continue;
            }
            
            used[i] = true;
            current.add(nums[i]);
            backtrack(result, current, nums, used);
            used[i] = false;
            current.remove(current.size() - 1);
        }
    }
}
```

### Complexity
- **Time**: O(N * N!)
- **Space**: O(N)

## Key Takeaways
- Sorting facilitates duplicate handling
- Check `!used[i-1]` ensures we maintain relative order of duplicates
