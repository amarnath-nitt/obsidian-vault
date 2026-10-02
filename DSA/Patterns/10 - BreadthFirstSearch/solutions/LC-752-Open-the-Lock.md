---
solved: false
difficulty: Medium
pattern: Breadth First Search
lc_number: 752
date_solved: 
tags:
  - dsa
  - breadth-first-search
  - medium
---
# Open the Lock (LC 752)

**Difficulty**: Medium  
**Pattern**: Breadth-First Search  
**LeetCode**: https://leetcode.com/problems/open-the-lock/

## Problem Statement
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: however we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of `deadends` meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

**Example:**
```
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
```

## Approach: BFS

### Intuition
Shortest path from '0000' to `target`.
Each state has 8 neighbors (4 wheels * 2 directions).
Skip deadends and visited states.

### Java Code
```java
class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>();
        for (String d : deadends) dead.add(d);
        
        if (dead.contains("0000")) return -1;
        if ("0000".equals(target)) return 0;
        
        Queue<String> queue = new LinkedList<>();
        queue.offer("0000");
        Set<String> visited = new HashSet<>();
        visited.add("0000");
        
        int steps = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String curr = queue.poll();
                if (curr.equals(target)) return steps;
                
                for (int j = 0; j < 4; j++) {
                    char c = curr.charAt(j);
                    
                    // Move forward
                    String s1 = curr.substring(0, j) + (c == '9' ? 0 : c - '0' + 1) + curr.substring(j + 1);
                    // Move backward
                    String s2 = curr.substring(0, j) + (c == '0' ? 9 : c - '0' - 1) + curr.substring(j + 1);
                    
                    if (!dead.contains(s1) && !visited.contains(s1)) {
                        queue.offer(s1);
                        visited.add(s1);
                    }
                    if (!dead.contains(s2) && !visited.contains(s2)) {
                        queue.offer(s2);
                        visited.add(s2);
                    }
                }
            }
            steps++;
        }
        
        return -1;
    }
}
```

### Complexity
- **Time**: O(10^4 * 4^2 + D), total states limited. D is deadends size.
- **Space**: O(10^4)

## Key Takeaways
- State space exploration BFS
- Handing circular moves
