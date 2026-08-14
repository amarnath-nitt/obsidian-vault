# Range Sum Query - Immutable (LC 303)

**Difficulty**: Easy  
**Pattern**: Prefix Sum  
**LeetCode**: https://leetcode.com/problems/range-sum-query-immutable/

## Problem Statement
Given an integer array `nums`, handle multiple queries of the following type:
- Calculate the **sum** of the elements of `nums` between indices `left` and `right` inclusive where `left <= right`.

**Example:**
```
Input: nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

## Approach: Prefix Sum

### Intuition
Naive approach sums from left to right for each query: O(N) per query.
With Prefix Sum array where `P[i] = sum(nums[0]...nums[i-1])`, sum(left, right) = `P[right+1] - P[left]`.
Construction: O(N), Query: O(1).

### Java Code
```java
class NumArray {
    private int[] prefixSum;

    public NumArray(int[] nums) {
        prefixSum = new int[nums.length + 1];
        prefixSum[0]=0;
        for (int i = 1; i <= nums.length; i++) {
            prefixSum[i] = prefixSum[i-1] + nums[i-1];
        }
    }
    
    public int sumRange(int left, int right) {
        return prefixSum[right + 1] - prefixSum[left];
    }
}
```

### Complexity
- **Time**: O(N) constructor, O(1) query
- **Space**: O(N)

## Key Takeaways
- Classic Prefix Sum application
- 0-padding prefix array simplifies `P[left] - P[right+1]` logic (avoids negative index check)
