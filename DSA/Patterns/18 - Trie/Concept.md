# Trie (Prefix Tree) — Concept

## What Is It?

A Trie is a tree-like data structure where each node represents a character. Paths from root to nodes form prefixes, enabling O(L) search/insert where L is the word length — independent of dictionary size.

---

## When to Use

> **Trigger keywords:** "prefix", "autocomplete", "dictionary", "word search", "starts with", "longest common prefix"

---

## Template

```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

class Trie {
    TrieNode root = new TrieNode();
    
    void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null)
                node.children[c - 'a'] = new TrieNode();
            node = node.children[c - 'a'];
        }
        node.isEnd = true;
    }
    
    boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEnd;
    }
    
    boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }
    
    private TrieNode searchPrefix(String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            if (node.children[c - 'a'] == null) return null;
            node = node.children[c - 'a'];
        }
        return node;
    }
}
```

---

## Visual Walkthrough

```
Insert: "app", "apple", "apt", "bat"

         root
        /    \
       a      b
       |      |
       p      a
      / \     |
     p   t    t
     |
     l
     |
     e

search("app")   → true  (isEnd at second 'p')
search("ap")    → false (isEnd not set)
startsWith("ap") → true
```

---

## Time/Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(L) | O(L) per word |
| Search | O(L) | — |
| StartsWith | O(L) | — |
| Total space | — | O(N × L × 26) worst case |

---

## Common Mistakes

1. **Not setting `isEnd = true`** → "app" won't be found if only "apple" was inserted
2. **Using HashMap children vs array** → Array is faster for lowercase English; HashMap for Unicode
3. **Not pruning in Word Search II** → Remove words after finding them to avoid TLE

---

## Related Patterns

- [[09 - ModifiedBinarySearch/Concept|Modified Binary Search]] — Alternative for sorted dictionary lookups
- [[19 - Backtracking/Concept|Backtracking]] — Word Search II combines Trie + DFS backtracking

---

#trie #prefix-tree #dsa #concept
