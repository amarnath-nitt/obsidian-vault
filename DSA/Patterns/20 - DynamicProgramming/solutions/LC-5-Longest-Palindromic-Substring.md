---
solved: false
difficulty: Medium
pattern: Dynamic Programming
lc_number: 5
date_solved: 
tags:
  - dsa
  - dynamic-programming
  - medium
---
# Longest Palindromic Substring (LC 5)

**Difficulty**: Medium  
**Pattern**: Dynamic Programming / Expand Around Center  
**LeetCode**: https://leetcode.com/problems/longest-palindromic-substring/

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

**Example:**
```
Input: s = "babad"
Output: "bab"
```

## Approach 1: Expand Around Center

### Intuition
A palindrome mirrors around its center.
Centers can be a character (odd length) or between characters (even length).
Total centers = `2n - 1`.
Expand from each center as long as `s[left] == s[right]`.

### Java Code
```java
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);     // Odd cases
            int len2 = expandAroundCenter(s, i, i + 1); // Even cases
            int len = Math.max(len1, len2);
            
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }
    
    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```

## Approach 2: DP

### Intuition
`dp[i][j]` = true if `s[i...j]` is palindrome.
`dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]`.
Base cases: len=1 true, len=2 check chars.

### Complexity
- **Time**: O(N^2)
- **Space**: O(1) for Expand, O(N^2) for DP

## Key Takeaways
- "Expand Around Center" saves space compared to DP
- Handling both odd and even length centers is key
