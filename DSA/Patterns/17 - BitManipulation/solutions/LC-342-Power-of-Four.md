---
solved: false
difficulty: Easy
pattern: Bit Manipulation
lc_number: 342
date_solved: 
tags:
  - dsa
  - bit-manipulation
  - easy
---
# Power of Four (LC 342)

**Difficulty**: Easy  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/power-of-four/

## Problem Statement
Given an integer `n`, return `true` if it is a power of four. Otherwise, return `false`.

**Example:**
```
Input: n = 16
Output: true
```

## Approach: Bit Masks

### Intuition
First, check if `n` is power of two: `n > 0 && (n & (n - 1)) == 0`.
If it is power of two, it has only one bit set.
For power of four (1, 4, 16, 64...), the bit must be at an even position (0-indexed: 0, 2, 4, 6...).
Create a mask with 1s at all even positions: `0x55555555` (binary `...010101`).
If `(n & mask) != 0`, then the single bit is at an even position.

### Java Code
```java
class Solution {
    public boolean isPowerOfFour(int n) {
        return (n > 0) && 
               ((n & (n - 1)) == 0) && 
               ((n & 0x55555555) != 0);
    }
}
```

### Complexity
- **Time**: O(1)
- **Space**: O(1)

## Key Takeaways
- Use hex masks for position checks
- Combine checks (Power of 2 + Specific Position)
