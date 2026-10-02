# Decode Ways

**Difficulty:** Medium
**Category:** Dynamic Programming
**LeetCode Link:** [Decode Ways](https://leetcode.com/problems/decode-ways/)

---

## Problem Statement

A message is encoded where `'A'→1`, `'B'→2`, ..., `'Z'→26`. Given a string of digits, return the number of ways to decode it.

**Example:**
```
Input: s = "226"
Output: 3  ("2,2,6" | "22,6" | "2,26")
```

---

## Intuition

At each position, we can decode one digit (if it's not '0') or two digits (if the two-digit number is between 10 and 26). This is similar to Climbing Stairs — at each step we can take 1 or 2 steps, with validity constraints.

---

## Approach: O(1) Space DP

### Algorithm
- `prev1` = ways to decode up to current position
- `prev2` = ways to decode up to two positions back
- For each character:
  - If current digit != '0': can decode as single digit → add `prev1`
  - If two-digit number (with previous digit) is 10–26: can decode as two digits → add `prev2`

### Java Code
```java
class Solution {
    public int numDecodings(String s) {
        if (s.charAt(0) == '0') return 0;

        int prev2 = 1; // dp[i-2]
        int prev1 = 1; // dp[i-1]

        for (int i = 1; i < s.length(); i++) {
            int current = 0;

            // Single digit decode (not '0')
            if (s.charAt(i) != '0') {
                current = prev1;
            }

            // Two digit decode (10–26)
            int twoDigit = Integer.parseInt(s.substring(i - 1, i + 1));
            if (twoDigit >= 10 && twoDigit <= 26) {
                current += prev2;
            }

            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}
```

### Step-by-Step Example
`s = "226"`:
```
i=0: prev2=1, prev1=1 (base)
i=1: s[1]='2' != '0' → current=prev1=1; twoDigit=22 ∈ [10,26] → current+=prev2=1 → current=2; prev2=1, prev1=2
i=2: s[2]='6' != '0' → current=prev1=2; twoDigit=26 ∈ [10,26] → current+=prev2=1 → current=3; prev2=2, prev1=3
Return 3
```

### Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Key Takeaways

1. **Pattern:** Fibonacci-style DP with validity constraints
2. **'0' handling:** A standalone '0' is invalid; only valid as part of 10 or 20
3. **Two-digit range:** Only 10–26 maps to valid letters

---

## Tags
#dynamic-programming #medium #blind75
