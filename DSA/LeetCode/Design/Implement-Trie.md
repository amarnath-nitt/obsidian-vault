# Implement Trie (Prefix Tree)

**LeetCode Problem:** [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)  
**Difficulty:** Medium  
**Topic:** Design, Trie, String, Hash Table

---

## Problem Statement

A **trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string word into the trie.
- `boolean search(String word)` Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- `boolean startsWith(String prefix)` Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

---

## Examples

### Example 1:
```
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
[null, null, true, false, true, null, true]

Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

---

## Approach

### Key Insights:
1. **TrieNode Structure**: Each node contains:
   - Array of 26 children (for 'a' to 'z')
   - Boolean flag `isEndOfWord` to mark complete words
   
2. **Tree Structure**: Root is empty, each path from root to leaf represents a word

3. **Operations**:
   - **Insert**: Follow/create path for each character, mark end
   - **Search**: Follow path, check `isEndOfWord` at end
   - **StartsWith**: Follow path, no need to check `isEndOfWord`

---

## Java Implementation - Approach 1 (Array-based)

```java
class Trie {
    // TrieNode class
    class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;
        
        TrieNode() {
            children = new TrieNode[26]; // for 'a' to 'z'
            isEndOfWord = false;
        }
    }
    
    private TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    // Insert a word into the trie - O(m) where m is word length
    public void insert(String word) {
        TrieNode current = root;
        
        for (char ch : word.toCharArray()) {
            int index = ch - 'a';
            
            // Create new node if path doesn't exist
            if (current.children[index] == null) {
                current.children[index] = new TrieNode();
            }
            
            current = current.children[index];
        }
        
        // Mark the end of word
        current.isEndOfWord = true;
    }
    
    // Search if word exists in trie - O(m)
    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEndOfWord;
    }
    
    // Check if any word starts with given prefix - O(m)
    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }
    
    // Helper method to search for a prefix
    private TrieNode searchPrefix(String prefix) {
        TrieNode current = root;
        
        for (char ch : prefix.toCharArray()) {
            int index = ch - 'a';
            
            if (current.children[index] == null) {
                return null; // Prefix not found
            }
            
            current = current.children[index];
        }
        
        return current;
    }
}
```

---

## Java Implementation - Approach 2 (HashMap-based)

**More flexible, supports any characters (not just lowercase a-z)**

```java
class Trie {
    class TrieNode {
        HashMap<Character, TrieNode> children;
        boolean isEndOfWord;
        
        TrieNode() {
            children = new HashMap<>();
            isEndOfWord = false;
        }
    }
    
    private TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode current = root;
        
        for (char ch : word.toCharArray()) {
            current.children.putIfAbsent(ch, new TrieNode());
            current = current.children.get(ch);
        }
        
        current.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }
    
    private TrieNode searchPrefix(String prefix) {
        TrieNode current = root;
        
        for (char ch : prefix.toCharArray()) {
            if (!current.children.containsKey(ch)) {
                return null;
            }
            current = current.children.get(ch);
        }
        
        return current;
    }
}
```

---

## Complexity Analysis

### Time Complexity:
- **insert(word)**: O(m), where m is the length of the word
- **search(word)**: O(m)
- **startsWith(prefix)**: O(m)

### Space Complexity:
- **Array-based**: O(ALPHABET_SIZE × N × M)
  - N = number of words
  - M = average length of words
  - ALPHABET_SIZE = 26 (for lowercase letters)
  - Wastes space if not all characters are used
  
- **HashMap-based**: O(N × M)
  - More space-efficient for sparse tries
  - Overhead of HashMap objects

---

## Visual Example

```
After inserting "apple", "app", "application":

        root
         |
         a
         |
         p
         |
         p [END] ← "app"
         |
         l
         |
    e [END]    i
    ↑          |
  "apple"      c
               |
               a
               |
               t
               |
               i
               |
               o
               |
               n [END] ← "application"
