---
solved: false
difficulty: Hard
pattern: Trie
lc_number: 745
date_solved: 
tags:
  - dsa
  - trie
  - hard
---
# Prefix and Suffix Search

[Problem Link](https://leetcode.com/problems/prefix-and-suffix-search/)

## Problem Statement
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.
Implement the `WordFilter` class:
- `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary.
- `f(string pref, string suff)` Returns the index of the word in the dictionary, which has the prefix `pref` and the suffix `suff`. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return `-1`.

## Approach
Trie with special keys.
For each word "apple", insert "apple{apple", "e{apple", "le{apple", "ple{apple", "pple{apple", "apple{apple".
Search for "suff{pref".
Or use two Tries.
Or simple HashMap with all combinations `pref|suff`.
Given constraints, `suffix + '{' + word` insertion into Trie is efficient.
Search query becomes `suff + '{' + pref`.

## Time and Space Complexity
- **Time Complexity:** O(N * L^2) init, O(L) query.
- **Space Complexity:** O(N * L^2).

## Code
```java
class WordFilter {
    class TrieNode {
        TrieNode[] children = new TrieNode[27]; // 'a'-'z' + '{'
        int weight = -1;
    }
    
    TrieNode root;

    public WordFilter(String[] words) {
        root = new TrieNode();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            String key = "{" + word;
            insert(key, i);
            for (int j = 0; j < word.length(); j++) {
                key = word.charAt(word.length() - 1 - j) + key;
                insert(key, i);
            }
        }
    }
    
    private void insert(String word, int weight) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (c == '{') idx = 26;
            
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
            node.weight = weight;
        }
    }
    
    public int f(String pref, String suff) {
        TrieNode node = root;
        String key = suff + "{" + pref;
        
        for (char c : key.toCharArray()) {
            int idx = c - 'a';
            if (c == '{') idx = 26;
            
            if (node.children[idx] == null) return -1;
            node = node.children[idx];
        }
        return node.weight;
    }
}
```
