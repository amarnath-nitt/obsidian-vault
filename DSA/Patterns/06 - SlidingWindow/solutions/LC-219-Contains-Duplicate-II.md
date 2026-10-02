---
solved: false
difficulty: Easy
pattern: Sliding Window
lc_number: 219
date_solved: 
tags:
  - dsa
  - sliding-window
  - easy
---
# Contains Duplicate II

[Problem Link](https://leetcode.com/problems/contains-duplicate-ii/)

## Problem Statement
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Approach
We can use a sliding window approach with a HashSet. The set will store the elements in the current window of size `k`.
1.  Iterate through the array.
2.  If the set already contains the current element, we found a duplicate within distance `k`, so return `true`.
3.  Add the current element to the set.
4.  If the size of the set exceeds `k`, remove the element at `i - k` to maintain the window size.

## Time and Space Complexity
- **Time Complexity:** O(N), where N is the length of `nums`. We traverse the array once, and set operations are O(1) on average.
- **Space Complexity:** O(min(N, k)), to store the elements in the HashSet.

## Code
```java
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            // If the set contains the current number, we found a duplicate
            // within the last k elements (since we maintain set size <= k)
            if (set.contains(nums[i])) {
                return true;
            }
            
            set.add(nums[i]);
            
            // Maintain the window size of k
            // If the set size is greater than k, remove the oldest element
            if (set.size() > k) {
                set.remove(nums[i - k]);
            }
        }
        
        return false;
    }
}
```
