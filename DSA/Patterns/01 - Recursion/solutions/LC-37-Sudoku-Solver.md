---
status: complete
---

# Sudoku Solver (LC 37)

**Difficulty**: Hard  
**Pattern**: Recursion / Backtracking  
**LeetCode**: https://leetcode.com/problems/sudoku-solver/

## Problem Statement
Fill a `9 x 9` Sudoku board so that each row, column, and `3 x 3` box contains digits `1` through `9`.

## Recursive Idea
Find an empty cell, try every valid digit, recurse, and undo the digit if it does not lead to a solution.

## Interview Approach & Key Intuition

### 1. The Core Idea: Backtracking with Constraint Validation
**Strategy:**
- Find the first empty cell (marked with '.')
- Try digits 1-9 in that cell
- For each digit, validate it against row/column/3×3 box constraints
- If valid, place the digit and recurse to solve the rest of the board
- If recursion finds a solution, return true immediately
- If recursion fails, undo the placement (backtrack) and try the next digit

This explores the search space intelligently through early constraint checking.

### 2. The Main Challenge: O(1) Constraint Checking
**Naive approach**: For each digit, scan the entire row, column, and box
- Time per validation: O(9) = O(1) in practice (constant size)
- But conceptually, we want instant validation

**The Efficient Trick**: Check three constraints in a single loop
```java
for (int i = 0; i < 9; i++) {
    if (board[row][i] == digit) return false;      // Row check
    if (board[i][col] == digit) return false;      // Column check
    if (board[boxRow + i/3][boxCol + i%3] == digit) return false; // Box check
}
```

**Box Index Formula** (The Key!)
For any cell (row, col), the top-left corner of its 3×3 box is:
- `boxRow = (row / 3) * 3`
- `boxCol = (col / 3) * 3`

**Example**: Cell (5, 7)
```
boxRow = (5 / 3) * 3 = 1 * 3 = 3  (top row: 3,4,5)
boxCol = (7 / 3) * 3 = 2 * 3 = 6  (left col: 6,7,8)
Box coordinates: rows 3-5, cols 6-8 ✓
```

### 3. Why Backtracking Works for NP-Complete Problems
Sudoku is **NP-Complete** → no known polynomial-time algorithm exists.

