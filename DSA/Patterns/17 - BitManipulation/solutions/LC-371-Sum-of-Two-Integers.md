---
solved: false
difficulty: Medium
pattern: Bit Manipulation
lc_number: 371
date_solved: 
tags:
  - dsa
  - bit-manipulation
  - medium
---
# Sum of Two Integers (LC 371)

**Difficulty**: Medium  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/sum-of-two-integers/

## Problem Statement
Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

**Example:**
```
Input: a = 1, b = 2
Output: 3
```

## Approach: Full Adder Logic

### Intuition
Sum = `a ^ b` (XOR handles sum without carry).
Carry = `(a & b) << 1` (AND finds bits that generate carry, shift left to apply to next position).
Repeat until carry is 0.

### Java Code
```java
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}
```

### Complexity
- **Time**: O(1) (bounded by number of bits)
- **Space**: O(1)

## Key Takeaways
- Hardware addition logic implemented in software
- `^` is sum, `& << 1` is carry