```

---

## Extended Implementation with Delete

```java
class TrieWithDelete {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEndOfWord = false;
    }
    
    private TrieNode root = new TrieNode();
    
    public void insert(String word) {
        TrieNode current = root;
        for (char ch : word.toCharArray()) {
            int index = ch - 'a';
            if (current.children[index] == null) {
                current.children[index] = new TrieNode();
            }
            current = current.children[index];
        }
        current.isEndOfWord = true;
    }
    
    public boolean delete(String word) {
        return deleteHelper(root, word, 0);
    }
    
    private boolean deleteHelper(TrieNode current, String word, int index) {
        if (index == word.length()) {
            // Word doesn't exist
            if (!current.isEndOfWord) {
                return false;
            }
            current.isEndOfWord = false;
            // Return true if node has no children (can be deleted)
            return isEmpty(current);
        }
        
        int charIndex = word.charAt(index) - 'a';
        TrieNode child = current.children[charIndex];
        
        if (child == null) {
            return false; // Word doesn't exist
        }
        
        boolean shouldDeleteChild = deleteHelper(child, word, index + 1);
        
        if (shouldDeleteChild) {
            current.children[charIndex] = null;
            // Return true if current node can be deleted
            return !current.isEndOfWord && isEmpty(current);
        }
        
        return false;
    }
    
    private boolean isEmpty(TrieNode node) {
        for (TrieNode child : node.children) {
            if (child != null) return false;
        }
        return true;
    }
}
```

---

## Key Points for Interviews

1. **Why Trie?**
   - Fast prefix-based searches (autocomplete, spell check)
   - Space-efficient for large datasets with common prefixes
   - O(m) search vs O(n×m) for array of strings

2. **Array vs HashMap:**
   - **Array**: Faster, fixed alphabet size, wastes space
   - **HashMap**: Flexible, space-efficient, HashMap overhead

3. **Applications:**
   - Autocomplete systems
   - Spell checkers
   - IP routing (longest prefix matching)
   - Dictionary implementations
   - Word games (Boggle, Scrabble)

4. **Common Variations:**
   - Case-insensitive search
   - Support for special characters
   - Count word frequencies
   - Find all words with prefix
   - Wildcard search (Add and Search Words Data Structure)

5. **Common Mistakes:**
   - Forgetting to mark `isEndOfWord`
   - Not handling empty strings
   - Memory leak in delete operation
   - Wrong index calculation (ch - 'a')

6. **Optimization:**
   - Compressed Trie (Patricia Trie) - merge single-child nodes
   - Ternary Search Tree - more space-efficient

---

## Advanced: Trie with Word Count

```java
class TrieWithCount {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        int wordCount = 0; // Number of times this word was inserted
        int prefixCount = 0; // Number of words with this prefix
    }
    
    private TrieNode root = new TrieNode();
    
    public void insert(String word) {
        TrieNode current = root;
        for (char ch : word.toCharArray()) {
            int index = ch - 'a';
            if (current.children[index] == null) {
                current.children[index] = new TrieNode();
            }
            current = current.children[index];
            current.prefixCount++;
        }
        current.wordCount++;
    }
    
    public int countWordsEqualTo(String word) {
        TrieNode node = searchPrefix(word);
        return node == null ? 0 : node.wordCount;
    }
    
    public int countWordsStartingWith(String prefix) {
        TrieNode node = searchPrefix(prefix);
        return node == null ? 0 : node.prefixCount;
    }
    
    private TrieNode searchPrefix(String prefix) {
        TrieNode current = root;
        for (char ch : prefix.toCharArray()) {
            int index = ch - 'a';
            if (current.children[index] == null) return null;
            current = current.children[index];
        }
        return current;
    }
}
```

---

## Related Problems

- [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/)
- [1804. Implement Trie II (Prefix Tree)](https://leetcode.com/problems/implement-trie-ii-prefix-tree/)
- [648. Replace Words](https://leetcode.com/problems/replace-words/)

---

## Tags

`#design` `#trie` `#prefix-tree` `#string` `#medium` `#data-structure`
