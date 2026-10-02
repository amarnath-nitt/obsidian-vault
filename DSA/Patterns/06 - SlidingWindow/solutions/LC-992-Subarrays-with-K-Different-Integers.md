---
solved: false
difficulty: Hard
pattern: Sliding Window
lc_number: 992
date_solved: 
tags:
  - dsa
  - sliding-window
  - hard
---
# Subarrays with K Different Integers

[Problem Link](https://leetcode.com/problems/subarrays-with-k-different-integers/)

## Problem Statement
Given an integer array `nums` and an integer `k`, return the number of good subarrays of `nums`. A good subarray is a subarray where the number of different integers in that subarray is exactly `k`.

## Approach
Exact `k` is hard to solve directly with sliding window. It's easier to find "at most `k`".
`exactly(k) = atMost(k) - atMost(k - 1)`
Function `atMost(k)`: Counts subarrays with at most `k` distinct integers.
1.  Use sliding window with a frequency map.
2.  Expand `right`, add to map.
3.  If map size > `k`, shrink `left` until map size <= `k`.
4.  Number of valid subarrays ending at `right` is `right - left + 1`.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N) for the map.

## Code
```java
class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMostK(nums, k) - atMostK(nums, k - 1);
    }
    
    private int atMostK(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        int left = 0;
        int result = 0;
        
        for (int right = 0; right < nums.length; right++) {
            count.put(nums[right], count.getOrDefault(nums[right], 0) + 1);
            
            while (count.size() > k) {
                count.put(nums[left], count.get(nums[left]) - 1);
                if (count.get(nums[left]) == 0) {
                    count.remove(nums[left]);
                }
                left++;
            }
            
            result += right - left + 1;
        }
        
        return result;
    }
}
```
