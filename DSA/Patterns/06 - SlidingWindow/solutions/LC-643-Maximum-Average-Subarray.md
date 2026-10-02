---
solved: false
difficulty: Easy
pattern: Sliding Window
lc_number: 643
date_solved: 
tags:
  - dsa
  - sliding-window
  - easy
---
# Maximum Average Subarray I (LC 643)

**Difficulty**: Easy  
**Pattern**: Sliding Window  
**LeetCode**: https://leetcode.com/problems/maximum-average-subarray-i/

## Problem Statement
You are given an integer array `nums` consisting of `n` elements, and an integer `k`. Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value.

**Example 1:**
```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

## Approach 1: Brute Force

### Intuition
Calculate the sum of every possible subarray of size k and find the maximum average.

### Java Code
```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double maxAvg = Integer.MIN_VALUE;
        
        // Try all subarrays of size k
        for (int i = 0; i <= nums.length - k; i++) {
            int sum = 0;
            for (int j = i; j < i + k; j++) {
                sum += nums[j];
            }
            double avg = (double) sum / k;
            maxAvg = Math.max(maxAvg, avg);
        }
        
        return maxAvg;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n × k) - For each position, calculate sum of k elements
- **Space Complexity**: O(1)

## Approach 2: Optimized (Fixed Sliding Window)

### Intuition
Instead of recalculating the entire sum for each window, maintain a running sum. When sliding the window, subtract the element going out and add the element coming in.

### Java Code
```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // Calculate sum of first window
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }
        
        int maxSum = windowSum;
        
        // Slide the window
        for (int i = k; i < nums.length; i++) {
            // Remove leftmost element, add rightmost element
            windowSum = windowSum - nums[i - k] + nums[i];
            maxSum = Math.max(maxSum, windowSum);
        }
        
        return (double) maxSum / k;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass through array
- **Space Complexity**: O(1) - Only storing sum variables

## Key Takeaways
- Fixed-size sliding window problems can be optimized by reusing calculations
- Subtract outgoing element, add incoming element pattern
- Division by k can be done once at the end to avoid repeated float operations
- Classic example of reducing O(n×k) to O(n)
