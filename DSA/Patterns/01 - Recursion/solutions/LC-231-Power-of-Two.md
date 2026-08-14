# Power of Two (LC 231)

**Difficulty**: Easy  
**Pattern**: Recursion  
**LeetCode**: https://leetcode.com/problems/power-of-two/

## Problem Statement
Return `true` if `n` is a power of two.

## Recursive Idea
A positive number is a power of two if it can keep dividing evenly by `2` until it becomes `1`.

## Java Code
```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n == 1) {
            return true;
        }
        if (n <= 0 || n % 2 != 0) {
            return false;
        }
        return isPowerOfTwo(n / 2);
    }
}
```

## Alternative Optimal Solution: Bit Manipulation
A power of two has exactly one set bit. Subtracting `1` flips that bit and all bits after it, so `n & (n - 1)` becomes `0`.

### Why The Bit Trick Works

**Powers of two in binary** have exactly ONE '1' bit set:
```
1 = 0001 (2^0)
2 = 0010 (2^1)
4 = 0100 (2^2)
8 = 1000 (2^3)
16 = 10000 (2^4)
```

All other numbers have **multiple '1' bits**:
```
3 = 0011 (two 1-bits)
5 = 0101 (two 1-bits)
6 = 0110 (two 1-bits)
7 = 0111 (three 1-bits)
```

**When you subtract 1 from a power of two**, something magical happens:

```
  4 = 0100
- 1 = 0001
-------
  3 = 0011

  8 = 1000
- 1 = 0001
-------
  7 = 0111

  16 = 10000
-  1 = 00001
-------
  15 = 01111
```

The single '1' bit flips to '0', and all bits to the right become '1'.

**Now apply AND** to n and (n-1):
```
  4 & 3: 0100 & 0011 = 0000 ✓ (power of two!)
  8 & 7: 1000 & 0111 = 0000 ✓ (power of two!)
  3 & 2: 0011 & 0010 = 0010 ✗ (not a power of two)
  5 & 4: 0101 & 0100 = 0100 ✗ (not a power of two)
```

**Why this works:**
- For power of two: the single '1' bit cancels out in AND → result is 0
- For non-power: multiple '1' bits remain after AND → result ≠ 0

**The complete check:**
```java
return n > 0 && (n & (n - 1)) == 0;
```
- `n > 0`: Handles edge case (0 is not a power of two)
- `(n & (n - 1)) == 0`: True only for powers of two

```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}
```

### Alternative Complexity
- **Time**: O(1)
- **Space**: O(1)

## Complexity
- **Time**: O(log n)
- **Space**: O(log n)

## Key Takeaways
- Recursive division is useful when each call shrinks the input by a factor.
