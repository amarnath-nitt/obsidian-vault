# Word Search

**Difficulty:** Medium
**Category:** Backtracking
**LeetCode Link:** [Word Search](https://leetcode.com/problems/word-search/)

---

## Problem Statement

Given an `m x n` grid of characters and a string `word`, return `true` if the word exists in the grid. The word must be constructed from sequentially adjacent cells (horizontally or vertically), and each cell may only be used once.

**Example:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

---

## Intuition

Try starting the word from every cell. At each cell, if the character matches the current letter in the word, explore all 4 directions for the next letter. Mark the cell as visited during exploration and restore it after (backtrack) to allow other paths to use it.

---

## Approach: Backtracking DFS

### Algorithm
1. For every cell `(i, j)`, try starting DFS if `board[i][j] == word[0]`
2. In DFS:
   - If `index == word.length()` → found the word, return true
   - If out of bounds, wrong character, or already visited → return false
   - Mark cell as visited (`board[i][j] = '#'`)
   - Explore all 4 directions for `word[index+1]`
   - Restore cell (backtrack)

### Java Code
```java
class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dfs(board, word, i, j, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int i, int j, int index) {
        if (index == word.length()) return true;
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length
            || board[i][j] != word.charAt(index)) return false;

        char temp = board[i][j];
        board[i][j] = '#'; // Mark visited

        boolean found = dfs(board, word, i + 1, j, index + 1) ||
                        dfs(board, word, i - 1, j, index + 1) ||
                        dfs(board, word, i, j + 1, index + 1) ||
                        dfs(board, word, i, j - 1, index + 1);

        board[i][j] = temp; // Restore (backtrack)
        return found;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(m × n × 4^L) — L = word length, 4 directions at each step
- **Space Complexity:** O(L) — recursion stack depth

---

## Key Takeaways

1. **In-place visited marking:** Temporarily replace cell with `'#'` — no extra visited array needed
2. **Restore on backtrack:** Always restore the cell after recursion
3. **Early termination:** `||` short-circuits — stops as soon as word is found

---

## Tags
#backtracking #dfs #medium #blind75
