---
solved: false
difficulty: Medium
pattern: Dynamic Programming
lc_number: 213
date_solved: 
tags:
  - dsa
  - dynamic-programming
  - medium
---
# House Robber II (LC 213)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/house-robber-ii/

## Problem Statement
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Similar to House Robber I, you cannot rob adjacent houses.
Return the maximum amount of money you can rob tonight without alerting the police.

**Example:**
```
Input: nums = [2,3,2]
Output: 3 (cannot rob 2 and 2)
```

## Approach: Break Circle

### Intuition
The circle means we can't rob both First and Last house.
Two cases:
1. Rob houses `0` to `n-2` (Exclude Last).
2. Rob houses `1` to `n-1` (Exclude First).
Result is `max(Case1, Case2)`.
Use strict House Robber I helper function.

### Java Code
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        
        return Math.max(robRange(nums, 0, nums.length - 2), 
                        robRange(nums, 1, nums.length - 1));
    }
    
    private int robRange(int[] nums, int start, int end) {
        int prev2 = 0;
        int prev1 = 0;
        
        for (int i = start; i <= end; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Problem decomp: Circle -> Linear Arrays
