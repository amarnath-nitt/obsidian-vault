# Last Stone Weight (LC 1046)

**Difficulty**: Easy  
**Pattern**: Top K Elements / Heap  
**LeetCode**: https://leetcode.com/problems/last-stone-weight/

## Problem Statement
You are given an array of integers `stones` where `stones[i]` is the weight of the `i`th stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:
- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.
At the end of the game, there is at most one stone left. Return the weight of the last remaining stone. If there are no stones left, return 0.

**Example:**
```
Input: stones = [2,7,4,1,8,1]
Output: 1
```

## Approach: Max-Heap

### Intuition
Always need "heaviest two stones". Use Max-Heap.
Extract two, calculate diff, push back if diff > 0.

### Java Code
```java
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        for (int stone : stones) {
            maxHeap.offer(stone);
        }
        
        while (maxHeap.size() > 1) {
            int y = maxHeap.poll();
            int x = maxHeap.poll();
            
            if (x != y) {
                maxHeap.offer(y - x);
            }
        }
        
        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}
```

### Complexity
- **Time**: O(N log N)
- **Space**: O(N)

## Key Takeaways
- Simulation using Heap
