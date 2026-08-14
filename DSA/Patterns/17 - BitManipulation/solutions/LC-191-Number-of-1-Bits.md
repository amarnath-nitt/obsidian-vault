# Number of 1 Bits (LC 191)

**Difficulty**: Easy  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/number-of-1-bits/

## Problem Statement
Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).

**Example:**
```
Input: n = 11 (binary 00000000000000000000000000001011)
Output: 3
```

## Approach 1: Loop and Flip

### Java Code
```java
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count += (n & 1);
            n = n >>> 1; // Unsigned right shift
        }
        return count;
    }
}
```

## Approach 2: Brian Kernighan's Algorithm (Optimized)

### Intuition
`n & (n-1)` flips the least significant set bit to 0.
Example: `n=12` (1100). `n-1=11` (1011). `n & (n-1) = 1000`. One bit removed.
Repeat until n becomes 0. Loop runs exactly as many times as there are 1s.

### Java Code
```java
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n = n & (n - 1);
            count++;
        }
        return count;
    }
}
```

### Complexity
- **Time**: O(k) where k is number of 1s (or O(32) = O(1))
- **Space**: O(1)

## Key Takeaways
- `n & (n-1)` removes the last set bit
- `>>>` is unsigned shift, `>>` is signed shift
