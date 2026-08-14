# Factorial

**Difficulty**: Easy  
**Pattern**: Recursion

## Problem Statement
Return `n!`, where `n! = n * (n - 1) * ... * 1`. By definition, `0! = 1`.

## Recursive Idea
The answer for `n` depends on the answer for `n - 1`.

Base case: `n <= 1` returns `1`.  
Recursive case: `n * factorial(n - 1)`.

## Java Code
```java
class Solution {
    public long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be non-negative");
        }
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
```

## Alternative Optimal Solution: Iterative
For Java, iteration avoids recursion stack growth while keeping the same time complexity.

```java
class Solution {
    public long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be non-negative");
        }

        long answer = 1;
        for (int i = 2; i <= n; i++) {
            answer *= i;
        }
        return answer;
    }
}
```

### Alternative Complexity
- **Time**: O(n)
- **Space**: O(1)

## Complexity
- **Time**: O(n)
- **Space**: O(n) recursion stack

## Key Takeaways
- Factorial is the simplest linear recursion pattern.
- Write the base case before the recursive call.
