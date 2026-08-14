# Add and Search Word - Data Structure Design

**Difficulty:** Medium  
**Category:** Tries  
**LeetCode Link:** [Add and Search Word](https://leetcode.com/problems/add-and-search-word-data-structure-design/)

---

## Approach: Trie with Wildcard Search

### Java Code
```java
class WordDictionary {
    private class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isWord = false;
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
        node.isWord = true;
    }
    
    public boolean search(String word) {
        return searchHelper(word, 0, root);
    }
    
    private boolean searchHelper(String word, int index, TrieNode node) {
        if (index == word.length()) {
            return node.isWord;
        }
        
        char c = word.charAt(index);
        if (c == '.') {
            for (TrieNode child : node.children) {
                if (child != null && searchHelper(word, index + 1, child)) {
                    return true;
                }
            }
            return false;
        } else {
            int idx = c - 'a';
            if (node.children[idx] == null) return false;
            return searchHelper(word, index + 1, node.children[idx]);
        }
    }
}
```

### Complexity
- **addWord:** O(m)
- **search:** O(26^m) worst case with wildcards
- **Space:** O(n × m)

---

## Tags
#trie #design #backtracking #medium #blind75
