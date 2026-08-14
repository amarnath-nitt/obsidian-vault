# Longest Increasing Subsequence (LC 300)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming  
**LeetCode**: https://leetcode.com/problems/longest-increasing-subsequence/

## Problem Statement
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**Example:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], length 4.
```

## Approach 1: DP Tabulation

### Intuition
`dp[i]` = length of LIS ending at index `i`.
For each `j < i`, if `nums[j] < nums[i]`, `dp[i] = max(dp[i], dp[j] + 1)`.

### Java Code
```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) return 0;
        
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int maxLen = 1;
        
        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }
        
        return maxLen;
    }
}
```

### Complexity
- **Time**: O(n²)
- **Space**: O(n)

## Approach 2: Patience Sorting (Binary Search) (Optimized)

### Intuition
Maintain a list `tails` where `tails[i]` stores the smallest tail of all increasing subsequences of length `i+1`. This list will always be sorted.
For each x in nums:
- If x > all tails, append it (extends longest subsequence)
- If x <= some tails, replace the smallest tail >= x with x (gives us better potential for future)

### Java Code
```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        
        for (int num : nums) {
            int i = 0, j = size;
            
            // Binary search for insertion point
            while (i < j) {
                int m = (i + j) / 2;
                if (tails[m] < num) {
                    i = m + 1;
                } else {
                    j = m;
                }
            }
            
            tails[i] = num;
            if (i == size) size++;
        }
        
        return size;
    }
}
```

### Complexity
- **Time**: O(n log n)
- **Space**: O(n)

## Key Takeaways
- Classic DP problem (O(n²))
- Can be optimized to O(n log n) using binary search strategy
- Subsequence vs Subarray (Subsequence non-contiguous)
