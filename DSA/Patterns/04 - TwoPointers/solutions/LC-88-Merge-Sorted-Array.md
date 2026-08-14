# Merge Sorted Array

[Problem Link](https://leetcode.com/problems/merge-sorted-array/)

## Problem Statement
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively. Merge `nums1` and `nums2` into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`.

## Approach
Start from the end of both arrays. Compare elements and place the larger one at the end of `nums1` (at index `m + n - 1`).
1.  Pointers `p1` at `m-1`, `p2` at `n-1`, `p` at `m+n-1`.
2.  While `p1 >= 0` and `p2 >= 0`:
    - If `nums1[p1] > nums2[p2]`, set `nums1[p] = nums1[p1]`, decrement `p1`.
    - Else, set `nums1[p] = nums2[p2]`, decrement `p2`.
    - Decrement `p`.
3.  If elements remain in `nums2`, copy them to `nums1`.

## Time and Space Complexity
- **Time Complexity:** O(m + n).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int p = m + n - 1;
        
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[p] = nums1[p1];
                p1--;
            } else {
                nums1[p] = nums2[p2];
                p2--;
            }
            p--;
        }
        
        // If p2 is not exhausted, copy remaining elements
        // If p1 is not exhausted, they are already in place
        while (p2 >= 0) {
            nums1[p] = nums2[p2];
            p2--;
            p--;
        }
    }
}
```
