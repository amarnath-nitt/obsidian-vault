# Implement Trie

**Difficulty:** Medium  
**Category:** Tries  
**LeetCode Link:** [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)

---

## Problem Statement

A **trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.

Implement the Trie class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string that has the prefix `prefix`.

**Example:**
```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output
[null, null, true, false, true, null, true]
```

**Constraints:**
- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10^4` calls in total will be made to `insert`, `search`, and `startsWith`.

---

## Intuition

A Trie is a tree where each node represents a character. Words share common prefixes, making prefix searches very efficient.

---

## Approach: TrieNode with Children Array

### Algorithm
1. Each TrieNode has an array of 26 children (for 'a'-'z')
2. Each node has a boolean flag `isEndOfWord`
3. **Insert:** Create nodes for each character if they don't exist
4. **Search:** Traverse nodes, check if last node is end of word
5. **StartsWith:** Traverse nodes, return true if path exists

### Java Code
```java
class TrieNode {
    TrieNode[] children;
    boolean isEndOfWord;
    
    public TrieNode() {
        children = new TrieNode[26];
        isEndOfWord = false;
    }
}

class Trie {
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
    
    private TrieNode searchPrefix(String prefix) {
        TrieNode node = root;
        
        for (char c : prefix.toCharArray()) {
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

### Complexity Analysis
- **Time Complexity:** 
  - Insert: O(m) where m = word length
  - Search: O(m)
  - StartsWith: O(m)
- **Space Complexity:** O(n * m * 26) where n = number of words

### Why This Works
- ✅ Efficient prefix searches
- ✅ O(m) time for all operations
- ✅ Shared prefixes save space
- ✅ No hash collisions

---

## Key Takeaways

1. **Pattern:** Tree structure for string storage
2. **Children array:** Fixed size 26 for lowercase letters
3. **isEndOfWord:** Distinguishes complete words from prefixes
4. **Shared prefixes:** Multiple words share common path

---

## Visual Example

After inserting "app", "apple", "application":
```
        root
         |
         a
         |
         p
         |
         p (end: "app")
        / \
       l   l
       |   |
       e   i
       |   |
      (end) c
            |
            a
            |
            t
            |
            i
            |
            o
            |
            n
            |
          (end)
```

---

## Tags
#trie #design #string #medium #blind75
