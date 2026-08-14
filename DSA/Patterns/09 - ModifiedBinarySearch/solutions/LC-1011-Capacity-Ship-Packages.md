# Capacity To Ship Packages Within D Days (LC 1011)

**Difficulty**: Medium  
**Pattern**: Modified Binary Search  
**LeetCode**: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

## Problem Statement
A conveyor belt has packages that must be shipped from one port to another within `days` days.
The `i`th package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

**Example:**
```
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
```

## Approach: Binary Search on Answer

### Intuition
Search Space: `[max(weights), sum(weights)]`.
Min capacity must handle heaviest package. Max capacity is total weight (1 day).
Condition `possible(capacity)`: Simulates shipping. Count days needed.
If `daysNeeded <= days`, capacity is sufficient. Try smaller (`right = mid`).

### Java Code
```java
class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left = 0, right = 0;
        for (int w : weights) {
            left = Math.max(left, w);
            right += w;
        }
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canShip(weights, days, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
    
    private boolean canShip(int[] weights, int days, int capacity) {
        int daysNeeded = 1;
        int currentLoad = 0;
        
        for (int w : weights) {
            if (currentLoad + w > capacity) {
                daysNeeded++;
                currentLoad = 0;
            }
            currentLoad += w;
        }
        
        return daysNeeded <= days;
    }
}
```

### Complexity
- **Time**: O(N log(SumWeights))
- **Space**: O(1)

## Key Takeaways
- Similar to Koko Eating Bananas
- Determine search range carefully
