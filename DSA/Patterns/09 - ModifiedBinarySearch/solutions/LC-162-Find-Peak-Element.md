# Find Peak Element (LC 162)

**Difficulty**: Medium  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/find-peak-element/

## Problem Statement
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that `nums[-1] = nums[n] = -∞`.
You must write an algorithm that runs in `O(log n)` time.

**Example:**
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5 (Index of 6)
```

## Approach: Hill Climbing with Binary Search

### Intuition
If `nums[mid] < nums[mid + 1]`, we are on an uphill slope. A peak must exist to the right (since `nums[n] = -∞`). Move right.
If `nums[mid] > nums[mid + 1]`, we are on a downhill slope. A peak must exist to the left (including `mid`). Move left.

### Java Code
```java
class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] < nums[mid + 1]) {
                // Uphill, peak is to the right
                left = mid + 1;
            } else {
                // Downhill, peak is here or to the left
                right = mid;
            }
        }
        
        return left;
    }
}
```

### Complexity
- **Time**: O(log N)
- **Space**: O(1)

## Key Takeaways
- Using local gradient to guide global search
- `mid` vs `mid+1` comparison for slope
