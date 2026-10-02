---
solved: false
difficulty: Easy
pattern: Modified Binary Search
lc_number: 69
date_solved: 
tags:
  - dsa
  - modified-binary-search
  - easy
---
# Sqrt(x) (LC 69)

**Difficulty**: Easy  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/sqrtx/

## Problem Statement
Given a non-negative integer `x`, compute and return the square root of `x`.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

**Example:**
```
Input: x = 8
Output: 2
```

## Approach: Binary Search on Answer

### Intuition
Search range `[0, x]`.
Find largest integer `ans` such that `ans * ans <= x`.
If `mid * mid <= x`, `mid` is a candidate, try larger (`left = mid + 1`, result = mid).
If `mid * mid > x`, too big (`right = mid - 1`).
Use `long` to avoid overflow during `mid * mid`.

### Java Code
```java
class Solution {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        int left = 1, right = x;
        int ans = 0;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (mid <= x / mid) { // Use division to avoid overflow
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return ans;
    }
}
```

### Complexity
- **Time**: O(log X)
- **Space**: O(1)

## Key Takeaways
- Search on Answer Space
- Overflow handling (`mid <= x / mid` vs `mid * mid <= x`)
