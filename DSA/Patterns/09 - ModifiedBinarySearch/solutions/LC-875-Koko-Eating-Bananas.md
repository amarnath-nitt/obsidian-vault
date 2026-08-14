# Koko Eating Bananas (LC 875)

**Difficulty**: Medium  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/koko-eating-bananas/

## Problem Statement
Koko loves to eat bananas. There are `n` piles of bananas, where the `i`th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

**Example:**
```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

## Approach: Binary Search on Answer

### Intuition
Search Space for `k`: `[1, max(piles)]`.
Condition `canEatAll(speed, h)`: Calculate total hours needed.
`hours += (pile + speed - 1) / speed` (Ceiling division).
If `totalHours <= h`, speed is sufficient. Try smaller speed (`right = mid`).
Else, need faster speed (`left = mid + 1`).

### Java Code
```java
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = 0;
        for (int p : piles) right = Math.max(right, p);
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canFinish(piles, h, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
    
    private boolean canFinish(int[] piles, int h, int k) {
        int hours = 0;
        for (int p : piles) {
            hours += (p + k - 1) / k; // Ceiling division
        }
        return hours <= h;
    }
}
```

### Complexity
- **Time**: O(N log(MaxPile))
- **Space**: O(1)

## Key Takeaways
- "Min K to satisfy condition" -> Binary Search on Answer
- Ceiling formula `(a + b - 1) / b`
