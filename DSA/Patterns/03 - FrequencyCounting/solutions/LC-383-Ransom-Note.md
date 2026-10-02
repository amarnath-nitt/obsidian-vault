---
solved: true
difficulty: Easy
pattern: Frequency Counting
lc_number: 383
date_solved: 
tags:
  - dsa
  - frequency-counting
  - easy
---
# Ransom Note

[Problem Link](https://leetcode.com/problems/ransom-note/)

## Problem Statement
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.
Each letter in `magazine` can only be used once in `ransomNote`.

## Approach
Frequency Counting (Array or HashMap).
1.  Count frequency of char in `magazine`.
2.  Iterate `ransomNote`, decrement count.
3.  If count < 0, return false.

## Time and Space Complexity
- **Time Complexity:** O(M + N).
- **Space Complexity:** O(1) (for 26 chars).

## Code
```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] count = new int[26];
        
        for (char c : magazine.toCharArray()) {
            count[c - 'a']++;
        }
        
        for (char c : ransomNote.toCharArray()) {
            count[c - 'a']--;
            if (count[c - 'a'] < 0) {
                return false;
            }
        }
        
        return true;
    }
}
```
