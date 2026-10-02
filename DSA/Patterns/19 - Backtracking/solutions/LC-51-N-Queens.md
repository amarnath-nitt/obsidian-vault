---
solved: false
difficulty: Hard
pattern: Backtracking
lc_number: 51
date_solved: 
tags:
  - dsa
  - backtracking
  - hard
---
# N-Queens (LC 51)

**Difficulty**: Hard  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/n-queens/

## Problem Statement
The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.
Given an integer `n`, return all distinct solutions to the n-queens puzzle.

**Example:**
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

## Approach: Backtracking with State Arrays

### Intuition
Place queens row by row.
For each row, try all columns.
Constraints:
1. Column must not be occupied.
2. Diagonals (major and minor) must not be occupied.
Use boolean arrays for `cols`, `diag1` (row - col), `diag2` (row + col) to check validity in O(1).
`diag1` index: `row - col + (n - 1)`.
`diag2` index: `row + col`.

### Java Code
```java
class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        
        boolean[] cols = new boolean[n];
        boolean[] d1 = new boolean[2 * n]; // Main diagonal
        boolean[] d2 = new boolean[2 * n]; // Anti-diagonal
        
        backtrack(0, n, board, result, cols, d1, d2);
        return result;
    }
    
    private void backtrack(int r, int n, char[][] board, List<List<String>> result,
                          boolean[] cols, boolean[] d1, boolean[] d2) {
        if (r == n) {
            List<String> solution = new ArrayList<>();
            for (char[] row : board) solution.add(new String(row));
            result.add(solution);
            return;
        }
        
        for (int c = 0; c < n; c++) {
            int id1 = r - c + n;
            int id2 = r + c;
            
            if (!cols[c] && !d1[id1] && !d2[id2]) {
                board[r][c] = 'Q';
                cols[c] = true; d1[id1] = true; d2[id2] = true;
                
                backtrack(r + 1, n, board, result, cols, d1, d2);
                
                board[r][c] = '.';
                cols[c] = false; d1[id1] = false; d2[id2] = false;
            }
        }
    }
}
```

### Complexity
- **Time**: O(N!)
- **Space**: O(N)

## Key Takeaways
- Optimization using boolean arrays for diagonals
- Classic placing/removing pattern
