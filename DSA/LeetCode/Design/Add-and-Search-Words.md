 # Design Add and Search Words Data Structure

**LeetCode Problem:** [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)  
**Difficulty:** Medium  
**Topic:** Design, String, Trie, Depth-First Search, Backtracking

---

## Problem Statement

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `boolean search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

---

## Examples

### Example 1:
```
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output:
[null,null,null,null,false,true,true,true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

---

## Approach: Trie with DFS for Wildcard Matching

### Key Insights:
1. **Trie Structure**: Store words in a Trie (prefix tree)
2. **Wildcard Handling**: Use DFS/Backtracking when encountering `'.'`
3. **Regular Search**: For regular characters, follow normal Trie path
4. **Dot Character**: Try all 26 possible children recursively

### Algorithm:

**addWord(word)**:
- Standard Trie insertion
- Time: O(m) where m is word length

**search(word)**:
- If regular character: follow that path
- If `'.'`: recursively try all children
- Use DFS with backtracking
- Time: O(m) best case (no dots), O(26^m) worst case (all dots)

---

## Java Implementation

```java
class WordDictionary {
    // TrieNode class
    class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;
        
        TrieNode() {
            children = new TrieNode[26]; // 'a' to 'z'
            isEndOfWord = false;
        }
    }
    
    private TrieNode root;
    
    public WordDictionary() {
        root = new TrieNode();
    }
    
    // Add word to trie - O(m) where m is word length
    public void addWord(String word) {
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
    
    // Search with wildcard support - O(m) to O(26^m)
    public boolean search(String word) {
        return searchHelper(word, 0, root);
    }
    
    // DFS helper for wildcard search
    private boolean searchHelper(String word, int index, TrieNode node) {
        // Base case: reached end of word
        if (index == word.length()) {
            return node.isEndOfWord;
        }
        
        char ch = word.charAt(index);
        
        if (ch == '.') {
            // Wildcard: try all possible children
            for (TrieNode child : node.children) {
                if (child != null && searchHelper(word, index + 1, child)) {
                    return true;
                }
            }
            return false;
        } else {
            // Regular character: follow specific path
            int charIndex = ch - 'a';
            TrieNode child = node.children[charIndex];
            
            if (child == null) {
                return false;
            }
            
            return searchHelper(word, index + 1, child);
        }
    }
}
```

---

## Alternative Implementation with Cleaner Structure

```java
class WordDictionary {
    class TrieNode {
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
            int i = c - 'a';
            if (node.children[i] == null) {
                node.children[i] = new TrieNode();
            }
            node = node.children[i];
        }
        node.isWord = true;
    }
    
    public boolean search(String word) {
        return dfs(word, 0, root);
    }
    
    private boolean dfs(String word, int pos, TrieNode node) {
        if (pos == word.length()) {
            return node.isWord;
        }
        
        char c = word.charAt(pos);
        
        if (c == '.') {
            // Try all 26 children
            for (int i = 0; i < 26; i++) {
                if (node.children[i] != null && dfs(word, pos + 1, node.children[i])) {
                    return true;
                }
            }
            return false;
        } else {
            // Specific character
            int i = c - 'a';
            return node.children[i] != null && dfs(word, pos + 1, node.children[i]);
        }
    }
}
```

---

## Complexity Analysis

### Time Complexity:
- **addWord(word)**: O(m)
  - m = length of word
  - Same as standard Trie insertion
  
- **search(word)**:
  - **Best Case**: O(m) when no wildcards
  - **Average Case**: O(m × k) where k is average branching factor
  - **Worst Case**: O(26^d × m) where d is number of dots
    - Example: "..." with 3 dots → explores 26³ = 17,576 paths

### Space Complexity:
- **O(N × M)** 
  - N = number of words
  - M = average length of words
  - Standard Trie space complexity

---

## Optimization: Length-Based Buckets

**For faster search, group words by length:**

```java
class WordDictionaryOptimized {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isWord = false;
    }
    
    // Separate tries for each word length
    private HashMap<Integer, TrieNode> triesByLength;
    
    public WordDictionaryOptimized() {
        triesByLength = new HashMap<>();
    }
    
    public void addWord(String word) {
        int len = word.length();
        triesByLength.putIfAbsent(len, new TrieNode());
        
        TrieNode node = triesByLength.get(len);
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (node.children[i] == null) {
                node.children[i] = new TrieNode();
            }
            node = node.children[i];
        }
        node.isWord = true;
    }
    
    public boolean search(String word) {
        int len = word.length();
        if (!triesByLength.containsKey(len)) {
            return false;
        }
        return dfs(word, 0, triesByLength.get(len));
    }
    
    private boolean dfs(String word, int pos, TrieNode node) {
        if (pos == word.length()) {
            return node.isWord;
        }
        
        char c = word.charAt(pos);
        
        if (c == '.') {
            for (int i = 0; i < 26; i++) {
                if (node.children[i] != null && dfs(word, pos + 1, node.children[i])) {
                    return true;
                }
            }
            return false;
        } else {
            int i = c - 'a';
            return node.children[i] != null && dfs(word, pos + 1, node.children[i]);
        }
    }
}
```

**Benefits:**
- Prunes search space by length
- If searching for "abc" (length 3), only searches in length-3 trie
- Reduces false path exploration

---

## Key Points for Interviews

1. **Why Trie?**
   - Efficient prefix-based operations
   - Natural fit for word storage
   - Enables wildcard matching with DFS

2. **Wildcard Strategy:**
   - Regular character → follow single path
   - Dot → explore all 26 children recursively
   - Use DFS/backtracking to try all possibilities

3. **Optimization Techniques:**
   - Group by length (reduces search space)
   - Early termination in DFS
   - Memoization (if patterns repeat)

4. **Edge Cases:**
   - Empty string
   - All dots: "..."
   - No dots (regular search)
   - Word not in dictionary
   - Single character word

5. **Common Mistakes:**
   - Not checking `isEndOfWord` in base case
   - Forgetting to check if child is null before recursing
   - Using iteration instead of recursion for dots
   - Not handling empty input

6. **Follow-up Questions:**
   - Support for other wildcards (*, +, ?)?
   - Support for regex patterns?
   - How to optimize for many dots?
   - Can you make it case-insensitive?

---

## Visual Example

```
After adding: "bad", "dad", "mad"

Trie Structure:
        root
       /  |  \
      b   d   m
      |   |   |
      a   a   a
      |   |   |
      d*  d*  d*  (* = isEndOfWord)

Search ".ad":
- Start at root
- '.' → try all children (b, d, m)
  - Try 'b': 'a' → 'd' → isEndOfWord? YES ✓
  - Return true
  
Search "b..":
- 'b' → specific path to b-node
- '.' → try all children from b (only 'a')
  - 'a' → '.' → try all from a (only 'd')
    - 'd' → isEndOfWord? YES ✓
```

---

## Test Cases

```java
public class WordDictionaryTest {
    public static void main(String[] args) {
        WordDictionary wd = new WordDictionary();
        
        // Test 1: Basic operations
        wd.addWord("bad");
        wd.addWord("dad");
        wd.addWord("mad");
        
        System.out.println(wd.search("pad"));  // false
        System.out.println(wd.search("bad"));  // true
        System.out.println(wd.search(".ad"));  // true
        System.out.println(wd.search("b.."));  // true
        
        // Test 2: Edge cases
        System.out.println(wd.search("..."));  // true
        System.out.println(wd.search(".."));   // false
        
        // Test 3: No wildcards
        wd.addWord("a");
        System.out.println(wd.search("a"));    // true
        System.out.println(wd.search("."));    // true
        
        // Test 4: Multiple dots
        wd.addWord("abc");
        System.out.println(wd.search("a.c"));  // true
        System.out.println(wd.search("a.."));  // true
    }
}
```

---

## Related Problems

- [[Implement-Trie|208. Implement Trie (Prefix Tree)]]
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/)
- [79. Word Search](https://leetcode.com/problems/word-search/)
- [676. Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)

---

## Tags

`#design` `#trie` `#dfs` `#backtracking` `#wildcard` `#medium` `#recursion`
