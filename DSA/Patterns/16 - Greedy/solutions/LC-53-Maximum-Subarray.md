---
solved: false
difficulty: Medium
pattern: Greedy
lc_number: 53
date_solved: 
tags:
  - dsa
  - greedy
  - medium
---
# Maximum Subarray (LC 53)

**Difficulty**: Medium  
**Pattern**: Greedy / Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/maximum-subarray/

## Problem Statement
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

**Example:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: Subarray [4,-1,2,1] has the largest sum 6.
```

## Approach 1: Brute Force

### Intuition
Check all subarrays (O(n²)).

## Approach 2: Kadane's Algorithm (Greedy/DP)

### Intuition
Decide at each position: Should I start a new subarray here (discarding previous history), or extend the existing one?
If `current_sum + nums[i] < nums[i]`, it means `current_sum` was contributing negatively (or less than starting fresh), so we restart.
Equivalently: `current_sum = max(nums[i], current_sum + nums[i])`.

### Java Code
```java
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSoFar = nums[0];
        int currentMax = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            // Either extend previous subarray or start new one
            currentMax = Math.max(nums[i], currentMax + nums[i]);
            maxSoFar = Math.max(maxSoFar, currentMax);
        }
        
        return maxSoFar;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Approach 3: Divide and Conquer

### Intuition
Split array into left and right halves. Max crossing sum + max left + max right logic.

### Complexity
- **Time**: O(n log n)
- **Space**: O(log n)

## Key Takeaways
- Kadane's Algorithm is the standard O(n) solution
- Subarray must be contiguous
- Handle all negative numbers correctly (Kadane's does this automatically with `max(nums[i], ...)`)
