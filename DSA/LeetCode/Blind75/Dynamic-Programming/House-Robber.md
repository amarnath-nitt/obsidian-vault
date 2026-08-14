# House Robber

**Difficulty:** Medium  
**Category:** Dynamic Programming  
**LeetCode Link:** [House Robber](https://leetcode.com/problems/house-robber/)

---

## Problem Statement

You are a professional robber. Each house has a certain amount of money. Adjacent houses have security systems connected and will alert the police if two adjacent houses are broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob without alerting the police.

---

## Approach: DP with O(1) Space

### Java Code
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        
        int prev2 = 0;
        int prev1 = 0;
        
        for (int num : nums) {
            int current = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
}
```

### Complexity
- **Time:** O(n)
- **Space:** O(1)

---

## Tags
#dynamic-programming #medium #blind75
