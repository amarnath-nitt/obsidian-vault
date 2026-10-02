# Surrounded Regions

**LeetCode 130** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/surrounded-regions/)

### Approach

- 'O's connected to the boundary cannot be flipped
- DFS from all boundary 'O's → mark as safe
- Flip remaining 'O' → 'X', restore safe marks → 'O'

```java
class Solution {
    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;
        // Mark boundary-connected O's as safe
        for (int i = 0; i < m; i++) {
            dfs(board, i, 0); dfs(board, i, n-1);
        }
        for (int j = 0; j < n; j++) {
            dfs(board, 0, j); dfs(board, m-1, j);
        }
        // Flip
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == '#') board[i][j] = 'O';
            }
    }

    void dfs(char[][] board, int r, int c) {
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != 'O') return;
        board[r][c] = '#'; // safe marker
        dfs(board, r+1, c); dfs(board, r-1, c);
        dfs(board, r, c+1); dfs(board, r, c-1);
    }
}
```

---
