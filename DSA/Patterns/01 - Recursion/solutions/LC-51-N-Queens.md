---
solved: true
difficulty: Hard
pattern: Recursion
lc_number: 51
date_solved: 
tags:
  - dsa
  - recursion
  - hard
---
# N-Queens (LC 51)

**Difficulty**: Hard  
**Pattern**: Recursion / Backtracking  
**LeetCode**: https://leetcode.com/problems/n-queens/

## Problem Statement
Place `n` queens on an `n x n` chessboard so that no two queens attack each other.

## Recursive Idea
Place one queen per row. For each row, try every valid column, recurse to the next row, then undo the placement.

## Interview Approach & Key Intuition

This section breaks down how to think about the problem in an interview setting, making it easier to recall and explain.

**1. The Core Idea: Backtracking by Row**
The simplest way to structure the search is to place one queen in each row, starting from row 0. This guarantees that no two queens will ever be in the same row. Our only job is to find a valid column for each queen.

-   **Function Signature:** Your backtracking function will likely be `backtrack(int row, ...)`. The `row` parameter tells you which queen you are currently trying to place.
-   **Base Case:** If `row == n`, it means you have successfully placed a queen in every row from `0` to `n-1`. You've found a valid solution, so add it to your results and return.

**2. The Main Challenge: O(1) Attack Checks**
A naive approach would be to place a queen and then scan the whole board to see if it's attacked. This is too slow. The key insight is to track attacked positions in O(1) time.

-   **Columns:** A `Set<Integer>` or a `boolean[]` array can track which columns are occupied. This is straightforward.
-   **Diagonals (The "Trick"):**
    -   For any **main diagonal** (top-left to bottom-right), the value of `row - col` is constant.
    -   For any **anti-diagonal** (top-right to bottom-left), the value of `row + col` is constant.

    By storing these constant values in two separate sets (`diagonal1` and `diagonal2`), you can instantly check if a diagonal is occupied.

**3. The Backtracking "Choose, Explore, Unchoose" Pattern**

Inside your `backtrack(row, ...)` function, you'll loop through every possible column for the current `row`:

```
for (int col = 0; col < n; col++) {
    // 1. CHECK if the spot (row, col) is safe
    if (is_attacked(col, row-col, row+col)) continue;

    // 2. CHOOSE: Place the queen and update tracking sets
    place_queen_and_update_sets(row, col);

    // 3. EXPLORE: Recurse to the next row
    backtrack(row + 1, ...);

    // 4. UNCHOOSE (Backtrack): Remove the queen and revert sets
    remove_queen_and_revert_sets(row, col);
}
```

**How to Memorize & Revise:**
-   **Focus on the `HashSet` solution first.** It's the most readable and directly maps to the diagonal trick: `columns.contains(col)`, `diagonal1.contains(row - col)`, `diagonal2.contains(row + col)`.
-   **Verbalize the logic:** "I'll use backtracking, placing one queen per row. To check for attacks in constant time, I'll use three sets: one for columns, one for main diagonals where `r-c` is constant, and one for anti-diagonals where `r+c` is constant."
-   **Mention Optimizations:** If asked, you can then discuss replacing `HashSet` with `boolean[]` arrays (remembering to offset the `r-c` index) or bitmasks for ultimate performance.

## Java Code
```java
class Solution {
    public List<List<String>> solveNQueens(int n) {
        // 1. Initialization
        List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(board[i], '.');
        }

        // Sets to track occupied columns and diagonals
        Set<Integer> columns = new HashSet<>();
        Set<Integer> diagonal1 = new HashSet<>(); // For (row - col)
        Set<Integer> diagonal2 = new HashSet<>(); // For (row + col)

        // Start the backtracking process from the first row
        backtrack(0, n, board, columns, diagonal1, diagonal2, result);
        return result;
    }

    private void backtrack(
            int row, int n, char[][] board,
            Set<Integer> columns, Set<Integer> diagonal1, Set<Integer> diagonal2,
            List<List<String>> result) {

        // 2. Base Case: If all queens are placed successfully
        if (row == n) {
            // Convert the board to a list of strings and add to the result
            List<String> solution = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                solution.add(new String(board[i]));
            }
            result.add(solution);
            return;
        }

        // 3. Recursive Step: Try placing a queen in each column of the current row
        for (int col = 0; col < n; col++) {
            int d1 = row - col; // Identifier for the main diagonal
            int d2 = row + col; // Identifier for the anti-diagonal

            // 4. Constraint Check: Ensure the current position is not under attack
            if (columns.contains(col) || diagonal1.contains(d1) || diagonal2.contains(d2)) {
                // This position is unsafe, skip to the next column
                continue;
            }

            // 5. Choose: Place the queen and update tracking sets
            board[row][col] = 'Q';
            columns.add(col);
            diagonal1.add(d1);
            diagonal2.add(d2);

            // 6. Explore: Recurse to the next row
            backtrack(row + 1, n, board, columns, diagonal1, diagonal2, result);

            // 7. Unchoose (Backtrack): Remove the queen and revert tracking sets
            // This is crucial for exploring other possibilities.
            board[row][col] = '.';
            columns.remove(col);
            diagonal1.remove(d1);
            diagonal2.remove(d2);
        }
    }
}
```

