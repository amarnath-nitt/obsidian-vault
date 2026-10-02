---
solved: false
difficulty: Hard
pattern: Greedy
lc_number: 1326
date_solved: 
tags:
  - dsa
  - greedy
  - hard
---
# Minimum Number of Taps to Open to Water a Garden

[Problem Link](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)

## Problem Statement
There is a one-dimensional garden on the x-axis. The garden starts at the point `0` and ends at the point `n`. (Length `n`).
There are `n + 1` taps located at points `[0, 1, ..., n]` in the garden.
Given an integer `n` and an integer array `ranges` of length `n + 1` where `ranges[i]` (0-indexed) means the `i-th` tap can water the area `[i - ranges[i], i + ranges[i]]` if it was open.
Return the minimum number of taps that should be open to water the whole garden `[0, n]`. If the garden cannot be watered completely return `-1`.

## Approach
Jump Game II Variation (Greedy).
1.  Compute the max reach from each possible starting point. `maxReach[i]` = farthest point reachable from interval starting at or before `i`.
    - Actually, convert taps to intervals `[start, end]`. Map `start` to max `end`.
    - `arr[start] = max(arr[start], end)`.
    - We need to cover range `[0, n]`.
2.  Iterate from `0` to `n-1`.
    - Keep track of `currentEnd` and `farthest`.
    - `farthest = max(farthest, arr[i])`.
    - If `i == currentEnd`:
        - Jump! `taps++`.
        - `currentEnd = farthest`.
        - If `currentEnd >= n` return taps.

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```java
class Solution {
    public int minTaps(int n, int[] ranges) {
        int[] maxReach = new int[n + 1];
        
        for (int i = 0; i <= n; i++) {
            int start = Math.max(0, i - ranges[i]);
            int end = Math.min(n, i + ranges[i]);
            maxReach[start] = Math.max(maxReach[start], end);
        }
        
        int taps = 0;
        int currentEnd = 0;
        int farthest = 0;
        
        for (int i = 0; i < n; i++) {
            farthest = Math.max(farthest, maxReach[i]);
            
            if (i == currentEnd) {
                if (farthest <= i) return -1; // Cannot extend further
                taps++;
                currentEnd = farthest;
            }
        }
        
        return currentEnd >= n ? taps : -1;
    }
}
```
