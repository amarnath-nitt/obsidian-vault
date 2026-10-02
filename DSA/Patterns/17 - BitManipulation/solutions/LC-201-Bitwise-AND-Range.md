---
solved: false
difficulty: Medium
pattern: Bit Manipulation
lc_number: 201
date_solved: 
tags:
  - dsa
  - bit-manipulation
  - medium
---
# Bitwise AND of Numbers Range (LC 201)

**Difficulty**: Medium  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/bitwise-and-of-numbers-range/

## Problem Statement
Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

**Example:**
```
Input: left = 5, right = 7
Output: 4
```

## Approach: Common Prefix

### Intuition
AND operation of a range preserves the common high-order bits of `left` and `right`.
Any bit that varies between `left` and `right` will eventually encounter a 0 in the sequence `left, left+1, ..., right`, causing the result bit to be 0.
We just need to find the common prefix of `left` and `right`.
Shift both right until they are equal, counting shifts. Then shift result back left.

### Java Code
```java
class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        
        // Find common prefix
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        
        return left << shift;
    }
}
```

### Complexity
- **Time**: O(1) (max 32 shifts)
- **Space**: O(1)

## Key Takeaways
- Range AND = Common High Bits
- Effectively finding the largest power of 2 prefix shared by both
