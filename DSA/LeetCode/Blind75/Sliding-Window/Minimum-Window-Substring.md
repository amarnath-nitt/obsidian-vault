# Minimum Window Substring

**Difficulty:** Hard  
**Category:** Sliding Window  
**LeetCode Link:** [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

---

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

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

**Example 3:**
```
Input: s = "a", t = "aa"
Output: ""
```

**Constraints:**
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

**Follow up:** Could you find an algorithm that runs in O(m + n) time?

---

## Intuition

We need to find the smallest substring of `s` that contains all characters from `t`. Use sliding window: expand to find valid window, then contract to minimize.

---

## Approach 1: Brute Force (Naive Solution)

### Algorithm
1. Generate all substrings of `s`
2. Check if each substring contains all characters from `t`
3. Track the minimum valid substring

### Java Code
```java
class Solution {
    public String minWindow(String s, String t) {
        String result = "";
        int minLen = Integer.MAX_VALUE;
        
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
        
        for (char c : s.toCharArray()) {
            if (tCount.containsKey(c)) {
                tCount.put(c, tCount.get(c) - 1);
                if (tCount.get(c) == 0) {
                    tCount.remove(c);
                }
            }
        }
        
        return tCount.isEmpty();
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n³) - O(n²) substrings × O(n) validation
- **Space Complexity:** O(m) - HashMap for character counts

---

## Approach 2: Sliding Window (Optimized Solution)

### Algorithm
1. Count character frequencies in `t`
2. Use two pointers for sliding window
3. Expand window (right++) until all characters from `t` are included
4. Contract window (left++) while maintaining validity
5. Track minimum valid window

### Java Code
```java
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        
        // Count characters in t
        Map<Character, Integer> tCount = new HashMap<>();
        for (char c : t.toCharArray()) {
            tCount.put(c, tCount.getOrDefault(c, 0) + 1);
        }
        
        // Sliding window
        Map<Character, Integer> windowCount = new HashMap<>();
        int left = 0;
        int minLen = Integer.MAX_VALUE;
        int minStart = 0;
        int required = tCount.size(); // Unique characters needed
        int formed = 0; // Unique characters satisfied
        
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            windowCount.put(c, windowCount.getOrDefault(c, 0) + 1);
            
            // Check if current character satisfies requirement
            if (tCount.containsKey(c) && 
                windowCount.get(c).intValue() == tCount.get(c).intValue()) {
                formed++;
            }
            
            // Try to contract window
            while (left <= right && formed == required) {
                // Update result if smaller
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }
                
                // Remove left character
                char leftChar = s.charAt(left);
                windowCount.put(leftChar, windowCount.get(leftChar) - 1);
                
                if (tCount.containsKey(leftChar) && 
                    windowCount.get(leftChar) < tCount.get(leftChar)) {
                    formed--;
                }
                
                left++;
            }
        }
        
        return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(m + n) - Each character visited at most twice
- **Space Complexity:** O(m + n) - HashMaps for character counts

### Why This is Better
- ✅ O(m + n) time - meets follow-up requirement
- ✅ Single pass with two pointers
- ✅ Efficient window contraction
- ✅ Optimal solution

---

## Key Takeaways

1. **Pattern:** Sliding window with character frequency matching
2. **Two maps:** One for target, one for current window
3. **Formed counter:** Track how many unique characters are satisfied
4. **Window contraction:** Shrink from left while maintaining validity
5. **Result tracking:** Update minimum when valid window found

---

## Edge Cases

- No valid window: `s="a", t="aa"` → `""`
- Exact match: `s="a", t="a"` → `"a"`
- Multiple valid windows: Return smallest
- t longer than s: Return `""`

---

## Related Problems
- [[Longest-Substring-Without-Repeating-Characters]] - Similar sliding window
- [[Substring-with-Concatenation-of-All-Words]] - Similar pattern matching
- [[Find-All-Anagrams]] - Similar frequency matching

---

## Tags
#strings #sliding-window #hash-table #hard #blind75
