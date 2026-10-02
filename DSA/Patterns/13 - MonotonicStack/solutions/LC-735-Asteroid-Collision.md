---
solved: false
difficulty: Medium
pattern: Monotonic Stack
lc_number: 735
date_solved: 
tags:
  - dsa
  - monotonic-stack
  - medium
---
# Asteroid Collision (LC 735)

**Difficulty**: Medium  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/asteroid-collision/

## Problem Statement
We are given an array `asteroids` of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

**Example:**
```
Input: asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
```

## Approach: Stack Simulation

### Intuition
Traverse asteroids.
If current `ast > 0` (moving right), push to stack.
If current `ast < 0` (moving left):
- It collides with stack top if `stack.peek() > 0`.
- While collision happens:
  - If `stack.peek() < |ast|`, stack top explodes (pop). Continue checking.
  - If `stack.peek() == |ast|`, both explode (pop) and currents destroys. Stop checking.
  - If `stack.peek() > |ast|`, current destroys. Stop checking.
- If stack empty or top is negative (moving left), push current (no collision).

### Java Code
```java
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int ast : asteroids) {
            boolean exploded = false;
            while (!stack.isEmpty() && ast < 0 && stack.peek() > 0) {
                if (stack.peek() < -ast) {
                    stack.pop();
                    continue; // Continue checking next stack element
                } else if (stack.peek() == -ast) {
                    stack.pop();
                    exploded = true;
                    break;
                } else {
                    // stack.peek() > -ast
                    exploded = true;
                    break;
                }
            }
            if (!exploded) {
                stack.push(ast);
            }
        }
        
        int[] result = new int[stack.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }
        return result;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- Simulation using stack to handle collisions
- Similar to parentheses matching but with "exploding" logic
