---
solved: false
difficulty: Medium
pattern: Modified Binary Search
lc_number: 34
date_solved: 
tags:
  - dsa
  - modified-binary-search
  - medium
---
# Find First and Last Position of Element in Sorted Array (LC 34)

**Difficulty**: Medium  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Problem Statement
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
If `target` is not found in the array, return `[-1, -1]`.

**Example:**
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

## Approach: Double Binary Search

### Intuition
Run Binary Search twice.
1. Find First Position (`findFirst`): Lower Bound.
   If `nums[mid] >= target`: `right = mid - 1`, store `mid` if equal.
2. Find Last Position (`findLast`): Upper Bound.
   If `nums[mid] <= target`: `left = mid + 1`, store `mid` if equal.

### Java Code
```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1, -1};
        result[0] = findFirst(nums, target);
        if (result[0] != -1) {
            result[1] = findLast(nums, target);
        }
        return result;
    }
    
    private int findFirst(int[] nums, int target) {
        int idx = -1;
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            if (nums[mid] == target) idx = mid;
        }
        return idx;
    }
    
    private int findLast(int[] nums, int target) {
        int idx = -1;
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
            if (nums[mid] == target) idx = mid;
        }
        return idx;
    }
}
```

### Complexity
- **Time**: O(log N)
- **Space**: O(1)

## Key Takeaways
- Bias `left` or `right` updates to scan for boundaries
