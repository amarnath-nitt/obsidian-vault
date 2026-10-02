# String to Integer (atoi)

**LeetCode 8** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/string-to-integer-atoi/)

### Problem
Implement `atoi`. Handle leading spaces, sign, digits, overflow.

### Approach

1. Skip leading whitespace
2. Handle optional `+` or `-`
3. Parse digits until non-digit
4. Clamp to `[Integer.MIN_VALUE, Integer.MAX_VALUE]`

### Java Solution

```java
class Solution {
    public int myAtoi(String s) {
        int i = 0, n = s.length();
        while (i < n && s.charAt(i) == ' ') i++; // skip spaces

        int sign = 1;
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            if (s.charAt(i) == '-') sign = -1;
            i++;
        }

        long result = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            result = result * 10 + (s.charAt(i) - '0');
            i++;
            if (result * sign > Integer.MAX_VALUE) return Integer.MAX_VALUE;
            if (result * sign < Integer.MIN_VALUE) return Integer.MIN_VALUE;
        }
        return (int)(result * sign);
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---
