# Sudoku Solver (LC 37)

**Difficulty**: Hard  
**Pattern**: Backtracking  
**LeetCode**: https://leetcode.com/problems/sudoku-solver/

## Problem Statement
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes.
The '.' character indicates empty cells.

**Example:**
Input: grid with '.'s.
Output: grid with numbers.

## Approach: Backtracking

### Intuition
Try filling numbers 1-9 in empty cells.
Validate placement (Row, Col, Box).
Recurse to next empty cell.
If we reach end with valid placement, return true to stop searching.
`isValid`: Check row, col, and sub-box `3 * (row / 3) + i / 3`, `3 * (col / 3) + i % 3`.

### Java Code
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
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    private boolean isValid(char[][] board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == c) return false;
            if (board[i][col] == c) return false;
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) return false;
        }
        return true;
    }
}
```

### Complexity
- **Time**: O(9^(M*N)), heavily pruned
- **Space**: O(M*N) recursion stack

## Key Takeaways
- Exhaustive search with validity check
- Box index formula: `3 * (r/3) + i/3`
