# Dynamic Programming — Concept

## What Is It?

Dynamic Programming (DP) solves problems by breaking them into **overlapping subproblems** and storing results to avoid recomputation. It works when a problem has **optimal substructure** (optimal solution = optimal sub-solutions) and **overlapping subproblems**.

---

## When to Use

> **Trigger keywords:** "minimum/maximum", "count ways", "is it possible", "longest/shortest", "optimize"

| Trigger | Example |
|---------|---------|
| **Count** the number of ways | Climbing Stairs, Decode Ways |
| **Minimize/maximize** a value | Coin Change, House Robber |
| **Can we reach** / is it possible | Word Break, Jump Game |
| **Longest/shortest** sequence | LIS, LCS, Edit Distance |

---

## Framework: FAST Method

1. **F**ind the recursive solution
2. **A**nalyze for overlapping subproblems
3. **S**ave results (memoization / tabulation)
4. **T**urn bottom-up (optional optimization)

---

## Variants

### 1. Linear DP (1D)
```java
// House Robber: dp[i] = max money up to house i
dp[0] = nums[0];
dp[1] = Math.max(nums[0], nums[1]);
for (int i = 2; i < n; i++) {
    dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
}
```

### 2. Grid DP (2D)
```java
// Unique Paths: dp[i][j] = ways to reach (i,j)
for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
        if (i == 0 || j == 0) dp[i][j] = 1;
        else dp[i][j] = dp[i-1][j] + dp[i][j-1];
    }
}
```

### 3. Knapsack (0/1)
```java
// Can we make target sum from array elements?
boolean[] dp = new boolean[target + 1];
dp[0] = true;
for (int num : nums) {
    for (int j = target; j >= num; j--) { // reverse to avoid reuse
        dp[j] = dp[j] || dp[j - num];
    }
}
```

### 4. String DP (LCS)
```java
for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= n; j++) {
        if (s1.charAt(i-1) == s2.charAt(j-1))
            dp[i][j] = dp[i-1][j-1] + 1;
        else
            dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
    }
}
```

---

## Visual Walkthrough

### House Robber: `[2, 7, 9, 3, 1]`
```
Houses:  [2]  [7]  [9]  [3]  [1]
dp[0] = 2
dp[1] = max(2, 7) = 7
dp[2] = max(7, 2+9) = 11     ← rob house 0 + house 2
dp[3] = max(11, 7+3) = 11
dp[4] = max(11, 11+1) = 12   ← rob house 0 + house 2 + house 4

Answer: 12
```

---

## How to Identify DP Type

| If you see... | DP Type | Example |
|---------------|---------|---------|
| Single array/sequence | Linear 1D | House Robber, Climbing Stairs |
| Two sequences | 2D String DP | LCS, Edit Distance |
| Grid/matrix | Grid DP | Unique Paths, Min Path Sum |
| "Include or exclude" items | Knapsack | Partition Equal Subset Sum |
| Intervals | Interval DP | Burst Balloons |

---

## Time/Space Complexity

| DP Type | Time | Space | Space-Optimized |
|---------|------|-------|-----------------|
| Linear 1D | O(n) | O(n) | O(1) with 2 vars |
| Grid 2D | O(m×n) | O(m×n) | O(n) with 1 row |
| Knapsack | O(n×W) | O(n×W) | O(W) |
| LCS/Edit Distance | O(m×n) | O(m×n) | O(n) |

---

## Common Mistakes

1. **Wrong state definition** → Clearly define what `dp[i]` represents before coding
2. **Wrong transition** → Draw out small examples to verify the recurrence
3. **Off-by-one in base cases** → Initialize `dp[0]` (and sometimes `dp[1]`) carefully
4. **Forgetting space optimization** → If dp[i] only depends on dp[i-1], use rolling variables

---

## Related Patterns

- [[01 - Recursion/Concept|Recursion]] — Top-down DP = memoized recursion
- [[19 - Backtracking/Concept|Backtracking]] — When backtracking has overlapping subproblems → DP
- [[16 - Greedy/Concept|Greedy]] — When greedy works, it's simpler than DP

---

#dynamic-programming #dp #dsa #concept
