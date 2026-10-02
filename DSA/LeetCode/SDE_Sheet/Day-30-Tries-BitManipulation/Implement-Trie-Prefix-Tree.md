# Implement Trie (Prefix Tree)

**LeetCode 208** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/implement-trie-prefix-tree/)

### Approach
- A Trie is an efficient information-retrieval data structure.
- Each node contains an array of children nodes (usually of size 26 for English letters) and a boolean flag `isEnd` indicating if the node marks the end of a word.

### Java Solution

```java
class Trie {
    private class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
    }

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
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

    public boolean search(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) return false;
            curr = curr.children[idx];
        }
        return curr.isEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for (char c : prefix.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) return false;
            curr = curr.children[idx];
        }
        return true;
    }
}
```

**Complexity:**
- **Insert:** Time $O(L)$ · Space $O(L \times N)$ (where $L$ is word length, $N$ is number of inserted words)
- **Search / StartsWith:** Time $O(L)$ · Space $O(1)$

---
