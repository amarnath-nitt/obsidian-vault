# Valid Parentheses

**Difficulty:** Easy  
**Category:** Stack  
**LeetCode Link:** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

## Problem Statement

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only '()[]{}'.

---

## Intuition

We need to efficiently solve this problem using appropriate data structures.

---

## Approach 1: Naive Solution

### Algorithm
1. For each closing bracket, search backwards for matching opening bracket
2. Mark used brackets
3. Check if all brackets are matched

### Java Code
```java
class Solution {
    public boolean isValid(String s) {
        // Naive: repeatedly remove valid pairs until none left
        while (s.contains("()") || s.contains("[]") || s.contains("{}")) {
            s = s.replace("()", "");
            s = s.replace("[]", "");
            s = s.replace("{}", "");
        }
        return s.isEmpty();
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n²) - Multiple passes through string
- **Space Complexity:** O(n) - String replacements create new strings

### Drawbacks
- Inefficient for large inputs
- Can be optimized significantly

---

## Approach 2: Optimized Solution

### Algorithm
1. Use a stack to track opening brackets
2. For each character:
   - If opening bracket, push to stack
   - If closing bracket, check if it matches top of stack
3. Stack should be empty at the end

### Java Code
```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            // Push opening brackets
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            }
            // Check closing brackets
            else {
                if (stack.isEmpty()) return false;
                
                char top = stack.pop();
                if (c == ')' && top != '(') return false;
                if (c == ']' && top != '[') return false;
                if (c == '}' && top != '{') return false;
            }
        }
        
        return stack.isEmpty();
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass through string
- **Space Complexity:** O(n) - Stack can hold up to n/2 brackets

### Why This is Better
- ✅ Optimal time complexity
- ✅ Clean and readable
- ✅ Handles all edge cases

---

## Key Takeaways

1. **Pattern:** Stack is perfect for matching pairs
2. **LIFO property:** Last opened must be first closed
3. **Edge cases:** Empty stack when closing, remaining items at end

---

## Edge Cases

- Empty string: `""` → `true`
- Only opening: `"((("` → `false`
- Only closing: `")))"` → `false`
- Wrong order: `"([)]"` → `false`

---

## Related Problems
- Similar problems in the same category

---

## Tags
#stack #easy #blind75

---

## Visualization

- Embed: `![](../assets/valid-parentheses/step-1.svg)`
- Obsidian embed: `![[../assets/valid-parentheses/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="600" height="120">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="24" fill="#222">Stack snapshot while parsing "()[]{}"</text>
    <g transform="translate(20,40)">
        <rect x="0" y="0" width="40" height="24" fill="#fff" stroke="#4b6cc1"/>
        <text x="20" y="16" text-anchor="middle">(</text>
        <rect x="50" y="0" width="40" height="24" fill="#fff" stroke="#4b6cc1"/>
        <text x="70" y="16" text-anchor="middle">[</text>
    </g>
</svg>
