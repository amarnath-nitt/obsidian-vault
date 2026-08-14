# 4Sum

[Problem Link](https://leetcode.com/problems/4sum/)

## Problem Statement
Given an array `nums` of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
- `0 <= a, b, c, d < n`
- `a, b, c, and d` are distinct.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

## Approach
Extension of 3Sum. Sort the array. Use two nested loops for the first two numbers, then use Two Pointers for the remaining two.
1.  Sort `nums`.
2.  Loop `i` from `0` to `n-3`. Skip duplicates.
3.  Loop `j` from `i+1` to `n-2`. Skip duplicates.
4.  Use `left` = `j+1`, `right` = `n-1`.
5.  Sum = `nums[i] + nums[j] + nums[left] + nums[right]`. Check against `target`.
    - **Note:** Use `long` for sum to avoid overflow.
    - If equal, add to result, move `left`, `right`, skip duplicates.

## Time and Space Complexity
- **Time Complexity:** O(N^3).
- **Space Complexity:** O(1) (excluding result list).

## Code
```java
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length < 4) return result;
        Arrays.sort(nums);
        int n = nums.length;
        
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue; // skip duplicates
            
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j-1]) continue; // skip duplicates
                
                int left = j + 1;
                int right = n - 1;
                
                while (left < right) {
                    long sum = (long)nums[i] + nums[j] + nums[left] + nums[right];
                    
                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        
                        while (left < right && nums[left] == nums[left+1]) left++;
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
        }
        return result;
    }
}
```
