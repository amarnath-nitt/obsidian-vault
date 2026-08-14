# Word Search II

[Problem Link](https://leetcode.com/problems/word-search-ii/)

## Problem Statement
Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Approach
Backtracking + Trie.
1.  Build a Trie from the `words`.
2.  Iterate through each cell of the board.
3.  DFS from each cell, traversing the Trie.
    - If current char matches a child in Trie, move to that child and neighbor cell.
    - If Trie `isEnd` is true, we found a word. Add to result, and mark `isEnd` false (deduplicate).
    - Optimizations: Remove leaf node from Trie once exhausted effectively pruning the Trie.

## Time and Space Complexity
- **Time Complexity:** O(M * N * 3^L), where L is max word length.
- **Space Complexity:** O(Total characters in words) for Trie.

## Code
```java
class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        String word = null;
    }
    
    public List<String> findWords(char[][] board, String[] words) {
        List<String> result = new ArrayList<>();
        TrieNode root = new TrieNode();
        
        // Build Trie
        for (String w : words) {
            TrieNode node = root;
            for (char c : w.toCharArray()) {
                if (node.children[c - 'a'] == null) {
                    node.children[c - 'a'] = new TrieNode();
                }
                node = node.children[c - 'a'];
            }
            node.word = w;
        }
        
        int m = board.length;
        int n = board[0].length;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (root.children[board[i][j] - 'a'] != null) {
                    dfs(board, i, j, root, result);
                }
            }
        }
        return result;
    }
    
    private void dfs(char[][] board, int i, int j, TrieNode node, List<String> result) {
        char c = board[i][j];
        if (c == '#' || node.children[c - 'a'] == null) return;
        
        node = node.children[c - 'a'];
        if (node.word != null) {
            result.add(node.word);
            node.word = null; // Dedup
        }
        
        board[i][j] = '#'; // Mark visited
        
        if (i > 0) dfs(board, i - 1, j, node, result);
        if (j > 0) dfs(board, i, j - 1, node, result);
        if (i < board.length - 1) dfs(board, i + 1, j, node, result);
        if (j < board[0].length - 1) dfs(board, i, j + 1, node, result);
        
        board[i][j] = c; // Backtrack
    }
}
```
