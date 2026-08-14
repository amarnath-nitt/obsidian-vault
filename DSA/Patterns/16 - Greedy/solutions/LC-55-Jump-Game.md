# Jump Game (LC 55)

**Difficulty**: Medium  
**Pattern**: Greedy  
**LeetCode**: https://leetcode.com/problems/jump-game/

## Existing Solution Reference
This problem is in Blind75: → [Solution](../../../LeetCode/Blind75/Dynamic-Programming/Jump-Game.md)

## Problem Statement
Given an array where each element represents max jump length from that position, determine if you can reach the last index.

**Example:**
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

## Approach 1: Backtracking

### Java Code
```java
class Solution {
    public boolean canJump(int[] nums) {
        return canJumpFrom(0, nums);
    }
    
    private boolean canJumpFrom(int position, int[] nums) {
        if (position >= nums.length - 1) {
            return true;
        }
        
        int furthest = Math.min(position + nums[position], nums.length - 1);
        for (int nextPos = position + 1; nextPos <= furthest; nextPos++) {
            if (canJumpFrom(nextPos, nums)) {
                return true;
            }
        }
        
        return false;
    }
}
```

### Complexity
- **Time**: O(2^n)
- **Space**: O(n)

## Approach 2: Greedy (Optimized)

### Intuition
Work backwards. Track the leftmost position that can reach the end. If we can reach position 0, return true.

### Java Code
```java
class Solution {
    public boolean canJump(int[] nums) {
        int lastGoodIndex = nums.length - 1;
        
        for (int i = nums.length - 1; i >= 0; i--) {
            if (i + nums[i] >= lastGoodIndex) {
                lastGoodIndex = i;
            }
        }
        
        return lastGoodIndex == 0;
    }
}
```

### Alternative (Forward Greedy)
```java
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
            if (maxReach >= nums.length - 1) return true;
        }
        
        return true;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Takeaways
- Greedy approach tracks furthest reachable position
- Backward scan finds leftmost "good" position
- Forward scan checks if we can proceed at each step
- No need to try all possible jumps
