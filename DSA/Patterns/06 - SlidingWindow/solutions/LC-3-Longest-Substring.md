# Longest Substring Without Repeating Characters (LC 3)

**Difficulty**: Medium  
**Pattern**: Sliding Window  
**LeetCode**: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

## Approach 1: Brute Force

### Intuition
Check all possible substrings and verify if each one has all unique characters. Keep track of the maximum length found.

### Java Code
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLen = 0;
        
        // Try all possible substrings
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (allUnique(s, i, j)) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
    
    private boolean allUnique(String s, int start, int end) {
        Set<Character> set = new HashSet<>();
        for (int i = start; i <= end; i++) {
            char c = s.charAt(i);
            if (set.contains(c)) {
                return false;
            }
            set.add(c);
        }
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n³) - Two nested loops to generate substrings + O(n) to check uniqueness
- **Space Complexity**: O(min(n, m)) where m is charset size

## Approach 2: Optimized (Sliding Window with HashMap)

### Intuition
Use a sliding window approach with a HashMap to track character positions. When we encounter a duplicate character, we can jump the left pointer to the position after the previous occurrence of that character, rather than moving it one step at a time.

### Java Code
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charIndex = new HashMap<>();
        int maxLen = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            
            // If character is already in map and within current window
            if (charIndex.containsKey(currentChar)) {
                // Move left pointer to right of previous occurrence
                left = Math.max(left, charIndex.get(currentChar) + 1);
            }
            
            // Update character's latest position
            charIndex.put(currentChar, right);
            
            // Update max length
            maxLen = Math.max(maxLen, right - left + 1);
        }
        
        return maxLen;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass through the string
- **Space Complexity**: O(min(n, m)) - HashMap stores at most m characters (charset size)

## Key Takeaways
- Sliding window pattern is ideal for substring/subarray problems
- HashMap helps track character positions to avoid duplicates
- By storing indices, we can jump the left pointer intelligently
- This problem demonstrates how O(n³) can be optimized to O(n)
