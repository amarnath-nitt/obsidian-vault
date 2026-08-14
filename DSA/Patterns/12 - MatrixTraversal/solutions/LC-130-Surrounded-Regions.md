# Surrounded Regions (LC 130)

**Difficulty**: Medium  
**Pattern**: Matrix Traversal / DFS  
**LeetCode**: https://leetcode.com/problems/surrounded-regions/

## Problem Statement
Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`.
A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example:**
```
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
```

## Approach: Boundary DFS

### Intuition
Any `'O'` connected to the boundary cannot be captured.
1. Iterate over all boundary cells. If `'O'`, perform DFS to mark all connected `'O'`s as "Safe" (e.g., `'S'`).
2. Iterate over the entire board:
   - If `'O'`, it means it was not connected to boundary -> Flip to `'X'` (Captured).
   - If `'S'`, it means it was connected to boundary -> Flip back to `'O'` (Safe).

### Java Code
```java
class Solution {
    public void solve(char[][] board) {
        if (board == null || board.length == 0) return;
        int m = board.length;
        int n = board[0].length;
        
        // 1. Mark boundary 'O's as 'S'
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') dfs(board, i, 0);
            if (board[i][n - 1] == 'O') dfs(board, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') dfs(board, 0, j);
            if (board[m - 1][j] == 'O') dfs(board, m - 1, j);
        }
        
        // 2. Flip 'O' -> 'X', 'S' -> 'O'
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == 'S') {
                    board[i][j] = 'O';
                }
            }
        }
    }
    
    private void dfs(char[][] board, int r, int c) {
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != 'O') {
            return;
        }
        
        board[r][c] = 'S'; // Mark as safe
        
        dfs(board, r + 1, c);
        dfs(board, r - 1, c);
        dfs(board, r, c + 1);
        dfs(board, r, c - 1);
    }
}
```

### Complexity
- **Time**: O(mn)
- **Space**: O(mn)

## Key Takeaways
- "Inside-out" vs "Outside-in" thinking. Easier to find what is NOT captured.
- Temporary state marking ('S') avoids extra space for visited array
