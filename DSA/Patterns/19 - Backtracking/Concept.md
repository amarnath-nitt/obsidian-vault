# Backtracking — Concept

## What Is It?

Backtracking is a systematic way to explore all possible solutions by making a choice, exploring further, and **undoing the choice** (backtracking) if it doesn't lead to a valid solution. It's DFS on a decision tree with pruning.

---

## When to Use

> **Trigger keywords:** "all combinations", "all permutations", "generate all valid", "partition", "N-Queens", "Sudoku"

| Trigger | Example |
|---------|---------|
| Generate **all permutations** | Permutations, Permutations II |
| Generate **all subsets/combinations** | Subsets, Combination Sum |
| **Constraint satisfaction** | N-Queens, Sudoku Solver |
| **Partition** with conditions | Palindrome Partitioning |

---

## Template

```java
void backtrack(List<List<Integer>> result, List<Integer> current, 
               int[] nums, int start) {
    result.add(new ArrayList<>(current)); // or check if valid solution
    
    for (int i = start; i < nums.length; i++) {
        // 1. Choose
        current.add(nums[i]);
        
        // 2. Explore
        backtrack(result, current, nums, i + 1); // i+1 for combinations, i for reuse
        
        // 3. Un-choose (backtrack)
        current.remove(current.size() - 1);
    }
}
```

---

## Visual Walkthrough

### Subsets of `[1, 2, 3]`
```
                    []
               /     |     \
            [1]     [2]    [3]
           /   \     |
        [1,2] [1,3] [2,3]
          |
       [1,2,3]

Result: [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
```

### Key: Choose → Explore → Un-choose
```
current = []
  add 1 → current = [1]
    add 2 → current = [1,2]
      add 3 → current = [1,2,3]  ✓ record
      remove 3 → current = [1,2]  ← backtrack
    remove 2 → current = [1]      ← backtrack
    add 3 → current = [1,3]
      remove 3 → current = [1]
  remove 1 → current = []         ← backtrack
  add 2 → current = [2]
  ...
```

---

## Pruning Strategies

| Strategy | When | Example |
|----------|------|---------|
| **Skip duplicates** | Input has duplicates | `if (i > start && nums[i] == nums[i-1]) continue` |
| **Constraint check** | Early termination | N-Queens: check column, diagonal conflicts |
| **Sum exceeds target** | Combination sum | `if (sum > target) return` |

---

## Time/Space Complexity

| Problem | Time | Space |
|---------|------|-------|
| Subsets | O(2^n) | O(n) recursion depth |
| Permutations | O(n!) | O(n) |
| N-Queens | O(n!) | O(n) |
| Combination Sum | O(2^t) where t = target | O(t) |

---

## Common Mistakes

1. **Forgetting to backtrack** → Always undo the choice after recursive call
2. **Not creating a copy** → `result.add(new ArrayList<>(current))` not `result.add(current)`
3. **Not handling duplicates** → Sort first, then skip `nums[i] == nums[i-1]` when `i > start`

---

## Related Patterns

- [[01 - Recursion/Concept|Recursion]] — Backtracking is recursive by nature
- [[11 - DepthFirstSearch/Concept|DFS]] — Backtracking = DFS on decision tree
- [[20 - DynamicProgramming/Concept|Dynamic Programming]] — When backtracking has overlapping subproblems

---

#backtracking #dsa #concept
