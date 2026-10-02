# House Robber

**Difficulty:** Medium
**Category:** Dynamic Programming
**LeetCode Link:** [House Robber](https://leetcode.com/problems/house-robber/)

---

## Problem Statement

You are a robber. Adjacent houses have connected alarms — you cannot rob two adjacent houses. Given `nums[i]` = money at house `i`, return the maximum amount you can rob.

**Example:**
```
Input: nums = [2,7,9,3,1]
Output: 12  (2 + 9 + 1)
```

---

## Intuition

At each house, you have two choices: rob it (add its value + best from two houses back) or skip it (take best from previous house). The recurrence is: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.

---

## Approach 1: DP Array

### Algorithm
1. `dp[i]` = max money robbing houses `0..i`
2. `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`
3. For each `i >= 2`: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

### Java Code
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }

        return dp[nums.length - 1];
    }
}
```

---

## Approach 2: O(1) Space (Optimized)

### Algorithm
Only need the previous two values — no need for the full array.

### Java Code
```java
class Solution {
    public int rob(int[] nums) {
        int prev2 = 0, prev1 = 0;

        for (int num : nums) {
            int current = Math.max(prev1, prev2 + num);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Key Takeaways

1. **Recurrence:** `dp[i] = max(skip current, rob current + dp[i-2])`
2. **Space optimization:** Rolling two variables instead of full array
3. **Foundation:** House Robber II and III build on this exact pattern

---

## Tags
#dynamic-programming #medium #blind75
