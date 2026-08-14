# Design Add and Search Words Data Structure (LC 211)

**Difficulty**: Medium  
**Pattern**: Trie  
**LeetCode**: https://leetcode.com/problems/design-add-and-search-words-data-structure/

## Problem Statement
Design a data structure that supports adding new words and finding if a string matches any previously added string.
The `search` method supports the `.` character, which can match any letter.

**Example:**
```
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

## Approach: Trie with DFS

### Intuition
Standard Trie for `addWord`.
For `search`:
- If char is a letter, traverse normally.
- If char is `.`, we must try ALL possible children of the current node. This requires recursion/DFS.

### Java Code
```java
class WordDictionary {
    private class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;
        
        TrieNode() {
            children = new TrieNode[26];
            isEndOfWord = false;
        }
    }
    
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
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
        return searchHelper(word, 0, root);
    }
    
    private boolean searchHelper(String word, int index, TrieNode node) {
        if (index == word.length()) {
            return node.isEndOfWord;
        }
        
        char c = word.charAt(index);
        
        if (c == '.') {
            // Try all possible children
            for (int i = 0; i < 26; i++) {
                if (node.children[i] != null) {
                    if (searchHelper(word, index + 1, node.children[i])) {
                        return true;
                    }
                }
            }
            return false;
        } else {
            // Standard Trie traversal
            int childIndex = c - 'a';
            if (node.children[childIndex] == null) {
                return false;
            }
            return searchHelper(word, index + 1, node.children[childIndex]);
        }
    }
}
```

### Complexity
- **Time**: 
  - `addWord`: O(L) where L is word length.
  - `search`: O(M^L) where M is alphabet size (26) and L is word length (worst case with all dots).
- **Space**: O(N × L) nodes.

## Key Takeaways
- Trie is ideal for prefix/string matching
- Recursive DFS handles the `.` wildcard effectively
- backtracking/branching when wildcard is encountered
