---
solved: false
difficulty: Medium
pattern: Modified Binary Search
lc_number: 153
date_solved: 
tags:
  - dsa
  - modified-binary-search
  - medium
---
# Find Minimum in Rotated Sorted Array (LC 153)

**Difficulty**: Medium  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Problem Statement
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.
You must write an algorithm that runs in `O(log n)` time.

**Example:**
```
Input: nums = [3,4,5,1,2]
Output: 1
```

## Approach: Binary Search

### Intuition
We want to find the pivot point (the only element smaller than its predecessor).
If `nums[mid] > nums[right]`, then minimum must be to the right of `mid`.
If `nums[mid] < nums[right]`, then `mid` could be the minimum or the minimum is to the left (so `right = mid`).
Unlike standard BS, we compare `mid` with `right` (or `left`, but `right` is standard for min finding).

### Java Code
```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // If mid element is greater than rightmost, 
            // min must be in right half (excluding mid)
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // If mid is less than or equal rightmost, 
            // min is in left half (including mid)
            else {
                right = mid;
            }
        }
        
        return nums[left];
    }
}
```

### Complexity
- **Time**: O(log n)
- **Space**: O(1)

## Key Takeaways
- Compare `mid` with `right` to determine unsorted portion (which contains min)
- Loop condition `left < right` (no `=`) avoids infinite loop for `right = mid`
- Convergence at `left` (or `right`) gives the minimum
