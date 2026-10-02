---
solved: false
difficulty: Medium
pattern: Trie
lc_number: 677
date_solved: 
tags:
  - dsa
  - trie
  - medium
---
# Map Sum Pairs (LC 677)

**Difficulty**: Medium  
**Pattern**: Trie  
**LeetCode**: https://leetcode.com/problems/map-sum-pairs/

## Problem Statement
Design a map that allows you to:
- Map a string key to a given value.
- Return the sum of the values that have a key with a prefix equal to a given string.

**Example:**
```
Input: insert("apple", 3), sum("ap") -> 3, insert("app", 2), sum("ap") -> 5
```

## Approach: Trie with Prefix Sums

### Intuition
Store values in a Trie.
To query sum of prefix, traverse to the node representing prefix. Then sum all values in subtree.
Optimization: Store `sum` at *every* node during insertion?
Or store value at end node and DFS sum query?
Optimization 2: Each node stores sum of all words passing through it.
When updating "apple" from 3 to 5, update path nodes by +2.

### Java Code
```java
class MapSum {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        int val = 0; // Value of this word end
        int sum = 0; // Sum of subtree
    }
    
    private TrieNode root;
    private Map<String, Integer> map;

    public MapSum() {
        root = new TrieNode();
        map = new HashMap<>(); // Keep track of existing values to calculate delta
    }
    
    public void insert(String key, int val) {
        int delta = val - map.getOrDefault(key, 0);
        map.put(key, val);
        
        TrieNode curr = root;
        for (char c : key.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) {
                curr.children[idx] = new TrieNode();
            }
            curr = curr.children[idx];
            curr.sum += delta;
        }
    }
    
    public int sum(String prefix) {
        TrieNode curr = root;
        for (char c : prefix.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) {
                return 0;
            }
            curr = curr.children[idx];
        }
        return curr.sum;
    }
}
```

### Complexity
- **Time**: O(L) for insert and sum
- **Space**: O(N * L)

## Key Takeaways
- Aggregating values at Trie nodes speeds up prefix queries to O(L) instead of O(Subtree size)
- HashMap required to handle updates (calculate delta)
