# Regular Expression Matching (LC 10)

**Difficulty**: Hard  
**Pattern**: Recursion / Memoization  
**LeetCode**: https://leetcode.com/problems/regular-expression-matching/

## Problem Statement
Given a string `s` and pattern `p`, implement matching with `.` and `*`.

## Recursive Idea
Compare positions `i` in `s` and `j` in `p`. If the next pattern character is `*`, either skip the `x*` pattern or consume one matching character.

## Interview Approach & Key Intuition

### 1. The Core Idea: Two Pointers with Pattern Lookahead
We match positions in string `s` and pattern `p` simultaneously:
- Keep index `i` for string s
- Keep index `j` in pattern p
- **Always look ahead one position in pattern for `*`**

This allows us to handle star patterns correctly by making choices about whether to use them.

### 2. The Main Challenge: Handling `*` Wildcard
A `*` means "match 0 or more of the PREVIOUS character"

This creates a binary choice at each star:
- **Option A (Skip)**: Skip the `x*` pattern entirely (jump from j to j+2)
- **Option B (Use)**: If current character matches, consume one character and stay at same pattern position to potentially match more

**Example**: s="ab", p="a.*b"
- At position (1,2) comparing 'b' vs '.':
  - Option A: Skip ".*" entirely → need "" to match "" → true ✓
  - Option B: '.' matches any char, so could use it further
- Either path can lead to a match

### 3. Why Memoization is Critical
The recursion tree has massive overlap:
- Same (i, j) state can be reached from multiple paths
- With m characters in s and n in p, we have m×n possible states
- Without memoization: exponential time complexity
- With memoization: O(m×n) time complexity

### 4. Working Through an Example

**Example: s="aa", p="a"**
```
match(0, 0): Compare 'a' with 'a'
  → Match! No '*' follows
  → Need: match(1, 1)
  
match(1, 1): i==1 >= s.length()? Yes. j==1 >= p.length()? Yes.
  → Base case: return true ✓
```

**Example: s="aa", p="a*"**
```
match(0, 0): Compare 'a' with 'a'. Next char '*'? Yes!
  → Option A: Skip "a*" → match(0, 2)
    → i==0 < s.length() but j==2 >= p.length()
    → Need i==0, but i < s.length, so false
  → Option B: Consume 'a' → match(1, 0) (stay at 'a*')
    → match(1, 0): Compare 'a' with 'a'. Next char '*'? Yes!
      → Option A: Skip "a*" → match(1, 2)
        → i==1 < s.length() but j==2 >= p.length()
        → Need both i==1 AND j==2, but i < s.length, so false
      → Option B: match(2, 0) (stay at 'a*')
        → match(2, 0): i==2 >= s.length(), j==0 < p.length()
        → Need i==2 AND j==2, so false

Hmm, let me retrace... Actually match(0,0) with Option A should work differently.
```

**Better Example: s="aa", p="a*"** (Corrected)
```
match(0, 0): i=0, j=0, 'a' vs 'a', next='*'
  Option A: Skip "a*" → match(0, 2)
    match(0, 2): i==0, j==2 (at end of pattern)
    j==p.length()? Yes, so need i==s.length()
    i==s.length()? No (i==0, len==2), so false
  
  Option B: Use "a*" → match(1, 0) (stay at pattern j=0)
    match(1, 0): i=1, j=0, 'a' vs 'a', next='*'
      Option A: Skip "a*" → match(1, 2)
        j==p.length()? Yes, need i==s.length()
        i==s.length()? Yes! return true ✓
```

### 5. State Machine Perspective
Think of this as a state machine:
```
State: (i, j)
Transitions:
  - No '*' ahead: Must match current character, both pointers advance
  - '*' ahead: Two choices:
    - Skip pattern: advance j by 2
    - Consume: advance i by 1, stay at j

Terminal States:
  - j == p.length() AND i == s.length(): MATCH ✓
  - j == p.length() AND i < s.length(): NO MATCH ✗
  - i == s.length() AND p[j:] is all "x*" patterns: MATCH ✓
```

### How to Explain in Interview
"I'll use two pointers with memoization. The key insight is to always look ahead in the pattern for `*`. When I see a star, I have two choices: skip the entire `x*` pattern or use it if the current character matches. I'll use a 2D DP table to memoize (i, j) states since they can repeat across different recursive paths. This converts the exponential recursion tree into O(m×n) time and space."

## Java Code
```java
class Solution {
    public boolean isMatch(String s, String p) {
        Boolean[][] memo = new Boolean[s.length() + 1][p.length() + 1];
        return match(s, p, 0, 0, memo);
    }

    private boolean match(String s, String p, int i, int j, Boolean[][] memo) {
        if (memo[i][j] != null) {
            return memo[i][j];
        }
        if (j == p.length()) {
            return i == s.length();
        }

        boolean firstMatches = i < s.length()
                && (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.');

        boolean answer;
        if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
            answer = match(s, p, i, j + 2, memo)
                    || (firstMatches && match(s, p, i + 1, j, memo));
        } else {
            answer = firstMatches && match(s, p, i + 1, j + 1, memo);
        }

        memo[i][j] = answer;
        return answer;
    }
}
```

## Alternative Optimal Solution: Bottom-Up DP
Fill the same `(i, j)` states iteratively from the end of the strings.

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[m][n] = true;

        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                boolean firstMatches = i < m
                        && (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.');

                if (j + 1 < n && p.charAt(j + 1) == '*') {
                    dp[i][j] = dp[i][j + 2] || (firstMatches && dp[i + 1][j]);
                } else {
                    dp[i][j] = firstMatches && dp[i + 1][j + 1];
                }
            }
        }

        return dp[0][0];
    }
}
```

### Alternative Complexity
- **Time**: O(m * n)
- **Space**: O(m * n)

## Complexity
- **Time**: O(m * n)
- **Space**: O(m * n)

## Key Takeaways
- `*` means zero or more of the previous pattern character.
- Memoization is essential because many `(i, j)` states repeat.
