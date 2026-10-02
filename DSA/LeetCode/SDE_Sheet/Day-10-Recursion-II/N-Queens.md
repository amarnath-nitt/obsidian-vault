# N-Queens

**LeetCode 51** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/n-queens/)

### Problem
Place N queens on an N×N board such that no two queens attack each other.

### Approach

- Place queens row by row
- For each row, try each column
- Check if column, left diagonal, right diagonal are safe
- Use boolean arrays for O(1) safety checks

### Java Solution

```java
class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        boolean[] cols = new boolean[n];
        boolean[] diag1 = new boolean[2 * n]; // row - col + n (left diag)
        boolean[] diag2 = new boolean[2 * n]; // row + col (right diag)
        int[] queens = new int[n]; // queens[row] = col
        Arrays.fill(queens, -1);
        backtrack(0, n, queens, cols, diag1, diag2, result);
        return result;
    }

    private void backtrack(int row, int n, int[] queens,
                           boolean[] cols, boolean[] diag1, boolean[] diag2,
                           List<List<String>> result) {
        if (row == n) {
            result.add(buildBoard(queens, n));
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols[col] || diag1[row - col + n] || diag2[row + col]) continue;
            queens[row] = col;
            cols[col] = diag1[row - col + n] = diag2[row + col] = true;
            backtrack(row + 1, n, queens, cols, diag1, diag2, result);
            cols[col] = diag1[row - col + n] = diag2[row + col] = false;
        }
    }

    private List<String> buildBoard(int[] queens, int n) {
        List<String> board = new ArrayList<>();
        for (int q : queens) {
            char[] row = new char[n];
            Arrays.fill(row, '.');
            row[q] = 'Q';
            board.add(new String(row));
        }
        return board;
    }
}
```

**Complexity:** Time O(n!) · Space O(n²)

---
