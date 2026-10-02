---
solved: false
difficulty: Easy
pattern: Bit Manipulation
lc_number: 338
date_solved: 
tags:
  - dsa
  - bit-manipulation
  - easy
---
# Counting Bits (LC 338)

**Difficulty**: Easy  
**Pattern**: Bit Manipulation / DP  
**LeetCode**: https://leetcode.com/problems/counting-bits/

## Problem Statement
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1`'s in the binary representation of `i`.

**Example:**
```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10 (1)
3 --> 11 (2)
4 --> 100 (1)
5 --> 101 (2)
```

## Approach: DP / Bit Logic

### Intuition
Number of bits in `i` is related to `i/2` (i >> 1).
If `i` is even (ending in 0), `count(i) = count(i/2)` (shift right, no bit lost).
If `i` is odd (ending in 1), `count(i) = count(i/2) + 1`.

Or using `i & (i-1)`:
`count(i) = count(i & (i-1)) + 1`.

### Java Code
```java
class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            // ans[i] = ans[i >> 1] + (i & 1);
            // OR
            ans[i] = ans[i & (i - 1)] + 1;
        }
        
        return ans;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1) (excluding output)

## Key Takeaways
- Use previous results to compute current (DP)
- `i >> 1` removes LSB. `i & 1` gets LSB.
- Classic O(n) bit manipulation problem
