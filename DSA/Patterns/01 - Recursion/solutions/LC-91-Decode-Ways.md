# Decode Ways (LC 91)

**Difficulty**: Medium  
**Pattern**: Recursion / Memoization  
**LeetCode**: https://leetcode.com/problems/decode-ways/

## Problem Statement
Given a string of digits, return how many ways it can be decoded where `A = 1` through `Z = 26`.

## Recursive Idea
From each index, decode one digit if valid, and decode two digits if the number is between `10` and `26`.

## Intuition: Recurrence Relation & Memoization

### The Core Insight
To count ways to decode up to position i, consider what digit we see:

**At position i, we can:**
1. Decode the **single digit** (if it's 1-9)
   - Valid single digit contributes: `dp[i-1]` ways
2. Decode **two digits** (if they form 10-26)
   - Valid two-digit number contributes: `dp[i-2]` ways

**Recurrence Relation:**
```
dp[i] = (if digit[i] is 1-9: dp[i-1]) 
      + (if digit[i-1:i] is 10-26: dp[i-2])
```

### Why This Works
Each substring can extend the previous solution in only two independent ways:
- Last digit stands alone as a single-digit decode
- Last two digits form a valid two-digit decode (10-26 only)

Since these choices are mutually exclusive, we **add them**.

### Working Through Example: s="226"

Index mapping: `[0]='2', [1]='2', [2]='6'`

**Base Cases:**
- `dp[0]` = 1  (single digit '2' → 'B')
- `dp[1]` = ?
  - Single digit '2' → 'B' (valid, so at least 1)
  - Two digits '22' → 'V' (valid 10-26, so +1)
  - Total: `dp[1] = 2`

**Building up:**
- `dp[2]` = ?
  - Single digit '6' → 'F' (valid 1-9, so add `dp[1]` = 2)
  - Two digits '26' → 'Z' (valid 10-26, so add `dp[0]` = 1)
  - Total: `dp[2] = 2 + 1 = 3`

**The 3 Ways to Decode "226":**
1. `2 | 2 | 6` → {B, V, F}
2. `22 | 6` → {V, F}
3. `2 | 26` → {B, Z}

### Space Optimization
We only ever need the last two DP values:
```java
int prev2 = 1, prev1 = 1;  // dp[-1] and dp[0]
for (int i = 2; i <= n; i++) {
    int current = 0;
    if (oneDigitValid) current += prev1;
    if (twoDigitsValid) current += prev2;
    prev2 = prev1;
    prev1 = current;
}
return prev1;
```
Reduces space from O(n) to **O(1)** while keeping O(n) time.

## Java Code
```java
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.isEmpty() || s.charAt(0) == '0') {  
		    return 0;  
		}  
		int n = s.length();  
		int[] dp = new int[n + 1];  
		dp[0] = 1; // Base case: empty string has one way to decode  
		dp[1] = 1; // Base case: single character (not '0') has one way to decode  
		  
		for (int i = 2; i <= n; i++) {  
		    int oneDigit = Integer.parseInt(s.substring(i - 1, i));  
		    int twoDigits = Integer.parseInt(s.substring(i - 2, i));  
		  
		    // Check if the last one digit is valid (1-9)  
		    if (oneDigit >= 1 && oneDigit <= 9) {  
		        dp[i] += dp[i - 1];  
		    }  
		  
		    // Check if the last two digits form a valid number (10-26)  
		    if (twoDigits >= 10 && twoDigits <= 26) {  
		        dp[i] += dp[i - 2];  
		    }  
		}  
		  
		return dp[n];
    }
}
```

## Alternative Optimal Solution: Bottom-Up DP with O(1) Space
Let `dp[i]` mean the number of ways to decode from index `i`. Only `dp[i + 1]` and `dp[i + 2]` are needed.

```java
class Solution {
    public int numDecodings(String s) {
        int next = 1;
        int nextNext = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            int current = 0;
            if (s.charAt(i) != '0') {
                current = next;
                if (i + 1 < s.length()) {
                    int value = (s.charAt(i) - '0') * 10 + (s.charAt(i + 1) - '0');
                    if (value <= 26) {
                        current += nextNext;
                    }
                }
            }
            nextNext = next;
            next = current;
        }
        return next;
    }
}
```

### Alternative Complexity
- **Time**: O(n)
- **Space**: O(1)

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Takeaways
- A leading `0` cannot be decoded.
- The recursion branches on valid one-digit and two-digit choices.
