---
solved: false
difficulty: Medium
pattern: Matrix Traversal
lc_number: 79
date_solved: 
tags:
  - dsa
  - matrix-traversal
  - medium
---
# Word Search (LC 79)

**Difficulty**: Medium  
**Pattern**: Backtracking / Matrix Traversal  
**LeetCode**: https://leetcode.com/problems/word-search/

## Problem Statement
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

## Approach: DFS / Backtracking

### Intuition
Iterate through every cell. If cell matches first char of word, start DFS.
DFS(index): 
- Base case: index == word.length -> True.
- Mark current cell visited (e.g., replace with '#').
- Check all 4 neighbors recursively for `word[index+1]`.
- Backtrack (restore cell value).

### Java Code
```java
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if (dfs(board, i, j, word, 0)) return true;
                }
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, int r, int c, String word, int index) {
        if (index == word.length()) return true;
        
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(index)) {
            return false;
        }
        
        char temp = board[r][c];
        board[r][c] = '#'; // Mark visited
        
        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        for (int[] dir : dirs) {
            if (dfs(board, r + dir[0], c + dir[1], word, index + 1)) {
                return true; // Found path
            }
        }
        
        board[r][c] = temp; // Backtrack
        return false;
    }
}
```

### Complexity
- **Time**: O(M * N * 3^L) where L is word length
- **Space**: O(L) for recursion stack

## Key Takeaways
- Classic Grid Backtracking
- In-place visited marking helps save space