## Alternative Solution: Using Boolean Arrays

This approach uses boolean arrays for slightly better performance by avoiding hashing and object creation overhead. It's a common optimization.

```java
class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }

        // col, diag (r-c), anti-diag (r+c)
        backtrack(0, board, new boolean[n], new boolean[2 * n - 1], new boolean[2 * n - 1], result);
        return result;
    }

    private void backtrack(int row, char[][] board, boolean[] cols,
                           boolean[] mainDiagonals, boolean[] antiDiagonals, List<List<String>> result) {
        int n = board.length;
        if (row == n) {
            result.add(build(board));
            return;
        }

        for (int col = 0; col < n; col++) {
            // main diagonal: row - col is constant. Shift by n-1 to make it non-negative.
            int d = row - col + (n - 1);
            // anti-diagonal: row + col is constant.
            int a = row + col;
            if (cols[col] || mainDiagonals[d] || antiDiagonals[a]) {
                continue;
            }

            board[row][col] = 'Q';
            cols[col] = mainDiagonals[d] = antiDiagonals[a] = true;
            backtrack(row + 1, board, cols, mainDiagonals, antiDiagonals, result);
            cols[col] = mainDiagonals[d] = antiDiagonals[a] = false;
            board[row][col] = '.';
        }
    }

    private List<String> build(char[][] board) {
        List<String> answer = new ArrayList<>();
        for (char[] row : board) {
            answer.add(new String(row));
        }
        return answer;
    }
}
```


### Complexity Analysis
-   **Time Complexity**: `O(N!)`. The performance is slightly better in practice than the `HashSet` version due to direct array access, but the asymptotic complexity remains the same.
-   **Space Complexity**: `O(N^2)`. The space is dominated by the `board`. The boolean arrays for tracking attacks take `O(N)` space.

---

## Alternative Optimal Solution: Bitmask Backtracking
Use bitmasks for occupied columns and diagonals. This keeps validity checks compact and fast.

```java
class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        int[] queens = new int[n];
        Arrays.fill(queens, -1);
        backtrack(0, n, 0, 0, 0, queens, result);
        return result;
    }

    private void backtrack(int row, int n, int cols, int diag, int antiDiag,
                           int[] queens, List<List<String>> result) {
        if (row == n) {
            result.add(build(queens, n));
            return;
        }

        int available = ((1 << n) - 1) & ~(cols | diag | antiDiag);
        while (available != 0) {
            int bit = available & -available;
            available -= bit;

            int col = Integer.numberOfTrailingZeros(bit);
            queens[row] = col;
            backtrack(row + 1, n, cols | bit, (diag | bit) << 1,
                    (antiDiag | bit) >> 1, queens, result);
            queens[row] = -1;
        }
    }

    private List<String> build(int[] queens, int n) {
        List<String> board = new ArrayList<>();
        for (int row = 0; row < n; row++) {
            char[] line = new char[n];
            Arrays.fill(line, '.');
            line[queens[row]] = 'Q';
            board.add(new String(line));
        }
        return board;
    }
}
```

### Alternative Complexity
- **Time**: O(n!)
- **Space**: O(n), excluding output

## Complexity
- **Time**: O(n!)
- **Space**: O(n^2)

## Key Takeaways
- Use columns and diagonals to check validity in O(1).
- The row number is the recursion depth.
