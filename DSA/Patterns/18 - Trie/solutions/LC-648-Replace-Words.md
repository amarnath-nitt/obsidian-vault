---
solved: false
difficulty: Medium
pattern: Trie
lc_number: 648
date_solved: 
tags:
  - dsa
  - trie
  - medium
---
# Replace Words (LC 648)

**Difficulty**: Medium  
**Pattern**: Trie  
**LeetCode**: https://leetcode.com/problems/replace-words/

## Problem Statement
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

**Example:**
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

## Approach: Trie

### Intuition
Insert all dictionary roots into a Trie. Mark end of words.
For each word in sentence, traverse the Trie.
If we encounter an end-of-word marker, we found the shortest root. Replace and stop.
If we can't traverse or don't find a root, keep original word.

### Java Code
```java
class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
    }
    
    private TrieNode root = new TrieNode();
    
    public String replaceWords(List<String> dictionary, String sentence) {
        for (String word : dictionary) {
            insert(word);
        }
        
        StringBuilder result = new StringBuilder();
        String[] words = sentence.split(" ");
        
        for (String word : words) {
            if (result.length() > 0) result.append(" ");
            result.append(findRoot(word));
        }
        
        return result.toString();
    }
    
    private void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) {
                curr.children[idx] = new TrieNode();
            }
            curr = curr.children[idx];
        }
        curr.isEnd = true;
    }
    
    private String findRoot(String word) {
        TrieNode curr = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            int idx = c - 'a';
            
            // If we hit a root end, return substring
            if (curr.isEnd) {
                return word.substring(0, i); // Wait, if isEnd is true at current node 'curr' (which represents char at i-1).
                                             // Let's adjust logic.
                                             // Usually isEnd is on the node corresponding to last char.
            }
            
            if (curr.children[idx] == null) {
                return word; // No root found
            }
            curr = curr.children[idx];
        }
        
        // Edge case: root is same as word, or root is longer (impossible here)
        // If we finish loop and curr.isEnd is true, return word
        if (curr.isEnd) return word;
        return word;
    }
    // Corrected findRoot logic:
    // Check isEnd *after* moving? Or before?
    // If root="ca", insert c->a(end).
    // Word="cattle". i=0 'c', node C. i=1 'a', node A (end). Ret substring(0, 2) "ca".
}
```
*Correction in code block execution logic not required as I write text, but mental check:
Loop starts. if (curr.children[idx] == null) return word.
curr = curr.children[idx].
if (curr.isEnd) return word.substring(0, i + 1);
I will write clean code.*

### Java Code (Corrected)
```java
class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
    }
    
    private TrieNode root = new TrieNode();
    
    private void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) {
                curr.children[idx] = new TrieNode();
            }
            curr = curr.children[idx];
        }
        curr.isEnd = true;
    }
    
    private String findRoot(String word) {
        TrieNode curr = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            int idx = c - 'a';
            
            if (curr.children[idx] == null) {
                return word;
            }
            curr = curr.children[idx];
            
            if (curr.isEnd) {
                return word.substring(0, i + 1);
            }
        }
        return word;
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        for (String word : dictionary) insert(word);
        
        StringBuilder result = new StringBuilder();
        for (String word : sentence.split("\\s+")) {
            if (result.length() > 0) result.append(" ");
            result.append(findRoot(word));
        }
        return result.toString();
    }
}
```

### Complexity
- **Time**: O(N * L + S), N items in dict, L avg length, S sentence length
- **Space**: O(N * L) for Trie

## Key Takeaways
- Trie ideal for prefix matching
- "Shortest root" implies checking `isEnd` eagerly
