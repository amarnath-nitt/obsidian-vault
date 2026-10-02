# Divide Two Integers

**LeetCode 29** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/divide-two-integers/)

### Problem
Divide two integers without using multiplication, division, and mod operator.

### Approach
- We can find the quotient by shifting the divisor left (`divisor << i`) until it's just under the dividend.
- Subtract `(divisor << i)` from `dividend`, add `(1 << i)` to the quotient, and repeat.
- Handle overflow cases (like `Integer.MIN_VALUE / -1`).

### Java Solution

```java
class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE; // Overflow case
        }

        // Convert to long to prevent overflow during absolute value conversion
        long lDividend = Math.abs((long) dividend);
        long lDivisor = Math.abs((long) divisor);
        int quotient = 0;

        for (int i = 31; i >= 0; i--) {
            if ((lDivisor << i) <= lDividend) {
                lDividend -= (lDivisor << i);
                quotient += (1 << i);
            }
        }

        return (dividend > 0) == (divisor > 0) ? quotient : -quotient;
    }
}
```

**Complexity:** Time $O(\log(\text{dividend}))$ · Space $O(1)$

---
