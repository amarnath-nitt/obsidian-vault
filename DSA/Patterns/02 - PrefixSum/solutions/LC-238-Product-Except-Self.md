# Product of Array Except Self (LC 238)

**Difficulty**: Medium  
**Pattern**: Prefix Sum  
**LeetCode**: https://leetcode.com/problems/product-of-array-except-self/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Arrays-Hashing/Product-of-Array-Except-Self.md)

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`. You must write an algorithm that runs in O(n) time and without using the division operation.

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Approach 1: Brute Force

### Intuition
For each position, multiply all other elements.

### Java Code
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        
        for (int i = 0; i < n; i++) {
            int product = 1;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    product *= nums[j];
                }
            }
            answer[i] = product;
        }
        
        return answer;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1) excluding output array

## Approach 2: Optimized (Prefix & Suffix Products)

### Intuition
For each position i, answer[i] = (product of all elements before i) × (product of all elements after i). Use two passes: one for prefix products, one for suffix products.

### Java Code (Two Arrays)
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int[] answer = new int[n];
        
        // Build prefix products
        prefix[0] = 1;
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i-1] * nums[i-1];
        }
        
        // Build suffix products
        suffix[n-1] = 1;
        for (int i = n-2; i >= 0; i--) {
            suffix[i] = suffix[i+1] * nums[i+1];
        }
        
        // Combine
        for (int i = 0; i < n; i++) {
            answer[i] = prefix[i] * suffix[i];
        }
        
        return answer;
    }
}
```

### Space-Optimized Version (O(1) extra space)
```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        
        // Build prefix products in answer array
        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i-1] * nums[i-1];
        }
        
        // Multiply with suffix products on the fly
        int suffix = 1;
        for (int i = n-1; i >= 0; i--) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }
        
        return answer;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Two passes
- **Space Complexity**: O(1) - Only output array (not counted)

## Visual Example
```
nums = [1, 2, 3, 4]

Prefix products:  [1, 1, 2, 6]
Suffix products:  [24, 12, 4, 1]
Result:           [24, 12, 8, 6]

For i=1:
  prefix = 1 (product before index 1)
  suffix = 12 (product after index 1)
  answer = 1 × 12 = 12 ✓
```

## Key Takeaways
- Prefix/suffix product pattern avoids division
- Can optimize space by reusing output array
- Two-pass solution: forward for prefix, backward for suffix
- Classic example of prefix sum concept applied to products
- Handles zeros naturally
