---
solved: false
difficulty: Medium
pattern: Trie
lc_number: 208
date_solved: 
tags:
  - dsa
  - trie
  - medium
---
# Implement Trie (LC 208)

**Difficulty**: Medium  
**Pattern**: Trie (Prefix Tree)  
**LeetCode**: https://leetcode.com/problems/implement-trie-prefix-tree/

## Problem Statement
Implement the Trie class with `insert`, `search`, and `startsWith` methods.

**Example:**
```
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // true
trie.search("app");     // false
trie.startsWith("app"); // true
```

## Approach 1: HashMap-based

### Java Code
```java
class Trie {
    private Set<String> words;
    private Set<String> prefixes;
    
    public Trie() {
        words = new HashSet<>();
        prefixes = new HashSet<>();
    }
    
    public void insert(String word) {
        words.add(word);
        for (int i = 1; i <= word.length(); i++) {
            prefixes.add(word.substring(0, i));
        }
    }
    
    public boolean search(String word) {
        return words.contains(word);
    }
    
    public boolean startsWith(String prefix) {
        return prefixes.contains(prefix);
    }
}
```

### Complexity
- **Time**: insert O(n²), search/startsWith O(1)
- **Space**: O(n²) for all prefixes

## Approach 2: Trie Node Structure (Optimized)

### Java Code
```java
class Trie {
    class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;
        
        TrieNode() {
            children = new TrieNode[26];
            isEndOfWord = false;
        }
    }
    
    private TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
        }
        node.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }
    
    private TrieNode searchPrefix(String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                return null;
            }
            node = node.children[index];
        }
        return node;
    }
}
```

### Complexity
- **Time**: O(n) for all operations
- **Space**: O(ALPHABET_SIZE × N × M) worst case

## Key Takeaways
- Trie enables O(n) prefix operations
- Each node has 26 children (for lowercase English)
- `isEndOfWord` flag marks complete words
- Efficient for autocomplete, spell check, IP routing
