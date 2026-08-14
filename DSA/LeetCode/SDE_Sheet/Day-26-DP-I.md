# Day 26 — Dynamic Programming I (1D DP)

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** DP — 1D Problems, Fibonacci, House Robber
**Difficulty Mix:** Easy / Medium

---

## DP Framework

```
Step 1: Define the state
  dp[i] = answer for subproblem of size i

Step 2: Find the recurrence
  dp[i] = f(dp[i-1], dp[i-2], ...)

Step 3: Establish base cases
  dp[0] = ?, dp[1] = ?

Step 4: Order of computation
  Usually left to right (smaller to larger)

Step 5: Extract the answer
  Usually dp[n] or max(dp)
```

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Climbing Stairs]] | 70 | Easy | ⬜ |
| 2 | [[#House Robber]] | 198 | Medium | ⬜ |
| 3 | [[#House Robber II (Circular)]] | 213 | Medium | ⬜ |
| 4 | [[#Jump Game]] | 55 | Medium | ⬜ |
| 5 | [[#Jump Game II (Min Jumps)]] | 45 | Medium | ⬜ |
| 6 | [[#Decode Ways]] | 91 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Climbing Stairs | Recursive choices of 1 or 2 steps. O(2^n). | Memoization or DP array. O(n) space. | Fibonacci rolling variables. O(n), O(1). |
| House Robber | Try rob/skip recursively. O(2^n). | DP array where dp[i] is best till house i. O(n) space. | Two rolling values: prev2 and prev1. O(n), O(1). |
| House Robber II | Try circular choices recursively. Exponential. | Run linear House Robber twice with DP arrays. | Run rolling DP on ranges [0..n-2] and [1..n-1]. O(n), O(1). |
| Jump Game | Recursively try every jump. Exponential. | DP reachable from each index. O(n^2). | Greedy farthest reachable index. O(n). |
| Jump Game II | Recursively try all jump paths. Exponential. | DP min jumps for every index. O(n^2). | Greedy BFS-level window. O(n). |
| Decode Ways | Recursively split into 1-char/2-char decodes. Exponential. | Memoization or DP array. O(n). | Two rolling DP values. O(n), O(1). |

---

## Climbing Stairs

**LeetCode 70** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/climbing-stairs/)

### Problem
n stairs, can climb 1 or 2 steps. How many ways to reach top?

### Approach

- `dp[i]` = ways to reach stair i = `dp[i-1] + dp[i-2]` (Fibonacci!)

### Java Solution

```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int c = a + b;
            a = b; b = c;
        }
        return b;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## House Robber

**LeetCode 198** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/house-robber/)

### Problem
Rob houses in a row, cannot rob two adjacent. Maximize money.

### Approach

- `dp[i]` = max money from first i houses
- `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

### Java Solution

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        int prev2 = nums[0], prev1 = Math.max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) {
            int curr = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## House Robber II (Circular)

**LeetCode 213** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/house-robber-ii/)

### Problem
Houses arranged in a circle — first and last are adjacent.

### Approach

- Can't rob both first and last
- **Case 1:** Rob from `nums[0..n-2]` (exclude last)
- **Case 2:** Rob from `nums[1..n-1]` (exclude first)
- Take max of both cases

### Java Solution

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(
            robRange(nums, 0, n - 2),
            robRange(nums, 1, n - 1)
        );
    }

    private int robRange(int[] nums, int l, int r) {
        int prev2 = 0, prev1 = 0;
        for (int i = l; i <= r; i++) {
            int curr = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Jump Game

**LeetCode 55** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/jump-game/)

### Problem
Given jump lengths, can you reach the last index?

### Approach (Greedy)

- Track `maxReach` = farthest index reachable so far
- If current index > maxReach → stuck, return false

### Java Solution

```java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
        }
        return true;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Jump Game II (Min Jumps)

**LeetCode 45** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/jump-game-ii/)

### Problem
Find minimum number of jumps to reach the last index.

### Approach (Greedy — BFS levels)

- Track `currEnd` (farthest reachable in current jump) and `farthest`
- When we reach `currEnd` → must make another jump → `currEnd = farthest`

### Java Solution

```java
class Solution {
    public int jump(int[] nums) {
        int jumps = 0, currEnd = 0, farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == currEnd) { // exhausted current jump range
                jumps++;
                currEnd = farthest;
            }
        }
        return jumps;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Decode Ways

**LeetCode 91** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/decode-ways/)

### Problem
String of digits, decode like 'A'=1...'Z'=26. Count ways to decode.

### Approach

- `dp[i]` = ways to decode `s[0..i-1]`
- Single digit: if `s[i-1] != '0'` → `dp[i] += dp[i-1]`
- Two digits: if `s[i-2..i-1]` is `10-26` → `dp[i] += dp[i-2]`

### Java Solution

```java
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) == '0' ? 0 : 1;

        for (int i = 2; i <= n; i++) {
            int oneDigit = s.charAt(i-1) - '0';
            int twoDigit = Integer.parseInt(s.substring(i-2, i));

            if (oneDigit >= 1) dp[i] += dp[i-1]; // valid single digit
            if (twoDigit >= 10 && twoDigit <= 26) dp[i] += dp[i-2]; // valid two digits
        }
        return dp[n];
    }
}
```

**Complexity:** Time O(n) · Space O(n) → O(1) with variables

---

## 1D DP Common Patterns

| Pattern | Recurrence |
|---------|-----------|
| Fibonacci / Staircase | `dp[i] = dp[i-1] + dp[i-2]` |
| Max/Min subproblem | `dp[i] = max(dp[i-1], dp[i-2] + cost[i])` |
| Partition | `dp[i] = dp[i-1] or dp[i-2] based on condition` |
| Greedy + DP hybrid | Jump Game, Coin Change |

#sde-sheet #dynamic-programming #day26
