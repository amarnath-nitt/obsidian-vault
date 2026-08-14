# Two Sum

**Difficulty:** Easy  
**Category:** Arrays & Hashing  
**LeetCode Link:** [Two Sum](https://leetcode.com/problems/two-sum/)

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Constraints:**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

---

## Intuition

We need to find two numbers in the array that sum to the target. The key insight is that for each number `nums[i]`, we need to check if `target - nums[i]` exists in the array.

---

## Approach 1: Brute Force (Naive Solution)

### Algorithm
1. Use two nested loops to check every pair of numbers
2. For each element at index `i`, check all elements after it at index `j`
3. If `nums[i] + nums[j] == target`, return `[i, j]`

### Java Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Check every possible pair
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        // No solution found (shouldn't happen per constraints)
        return new int[] {};
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n²) - We check every pair of elements
- **Space Complexity:** O(1) - Only using constant extra space

### Drawbacks
- Very slow for large arrays
- Redundant comparisons

---

## Approach 2: Hash Map (Optimized Solution)

### Algorithm
1. Create a HashMap to store each number and its index
2. For each element `nums[i]`:
   - Calculate `complement = target - nums[i]`
   - Check if complement exists in the HashMap
   - If yes, return `[map.get(complement), i]`
   - If no, add `nums[i]` and its index to the HashMap
3. This works because we're building the map as we go

### Java Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // HashMap to store value -> index mapping
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // Check if complement exists in map
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            
            // Add current number to map
            map.put(nums[i], i);
        }
        
        // No solution found (shouldn't happen per constraints)
        return new int[] {};
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(n) - HashMap can store up to n elements

### Why This is Better
- ✅ Single pass through array
- ✅ O(1) lookup time for complement
- ✅ Much faster for large inputs
- ✅ Trade space for time efficiency

---

## Key Takeaways

1. **Pattern:** Hash Map for O(1) lookup is a common optimization for "find pair" problems
2. **Trade-off:** We use O(n) extra space to achieve O(n) time instead of O(n²)
3. **One-pass technique:** We don't need to build the entire map first; we can check and add as we go
4. **Complement pattern:** For sum problems, always think about `target - current_value`

---

## Related Problems
- [[Three-Sum]] - Extension to three numbers
- [[Four-Sum]] - Extension to four numbers
- [[Two-Sum-II]] - Sorted array variation

---

## Tags
#arrays #hashing #two-pointers #easy #blind75

---

## Visualization

- Embed: `![](../assets/two-sum/step-1.svg)`
- Obsidian embed: `![[../assets/two-sum/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="720" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:14px}</style>
    <rect x="10" y="10" width="700" height="120" fill="#f8f9fb" stroke="#d1d7e0" rx="8"/>
    <g transform="translate(30,30)">
        <rect x="0" y="0" width="64" height="64" fill="#ffffff" stroke="#4b6cc1"/>
        <text x="32" y="40" text-anchor="middle" fill="#111">2</text>
        <rect x="84" y="0" width="64" height="64" fill="#ffffff" stroke="#4b6cc1"/>
        <text x="116" y="40" text-anchor="middle" fill="#111">7</text>
        <rect x="168" y="0" width="64" height="64" fill="#ffffff" stroke="#4b6cc1"/>
        <text x="200" y="40" text-anchor="middle" fill="#111">11</text>
        <rect x="252" y="0" width="64" height="64" fill="#ffffff" stroke="#4b6cc1"/>
        <text x="284" y="40" text-anchor="middle" fill="#111">15</text>
        <text x="360" y="22" fill="#333">Map snapshot:</text>
        <rect x="440" y="0" width="160" height="64" fill="#fff6e6" stroke="#d4a017"/>
        <text x="520" y="28" text-anchor="middle" fill="#333">{ }</text>
    </g>
    <text x="28" y="120" fill="#666">Initial array and empty hashmap (example step)</text>
</svg>
