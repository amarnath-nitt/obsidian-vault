---
solved: false
difficulty: Medium
pattern: Sliding Window
lc_number: 567
date_solved: 
tags:
  - dsa
  - sliding-window
  - medium
---
# Permutation in String (LC 567)

**Difficulty**: Medium  
**Pattern**: Sliding Window  
**LeetCode**: https://leetcode.com/problems/permutation-in-string/

## Problem Statement
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. In other words, return `true` if one of `s1`'s permutations is a substring of `s2`.

**Example 1:**
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**
```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Approach 1: Brute Force (Generate All Permutations)

### Intuition
Generate all permutations of s1 and check if any of them exists as a substring in s2.

### Java Code
```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        List<String> permutations = new ArrayList<>();
        generatePermutations(s1.toCharArray(), 0, permutations);
        
        for (String perm : permutations) {
            if (s2.contains(perm)) {
                return true;
            }
        }
        return false;
    }
    
    private void generatePermutations(char[] arr, int index, List<String> result) {
        if (index == arr.length) {
            result.add(new String(arr));
            return;
        }
        
        for (int i = index; i < arr.length; i++) {
            swap(arr, i, index);
            generatePermutations(arr, index + 1, result);
            swap(arr, i, index);
        }
    }
    
    private void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
```

### Complexity Analysis
- **Time Complexity**: O(n! × m) - Generate n! permutations, check each in string of length m
- **Space Complexity**: O(n!) - Store all permutations

## Approach 2: Optimized (Sliding Window with Frequency Count)

### Intuition
Instead of generating permutations, use a sliding window of size s1.length() in s2. A permutation exists if character frequencies match. Use two arrays to track frequencies and slide the window while updating counts.

### Java Code
```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        
        int[] s1Count = new int[26];
        int[] s2Count = new int[26];
        
        // Count frequency of characters in s1 and first window of s2
        for (int i = 0; i < s1.length(); i++) {
            s1Count[s1.charAt(i) - 'a']++;
            s2Count[s2.charAt(i) - 'a']++;
        }
        
        // Check if first window matches
        if (matches(s1Count, s2Count)) return true;
        
        // Slide the window
        for (int i = s1.length(); i < s2.length(); i++) {
            // Add new character to window
            s2Count[s2.charAt(i) - 'a']++;
            // Remove old character from window
            s2Count[s2.charAt(i - s1.length()) - 'a']--;
            
            if (matches(s1Count, s2Count)) return true;
        }
        
        return false;
    }
    
    private boolean matches(int[] s1Count, int[] s2Count) {
        for (int i = 0; i < 26; i++) {
            if (s1Count[i] != s2Count[i]) return false;
        }
        return true;
    }
}
```

### Optimized Version (Single Counter)
```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        
        int[] count = new int[26];
        // Initialize with s1 frequencies (negative) and first window of s2 (positive)
        for (int i = 0; i < s1.length(); i++) {
            count[s1.charAt(i) - 'a']--;
            count[s2.charAt(i) - 'a']++;
        }
        
        if (allZero(count)) return true;
        
        for (int i = s1.length(); i < s2.length(); i++) {
            count[s2.charAt(i) - 'a']++;
            count[s2.charAt(i - s1.length()) - 'a']--;
            if (allZero(count)) return true;
        }
        
        return false;
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
- **Time Complexity**: O(n + m) where n = s1.length, m = s2.length
- **Space Complexity**: O(1) - Fixed size array of 26

## Key Takeaways
- Permutation check = frequency count check
- Sliding window with frequency arrays avoids generating all permutations
- Can optimize further by tracking matching character count
- Demonstrates exponential to linear time optimization
