# Valid Parentheses

**LeetCode 20** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/valid-parentheses/)

### Approach

- Push opening brackets onto stack
- For closing bracket, check if top of stack matches

### Java Solution

```java
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        return stack.isEmpty();
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---
