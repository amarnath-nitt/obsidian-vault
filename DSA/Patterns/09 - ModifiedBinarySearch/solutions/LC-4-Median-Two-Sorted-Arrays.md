---
solved: false
difficulty: Hard
pattern: Modified Binary Search
lc_number: 4
date_solved: 
tags:
  - dsa
  - modified-binary-search
  - hard
---
# Median of Two Sorted Arrays (LC 4)

**Difficulty**: Hard  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/median-of-two-sorted-arrays/

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.
The overall run time complexity should be `O(log (m+n))`.

**Example:**
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
```

## Approach: Partitioning

### Intuition
Partition both arrays such that the left half contains `(m + n + 1) / 2` elements.
We need to find a partition `i` in `nums1` and `j` in `nums2` such that:
1. `max(nums1[i-1], nums2[j-1]) <= min(nums1[i], nums2[j])`
2. Total length of left half is correct.
Binary Search on the smaller array to find partition `i`. `j` is derived.
Constraints: `nums1[i-1] <= nums2[j]` and `nums2[j-1] <= nums1[i]`.

### Java Code
```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.length;
        int n = nums2.length;
        int left = 0, right = m;
        
        while (left <= right) {
            int partitionX = left + (right - left) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;
            
            int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : nums1[partitionX - 1];
            int minRightX = (partitionX == m) ? Integer.MAX_VALUE : nums1[partitionX];
            
            int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? Integer.MAX_VALUE : nums2[partitionY];
            
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // Correct partition
                if ((m + n) % 2 == 0) {
                    return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2.0;
                } else {
                    return Math.max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                right = partitionX - 1;
            } else {
                left = partitionX + 1;
            }
        }
        
        throw new IllegalArgumentException();
    }
}
```

### Complexity
- **Time**: O(log(min(m, n)))
- **Space**: O(1)

## Key Takeaways
- Advanced Binary Search on Partition Index
- Handling Edge Cases (empty parts) with MIN/MAX values
