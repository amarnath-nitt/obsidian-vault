# Subarray Sum Equals K (LC 560)

**Difficulty**: Medium  
**Pattern**: Prefix Sum  
**LeetCode**: https://leetcode.com/problems/subarray-sum-equals-k/

## Existing Solution Reference
This problem has related content in: → [Blind75 Dynamic Programming](../../../LeetCode/Blind75/Dynamic-Programming/Combination-Sum.md)

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

**Example 1:**
```
Input: nums = [1,1,1], k = 2
Output: 2
```

**Example 2:**
```
Input: nums = [1,2,3], k = 3
Output: 2
```

## Approach 1: Brute Force

### Intuition
Check all possible subarrays and count those with sum equal to k.

### Java Code
```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum == k) {
                    count++;
                }
            }
        }
        
        return count;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)

## Approach 2: Optimized (Prefix Sum with HashMap)

### Intuition
Use prefix sums with a HashMap. For each position, if `prefixSum - k` exists in the map, it means there's a subarray ending at current position with sum k.

**Key Formula**: `sum(i, j) = prefixSum[j] - prefixSum[i-1]`  
If `sum(i, j) = k`, then `prefixSum[j] - prefixSum[i-1] = k`  
Therefore: `prefixSum[i-1] = prefixSum[j] - k`

### Java Code
```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixSumCount = new HashMap<>();
        prefixSumCount.put(0, 1); // Empty subarray has sum 0
        
        int count = 0;
        int prefixSum = 0;
        
        for (int num : nums) {
            prefixSum += num;
            
            // Check if (prefixSum - k) exists
            // If yes, there are subarrays ending here with sum k
            if (prefixSumCount.containsKey(prefixSum - k)) {
                count += prefixSumCount.get(prefixSum - k);
            }
            
            // Update prefix sum count
            prefixSumCount.put(prefixSum, 
                prefixSumCount.getOrDefault(prefixSum, 0) + 1);
        }
        
        return count;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass
- **Space Complexity**: O(n) - HashMap storage

## Visual Example
```
nums = [1, 2, 3], k = 3

Index:      0   1   2
nums:       1   2   3
prefixSum:  1   3   6

i=0: prefixSum=1, looking for 1-3=-2 (not found), count=0
i=1: prefixSum=3, looking for 3-3=0 (found! count=1), count=1
i=2: prefixSum=6, looking for 6-3=3 (found! count=1), count=2

Subarrays: [3] and [1,2]
```

## Key Takeaways
- HashMap stores frequency of each prefix sum
- `prefixSum - k` tells us how many valid subarrays end at current position
- Initialize with `{0: 1}` to handle subarrays starting from index 0
- Classic prefix sum problem demonstrating O(n) optimization
- Can handle negative numbers unlike sliding window
