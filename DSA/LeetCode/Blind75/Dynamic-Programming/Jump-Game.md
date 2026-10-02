# Jump Game

**Difficulty:** Medium
**Category:** Dynamic Programming / Greedy
**LeetCode Link:** [Jump Game](https://leetcode.com/problems/jump-game/)

---

## Problem Statement

Given an integer array `nums` where `nums[i]` is the maximum jump length from index `i`, return `true` if you can reach the last index starting from index 0.

**Example:**
```
Input: nums = [2,3,1,1,4]
Output: true

Input: nums = [3,2,1,0,4]
Output: false  (always stuck at index 3)
```

---

## Intuition

At each index, track the farthest position reachable so far. If at any point the current index exceeds the farthest reachable position, we're stuck and can't proceed.

---

## Approach 1: Greedy (Optimal)

### Algorithm
1. Track `maxReach` = farthest index reachable so far
2. For each index `i`:
   - If `i > maxReach` → can't reach here → return false
   - Update `maxReach = max(maxReach, i + nums[i])`
3. If loop completes → return true

### Java Code
```java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
        }

        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Approach 2: DP (Backward)

### Algorithm
Work backwards — mark the last index as a "good" position. For each index, check if it can reach any "good" position. If index 0 is good, return true.

### Java Code
```java
class Solution {
    public boolean canJump(int[] nums) {
        int lastGood = nums.length - 1;

        for (int i = nums.length - 2; i >= 0; i--) {
            if (i + nums[i] >= lastGood) {
                lastGood = i;
            }
        }

        return lastGood == 0;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Key Takeaways

1. **Greedy insight:** Track max reachable index — no need to simulate every jump
2. **Stuck condition:** `i > maxReach` means we can never reach index `i`
3. **Backward DP:** Equivalent approach — find if index 0 can reach a "good" position

---

## Tags
#dynamic-programming #greedy #medium #blind75
