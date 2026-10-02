---
solved: true
difficulty: Easy
pattern: Two Pointers
lc_number: 283
date_solved: 
tags:
  - dsa
  - two-pointers
  - easy
---
# Move Zeroes

[Problem Link](https://leetcode.com/problems/move-zeroes/)

## Problem Statement
Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

## Approach
Use two pointers: `lastNonZeroFoundAt` and `current`.
1.  Iterate through the array with `current`.
2.  If `nums[current]` is non-zero, swap it with `nums[lastNonZeroFoundAt]`.
3.  Increment `lastNonZeroFoundAt`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public void moveZeroes(int[] nums) {
        int lastNonZeroFoundAt = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int temp = nums[lastNonZeroFoundAt];
                nums[lastNonZeroFoundAt] = nums[i];
                nums[i] = temp;
                lastNonZeroFoundAt++;
            }
        }
    }
}
```
