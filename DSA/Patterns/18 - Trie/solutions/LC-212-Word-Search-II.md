---
solved: false
difficulty: Hard
pattern: Trie
lc_number: 212
date_solved: 
tags:
  - dsa
  - trie
  - hard
---
# Word Search II (LC 212)

**Difficulty**: Hard  
**Pattern**: Trie + Backtracking  
**LeetCode**: https://leetcode.com/problems/word-search-ii/

## Problem Statement
Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example:**
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["oath","eat"]
```

## Approach: Trie + DFS (Backtracking)

### Intuition
Naive approach: For each word, do a DFS on the grid. O(W * M * N * 4^L). Too slow.
Optimized: Build a Trie from all `words`. Then iterate every cell in the grid and do DFS. If the current path matches a prefix in the Trie, keep going. If it matches a word, add to result.

### Java Code
```java
class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        String word = null; // Store full word at leaf for easy access
    }
    
    public List<String> findWords(char[][] board, String[] words) {
        List<String> result = new ArrayList<>();
        
        // Build Trie
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (char c : w.toCharArray()) {
                int idx = c - 'a';
                if (node.children[idx] == null) {
                    node.children[idx] = new TrieNode();
                }
                node = node.children[idx];
            }
            node.word = w;
        }
        
        // DFS from each cell
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (root.children[board[i][j] - 'a'] != null) {
                    dfs(board, i, j, root, result);
                }
            }
        }
        
        return result;
    }
    
    private void dfs(char[][] board, int r, int c, TrieNode node, List<String> result) {
        char letter = board[r][c];
        int idx = letter - 'a';
        TrieNode currNode = node.children[idx];
        
        if (currNode.word != null) {
            result.add(currNode.word);
            currNode.word = null; // Mark as found to avoid duplicates
        }
        
        board[r][c] = '#'; // Mark visited
        
        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        for (int[] dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            
            if (nr >= 0 && nr < board.length && nc >= 0 && nc < board[0].length && 
                board[nr][nc] != '#' && currNode.children[board[nr][nc] - 'a'] != null) {
                dfs(board, nr, nc, currNode, result);
            }
        }
        
        board[r][c] = letter; // Backtrack
        
        // Optimization: Prune leaf nodes
        if (currNode.children == null) {
            // Logic to prune would involve checking if all children are null
            // For simplicity, omitted here but helps speed
        }
    }
}
```

### Complexity
- **Time**: O(M * N * 4^L) where L is max word length. Trie construction O(Total chars in words).
- **Space**: O(Total chars) for Trie.

## Key Takeaways
- Trie allows checking multiple words simultaneously
- Store the word itself in Trie node to avoid reconstructing it
- Remove word from Trie (set to null) after finding to avoid duplicates
- Pruning Trie nodes can further optimize
