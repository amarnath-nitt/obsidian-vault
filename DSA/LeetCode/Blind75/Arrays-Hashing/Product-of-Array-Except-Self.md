# Product of Array Except Self

**Difficulty:** Medium  
**Category:** Arrays & Hashing  
**LeetCode Link:** [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

---

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in **O(n)** time and **without using the division operation**.

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: 
answer[0] = 2*3*4 = 24
answer[1] = 1*3*4 = 12
answer[2] = 1*2*4 = 8
answer[3] = 1*2*3 = 6
```

**Example 2:**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints:**
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix is guaranteed to fit in a 32-bit integer.

**Follow up:** Can you solve it in O(1) extra space? (Output array doesn't count)

---

## Intuition

For each position i, we need the product of all elements except nums[i]. This equals: (product of all elements to the left) × (product of all elements to the right).

---

## Approach 1: Brute Force (Naive Solution)

### Algorithm
1. For each index i, calculate product of all other elements
2. Use nested loop to multiply all elements except current

### Java Code
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        
        for (int i = 0; i < n; i++) {
            int product = 1;
            // Multiply all elements except nums[i]
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    product *= nums[j];
                }
            }
            result[i] = product;
        }
        
        return result;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n²) - Nested loops
- **Space Complexity:** O(1) - Excluding output array

### Drawbacks
- Too slow for large arrays
- Doesn't meet O(n) requirement

---

## Approach 2: Left and Right Products (Optimized Solution)

### Algorithm
1. Create two arrays: `left` and `right`
2. `left[i]` = product of all elements to the left of i
3. `right[i]` = product of all elements to the right of i
4. `result[i] = left[i] * right[i]`

### Java Code
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        
        // Arrays to store left and right products
        int[] left = new int[n];
        int[] right = new int[n];
        int[] result = new int[n];
        
        // Build left products
        left[0] = 1;
        for (int i = 1; i < n; i++) {
            left[i] = left[i - 1] * nums[i - 1];
        }
        
        // Build right products
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }
        
        // Combine left and right
        for (int i = 0; i < n; i++) {
            result[i] = left[i] * right[i];
        }
        
        return result;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Three passes through array
- **Space Complexity:** O(n) - Two extra arrays

---

## Approach 3: Space Optimized (Most Optimized)

### Algorithm
1. Use output array to store left products first
2. Use a variable to track right product while building final result
3. Multiply left product (in result array) with running right product

### Java Code
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        
        // Build left products in result array
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }
        
        // Build right products and multiply with left
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] = result[i] * rightProduct;
            rightProduct *= nums[i];
        }
        
        return result;
    }
}
```

### Step-by-Step Example
For `nums = [1, 2, 3, 4]`:

**After left products:**
```
result = [1, 1, 2, 6]
         [1, 1*1, 1*2, 1*2*3]
```

**After right products:**
```
i=3: result[3] = 6 * 1 = 6,  rightProduct = 4
i=2: result[2] = 2 * 4 = 8,  rightProduct = 12
i=1: result[1] = 1 * 12 = 12, rightProduct = 24
i=0: result[0] = 1 * 24 = 24, rightProduct = 24

result = [24, 12, 8, 6]
```

### Complexity Analysis
- **Time Complexity:** O(n) - Two passes
- **Space Complexity:** O(1) - Only output array (doesn't count per problem)

### Why This is Better
- ✅ O(n) time complexity
- ✅ O(1) extra space (excluding output)
- ✅ Meets all requirements including follow-up
- ✅ Clean and elegant solution

---

## Key Takeaways

1. **Pattern:** Prefix/suffix products are common in array problems
2. **Space optimization:** Reuse output array to store intermediate results
3. **Two-pass technique:** Build left products, then right products
4. **Running product:** Track cumulative product with a variable
5. **No division:** We avoid division entirely by using prefix/suffix approach

---

## Visualization

```
nums    = [1,  2,  3,  4]
left    = [1,  1,  2,  6]  (product of all to the left)
right   = [24, 12, 4,  1]  (product of all to the right)
result  = [24, 12, 8,  6]  (left * right)
```

---

## Edge Cases

- Two elements: `[1, 2]` → `[2, 1]`
- Contains zero: `[1, 0, 3]` → `[0, 3, 0]`
- Multiple zeros: `[0, 0, 3]` → `[0, 0, 0]`
- Negative numbers: `[-1, 2, -3]` → `[-6, 3, -2]`

---

## Related Problems
- [[Maximum-Product-Subarray]] - Similar product calculations
- [[Trapping-Rain-Water]] - Similar prefix/suffix pattern
- [[Best-Time-to-Buy-Sell-Stock]] - Prefix/suffix optimization

---

## Tags
#arrays #prefix-sum #space-optimization #medium #blind75
