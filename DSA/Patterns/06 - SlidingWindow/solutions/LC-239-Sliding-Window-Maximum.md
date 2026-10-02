---
solved: false
difficulty: Hard
pattern: Sliding Window
lc_number: 239
date_solved: 
tags:
  - dsa
  - sliding-window
  - hard
---
# Sliding Window Maximum

[Problem Link](https://leetcode.com/problems/sliding-window-maximum/)

## Problem Statement
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

## Approach
We need to efficiently find the maximum in a moving window. A Monotonic Decreasing Deque (Double Ended Queue) is suitable for this.
1.  The Deque will store **indices** of elements.
2.  The elements corresponding to these indices will be in decreasing order.
3.  As we iterate `i` from `0` to `n-1`:
    - Remove indices that are out of the current window (`index < i - k + 1`).
    - Remove indices from the back whose values are smaller than the current element `nums[i]` (since they can't be the maximum if `nums[i]` is in the window).
    - Add `i` to the back.
    - If `i >= k - 1`, the front of the deque has the index of the maximum element for the current window.

## Time and Space Complexity
- **Time Complexity:** O(N). Each element is added and removed from the deque at most once.
- **Space Complexity:** O(k) for the deque.

## Code
```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) return new int[0];
        
        int n = nums.length;
        int[] result = new int[n - k + 1];
        int ri = 0; // result index
        
        // Deque to store indices
        Deque<Integer> deque = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            // Remove indices that are out of this window
            while (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
                deque.pollFirst();
            }
            
            // Remove indices whose values are less than nums[i]
            // maintain monotonic decreasing deque
            while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
                deque.pollLast();
            }
            
            deque.offerLast(i);
            
            // Add to result if full window
            if (i >= k - 1) {
                result[ri++] = nums[deque.peekFirst()];
            }
        }
        
        return result;
    }
}
```
