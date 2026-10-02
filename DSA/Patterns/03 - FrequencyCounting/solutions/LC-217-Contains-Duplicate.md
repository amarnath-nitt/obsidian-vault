---
solved: true
difficulty: Easy
pattern: Frequency Counting
lc_number: 217
date_solved: 
tags:
  - dsa
  - frequency-counting
  - easy
---
# Contains Duplicate

[Problem Link](https://leetcode.com/problems/contains-duplicate/)

## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Approach
HashSet.
Iterate and add to set. If exists, return true.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (!set.add(num)) {
                return true;
            }
        }
        return false;
    }
}
```
