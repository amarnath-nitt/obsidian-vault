---
solved: true
difficulty: Medium
pattern: Two Pointers
lc_number: 15
date_solved: 
tags:
  - dsa
  - two-pointers
  - medium
---
# 3Sum (LC 15)

**Difficulty**: Medium  
**Pattern**: Two Pointers  
**LeetCode**: https://leetcode.com/problems/3sum/

## Problem Statement
Given an integer array `nums`, return all triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

**Example 1:**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

## Approach 1: Brute Force

### Intuition
Try all possible triplets and check if they sum to 0.

### Java Code
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> triplet = Arrays.asList(nums[i], nums[j], nums[k]);
                        Collections.sort(triplet);
                        result.add(triplet);
                    }
                }
            }
        }
        
        return new ArrayList<>(result);
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n³)
- **Space Complexity**: O(n) for result set

## Approach 2: Optimized (Sort + Two Pointers)

### Intuition
Sort the array first. For each element, use two pointers to find pairs that sum to `-nums[i]`. Skip duplicates to avoid duplicate triplets.

### Java Code
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate values for first element
            if (i > 0 && nums[i] == nums[i-1]) continue;
            
            int left = i + 1;
            int right = nums.length - 1;
            int target = -nums[i];
            
            while (left < right) {
                int sum = nums[left] + nums[right];
                
                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Skip duplicates for second element
                    while (left < right && nums[left] == nums[left+1]) left++;
                    // Skip duplicates for third element
                    while (left < right && nums[right] == nums[right-1]) right--;
                    
                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return result;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n²) - O(n log n) sort + O(n²) two pointer
- **Space Complexity**: O(1) excluding output

## Visual Example
```
nums = [-1, 0, 1, 2, -1, -4]
Sorted: [-4, -1, -1, 0, 1, 2]

i=0: nums[i]=-4, target=4
  left=1, right=5: -1+2=1 < 4, left++
  left=2, right=5: -1+2=1 < 4, left++
  left=3, right=5: 0+2=2 < 4, left++
  left=4, right=5: 1+2=3 < 4, left++
  No triplet

i=1: nums[i]=-1, target=1
  left=2, right=5: -1+2=1 ✓ → [-1,-1,2]
  Skip duplicate at i=2 (nums[2]=-1)

i=3: nums[i]=0, target=0
  left=4, right=5: 1+2=3 > 0, right--
  left=4, right=4: done
  
Actually, let me fix: 
i=1: nums[i]=-1
  left=2, right=5: -1+2=1, need -1+?+?=0, so ?+?=1
  ...leads to [-1,-1,2] and [-1,0,1]
```

## Key Takeaways
- Sort first to enable two-pointer technique
- Fix one element, use two pointers for remaining two
- Skip duplicates at all three positions
- Reduces O(n³) to O(n²)
- Classic 3Sum pattern extends to 4Sum, kSum problems
