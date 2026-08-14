# Fibonacci Number (LC 509)

**Difficulty**: Easy  
**Pattern**: Recursion / Memoization  
**LeetCode**: https://leetcode.com/problems/fibonacci-number/

## Problem Statement
Return the `n`th Fibonacci number. `fib(0) = 0`, `fib(1) = 1`, and `fib(n) = fib(n - 1) + fib(n - 2)`.

## Approach: Memoized Recursion
Plain recursion repeats the same calls many times. Cache each computed value once.

## Java Code
```java
class Solution {
    public int fib(int n) {
        int[] memo = new int[n + 1];
        Arrays.fill(memo, -1);
        return solve(n, memo);
    }

    private int solve(int n, int[] memo) {
        if (n <= 1) {
            return n;
        }
        if (memo[n] != -1) {
            return memo[n];
        }
        memo[n] = solve(n - 1, memo) + solve(n - 2, memo);
        return memo[n];
    }
}
```

## Alternative Optimal Solution: Bottom-Up DP
Build the answer from the base cases upward. This removes recursion and only keeps the previous two values.

```java
class Solution {
    public int fib(int n) {
        if (n <= 1) {
            return n;
        }

        int prev2 = 0;
        int prev1 = 1;
        for (int i = 2; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
```

### Alternative Complexity
- **Time**: O(n)
- **Space**: O(1)

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Takeaways
- Tree recursion often creates repeated subproblems.
- Memoization turns exponential recursion into linear time.
