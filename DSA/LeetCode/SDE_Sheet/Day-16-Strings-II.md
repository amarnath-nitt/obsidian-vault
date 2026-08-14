# Day 16 — Strings II

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** String — DP, Wildcards, Advanced
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Palindrome Partitioning II (Min Cuts)]] | 132 | Hard | ⬜ |
| 2 | [[#Word Break]] | 139 | Medium | ⬜ |
| 3 | [[#Wildcard Matching]] | 44 | Hard | ⬜ |
| 4 | [[#Regular Expression Matching]] | 10 | Hard | ⬜ |
| 5 | [[#String to Integer (atoi)]] | 8 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Palindrome Partitioning II | Generate every partition and count cuts. Exponential. | Precompute palindrome table and DP cuts. O(n^2). | Center expansion updates cuts with O(n) space. O(n^2). |
| Word Break | Try all split combinations recursively. Exponential. | Memoized DFS by start index. O(n^2). | Bottom-up DP with HashSet/trie pruning. O(n^2). |
| Wildcard Matching | Recursive branching on star. Exponential. | DP over pattern/string. O(n*m). | Greedy two-pointer with last star fallback. O(n+m), O(1). |
| Regular Expression Matching | Recursive branching for star. Exponential. | Memoized recursion. O(n*m). | Bottom-up or rolling DP. O(n*m). |
| String to Integer (atoi) | Use parsing/library conversion and clamp after; overflow risk. | Manual scan with long accumulator. O(n). | Manual scan with pre-overflow checks. O(n), O(1). |

---

## Palindrome Partitioning II (Min Cuts)

**LeetCode 132** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/palindrome-partitioning-ii/)

### Problem
Find the minimum number of cuts to partition string into palindromes.

### Approach (DP)

- `dp[i]` = min cuts for `s[0..i]`
- For each `i`, expand from every center to find palindromes
- If `s[j..i]` is palindrome: `dp[i] = min(dp[i], dp[j-1] + 1)`

### Java Solution

```java
class Solution {
    public int minCut(String s) {
        int n = s.length();
        boolean[][] isPalin = new boolean[n][n];
        int[] dp = new int[n];

        // Precompute palindromes
        for (int i = 0; i < n; i++) {
            Arrays.fill(isPalin[i], false);
            dp[i] = i; // max cuts = i (cut every character)
        }

        for (int center = 0; center < 2 * n - 1; center++) {
            int l = center / 2, r = l + center % 2;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                isPalin[l][r] = true;
                if (l == 0) dp[r] = 0;
                else dp[r] = Math.min(dp[r], dp[l-1] + 1);
                l--; r++;
            }
        }
        return dp[n - 1];
    }
}
```

**Complexity:** Time O(n²) · Space O(n²)

---

## Word Break

**LeetCode 139** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/word-break/)

### Problem
Can `s` be segmented into words from `wordDict`?

### Approach (DP)

- `dp[i]` = can `s[0..i-1]` be segmented?
- For each position `i`, check all substrings `s[j..i]` where `dp[j]` is true

### Java Solution

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && dict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
```

**Complexity:** Time O(n³) (or O(n²) with trie) · Space O(n)

---

## Wildcard Matching

**LeetCode 44** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/wildcard-matching/)

### Problem
`?` matches any single character. `*` matches any sequence (including empty).

### Approach (DP)

- `dp[i][j]` = does `s[0..i-1]` match `p[0..j-1]`?
- If `p[j-1] == '*'`: `dp[i][j] = dp[i][j-1]` (empty) OR `dp[i-1][j]` (match one more char)
- If `p[j-1] == '?' || p[j-1] == s[i-1]`: `dp[i][j] = dp[i-1][j-1]`

### Java Solution

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;

        // '*' can match empty string
        for (int j = 1; j <= n; j++)
            if (p.charAt(j-1) == '*') dp[0][j] = dp[0][j-1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j-1) == '*') {
                    dp[i][j] = dp[i][j-1] || dp[i-1][j]; // empty or match one
                } else if (p.charAt(j-1) == '?' || p.charAt(j-1) == s.charAt(i-1)) {
                    dp[i][j] = dp[i-1][j-1];
                }
            }
        }
        return dp[m][n];
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n) → optimizable to O(n)

---

## Regular Expression Matching

**LeetCode 10** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/regular-expression-matching/)

### Problem
`.` matches any single char. `*` matches zero or more of the preceding element.

### Approach (DP)

- `dp[i][j]` = does `s[0..i-1]` match `p[0..j-1]`?
- If `p[j-1] == '*'`:
  - Zero of preceding: `dp[i][j] = dp[i][j-2]`
  - One or more of preceding: `dp[i][j] |= dp[i-1][j]` if `s[i-1]` matches `p[j-2]`

### Java Solution

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;

        for (int j = 2; j <= n; j++)
            if (p.charAt(j-1) == '*') dp[0][j] = dp[0][j-2];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j-1) == '*') {
                    dp[i][j] = dp[i][j-2]; // zero occurrences
                    if (p.charAt(j-2) == '.' || p.charAt(j-2) == s.charAt(i-1))
                        dp[i][j] |= dp[i-1][j]; // one or more occurrences
                } else if (p.charAt(j-1) == '.' || p.charAt(j-1) == s.charAt(i-1)) {
                    dp[i][j] = dp[i-1][j-1];
                }
            }
        }
        return dp[m][n];
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n)

---

## String to Integer (atoi)

**LeetCode 8** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/string-to-integer-atoi/)

### Problem
Implement `atoi`. Handle leading spaces, sign, digits, overflow.

### Approach

1. Skip leading whitespace
2. Handle optional `+` or `-`
3. Parse digits until non-digit
4. Clamp to `[Integer.MIN_VALUE, Integer.MAX_VALUE]`

### Java Solution

```java
class Solution {
    public int myAtoi(String s) {
        int i = 0, n = s.length();
        while (i < n && s.charAt(i) == ' ') i++; // skip spaces

        int sign = 1;
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            if (s.charAt(i) == '-') sign = -1;
            i++;
        }

        long result = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            result = result * 10 + (s.charAt(i) - '0');
            i++;
            if (result * sign > Integer.MAX_VALUE) return Integer.MAX_VALUE;
            if (result * sign < Integer.MIN_VALUE) return Integer.MIN_VALUE;
        }
        return (int)(result * sign);
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## String DP Patterns

```
Problem                      → DP State
───────────────────────────────────────────────
Word Break                   → dp[i] = can segment s[0..i]
Palindrome min cuts          → dp[i] = min cuts for s[0..i]
Wildcard matching            → dp[i][j] = s[0..i] matches p[0..j]
Regex matching               → dp[i][j] = s[0..i] matches p[0..j]
Longest Palindromic Subseq   → dp[i][j] = LPS of s[i..j]
Edit Distance                → dp[i][j] = min ops to convert s[0..i] to t[0..j]
```

#sde-sheet #strings #dp #day16
