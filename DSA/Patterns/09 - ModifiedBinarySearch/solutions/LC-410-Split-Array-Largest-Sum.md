# Split Array Largest Sum

[Problem Link](https://leetcode.com/problems/split-array-largest-sum/)

## Problem Statement
Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.

## Approach
Binary Search on Answer.
The range of possible answers is `[max(nums), sum(nums)]`.
1.  `left = max(nums)`, `right = sum(nums)`.
2.  `mid = left + (right - left) / 2`.
3.  Check if it's possible to split array into <= k subarrays such that each subarray sum <= `mid`.
    - If yes, `mid` could be the answer, try smaller: `right = mid`.
    - If no, `mid` is too small, need larger capacity: `left = mid + 1`.

## Time and Space Complexity
- **Time Complexity:** O(N * log(Sum - Max)).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public int splitArray(int[] nums, int k) {
        int max = 0;
        int sum = 0;
        for (int num : nums) {
            max = Math.max(max, num);
            sum += num;
        }
        
        int left = max, right = sum;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canSplit(nums, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    
    private boolean canSplit(int[] nums, int k, int maxSubarraySum) {
        int splitCount = 1;
        int currentSum = 0;
        
        for (int num : nums) {
            if (currentSum + num > maxSubarraySum) {
                splitCount++;
                currentSum = num;
            } else {
                currentSum += num;
            }
        }
        return splitCount <= k;
    }
}
```
