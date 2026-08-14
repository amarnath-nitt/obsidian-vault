# Climbing Stairs

**Difficulty:** Easy  
**Category:** Dynamic Programming  
**LeetCode Link:** [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

---

## Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**
```
Input: n = 2
Output: 2
Explanation: 1+1 or 2
```

**Example 2:**
```
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, or 2+1
```

**Constraints:**
- `1 <= n <= 45`

---

## Intuition

This is a Fibonacci problem! To reach step `n`, you must come from step `n-1` (take 1 step) or step `n-2` (take 2 steps). So `ways(n) = ways(n-1) + ways(n-2)`.

---

## Approach 1: Recursion (Naive)

### Algorithm
1. Base cases: n=1 → 1 way, n=2 → 2 ways
2. Recursively calculate: ways(n) = ways(n-1) + ways(n-2)

### Java Code
```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(2^n) - Exponential, many repeated calculations
- **Space Complexity:** O(n) - Recursion stack

### Drawbacks
- ❌ Extremely slow for large n
- ❌ Recalculates same subproblems many times

---

## Approach 2: Dynamic Programming (Optimized)

### Algorithm
1. Use two variables to track previous two values
2. Iterate from 3 to n
3. Calculate current as sum of previous two
4. Update variables for next iteration

### Java Code
```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        
        int prev2 = 1;  // ways(1)
        int prev1 = 2;  // ways(2)
        
        for (int i = 3; i <= n; i++) {
            int current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single loop
- **Space Complexity:** O(1) - Only two variables

### Why This is Better
- ✅ Linear time vs exponential
- ✅ Constant space
- ✅ No recursion overhead
- ✅ Simple and efficient

---

## Alternative: DP Array

### Java Code
```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
}
```

- **Space:** O(n) but easier to understand

---

## Key Takeaways

1. **Pattern:** Fibonacci sequence in disguise
2. **DP optimization:** Reduce space from O(n) to O(1)
3. **Recurrence relation:** f(n) = f(n-1) + f(n-2)
4. **Bottom-up:** Build solution from base cases

---

## Step-by-Step Example

For `n = 5`:
```
n=1: 1 way
n=2: 2 ways
n=3: 1+2 = 3 ways
n=4: 2+3 = 5 ways
n=5: 3+5 = 8 ways
```

---

## Tags
#dynamic-programming #fibonacci #easy #blind75
