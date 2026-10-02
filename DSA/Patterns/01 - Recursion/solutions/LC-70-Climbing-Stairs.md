---
solved: true
difficulty: Easy
pattern: Recursion
lc_number: 70
date_solved: 
tags:
  - dsa
  - recursion
  - easy
---
# Climbing Stairs (LC 70)

**Difficulty**: Easy  
**Pattern**: Recursion / Memoization  
**LeetCode**: https://leetcode.com/problems/climbing-stairs/

## Problem Statement
You can climb `1` or `2` steps at a time. Return the number of distinct ways to reach step `n`.

## Approach: Top-Down DP
Ways to reach `n` = ways to reach `n - 1` + ways to reach `n - 2`.

## Java Code
```java
class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n + 1];
        return count(n, memo);
    }

    private int count(int n, int[] memo) {
        if (n <= 2) {
            return n;
        }
        if (memo[n] != 0) {
            return memo[n];
        }
        memo[n] = count(n - 1, memo) + count(n - 2, memo);
        return memo[n];
    }
}
```

## Alternative Optimal Solution: Iterative DP
The recurrence is Fibonacci-style, so keep only the last two answers.

```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int oneStepBefore = 2;
        int twoStepsBefore = 1;
        for (int step = 3; step <= n; step++) {
            int current = oneStepBefore + twoStepsBefore;
            twoStepsBefore = oneStepBefore;
            oneStepBefore = current;
        }
        return oneStepBefore;
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
- This is Fibonacci with a story wrapped around it.
- Memoize because the recursion tree overlaps heavily.
