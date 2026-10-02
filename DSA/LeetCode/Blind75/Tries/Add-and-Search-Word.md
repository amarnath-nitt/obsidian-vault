# Add and Search Word

**Difficulty:** Medium
**Category:** Tries
**LeetCode Link:** [Add and Search Word](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

---

## Problem Statement

Design a data structure that supports adding new words and searching for a string that may contain `.` as a wildcard matching any letter.

**Example:**
```
addWord("bad"), addWord("dad"), addWord("mad")
search("pad") → false
search(".ad") → true
search("b..") → true
```

---

## Intuition

Use a Trie for storage. For `search`, when we encounter a `.`, we must try all 26 possible children recursively. For regular characters, follow the normal Trie path.

---

## Approach: Trie with Recursive Wildcard Search

### Algorithm
- **addWord:** Standard Trie insert
- **search:** DFS through Trie; on `.` try all non-null children; on regular char follow that child

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
            int idx = c - 'a';
            if (node.children[idx] == null) node.children[idx] = new TrieNode();
            node = node.children[idx];
        }
        node.isWord = true;
    }

    public boolean search(String word) {
        return searchHelper(word, 0, root);
    }

    private boolean searchHelper(String word, int index, TrieNode node) {
        if (index == word.length()) return node.isWord;

        char c = word.charAt(index);

        if (c == '.') {
            // Try all possible children
            for (TrieNode child : node.children) {
                if (child != null && searchHelper(word, index + 1, child)) return true;
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

### Complexity Analysis
- **addWord:** O(m) — m = word length
- **search:** O(26^m) worst case with all wildcards; O(m) for no wildcards
- **Space:** O(n × m × 26)

---

## Key Takeaways

1. **Trie for storage:** Efficient prefix-based structure
2. **Wildcard = branch all:** `.` forces trying all 26 children recursively
3. **Recursive DFS:** Natural fit for wildcard matching in a tree

---

## Tags
#trie #design #backtracking #medium #blind75
