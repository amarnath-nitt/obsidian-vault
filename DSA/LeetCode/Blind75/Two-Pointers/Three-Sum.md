# Three Sum

**Difficulty:** Medium  
**Category:** Two Pointers  
**LeetCode Link:** [Three Sum](https://leetcode.com/problems/3sum/)

---

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2:**
```
Input: nums = [0,1,1]
Output: []
```

**Example 3:**
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

**Constraints:**
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

---

## Intuition

This is an extension of Two Sum. For each number, we need to find two other numbers that sum to its negative (so the total is zero).

---

## Approach 1: Brute Force (Naive Solution)

### Algorithm
1. Use three nested loops to check all possible triplets
2. Check if sum equals zero
3. Use a set to avoid duplicates

### Java Code
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        
        // Check all triplets
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
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
- **Time Complexity:** O(n³) - Three nested loops
- **Space Complexity:** O(n) - Set to store results

### Drawbacks
- Extremely slow for large inputs
- Inefficient duplicate handling

---

## Approach 2: Two Pointers (Optimized Solution)

### Algorithm
1. Sort the array
2. For each number at index `i`:
   - Use two pointers: `left = i + 1`, `right = n - 1`
   - Find pairs that sum to `-nums[i]`
   - Skip duplicates to avoid duplicate triplets
3. Move pointers based on sum comparison

### Java Code
```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate values for i
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int left = i + 1;
            int right = nums.length - 1;
            int target = -nums[i];
            
            while (left < right) {
                int sum = nums[left] + nums[right];
                
                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Skip duplicates for left
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    // Skip duplicates for right
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
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

### Step-by-Step Example
For `nums = [-1, 0, 1, 2, -1, -4]`:

```
After sorting: [-4, -1, -1, 0, 1, 2]

i=0, nums[i]=-4, target=4:
  left=1(-1), right=5(2): sum=1 < 4 → left++
  left=2(-1), right=5(2): sum=1 < 4 → left++
  left=3(0), right=5(2): sum=2 < 4 → left++
  left=4(1), right=5(2): sum=3 < 4 → left++
  left=5, left >= right → done

i=1, nums[i]=-1, target=1:
  left=2(-1), right=5(2): sum=1 = 1 → found [-1,-1,2]
  Skip duplicates, left=3, right=4
  left=3(0), right=4(1): sum=1 = 1 → found [-1,0,1]
  left++, right--, left >= right → done

i=2, nums[i]=-1: skip (duplicate)

i=3, nums[i]=0, target=0:
  left=4(1), right=5(2): sum=3 > 0 → right--
  left >= right → done

Result: [[-1,-1,2], [-1,0,1]]
```

### Complexity Analysis
- **Time Complexity:** O(n²) - O(n log n) for sorting + O(n²) for two pointers
- **Space Complexity:** O(1) or O(n) - Depends on sorting algorithm

### Why This is Better
- ✅ O(n²) vs O(n³) - much faster
- ✅ Efficient duplicate handling
- ✅ Two pointers technique reduces one dimension
- ✅ Sorted array enables pointer movement logic

---

## Key Insights

1. **Sorting enables two pointers:** Sorted array allows us to move pointers intelligently
2. **Reduce to Two Sum:** Fix one number, find two others that sum to target
3. **Duplicate handling:** Skip duplicates at all three positions
4. **Pointer movement:**
   - If sum < target: increase sum by moving left pointer right
   - If sum > target: decrease sum by moving right pointer left

---

## Key Takeaways

1. **Pattern:** Reduce 3Sum to 2Sum by fixing one element
2. **Two pointers:** Works well on sorted arrays
3. **Duplicate handling:** Skip consecutive duplicates to avoid duplicate results
4. **Optimization:** Sorting + two pointers is better than brute force

---

## Edge Cases

- All zeros: `[0,0,0]` → `[[0,0,0]]`
- No solution: `[1,2,3]` → `[]`
- Multiple duplicates: `[-1,-1,-1,2]` → `[[-1,-1,2]]`
- Minimum size: `[0,0,0]` → `[[0,0,0]]`

---

## Related Problems
- [[Two-Sum]] - Foundation problem
- [[Four-Sum]] - Extension to four numbers
- [[3Sum-Closest]] - Find closest sum to target
- [[3Sum-Smaller]] - Count triplets with sum < target

---

## Tags
#arrays #two-pointers #sorting #medium #blind75
