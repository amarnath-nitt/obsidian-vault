# Generate Parentheses (LC 22)

**Difficulty**: Medium  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/generate-parentheses/

## Problem Statement
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

## Approach: Backtracking

### Intuition
Build the string one character at a time.
Constraint 1: We can add a `(` if `open < n`.
Constraint 2: We can add a `)` if `closed < open`.
Base case: `open == n && closed == n`.

### Java Code
```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(n, 0, 0, new StringBuilder(), result);
        return result;
    }
    
    private void backtrack(int n, int open, int closed, StringBuilder current, List<String> result) {
        if (current.length() == n * 2) {
            result.add(current.toString());
            return;
        }
        
        if (open < n) {
            current.append('(');
            backtrack(n, open + 1, closed, current, result);
            current.deleteCharAt(current.length() - 1);
        }
        
        if (closed < open) {
            current.append(')');
            backtrack(n, open, closed + 1, current, result);
            current.deleteCharAt(current.length() - 1);
        }
    }
}
```

### Complexity
- **Time**: O(4^n / sqrt(n)) - Catalan number
- **Space**: O(n)

## Key Takeaways
- Backtracking with state constraints (open < n, closed < open)
- Ensures validity during construction rather than validating after
