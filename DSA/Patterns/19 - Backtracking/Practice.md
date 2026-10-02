# Backtracking - Practice Notes

## Pattern Overview
A recursive technique for solving problems by trying to build a solution incrementally and abandoning solutions that fail to satisfy constraints.

## Key Concepts
- **Try all possibilities**: Explore all paths
- **Prune invalid paths**: Stop when constraints violated
- **Backtrack**: Undo choices and try alternatives
- **Time Complexity**: Often exponential O(2^n) or O(n!)

## Template Code

### Basic Backtracking
```java
public void backtrack(List<List<Integer>> result, List<Integer> current, 
                     int[] nums, boolean[] used) {
    // Base case - solution found
    if (current.size() == nums.length) {
        result.add(new ArrayList<>(current));
        return;
    }
    
    // Try all choices
    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;  // Skip if already used
        
        // Make choice
        current.add(nums[i]);
        used[i] = true;
        
        // Recurse
        backtrack(result, current, nums, used);
        
        // Undo choice (backtrack)
        current.remove(current.size() - 1);
        used[i] = false;
    }
}
```

### Combinations Template
```java
public void combine(List<List<Integer>> result, List<Integer> current,
                   int start, int n, int k) {
    if (current.size() == k) {
        result.add(new ArrayList<>(current));
        return;
    }
    
    for (int i = start; i <= n; i++) {
        current.add(i);
        combine(result, current, i + 1, n, k);
        current.remove(current.size() - 1);
    }
}
```

## Practice Problems

### Medium
- [ ] [Permutations](https://leetcode.com/problems/permutations/) (LC 46) → [Solution](solutions/LC-46-Permutations.md)
- [ ] [Permutations II](https://leetcode.com/problems/permutations-ii/) (LC 47) → [Solution](solutions/LC-47-Permutations-II.md)
- [ ] [Subsets](https://leetcode.com/problems/subsets/) (LC 78) → [Solution](solutions/LC-78-Subsets.md)
- [ ] [Combination Sum](https://leetcode.com/problems/combination-sum/) (LC 39) → [Solution](solutions/LC-39-Combination-Sum.md)
- [ ] [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (LC 17) → [Solution](solutions/LC-17-Letter-Combinations-Phone.md)
- [ ] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (LC 22) → [Solution](solutions/LC-22-Generate-Parentheses.md)
- [ ] [Word Search](https://leetcode.com/problems/word-search/) (LC 79) → [Solution](../MatrixTraversal/solutions/LC-79-Word-Search.md)
- [ ] [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) (LC 131) → [Solution](solutions/LC-131-Palindrome-Partitioning.md)

### Hard
- [ ] [N-Queens](https://leetcode.com/problems/n-queens/) (LC 51) → [Solution](solutions/LC-51-N-Queens.md)
- [ ] [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) (LC 37) → [Solution](solutions/LC-37-Sudoku-Solver.md)
- [ ] [Word Search II](https://leetcode.com/problems/word-search-ii/) (LC 212) → [Solution](solutions/LC-212-Word-Search-II.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gUc28SU6)
