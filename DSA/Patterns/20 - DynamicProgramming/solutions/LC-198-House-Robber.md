# House Robber (LC 198)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/house-robber/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Dynamic-Programming/House-Robber.md)

## Problem Statement
You are a robber planning to rob houses. Each house has a certain amount of money. Adjacent houses have security systems connected, so you cannot rob two adjacent houses. Return the maximum amount you can rob tonight.

**Example:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (2), house 3 (9), house 5 (1) = 2+9+1=12
```

## Approach 1: Recursion

### Java Code
```java
class Solution {
    public int rob(int[] nums) {
        return robFrom(0, nums);
    }
    
    private int robFrom(int i, int[] nums) {
        if (i >= nums.length) return 0;
        
        // Rob this house or skip it
        int robCurrent = nums[i] + robFrom(i+2, nums);
        int skipCurrent = robFrom(i+1, nums);
        
        return Math.max(robCurrent, skipCurrent);
    }
}
```

### Complexity
- **Time**: O(2^n)
- **Space**: O(n)

## Approach 2: DP Tabulation

### Java Code
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i-1], nums[i] + dp[i-2]);
        }
        
        return dp[nums.length-1];
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n)

## Approach 3: Space-Optimized

### Java Code
```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        
        int prev2 = nums[0];
        int prev1 = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.length; i++) {
            int curr = Math.max(prev1, nums[i] + prev2);
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
- Classic DP: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`
- Choose between robbing current or skipping
- Can optimize to O(1) space
