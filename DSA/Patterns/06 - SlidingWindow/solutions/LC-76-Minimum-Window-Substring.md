# Minimum Window Substring (LC 76)

**Difficulty**: Hard  
**Pattern**: Sliding Window  
**LeetCode**: https://leetcode.com/problems/minimum-window-substring/

## Problem Statement
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

**Example 1:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**
```
Input: s = "a", t = "a"
Output: "a"
```

## Approach 1: Brute Force

### Intuition
Generate all possible substrings of `s` and check if each one contains all characters from `t`. Keep track of the minimum length substring that satisfies the condition.

### Java Code
```java
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        
        String result = "";
        int minLen = Integer.MAX_VALUE;
        
        // Try all possible substrings
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                String substring = s.substring(i, j + 1);
                if (containsAll(substring, t)) {
                    if (substring.length() < minLen) {
                        minLen = substring.length();
                        result = substring;
                    }
                }
            }
        }
        
        return result;
    }
    
    private boolean containsAll(String s, String t) {
        Map<Character, Integer> tCount = new HashMap<>();
        for (char c : t.toCharArray()) {
            tCount.put(c, tCount.getOrDefault(c, 0) + 1);
        }
        
        Map<Character, Integer> sCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            sCount.put(c, sCount.getOrDefault(c, 0) + 1);
        }
        
        for (char c : tCount.keySet()) {
            if (sCount.getOrDefault(c, 0) < tCount.get(c)) {
                return false;
            }
        }
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n² × (n + m)) - O(n²) substrings, O(n+m) to check each
- **Space Complexity**: O(m) - HashMap for character counts

## Approach 2: Optimized (Dynamic Sliding Window)

### Intuition
Use two pointers (left and right) to form a dynamic window. Expand the window by moving right until all characters from `t` are included. Then contract from the left to find the minimum window. Use a HashMap to track character frequencies and a counter to track when window is valid.

### Java Code
```java
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        
        Map<Character, Integer> tCount = new HashMap<>();
        for (char c : t.toCharArray()) {
            tCount.put(c, tCount.getOrDefault(c, 0) + 1);
        }
        
        Map<Character, Integer> windowCount = new HashMap<>();
        int required = tCount.size(); // Unique characters in t
        int formed = 0; // Unique characters in window with correct frequency
        
        int left = 0, right = 0;
        int minLen = Integer.MAX_VALUE;
        int minLeft = 0;
        
        while (right < s.length()) {
            // Expand window
            char c = s.charAt(right);
            windowCount.put(c, windowCount.getOrDefault(c, 0) + 1);
            
            // Check if frequency matches for this character
            if (tCount.containsKey(c) && 
                windowCount.get(c).intValue() == tCount.get(c).intValue()) {
                formed++;
            }
            
            // Contract window while it's valid
            while (left <= right && formed == required) {
                // Update result if current window is smaller
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minLeft = left;
                }
                
                // Remove from left
                char leftChar = s.charAt(left);
                windowCount.put(leftChar, windowCount.get(leftChar) - 1);
                
                if (tCount.containsKey(leftChar) &&
                    windowCount.get(leftChar) < tCount.get(leftChar)) {
                    formed--;
                }
                
                left++;
            }
            
            right++;
        }
        
        return minLen == Integer.MAX_VALUE ? "" : s.substring(minLeft, minLeft + minLen);
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n + m) - Each character visited at most twice (by left and right)
- **Space Complexity**: O(m) - HashMap stores characters from t

## Key Takeaways
- Dynamic sliding window: expand when invalid, contract when valid
- Use `formed` counter to avoid checking entire HashMap every time
- Track minimum window parameters (start index and length) separately
- Classic hard problem demonstrating advanced sliding window technique
- Two-pointer technique with intelligent expansion/contraction
