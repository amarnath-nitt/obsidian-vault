---
solved: true
difficulty: Hard
pattern: Frequency Counting
lc_number: 41
date_solved: 
tags:
  - dsa
  - frequency-counting
  - hard
---
# First Missing Positive

[Problem Link](https://leetcode.com/problems/first-missing-positive/)

## Problem Statement
Given an unsorted integer array `nums`, return the smallest missing positive integer.
You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

## Approach
Cycle Sort / Hash in-place.
1.  Place each number `x` in its correct position `x-1` (if `0 < x <= n`).
2.  Iterate to find first index `i` where `nums[i] != i + 1`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        int i = 0;
        
        while (i < n) {
            int correctIdx = nums[i] - 1;
            if (nums[i] > 0 && nums[i] <= n && nums[i] != nums[correctIdx]) {
                swap(nums, i, correctIdx);
            } else {
                i++;
            }
        }
        
        for (i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        
        return n + 1;
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```
