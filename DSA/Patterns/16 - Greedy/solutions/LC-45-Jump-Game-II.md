# Jump Game II (LC 45)

**Difficulty**: Medium  
**Pattern**: Greedy  
**LeetCode**: https://leetcode.com/problems/jump-game-ii/

## Problem Statement
You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.
Each element `nums[i]` represents the maximum length of a forward jump from index `i`.
Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

**Example:**
```
Input: nums = [2,3,1,1,4]
Output: 2
```

## Approach: Greedy BFS

### Intuition
Level-by-level traversal.
`current_end`: The farthest point reachable with current number of jumps.
`farthest`: The farthest point reachable with current+1 jumps.
When we reach `i == current_end`, we increment jumps and update `current_end = farthest`.

### Java Code
```java
class Solution {
    public int jump(int[] nums) {
        int jumps = 0;
        int currentEnd = 0;
        int farthest = 0;
        
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
            }
        }
        
        return jumps;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Implicit BFS structure
- Updates happen only when we reach boundary of current level
