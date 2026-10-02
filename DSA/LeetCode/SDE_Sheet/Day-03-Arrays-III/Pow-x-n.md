# Pow(x, n)

**LeetCode 50** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/powx-n/)

### Problem
Implement `pow(x, n)`. Handle negative `n`.

### Approach (Fast Exponentiation / Binary Exponentiation)

- If `n` is even: `x^n = (x^(n/2))^2`
- If `n` is odd: `x^n = x * x^(n-1)`
- If `n < 0`: `x^n = (1/x)^(-n)`

This reduces O(n) multiplications to O(log n).

### Java Solution

```java
class Solution {
    public double myPow(double x, int n) {
        long N = n; // avoid Integer.MIN_VALUE overflow
        if (N < 0) { x = 1 / x; N = -N; }
        return fastPow(x, N);
    }

    private double fastPow(double x, long n) {
        if (n == 0) return 1.0;
        if (n % 2 == 0) {
            double half = fastPow(x, n / 2);
            return half * half;
        }
        return x * fastPow(x, n - 1);
    }
}
```

**Complexity:** Time O(log n) · Space O(log n) recursion stack

---
