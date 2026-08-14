# Day 10 — Recursion & Backtracking II

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Backtracking — Hard Problems
**Difficulty Mix:** Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#N-Queens]] | 51 | Hard | ⬜ |
| 2 | [[#Sudoku Solver]] | 37 | Hard | ⬜ |
| 3 | [[#M-Coloring Problem]] | — | Medium | ⬜ |
| 4 | [[#Rat in a Maze]] | — | Medium | ⬜ |
| 5 | [[#Word Break II]] | 140 | Hard | ⬜ |
| 6 | [[#Palindrome Partitioning]] | 131 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| N-Queens | Try queen placements and validate the whole board each time. Exponential. | Place row by row and scan column/diagonals for safety. | Track columns and diagonals with sets/bitmasks. O(n!) search with O(1) checks. |
| Sudoku Solver | Try 1-9 in every blank and rescan board for validity. | Backtrack with row/column/box sets. | Bitmasks plus choosing the cell with fewest candidates. |
| M-Coloring Problem | Try all m^V color assignments. | Backtrack and check colored neighbors before placing. | Use vertex ordering/bitsets to prune conflicts earlier. |
| Rat in a Maze | Try all paths, including revisits. Exponential and cyclic. | DFS with visited matrix and backtracking. | Direction arrays, boundary pruning, and lexicographic traversal. |
| Word Break II | Try every split and rebuild repeated suffixes. Exponential. | Memoize sentences for each start index. | Trie/dictionary-length pruning plus memoized DFS. |
| Palindrome Partitioning | Generate all partitions and check each substring. | Precompute palindrome table. O(n^2). | Backtrack using the table to append only palindromic cuts. |

---

## N-Queens

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

## Sudoku Solver

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

## M-Coloring Problem

**Problem:** Given an undirected graph and M colors, determine if the graph can be colored with M colors such that no two adjacent vertices have the same color.

### Approach

- Assign colors to vertices one by one
- For each vertex, try colors 1 to M
- Check if the color is safe (no adjacent vertex has same color)
- Backtrack if no color works

### Java Solution

```java
public class MColoring {
    static boolean isSafe(boolean[][] graph, int[] color, int vertex, int c, int n) {
        for (int i = 0; i < n; i++)
            if (graph[vertex][i] && color[i] == c) return false;
        return true;
    }

    static boolean solve(boolean[][] graph, int[] color, int vertex, int m, int n) {
        if (vertex == n) return true;
        for (int c = 1; c <= m; c++) {
            if (isSafe(graph, color, vertex, c, n)) {
                color[vertex] = c;
                if (solve(graph, color, vertex + 1, m, n)) return true;
                color[vertex] = 0; // backtrack
            }
        }
        return false;
    }

    static boolean graphColoring(boolean[][] graph, int m, int n) {
        int[] color = new int[n];
        return solve(graph, color, 0, m, n);
    }
}
```

**Complexity:** Time O(M^V) · Space O(V)

---

## Rat in a Maze

**Problem:** Rat starts at (0,0), find all paths to (n-1,n-1). Can move in all 4 directions.

### Approach

- DFS/backtracking: try all 4 directions
- Mark cell as visited while exploring, unmark when backtracking

### Java Solution

```java
public class RatMaze {
    static List<String> findPath(int[][] maze, int n) {
        List<String> paths = new ArrayList<>();
        boolean[][] visited = new boolean[n][n];
        if (maze[0][0] == 1) dfs(maze, visited, 0, 0, n, "", paths);
        return paths;
    }

    static int[] dr = {1, 0, 0, -1};
    static int[] dc = {0, -1, 1, 0};
    static char[] dir = {'D', 'L', 'R', 'U'};

    static void dfs(int[][] maze, boolean[][] visited,
                    int r, int c, int n, String path, List<String> paths) {
        if (r == n-1 && c == n-1) { paths.add(path); return; }

        visited[r][c] = true;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n
                    && maze[nr][nc] == 1 && !visited[nr][nc]) {
                dfs(maze, visited, nr, nc, n, path + dir[d], paths);
            }
        }
        visited[r][c] = false; // backtrack
    }
}
```

---

## Word Break II

**LeetCode 140** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/word-break-ii/)

### Problem
Return all possible sentences by inserting spaces into `s` using words from `wordDict`.

### Approach (Backtracking + Memoization)

- Try all prefixes of remaining string
- If prefix is in dictionary, recurse on suffix
- Memoize: `string → list of sentences` to avoid recomputation

### Java Solution

```java
class Solution {
    Map<String, List<String>> memo = new HashMap<>();

    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        return backtrack(s, dict);
    }

    private List<String> backtrack(String s, Set<String> dict) {
        if (memo.containsKey(s)) return memo.get(s);
        List<String> result = new ArrayList<>();
        if (s.isEmpty()) { result.add(""); return result; }

        for (int end = 1; end <= s.length(); end++) {
            String word = s.substring(0, end);
            if (dict.contains(word)) {
                List<String> rest = backtrack(s.substring(end), dict);
                for (String sentence : rest) {
                    result.add(word + (sentence.isEmpty() ? "" : " " + sentence));
                }
            }
        }
        memo.put(s, result);
        return result;
    }
}
```

---

## Palindrome Partitioning

**LeetCode 131** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/palindrome-partitioning/)

### Problem
Partition string `s` such that every substring of the partition is a palindrome.

### Approach (Backtracking)

- Try each prefix: if it's a palindrome, recurse on the suffix
- Add to result when entire string is consumed

### Java Solution

```java
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(String s, int start, List<String> current, List<List<String>> result) {
        if (start == s.length()) {
            result.add(new ArrayList<>(current)); return;
        }
        for (int end = start + 1; end <= s.length(); end++) {
            String sub = s.substring(start, end);
            if (isPalindrome(sub)) {
                current.add(sub);
                backtrack(s, end, current, result);
                current.remove(current.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) if (s.charAt(l++) != s.charAt(r--)) return false;
        return true;
    }
}
```

---

## Hard Backtracking Tips

> 💡 **N-Queens:** Boolean arrays for column/diagonal checks — O(1) instead of O(n)
> 💡 **Sudoku:** Box index = `(row/3)*3 + col/3`
> 💡 **Memoization** turns exponential backtracking into polynomial (Word Break II)
> 💡 **Always think:** what is my "undo" operation?

#sde-sheet #recursion #backtracking #day10
