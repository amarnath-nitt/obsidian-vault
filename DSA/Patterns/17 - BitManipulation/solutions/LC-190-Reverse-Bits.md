# Reverse Bits (LC 190)

**Difficulty**: Easy  
**Pattern**: Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/reverse-bits/

## Problem Statement
Reverse bits of a given 32 bits unsigned integer.

**Example:**
```
Input: n = 00000010100101000001111010011100
Output: 964176192 (00111001011110000010100101000000)
```

## Approach: Iterative Bit Manipulation

### Intuition
Iterate 32 times.
Extract LSB of `n` (`n & 1`).
Shift result left (`result << 1`) and add extracted bit (`result | bit`).
Shift `n` right (`n >> 1`).

### Java Code
```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result <<= 1;
            result |= (n & 1);
            n >>= 1;
        }
        return result;
    }
}
```

### Complexity
- **Time**: O(1) (32 iterations)
- **Space**: O(1)

## Key Takeaways
- Basic bit extraction and construction
- Understanding logical shifts vs arithmetic shifts (though here unsigned int behavior is simulated)
