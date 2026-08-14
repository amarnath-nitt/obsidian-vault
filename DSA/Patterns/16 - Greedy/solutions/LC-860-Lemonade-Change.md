# Lemonade Change (LC 860)

**Difficulty**: Easy  
**Pattern**: Greedy  
**LeetCode**: https://leetcode.com/problems/lemonade-change/

## Problem Statement
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time.
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Return `true` if you can provide every customer with correct change, or `false` otherwise.

**Example:**
```
Input: bills = [5,5,5,10,20]
Output: true
```

## Approach: Greedy Simulation

### Intuition
Count $5 and $10 bills.
When customer gives $5: increment 5s.
When customer gives $10: decrement 5s, increment 10s.
When customer gives $20: EITHER (give one $10 + one $5) OR (give three $5).
Greedy choice: Prefer to give $10 + $5 because $5 bills are more versatile.

### Java Code
```java
class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        
        for (int bill : bills) {
            if (bill == 5) {
                five++;
            } else if (bill == 10) {
                if (five == 0) return false;
                five--;
                ten++;
            } else { // bill == 20
                if (ten > 0 && five > 0) {
                    ten--;
                    five--;
                } else if (five >= 3) {
                    five -= 3;
                } else {
                    return false;
                }
            }
        }
        
        return true;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1)

## Key Takeaways
- Prioritize spending less flexible resources (spend 10s before 5s)
