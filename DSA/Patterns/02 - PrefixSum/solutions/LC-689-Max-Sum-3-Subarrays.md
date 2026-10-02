---
solved: false
difficulty: Hard
pattern: Prefix Sum
lc_number: 689
date_solved: 
tags:
  - dsa
  - prefix-sum
  - hard
---
# Maximum Sum of 3 Non-Overlapping Subarrays

[Problem Link](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/)

## Problem Statement
Given an integer array `nums` and an integer `k`, find three non-overlapping subarrays of length `k` with maximum sum and return them.
Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

## Approach
Prefix Sum + DP (Left/Right Arrays).
1.  Calculate sums of all windows of size `k`. `W[i]` is sum of window starting at `i`.
2.  `left[i]`: index of starting position of max window in range `[0, i]`.
3.  `right[i]`: index of starting position of max window in range `[i, n-k]`.
4.  Iterate middle window `j`.
    - `sum = W[left[j-k]] + W[j] + W[right[j+k]]`.
    - Track max sum and indices.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```java
class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        int[] w = new int[n - k + 1];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            if (i >= k) sum -= nums[i - k];
            if (i >= k - 1) w[i - k + 1] = sum;
        }
        
        int[] left = new int[w.length];
        int best = 0;
        for (int i = 0; i < w.length; i++) {
            if (w[i] > w[best]) best = i;
            left[i] = best;
        }
        
        int[] right = new int[w.length];
        best = w.length - 1;
        for (int i = w.length - 1; i >= 0; i--) {
            if (w[i] >= w[best]) best = i; // >= for lexicographically smallest
            right[i] = best;
        }
        
        int[] result = new int[]{-1, -1, -1};
        int finalMaxSum = 0; // Use -1 if values can be negative, but problem implies positive
        
        for (int i = k; i < w.length - k; i++) {
            int l = left[i - k];
            int r = right[i + k];
            int total = w[l] + w[i] + w[r];
            if (result[0] == -1 || total > finalMaxSum) {
                finalMaxSum = total;
                result[0] = l;
                result[1] = i;
                result[2] = r;
            }
        }
        
        return result;
    }
}
```
