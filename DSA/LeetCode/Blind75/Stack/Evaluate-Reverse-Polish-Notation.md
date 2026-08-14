# Evaluate Reverse Polish Notation

**Difficulty:** Medium  
**Category:** Stack  
**LeetCode Link:** [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation.

Evaluate the expression and return an integer that represents the value of the expression.

**Note:**
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- Division between two integers should truncate toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in reverse polish notation.

**Example 1:**
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Constraints:**
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator or an integer in the range `[-200, 200]`.

---

## Intuition

RPN (Reverse Polish Notation) naturally maps to stack operations: push operands, pop two operands when you see an operator, push result back.

---

## Approach: Stack-Based Evaluation

### Algorithm
1. Use a stack to store operands
2. For each token:
   - If it's a number, push to stack
   - If it's an operator, pop two operands, apply operation, push result
3. Final stack element is the answer

### Java Code
```java
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        
        for (String token : tokens) {
            if (isOperator(token)) {
                // Pop two operands (order matters for - and /)
                int b = stack.pop();
                int a = stack.pop();
                
                // Apply operator and push result
                int result = applyOperator(a, b, token);
                stack.push(result);
            } else {
                // Push number to stack
                stack.push(Integer.parseInt(token));
            }
        }
        
        return stack.pop();
    }
    
    private boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || 
               token.equals("*") || token.equals("/");
    }
    
    private int applyOperator(int a, int b, String operator) {
        switch (operator) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
            case "/": return a / b;
            default: throw new IllegalArgumentException("Invalid operator");
        }
    }
}
```

### Alternative Compact Version
```java
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        
        for (String token : tokens) {
            switch (token) {
                case "+":
                    stack.push(stack.pop() + stack.pop());
                    break;
                case "-":
                    int b = stack.pop();
                    int a = stack.pop();
                    stack.push(a - b);
                    break;
                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;
                case "/":
                    int divisor = stack.pop();
                    int dividend = stack.pop();
                    stack.push(dividend / divisor);
                    break;
                default:
                    stack.push(Integer.parseInt(token));
            }
        }
        
        return stack.pop();
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass through tokens
- **Space Complexity:** O(n) - Stack can hold up to n/2 operands

### Why This Works
- ✅ Stack naturally handles RPN evaluation
- ✅ LIFO property matches RPN semantics
- ✅ Simple and efficient
- ✅ Handles all operators correctly

---

## Key Takeaways

1. **Pattern:** Stack is perfect for RPN evaluation
2. **Order matters:** For subtraction and division, pop order is important
3. **RPN property:** No parentheses needed, unambiguous evaluation
4. **Stack depth:** Never exceeds number of operands

---

## Step-by-Step Example

For `["2","1","+","3","*"]`:

```
Token "2": stack = [2]
Token "1": stack = [2, 1]
Token "+": pop 1, pop 2, push 2+1=3, stack = [3]
Token "3": stack = [3, 3]
Token "*": pop 3, pop 3, push 3*3=9, stack = [9]
Result: 9
```

---

## Edge Cases

- Single number: `["42"]` → `42`
- Simple operation: `["1","2","+"]` → `3`
- Negative numbers: `["-1","2","+"]` → `1`
- Division truncation: `["4","13","5","/","+"]` → `6`

---

## Related Problems
- [[Basic-Calculator]] - Infix notation
- [[Basic-Calculator-II]] - Infix with operators
- [[Valid-Parentheses]] - Stack for matching

---

## Tags
#stack #math #medium #blind75
