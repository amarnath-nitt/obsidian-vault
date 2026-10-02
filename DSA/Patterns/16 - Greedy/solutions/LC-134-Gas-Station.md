---
solved: false
difficulty: Medium
pattern: Greedy
lc_number: 134
date_solved: 
tags:
  - dsa
  - greedy
  - medium
---
# Gas Station (LC 134)

**Difficulty**: Medium  
**Pattern**: Greedy  
**LeetCode**: https://leetcode.com/problems/gas-station/

## Problem Statement
There are `n` gas stations along a circular route. `gas[i]` is gas at station `i`, `cost[i]` is gas needed to travel from `i` to `i+1`.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. Solutions are guaranteed to be unique.

**Example:**
```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
```

## Approach: Greedy

### Intuition
1. If total gas < total cost, it's impossible. Return -1.
2. If we start at A and fail at B, then any station between A and B also cannot be a valid start. Why? Because we arrived at any intermediate station with >= 0 gas (since we didn't fail *before* B), so starting there with 0 gas is strictly worse.
3. So, if we fail, just try `B + 1` as the new start.

### Java Code
```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0;
        int totalCost = 0;
        
        for (int i = 0; i < gas.length; i++) {
            totalGas += gas[i];
            totalCost += cost[i];
        }
        
        if (totalGas < totalCost) return -1;
        
        int currentGas = 0;
        int start = 0;
        
        for (int i = 0; i < gas.length; i++) {
            currentGas += gas[i] - cost[i];
            
            // If tank drops below 0, we can't complete from 'start'
            // Reset start to next station and current gas to 0
            if (currentGas < 0) {
                start = i + 1;
                currentGas = 0;
            }
        }
        
        return start;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Takeaways
- Check feasibility first with global sums
- Greedy choice: extend as far as possible
- If stuck, skip past the stuck point (optimization over O(n²) simulation)
