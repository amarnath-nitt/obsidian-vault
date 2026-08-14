# Recursion - Practice

## Key Concepts
- **Base Case**: The condition that stops the recursion
- **Recursive Case**: Breaking the problem into smaller subproblems
- **Call Stack**: Each recursive call adds a frame to the call stack
- **Tail Recursion**: Recursive call is the last operation

## Common Recursion Patterns
1. **Divide & Conquer** - Split into halves, solve smaller pieces, combine answers
2. **Tree Recursion** - Multiple recursive calls per level
3. **Linear Recursion** - Single recursive call per level
4. **Mutual Recursion** - Two functions calling each other
5. **Memoized Recursion** - Cache repeated subproblems

---

## Problems

### Easy
- [x] Factorial - [Solution](solutions/Factorial.md) - `n * factorial(n - 1)`
- [x] [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (LC 509) - [Solution](solutions/LC-509-Fibonacci-Number.md) - Classic tree recursion
- [x] [Power of Two](https://leetcode.com/problems/power-of-two/) (LC 231) - [Solution](solutions/LC-231-Power-of-Two.md) - Repeated divide by 2
- [x] Sum of Digits - [Solution](solutions/Sum-of-Digits.md) - Peel off one digit
- [x] [Reverse String](https://leetcode.com/problems/reverse-string/) (LC 344) - [Solution](solutions/LC-344-Reverse-String.md) - Two recursive pointers

### Medium
- [x] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (LC 70) - [Solution](solutions/LC-70-Climbing-Stairs.md) - Fibonacci-style
- [x] [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (LC 17) - [Solution](solutions/LC-17-Letter-Combinations-Phone.md) - Cartesian product via recursion
- [x] [Permutations](https://leetcode.com/problems/permutations/) (LC 46) - [Solution](solutions/LC-46-Permutations.md) - Generate all permutations
- [x] [Subsets](https://leetcode.com/problems/subsets/) (LC 78) - [Solution](solutions/LC-78-Subsets.md) - Power set via recursion
- [x] [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) (LC 341) - [Solution](solutions/LC-341-Flatten-Nested-List-Iterator.md) - Recursive flattening
- [x] [Decode Ways](https://leetcode.com/problems/decode-ways/) (LC 91) - [Solution](solutions/LC-91-Decode-Ways.md) - Conditional branching
- [x] [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) (LC 779) - [Solution](solutions/LC-779-K-th-Symbol-in-Grammar.md) - Divide and conquer recursion

### Hard
- [x] [N-Queens](https://leetcode.com/problems/n-queens/) (LC 51) - [Solution](solutions/LC-51-N-Queens.md) - Recursive backtracking
- [ ] [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) (LC 10) - [Solution](solutions/LC-10-Regular-Expression-Matching.md) - Recursive pattern matching
- [ ] [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) (LC 37) - [Solution](solutions/LC-37-Sudoku-Solver.md) - Recursive constraint solving

---

## Tips
- **Always define your base case first** - prevents infinite recursion
- **Trust your recursive call** - assume it works correctly for the smaller input
- **Draw the recursion tree** - helps visualize branching and repeated work
- **Think about memoization** when you see repeated subproblems
