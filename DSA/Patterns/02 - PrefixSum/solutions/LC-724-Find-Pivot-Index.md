---
solved: true
difficulty: Easy
pattern: Prefix Sum
lc_number: 724
date_solved: 
tags:
  - dsa
  - prefix-sum
  - easy
---
# Find Pivot Index (LC 724)

**Difficulty**: Easy  
**Pattern**: Prefix Sum  
**LeetCode**: https://leetcode.com/problems/find-pivot-index/

## Problem Statement
Given an array of integers `nums`, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge, left sum is 0. If on right edge, right sum is 0.
Return the leftmost pivot index. If no such index exists, return -1.

**Example:**
```
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation: 
Left sum = 1 + 7 + 3 = 11
Right sum = 5 + 6 = 11
```

## Approach: Total Sum - Left Sum

### Intuition
Let `S` be total sum.
At any index `i`, `right_sum = S - left_sum - nums[i]`.
We want `left_sum == right_sum`.
So `left_sum == S - left_sum - nums[i]` => `2 * left_sum + nums[i] == S`.
Iterate and verify efficiently.

### Java Code
```java
class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        
        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (leftSum * 2 == totalSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        
        return -1;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Alternative Approach: Explicit Prefix Sum Array

### Intuition
This approach explicitly builds a prefix sum array first.
`prefixSum[i]` stores the sum of `numbs[0]` to `numbs[i-1]`.
`leftSum` for index `i` is `prefixSum[i]`.
`rightSum` for index `i` is `prefixSum[numbs.length] - prefixSum[i+1]`.

### Java Code
```java
class Solution {
    public int pivotIndex(int[] numbs) {
        int [] prefixSum = new int[numbs.length+1];
        for(int i=1; i<=numbs.length; i++){
            prefixSum[i] = prefixSum[i-1] + numbs[i-1];
        }
        for(int i=0; i<numbs.length; i++){ // Changed loop to start from 0
            int leftSum = prefixSum[i];
            int rightSum = prefixSum[numbs.length] - prefixSum[i+1];
            if(leftSum == rightSum) {
                return i;
            }
        }
        return -1;
    }
}
```

### Complexity
- **Time**: O(N) for building prefix sum array + O(N) for iteration = O(N)
- **Space**: O(N) for the prefix sum array

## Key Takeaways
- Prefix Sum concepts useful without explicit array construction
- Finding balance point using total sum
