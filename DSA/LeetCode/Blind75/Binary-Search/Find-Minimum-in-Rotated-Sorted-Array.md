# Find Minimum in Rotated Sorted Array

**Difficulty:** Medium  
**Category:** Binary Search  
**LeetCode Link:** [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

## Problem Statement

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times.

Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in **O(log n) time**.

**Example 1:**
```
Input: nums = [3,4,5,1,2]
Output: 1
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
```

**Example 3:**
```
Input: nums = [11,13,15,17]
Output: 11
```

**Constraints:**
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All integers are **unique**.

---

## Intuition

The minimum element is at the rotation point. We can use binary search to find where the array "breaks" (where a larger element is followed by a smaller one).

---

## Approach: Modified Binary Search

### Algorithm
1. Use binary search to find the inflection point
2. Compare mid element with rightmost element
3. If mid > right, minimum is in right half
4. Otherwise, minimum is in left half (including mid)

### Java Code
```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            // If mid element is greater than right element,
            // minimum must be in right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                // Minimum is in left half (including mid)
                right = mid;
            }
        }
        
        return nums[left];
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(log n) - Binary search
- **Space Complexity:** O(1) - Only using pointers

### Why This Works
- ✅ Optimal O(log n) time
- ✅ Simple and clean
- ✅ Handles all rotation cases
- ✅ Works for non-rotated arrays too

---

## Key Takeaways

1. **Pattern:** Binary search on rotated array
2. **Key comparison:** Compare mid with right (not left)
3. **Inflection point:** Where array transitions from high to low
4. **Loop invariant:** Minimum is always in [left, right]

---

## Step-by-Step Example

For `nums = [4,5,6,7,0,1,2]`:

```
left=0, right=6, mid=3
  nums[3]=7 > nums[6]=2
  Minimum in right half, left=4
  
left=4, right=6, mid=5
  nums[5]=1 < nums[6]=2
  Minimum in left half (including mid), right=5
  
left=4, right=5, mid=4
  nums[4]=0 < nums[5]=1
  Minimum in left half (including mid), right=4
  
left=4, right=4
  Return nums[4] = 0
```

---

## Edge Cases

- No rotation: `[1,2,3,4,5]` → `1`
- Single element: `[1]` → `1`
- Two elements: `[2,1]` → `1`
- Rotated at end: `[2,3,4,5,1]` → `1`

---

## Related Problems
- [[Search-in-Rotated-Sorted-Array]] - Search for target
- [[Find-Minimum-in-Rotated-Sorted-Array-II]] - With duplicates

---

## Tags
#binary-search #arrays #medium #blind75
