# Find the Duplicate Number (LC 287)

**Difficulty**: Medium  
**Pattern**: Fast & Slow Pointers  
**LeetCode**: https://leetcode.com/problems/find-the-duplicate-number/

## Problem Statement
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive. There is only one repeated number in `nums`, return this repeated number. You must solve the problem without modifying the array and using only constant extra space.

**Example 1:**
```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2:**
```
Input: nums = [3,1,3,4,2]
Output: 3
```

## Approach 1: Brute Force (Nested Loops)

### Intuition
Compare each element with every other element to find the duplicate.

### Java Code
```java
class Solution {
    public int findDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return nums[i];
                }
            }
        }
        return -1;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)

## Approach 2: Optimized (Fast & Slow Pointers - Floyd's Algorithm)

### Intuition
Treat the array as a linked list where `nums[i]` points to index `nums[i]`. Since there's a duplicate, there must be a cycle. Use Floyd's cycle detection to find where the cycle begins - that index is the duplicate number.

**Key Insight**: Array values are in range [1, n], so index 0 is never pointed to, making it a safe starting point.

### Java Code
```java
class Solution {
    public int findDuplicate(int[] nums) {
        // Phase 1: Find intersection point in cycle
        int slow = nums[0];
        int fast = nums[0];
        
        do {
            slow = nums[slow];           // Move 1 step
            fast = nums[nums[fast]];     // Move 2 steps
        } while (slow != fast);
        
        // Phase 2: Find entrance to cycle (duplicate number)
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return slow;
    }
}
```

### Why This Works
```
Example: [1,3,4,2,2]
Index:    0 1 2 3 4

Index → Value mapping creates linked list:
0 → 1 → 3 → 2 → 4 → 2 (cycle!)

The duplicate (2) creates the cycle entrance
```

### Complexity Analysis
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) - No modification, no extra space

## Alternative Approaches (Not O(1) space)

### Using HashSet
```java
public int findDuplicate(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    for (int num : nums) {
        if (seen.contains(num)) return num;
        seen.add(num);
    }
    return -1;
}
```
- Time: O(n), Space: O(n)

### Using Sorting (modifies array)
```java
public int findDuplicate(int[] nums) {
    Arrays.sort(nums);
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] == nums[i-1]) return nums[i];
    }
    return -1;
}
```
- Time: O(n log n), Space: O(1) but modifies array

## Key Takeaways
- Clever application of Floyd's algorithm on arrays
- Treat array values as pointers to indices
- Duplicate creates a cycle in the implicit linked list
- Achieves O(n) time and O(1) space without modification
- One of the most elegant uses of fast & slow pointers
