# Two Sum (LC 1)

**Difficulty**: Easy  
**Pattern**: Two Pointers / Frequency Counting  
**LeetCode**: https://leetcode.com/problems/two-sum/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Arrays-Hashing/Two-Sum.md)

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

## Approach 1: Brute Force

### Intuition
Try all possible pairs and check if they sum to target.

### Java Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {-1, -1};
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)

## Approach 2: Optimized (HashMap - One Pass)

### Intuition
For each number, check if `target - num` exists in HashMap. Store numbers as we iterate.

### Java Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numToIndex = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (numToIndex.containsKey(complement)) {
                return new int[] {numToIndex.get(complement), i};
            }
            
            numToIndex.put(nums[i], i);
        }
        
        return new int[] {-1, -1};
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass
- **Space Complexity**: O(n) - HashMap storage

## Approach 3: Two Pointers (Only if sorting is allowed)

**Note**: This changes indices, so only works if we don't need original indices or if we track them.

### Java Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create array of [value, original_index] pairs
        int[][] pairs = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            pairs[i] = new int[] {nums[i], i};
        }
        
        // Sort by value
        Arrays.sort(pairs, (a, b) -> a[0] - b[0]);
        
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int sum = pairs[left][0] + pairs[right][0];
            if (sum == target) {
                return new int[] {pairs[left][1], pairs[right][1]};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return new int[] {-1, -1};
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n log n) - Sorting
- **Space Complexity**: O(n) - Pairs array

## Key Takeaways
- HashMap approach is optimal for this problem
- One-pass solution by looking for complement
- Two pointers works only with sorting (loses original indices)
- Classic interview problem demonstrating hash table optimization