Backtracking with constraint pruning works well because:
- **Early pruning**: Invalid digits skip entire subtrees of impossible solutions
- **Fast constraint checking**: Remaining valid candidates shrink quickly after each placement
- **Single solution**: Once found, return immediately (we don't enumerate all solutions)
- **Practice**: Most Sudoku puzzles can be solved in milliseconds

### 4. Working Through a 4×4 Mini-Sudoku Example

**Initial Board:**
```
1 .
. .
-----
. 3
4 .
```

**Solution Process:**
```
Step 1: Find first empty at (0,1)
  Try digit '2':
    Check constraints: '2' not in row 0, col 1, or top-left box? ✓ Valid
    Place it: board[0][1] = '2'
    Recurse...

Step 2: Find empty at (1,0)
  Try digit '1': Already in row 0 (box) or... Let me check properly
  Try '2': '2' in col 1 of top-left box? Yes, skip
  Try '3': Valid? Check row, col, box... if valid, place it
  Try '4': Valid? Check...
  
  (Continue until we place all cells or hit a dead-end)

Step 3: If recursion returns false (dead-end), backtrack
  Undo the placement: board[row][col] = '.'
  Try next digit
```

### 5. State Space & Complexity
- **Search space**: Up to 9^(empty cells) possibilities
- **Pruning**: Constraint checking eliminates ~99% of branches early
- **Time complexity**: O(9^(empty cells)) worst-case, but typically much faster due to pruning
- **Space complexity**: O(empty cells) for recursion stack depth

### 6. Optimization: Minimum Remaining Values (MRV)
Instead of scanning left-to-right, pick the empty cell with **fewest valid candidates**:
```
For each empty cell:
    Count how many digits 1-9 are valid
    Pick the cell with minimum count

Why? A cell with only 1 valid option determines the solution faster
     than a cell with 5 valid options
```
This is implemented in the Bitmask alternative solution.

### How to Explain in Interview
"I use backtracking with constraint validation. For each empty cell, I try digits 1-9 and validate 
them against row, column, and 3×3 box constraints in O(1) time. The box formula is (row/3)*3 for 
the top-left corner. If a digit is valid, I place it and recurse. If recursion finds a solution, 
I return immediately. Otherwise, I backtrack by undoing the placement and trying the next digit. 
For optimization, I can use the MRV heuristic to pick cells with fewest candidates, significantly 
reducing the search tree size."

## Java Code
```java
class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }

    private boolean solve(char[][] board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] != '.') {
                    continue;
                }

                for (char digit = '1'; digit <= '9'; digit++) {
                    if (isValid(board, row, col, digit)) {
                        board[row][col] = digit;
                        if (solve(board)) {
                            return true;
                        }
                        board[row][col] = '.';
                    }
                }
                return false;
            }
        }
        return true;
    }

    private boolean isValid(char[][] board, int row, int col, char digit) {
        int boxRow = (row / 3) * 3;
        int boxCol = (col / 3) * 3;

        for (int i = 0; i < 9; i++) {
            if (board[row][i] == digit || board[i][col] == digit) {
                return false;
            }
            if (board[boxRow + i / 3][boxCol + i % 3] == digit) {
                return false;
            }
        }
        return true;
    }
}
```

## Alternative Optimal Solution: Bitmask Backtracking
Track used digits in row, column, and box masks. Pick the next empty cell with the fewest candidates to reduce branching.

```java
class Solution {
    private final int[] rows = new int[9];
    private final int[] cols = new int[9];
    private final int[] boxes = new int[9];
    private final List<int[]> emptyCells = new ArrayList<>();

    public void solveSudoku(char[][] board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') {
                    emptyCells.add(new int[]{row, col});
                } else {
                    int bit = 1 << (board[row][col] - '1');
                    rows[row] |= bit;
                    cols[col] |= bit;
                    boxes[box(row, col)] |= bit;
                }
            }
        }

        solve(board, 0);
    }

    private boolean solve(char[][] board, int index) {
        if (index == emptyCells.size()) {
            return true;
        }

        int best = index;
        int bestMask = 0;
        int fewestOptions = 10;

        for (int i = index; i < emptyCells.size(); i++) {
            int[] cell = emptyCells.get(i);
            int row = cell[0];
            int col = cell[1];
            int mask = candidates(row, col);
            int options = Integer.bitCount(mask);

            if (options < fewestOptions) {
                fewestOptions = options;
                best = i;
                bestMask = mask;
            }
        }

        Collections.swap(emptyCells, index, best);
        int[] cell = emptyCells.get(index);
        int row = cell[0];
        int col = cell[1];
        int box = box(row, col);
        int mask = bestMask;

        while (mask != 0) {
            int bit = mask & -mask;
            mask -= bit;

            rows[row] |= bit;
            cols[col] |= bit;
            boxes[box] |= bit;
            board[row][col] = (char) ('1' + Integer.numberOfTrailingZeros(bit));

            if (solve(board, index + 1)) {
                return true;
            }

            board[row][col] = '.';
            rows[row] &= ~bit;
            cols[col] &= ~bit;
            boxes[box] &= ~bit;
        }

        Collections.swap(emptyCells, index, best);
        return false;
    }

    private int candidates(int row, int col) {
        return ~(rows[row] | cols[col] | boxes[box(row, col)]) & 0x1FF;
    }

    private int box(int row, int col) {
        return (row / 3) * 3 + col / 3;
    }
}
```

### Alternative Complexity
- **Time**: O(9^e), where `e` is the number of empty cells, with much stronger pruning in practice
- **Space**: O(e)

## Complexity
- **Time**: O(9^e), where `e` is the number of empty cells
- **Space**: O(e)

## Key Takeaways
- Return `true` as soon as a full valid board is found.
- Undo failed placements to restore state for the next choice.
