# Climbing Stairs (LC 70)

**Difficulty**: Easy  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/climbing-stairs/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Dynamic-Programming/Climbing-Stairs.md)

## Problem Statement
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example:**
```
Input: n = 3
Output: 3
Explanation: Three ways: 1+1+1, 1+2, 2+1
```

## Approach 1: Recursion (Brute Force)

### Java Code
```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        return climbStairs(n-1) + climbStairs(n-2);
    }
}
```

### Complexity
- **Time**: O(2^n) - Exponential due to repeated calculations
- **Space**: O(n) - Recursion stack

## Approach 2: DP with Memoization

### Java Code
```java
class Solution {
    public int climbStairs(int n) {
        int[] memo = new int[n + 1];
        return climb(n, memo);
    }
    
    private int climb(int n, int[] memo) {
        if (n <= 2) return n;
        if (memo[n] > 0) return memo[n];
        
        memo[n] = climb(n-1, memo) + climb(n-2, memo);
        return memo[n];
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n)

## Approach 3: DP Tabulation (Optimized)

### Java Code
```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        
        return dp[n];
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n)

## Approach 4: Space-Optimized DP

### Java Code
```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        
        int prev2 = 1, prev1 = 2;
        for (int i = 3; i <= n; i++) {
            int curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        
        return prev1;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Takeaways
- Classic Fibonacci pattern: dp[i] = dp[i-1] + dp[i-2]  
- Can optimize space from O(n) to O(1)
- Foundation for many DP staircase problems
