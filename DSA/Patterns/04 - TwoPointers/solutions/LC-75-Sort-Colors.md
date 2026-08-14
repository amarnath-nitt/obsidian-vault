# Sort Colors

[Problem Link](https://leetcode.com/problems/sort-colors/)

## Problem Statement
Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

## Approach
Dutch National Flag problem. Use three pointers: `low`, `mid`, `high`.
- `0` to `low-1`: Red (0)
- `low` to `mid-1`: White (1)
- `mid` to `high`: Unknown
- `high+1` to `end`: Blue (2)

1.  Iterate `mid` from 0 to `high`.
2.  If `nums[mid] == 0`: Swap with `nums[low]`, increment `low` and `mid`.
3.  If `nums[mid] == 1`: Increment `mid`.
4.  If `nums[mid] == 2`: Swap with `nums[high]`, decrement `high` (don't increment `mid` yet as swapped element needs checking).

## Time and Space Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(1).

## Code
```java
class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else { // nums[mid] == 2
                swap(nums, mid, high);
                high--;
            }
        }
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```
