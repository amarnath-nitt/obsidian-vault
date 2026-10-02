---
solved: false
difficulty: Medium
pattern: Sliding Window
lc_number: 438
date_solved: 
tags:
  - dsa
  - sliding-window
  - medium
---
# Find All Anagrams in a String (LC 438)

**Difficulty**: Medium  
**Pattern**: Sliding Window  
**LeetCode**: https://leetcode.com/problems/find-all-anagrams-in-a-string/

## Problem Statement
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`.

**Example 1:**
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

## Approach 1: Brute Force

### Intuition
Check every substring of length p.length() and see if it's an anagram of p.

### Java Code
```java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) return result;
        
        for (int i = 0; i <= s.length() - p.length(); i++) {
            String substring = s.substring(i, i + p.length());
            if (isAnagram(substring, p)) {
                result.add(i);
            }
        }
        
        return result;
    }
    
    private boolean isAnagram(String s1, String s2) {
        int[] count = new int[26];
        for (char c : s1.toCharArray()) {
            count[c - 'a']++;
        }
        for (char c : s2. toCharArray()) {
            count[c - 'a']--;
        }
        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n × m) where n = s.length, m = p.length
- **Space Complexity**: O(1)

## Approach 2: Optimized (Sliding Window with Frequency Array)

### Intuition
Use a fixed-size sliding window of length p.length(). Maintain frequency counts and slide the window, updating counts incrementally.

### Java Code
```java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) return result;
        
        int[] pCount = new int[26];
        int[] sCount = new int[26];
        
        // Count frequency in p and first window  of s
        for (int i = 0; i < p.length(); i++) {
            pCount[p.charAt(i) - 'a']++;
            sCount[s.charAt(i) - 'a']++;
        }
        
        // Check first window
        if (Arrays.equals(pCount, sCount)) {
            result.add(0);
        }
        
        // Slide window
        for (int i = p.length(); i < s.length(); i++) {
            // Add new character
            sCount[s.charAt(i) - 'a']++;
            // Remove old character
            sCount[s.charAt(i - p.length()) - 'a']--;
            
            // Check if anagram
            if (Arrays.equals(pCount, sCount)) {
                result.add(i - p.length() + 1);
            }
        }
        
        return result;
    }
}
```

### Further Optimization (Avoid Arrays.equals)
```java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) return result;
        
        int[] count = new int[26];
        
        // Initialize: p frequencies negative, first window positive
        for (int i = 0; i < p.length(); i++) {
            count[p.charAt(i) - 'a']--;
            count[s.charAt(i) - 'a']++;
        }
        
        if (allZero(count)) result.add(0);
        
        // Slide window
        for (int i = p.length(); i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[s.charAt(i - p.length()) - 'a']--;
            
            if (allZero(count)) {
                result.add(i - p.length() + 1);
            }
        }
        
        return result;
    }
    
    private boolean allZero(int[] count) {
        for (int c : count) {
            if (c != 0) return false;
        }
        return true;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n) - Single pass with O(26) checks
- **Space Complexity**: O(1) - Fixed size array

## Key Takeaways
- Fixed-size sliding window perfect for anagram detection
- Can use single array with positive/negative counts
- Incrementally update frequencies instead of recounting
- Similar to "Permutation in String" problem
