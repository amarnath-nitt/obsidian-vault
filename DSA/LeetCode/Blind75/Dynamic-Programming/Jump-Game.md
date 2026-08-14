# Jump Game

**Difficulty:** Medium  
**Category:** Dynamic Programming  
**LeetCode Link:** [Jump Game](https://leetcode.com/problems/jump-game/)

---

## Approach: Greedy

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

### Complexity
- **Time:** O(n)
- **Space:** O(1)

---

## Tags
#dynamic-programming #greedy #medium #blind75
