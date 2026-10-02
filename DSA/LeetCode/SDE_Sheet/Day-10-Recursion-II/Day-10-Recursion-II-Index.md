# Day 10 — Recursion & Backtracking II

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Backtracking — Hard Problems
**Difficulty Mix:** Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [N-Queens](N-Queens.md) | LeetCode 51 | Hard | [LeetCode](https://leetcode.com/problems/n-queens/)
- [ ] [Sudoku Solver](Sudoku-Solver.md) | LeetCode 37 | Hard | [LeetCode](https://leetcode.com/problems/sudoku-solver/)
- [ ] [M-Coloring Problem](M-Coloring-Problem.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=M-Coloring+Problem)
- [ ] [Rat in a Maze](Rat-in-a-Maze.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Rat+in+a+Maze)
- [ ] [Word Break II](Word-Break-II.md) | LeetCode 140 | Hard | [LeetCode](https://leetcode.com/problems/word-break-ii/)
- [ ] [Palindrome Partitioning](Palindrome-Partitioning.md) | LeetCode 131 | Medium | [LeetCode](https://leetcode.com/problems/palindrome-partitioning/)

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

## Hard Backtracking Tips

> 💡 **N-Queens:** Boolean arrays for column/diagonal checks — O(1) instead of O(n)
> 💡 **Sudoku:** Box index = `(row/3)*3 + col/3`
> 💡 **Memoization** turns exponential backtracking into polynomial (Word Break II)
> 💡 **Always think:** what is my "undo" operation?

#sde-sheet #recursion #backtracking #day10
