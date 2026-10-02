---
solved: true
difficulty: Medium
pattern: Frequency Counting
lc_number: 49
date_solved: 
tags:
  - dsa
  - frequency-counting
  - medium
---
# Group Anagrams

[Problem Link](https://leetcode.com/problems/group-anagrams/)

## Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Approach
HashMap.
Key: Sorted string or character count string.
Value: List of strings.

## Time and Space Complexity
- **Time Complexity:** O(N * K log K) for sorting, where K is max length of string.
- **Space Complexity:** O(N * K).

## Code
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = new String(ca);
            
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        
        return new ArrayList<>(map.values());
    }
}
```
