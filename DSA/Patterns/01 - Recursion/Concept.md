# Recursion — Concept

## What Is It?

Recursion is a technique where a function calls itself to solve smaller instances of the same problem. Every recursive solution has a **base case** (stopping condition) and a **recursive case** (breaking into subproblems).

---

## When to Use

> **Trigger keywords:** "all combinations", "all permutations", "generate all", "subdivide", "tree structure", "nested structure"

| Trigger | Example |
|---------|---------|
| Problem has a **tree/nested structure** | File system traversal, JSON parsing |
| Need to **generate all possibilities** | Permutations, subsets, combinations |
| Problem can be split into **identical smaller subproblems** | Fibonacci, merge sort |
| **Backtracking** is needed | N-Queens, Sudoku |

---

## Variants

### 1. Linear Recursion
Single recursive call per level. Example: factorial, linked list traversal.
```
f(n) = n * f(n-1)
```

### 2. Tree Recursion (Branching)
Multiple recursive calls per level. Example: Fibonacci, binary tree operations.
```
f(n) = f(n-1) + f(n-2)
```

### 3. Divide & Conquer
Split into halves, solve, combine. Example: merge sort, binary search.
```
f(arr) = merge(f(left_half), f(right_half))
```

### 4. Tail Recursion
Recursive call is the last operation — can be optimized by compilers.
```java
int factorial(int n, int acc) {
    if (n <= 1) return acc;
    return factorial(n - 1, n * acc); // tail call
}
```

### 5. Memoized Recursion (Top-Down DP)
Cache results of subproblems to avoid recomputation.
```java
int fib(int n, int[] memo) {
    if (memo[n] != 0) return memo[n];
    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n];
}
```

---

## Visual Walkthrough

### Recursion Tree for `fib(5)`
```
                    fib(5)
                  /        \
             fib(4)        fib(3)
            /      \       /    \
        fib(3)   fib(2)  fib(2)  fib(1)
        /   \    /   \    /   \
    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
    /   \
fib(1) fib(0)

Repeated subproblems: fib(3), fib(2), fib(1), fib(0)
→ This is why memoization helps!
```

---

## Time/Space Complexity

| Variant | Time | Space |
|---------|------|-------|
| Linear | O(n) | O(n) stack |
| Tree (branching factor b, depth d) | O(b^d) | O(d) stack |
| With Memoization | O(n) | O(n) cache + O(n) stack |
| Tail Recursion (optimized) | O(n) | O(1) |

---

## Common Mistakes

1. **Forgetting the base case** → Infinite recursion, StackOverflow
2. **Not returning the recursive result** → Writing `func(n-1)` instead of `return func(n-1)`
3. **Modifying shared state without backtracking** → Especially in permutation/combination problems, always undo changes after the recursive call

---

## Related Patterns

- [[19 - Backtracking/Concept|Backtracking]] — Recursion + constraint pruning
- [[20 - DynamicProgramming/Concept|Dynamic Programming]] — Memoized recursion → tabulation
- [[11 - DepthFirstSearch/Concept|DFS]] — Recursive traversal of graphs/trees

---

#recursion #dsa #concept
