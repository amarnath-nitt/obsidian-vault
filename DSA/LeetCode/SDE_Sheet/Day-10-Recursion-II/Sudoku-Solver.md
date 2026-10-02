# Sudoku Solver

**LeetCode 37** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/sudoku-solver/)

### Problem
Solve a Sudoku puzzle by filling in empty cells.

### Approach

- For each empty cell (`.`), try digits 1-9
- Check if digit is valid in row, column, and 3×3 box
- Recurse; backtrack if no digit works

**Box index:** `(row/3)*3 + col/3`

### Java Solution

```java
class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }

    private boolean solve(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) {
                        if (isValid(board, i, j, c)) {
                            board[i][j] = c;
                            if (solve(board)) return true;
                            board[i][j] = '.'; // backtrack
                        }
                    }
                    return false; // no digit works
                }
            }
        }
        return true; // all filled
    }

    private boolean isValid(char[][] board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == c) return false;
            if (board[i][col] == c) return false;
            if (board[3*(row/3) + i/3][3*(col/3) + i%3] == c) return false;
        }
        return true;
    }
}
```

**Complexity:** Time O(9^81 worst) but practically very fast due to pruning

---
