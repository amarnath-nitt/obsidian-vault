# Word Break

**Difficulty:** Medium
**Category:** Dynamic Programming
**LeetCode Link:** [Word Break](https://leetcode.com/problems/word-break/)

---

## Problem Statement

Given a string `s` and a dictionary `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Example:**
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
```

---

## Intuition

`dp[i]` = can the substring `s[0..i-1]` be segmented using dictionary words? For each position `i`, check all substrings ending at `i` — if `dp[j]` is true and `s[j..i]` is in the dictionary, then `dp[i]` is true.

---

## Approach: Bottom-Up DP

### Algorithm
1. `dp[0] = true` (empty string is always valid)
2. For each `i` from 1 to `n`, for each `j` from 0 to `i`:
   - If `dp[j]` is true and `s.substring(j, i)` is in the word set → `dp[i] = true`
3. Return `dp[n]`

### Java Code
```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }
}
```

### Step-by-Step Example
`s = "leetcode"`, `wordDict = ["leet","code"]`:
```
dp[0] = true
dp[4]: j=0, dp[0]=true, s[0..4]="leet" ✓ → dp[4]=true
dp[8]: j=4, dp[4]=true, s[4..8]="code" ✓ → dp[8]=true
Return true
```

### Complexity Analysis
- **Time Complexity:** O(n² × m) — n² substrings, m = avg word length for substring comparison
- **Space Complexity:** O(n + dict size)

---

## Key Takeaways

1. **DP definition:** `dp[i]` = can `s[0..i-1]` be segmented
2. **HashSet:** O(1) word lookup instead of O(n) list search
3. **Break early:** Once `dp[i]` is set to true, no need to check more `j` values

---

## Tags
#dynamic-programming #medium #blind75
