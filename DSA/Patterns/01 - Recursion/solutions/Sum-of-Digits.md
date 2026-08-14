# Sum of Digits

**Difficulty**: Easy  
**Pattern**: Recursion

## Problem Statement
Given a non-negative integer `n`, return the sum of its digits.

## Recursive Idea
Use `n % 10` to take the last digit, then recurse on `n / 10`.

## Java Code
```java
class Solution {
    public int sumOfDigits(int n) {
        if (n < 10) {
            return n;
        }
        return (n % 10) + sumOfDigits(n / 10);
    }
}
```

## Alternative Optimal Solution: Iterative Digit Peeling
Use the same `% 10` and `/ 10` idea, but keep the state in variables instead of the call stack.

```java
class Solution {
    public int sumOfDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}
```

### Alternative Complexity
- **Time**: O(d), where `d` is the number of digits
- **Space**: O(1)

## Complexity
- **Time**: O(d), where `d` is the number of digits
- **Space**: O(d)

## Key Takeaways
- Modulo extracts the current piece.
- Integer division creates the smaller subproblem.
