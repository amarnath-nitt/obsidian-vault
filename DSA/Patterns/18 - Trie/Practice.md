# Prefix Search (Trie) - Practice Notes

## Pattern Overview
A tree-like data structure for efficient string prefix operations and word searching.

## Key Concepts
- **Trie Node**: Contains children map and end-of-word flag
- **Insert**: O(m) where m is word length
- **Search**: O(m) for exact match
- **Prefix Search**: O(m) for prefix

## Template Code

### Trie Implementation
```java
class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEndOfWord = false;
}

class Trie {
    private TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode node = findNode(word);
        return node != null && node.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        return findNode(prefix) != null;
    }
    
    private TrieNode findNode(String str) {
        TrieNode node = root;
        for (char c : str.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return null;
            }
            node = node.children.get(c);
        }
        return node;
    }
}
```

### Array-based Trie (for lowercase letters)
```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEndOfWord = false;
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
```

## Practice Problems

### Medium
- [ ] [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) (LC 208) → [Solution](solutions/LC-208-Implement-Trie.md)
- [ ] [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) (LC 211) → [Solution](solutions/LC-211-Design-Add-and-Search-Words.md)
- [ ] [Replace Words](https://leetcode.com/problems/replace-words/) (LC 648) → [Solution](solutions/LC-648-Replace-Words.md)
- [ ] [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) (LC 677) → [Solution](solutions/LC-677-Map-Sum-Pairs.md)
- [ ] [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) (LC 421) → [Solution](solutions/LC-421-Maximum-XOR.md)
- [ ] [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) (LC 720) → [Solution](solutions/LC-720-Longest-Word.md)

### Hard
- [ ] [Word Search II](https://leetcode.com/problems/word-search-ii/) (LC 212) → [Solution](solutions/LC-212-Word-Search-II.md)
- [ ] [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) (LC 745) → [Solution](solutions/LC-745-Prefix-Suffix-Search.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gk_BPhWu)
