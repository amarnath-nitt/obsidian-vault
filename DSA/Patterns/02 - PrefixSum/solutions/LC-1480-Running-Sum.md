# Running Sum of 1d Array

[Problem Link](https://leetcode.com/problems/running-sum-of-1d-array/)

## Problem Statement
Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.
Return the running sum of `nums`.

## Approach
Prefix sum. Iterate array and add previous sum to current.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1) (if modified in-place or O(N) for result).

## Code
```java
class Solution {
    public int[] runningSum(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
}
```
