---
solved: false
difficulty: Medium
pattern: Dynamic Programming
lc_number: 152
date_solved: 
tags:
  - dsa
  - dynamic-programming
  - medium
---
# Maximum Product Subarray (LC 152)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/maximum-product-subarray/

## Problem Statement
Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

**Example:**
```
Input: nums = [2,3,-2,4]
Output: 6 ([2,3])
```

## Approach: Tracking Max and Min

### Intuition
Product can become negative. A small negative number multiplied by a negative number becomes a large positive number.
So we need to track both `max_so_far` and `min_so_far`.
`current_max = max(num, max_so_far * num, min_so_far * num)`
`current_min = min(num, max_so_far * num, min_so_far * num)`
Update global max.

### Java Code
```java
class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) return 0;
        
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            int curr = nums[i];
            int tempMax = Math.max(curr, Math.max(maxSoFar * curr, minSoFar * curr));
            minSoFar = Math.min(curr, Math.min(maxSoFar * curr, minSoFar * curr));
            
            maxSoFar = tempMax;
            
            result = Math.max(result, maxSoFar);
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- When negatives are involved, keep track of Min (potential future Max)
