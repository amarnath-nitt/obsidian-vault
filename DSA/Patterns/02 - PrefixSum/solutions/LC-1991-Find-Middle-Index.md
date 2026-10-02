---
solved: true
difficulty: Easy
pattern: Prefix Sum
lc_number: 1991
date_solved: 
tags:
  - dsa
  - prefix-sum
  - easy
---
# Find the Middle Index in Array

[Problem Link](https://leetcode.com/problems/find-the-middle-index-in-array/)

## Problem Statement
Given a 0-indexed integer array `nums`, find the leftmost `middleIndex` (i.e., that uses fewer operations).
A `middleIndex` is an index where `nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]`.
If `middleIndex == 0`, the left side sum is considered to be `0`. Similarly for `nums.length - 1`.
Return the leftmost `middleIndex` that satisfies the condition, or `-1` if there is no such index.

## Approach
1.  Calculate total sum.
2.  Iterate and keep track of `leftSum`.
3.  `rightSum = totalSum - leftSum - nums[i]`.
4.  If `leftSum == rightSum`, return `i`.
5.  Update `leftSum`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public int findMiddleIndex(int[] nums) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        
        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}
```
