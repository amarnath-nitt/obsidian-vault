# Longest Increasing Subsequence

**Difficulty:** Medium
**Category:** Dynamic Programming
**LeetCode Link:** [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

---

## Problem Statement

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

**Example:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4  ([2,3,7,101])
```

---

## Intuition

For each element, the longest increasing subsequence ending at that element = 1 + the longest subsequence ending at any previous smaller element. Build this bottom-up.

---

## Approach 1: DP — O(n²)

### Algorithm
1. `dp[i]` = length of LIS ending at index `i`
2. Initialize all `dp[i] = 1` (each element alone is a subsequence of length 1)
3. For each `i`, check all `j < i`: if `nums[i] > nums[j]`, update `dp[i] = max(dp[i], dp[j] + 1)`
4. Answer = max of all `dp[i]`

### Java Code
```java
class Solution {
    public int lengthOfLIS(int[] nums) {
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

### Complexity Analysis
- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

---

## Approach 2: Binary Search — O(n log n)

### Algorithm
Maintain a `tails` array where `tails[i]` = smallest tail element of all increasing subsequences of length `i+1`. For each number, binary search for its position in `tails` and replace or extend.

### Java Code
```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> tails = new ArrayList<>();

        for (int num : nums) {
            int lo = 0, hi = tails.size();
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (tails.get(mid) < num) lo = mid + 1;
                else hi = mid;
            }
            if (lo == tails.size()) tails.add(num);
            else tails.set(lo, num);
        }

        return tails.size();
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

---

## Key Takeaways

1. **DP definition:** `dp[i]` = LIS length ending at index `i`
2. **O(n²) is sufficient** for most interviews; O(n log n) is the follow-up
3. **Binary search trick:** `tails` array doesn't store the actual LIS, just its length

---

## Tags
#dynamic-programming #binary-search #medium #blind75
