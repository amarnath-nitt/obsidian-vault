---
solved: false
difficulty: Medium
pattern: Monotonic Stack
lc_number: 402
date_solved: 
tags:
  - dsa
  - monotonic-stack
  - medium
---
# Remove K Digits (LC 402)

**Difficulty**: Medium  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/remove-k-digits/

## Problem Statement
Given string `num` representing a non-negative integer `num`, and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.
Result should not contain leading zeros.

**Example:**
```
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

## Approach: Monotonic Stack (Increasing)

### Intuition
To make a number smaller, we prefer smaller digits at the front (higher significance).
If `num[i] < num[i-1]`, we should remove `num[i-1]`.
Use a stack to maintain an increasing sequence of digits.
If current digit `<` stack top, pop stack (remove digit) and decrease `k`.

### Java Code
```java
class Solution {
    public String removeKdigits(String num, int k) {
        if (k >= num.length()) return "0";
        
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : num.toCharArray()) {
            while (k > 0 && !stack.isEmpty() && stack.peek() > c) {
                stack.pop();
                k--;
            }
            stack.push(c);
        }
        
        // If k > 0, remove digits from the end
        while (k > 0) {
            stack.pop();
            k--;
        }
        
        // Construct string (reverse logic since stack is LIFO)
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        sb.reverse();
        
        // Remove leading zeros
        while (sb.length() > 1 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }
        
        return sb.toString();
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- "Smallest Subsequence" logic
- Greedy with Stack to maintain order
