# Power of Two (LC 231)

**Difficulty**: Easy  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/power-of-two/

## Problem Statement
Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

**Example:**
```
Input: n = 16
Output: true
```

## Approach: Bit Trick

### Intuition
Power of two numbers have exactly one bit set in binary representation (e.g., 1, 2, 4, 8 -> 1, 10, 100, 1000).
`n & (n - 1)` removes the rightmost set bit.
If `n` is power of two, removing the only set bit should result in 0.
Constraint: `n > 0`.

### Java Code
```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) return false;
        return (n & (n - 1)) == 0;
    }
}
```

### Complexity
- **Time**: O(1)
- **Space**: O(1)

## Key Takeaways
- `n & (n-1)` clears the lowest set bit
- Standard check for power of 2
