---
solved: true
difficulty: Easy
pattern: Two Pointers
lc_number: 26
date_solved: 
tags:
  - dsa
  - two-pointers
  - easy
---
# Remove Duplicates from Sorted Array

[Problem Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem Statement
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Return the number of unique elements.

## Approach
Use two pointers: `insertPos` and `i`.
1.  `insertPos` tracks where the next unique element should be placed.
2.  Iterate `i` through the array.
3.  If `nums[i]` is different from `nums[insertPos - 1]`, it's a new unique element.
    - `nums[insertPos] = nums[i]`
    - Increment `insertPos`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        
        int insertPos = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[insertPos] = nums[i];
                insertPos++;
            }
        }
        return insertPos;
    }
}
```
