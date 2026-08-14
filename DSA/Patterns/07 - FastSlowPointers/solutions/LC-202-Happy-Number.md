# Happy Number (LC 202)

**Difficulty**: Easy  
**Pattern**: Fast & Slow Pointers  
**LeetCode**: https://leetcode.com/problems/happy-number/

## Problem Statement
Write an algorithm to determine if a number `n` is happy. A happy number is defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (happy), or it loops endlessly in a cycle (not happy).
- Return `true` if `n` is a happy number, `false` otherwise.

**Example 1:**
```
Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
```

**Example 2:**
```
Input: n = 2
Output: false
```

## Approach 1: Brute Force (HashSet to Detect Cycle)

### Intuition
Keep computing the sum of squared digits. Use a HashSet to track numbers we've seen. If we see a number again, we're in a cycle (not happy). If we reach 1, it's happy.

### Java Code
```java
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        
        while (n != 1) {
            if (seen.contains(n)) {
                return false; // Cycle detected
            }
            seen.add(n);
            n = getNext(n);
        }
        
        return true; // Reached 1
    }
    
    private int getNext(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(log n) - Number of digits in n, cycle detection happens quickly
- **Space Complexity**: O(log n) - HashSet stores visited numbers

## Approach 2: Optimized (Fast & Slow Pointers - Floyd's Cycle Detection)

### Intuition
Treat this as a cycle detection problem similar to linked lists. Use fast & slow pointers. Slow computes next number once, fast computes it twice. If they meet at 1, it's happy. If they meet at any other number, there's a cycle (not happy).

### Java Code
```java
class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;
        
        do {
            slow = getNext(slow);              // Move 1 step
            fast = getNext(getNext(fast));     // Move 2 steps
        } while (slow != fast);
        
        return slow == 1; // If they meet at 1, it's happy
    }
    
    private int getNext(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(log n) - Similar to HashSet approach
- **Space Complexity**: O(1) - No extra data structure

## Key Takeaways
- Happy number problem is essentially cycle detection
- Fast & slow pointer works on sequences, not just linked lists
- Do-while loop ensures at least one iteration
- When pointers meet: if at 1, happy; otherwise, cycle detected
- Demonstrates Floyd's algorithm applicability beyond linked lists
