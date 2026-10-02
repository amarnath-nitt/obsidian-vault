---
solved: false
difficulty: Medium
pattern: Sliding Window
lc_number: 424
date_solved: 
tags:
  - dsa
  - sliding-window
  - medium
---
# Longest Repeating Character Replacement (LC 424)

**Difficulty**: Medium  
**Pattern**: Sliding Window  
**LeetCode**: https://leetcode.com/problems/longest-repeating-character-replacement/

## Problem Statement
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Example 1:**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2:**
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
```

## Approach 1: Brute Force

### Intuition
Try all possible substrings and check if each can be made uniform with at most k replacements.

### Java Code
```java
class Solution {
    public int characterReplacement(String s, int k) {
        int maxLen = 0;
        
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                String substring = s.substring(i, j + 1);
                if (canMakeUniform(substring, k)) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }
        
        return maxLen;
    }
    
    private boolean canMakeUniform(String s, int k) {
        int[] freq = new int[26];
        int maxFreq = 0;
        
        for (char c : s.toCharArray()) {
            freq[c - 'A']++;
            maxFreq = Math.max(maxFreq, freq[c - 'A']);
        }
        
        // Need to replace: total length - most frequent char count
        return s.length() - maxFreq <= k;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n² × 26) = O(n²)
- **Space Complexity**: O(1)

## Approach 2: Optimized (Sliding Window)

### Intuition
Use a sliding window where we track character frequencies. A window is valid if `windowSize - maxFreq <= k`. Expand window while valid, contract when invalid.

**Key Insight**: We need to replace `windowSize - maxFreq` characters to make all characters the same.

### Java Code
```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int maxCount = 0;  // Max frequency of any character in current window
        int maxLen = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            // Expand window
            count[s.charAt(right) - 'A']++;
            maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']);
            
            // Contract window if invalid
            // (window size - max freq) = replacements needed
            while (right - left + 1 - maxCount > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }
            
            // Update result
            maxLen = Math.max(maxLen, right - left + 1);
        }
        
        return maxLen;
    }
}
```

### Optimized Version (Avoid recalculating maxCount)
```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int maxCount = 0;
        int left = 0;
        int maxLen = 0;
        
        for (int right = 0; right < s.length(); right++) {
            count[s.charAt(right) - 'A']++;
            maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']);
            
            // Only need to check if current window is invalid
            // No need to update maxCount when shrinking
            if (right - left + 1 - maxCount > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }
            
            maxLen = Math.max(maxLen, right - left + 1);
        }
        
        return maxLen;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass
- **Space Complexity**: O(1) - Fixed array of size 26

## Visual Example
```
s = "AABABBA", k = 1

Window: AABAB
Freq: A=3, B=2
maxFreq = 3
WindowSize = 5
Replacements needed = 5 - 3 = 2 > k (invalid!)

Contract to: AABA
Freq: A=3, B=1
maxFreq = 3
WindowSize = 4
Replacements needed = 4 - 3 = 1 = k (valid!)
Result: 4
```

## Key Takeaways
- Window is valid when `windowSize - maxFreq <= k`
- maxCount tracks most frequent character in window
- Don't need to recalculate maxCount when shrinking (optimization)
- Classic example of variable-size sliding window
