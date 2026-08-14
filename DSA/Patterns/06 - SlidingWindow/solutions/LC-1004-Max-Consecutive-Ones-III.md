# Max Consecutive Ones III

[Problem Link](https://leetcode.com/problems/max-consecutive-ones-iii/)

## Problem Statement
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s.

## Approach
This problem is equivalent to finding the longest subarray with at most `k` zeros.
1.  Use a sliding window defined by `left` and `right`.
2.  Expand the window by moving `right`. If we encounter a `0`, increment a zero counter.
3.  If the zero counter exceeds `k`, shrink the window from the `left` until the zero counter is `<= k`.
4.  Track the maximum window size.

## Time and Space Complexity
- **Time Complexity:** O(N), where N is the length of `nums`.
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int maxLen = 0;
        int zeroCount = 0;
        
        for (int right = 0; right < nums.length; right++) {
            // If current element is 0, increment zero count
            if (nums[right] == 0) {
                zeroCount++;
            }
            
            // If zeros exceed k, shrink window from left
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }
            
            maxLen = Math.max(maxLen, right - left + 1);
        }
        
        return maxLen;
    }
}
```
