# Remove Duplicate Letters (LC 316)

**Difficulty**: Medium  
**Pattern**: Monotonic Stack  
**LeetCode**: https://leetcode.com/problems/remove-duplicate-letters/

## Problem Statement
Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

**Example:**
```
Input: s = "cbacdcbc"
Output: "acdb"
```

## Approach: Greedy + Stack

### Intuition
Similar to "Remove K Digits".
We want increasing sequence of characters if possible.
BUT we must ensure every character appears at least once.
Condition to pop `stack.peek()`:
1. `stack.peek() > current_char` (lexicographical order)
2. `stack.peek()` appears again later in string (count > 0).
3. `current_char` is not already in stack.

### Java Code
```java
class Solution {
    public String removeDuplicateLetters(String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        
        boolean[] inStack = new boolean[26];
        Deque<Character> stack = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            count[c - 'a']--; // Decrement remaining count
            
            if (inStack[c - 'a']) continue;
            
            while (!stack.isEmpty() && stack.peek() > c && count[stack.peek() - 'a'] > 0) {
                inStack[stack.pop() - 'a'] = false;
            }
            
            stack.push(c);
            inStack[c - 'a'] = true;
        }
        
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        return sb.reverse().toString();
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1) (Stack size max 26)

## Key Takeaways
- Complex conditions for popping stack
- Tracking "remaining count" is essential
