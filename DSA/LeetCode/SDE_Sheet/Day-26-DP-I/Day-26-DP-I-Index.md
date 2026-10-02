# Day 26 — Dynamic Programming I (1D DP)

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** DP — 1D Problems, Fibonacci, House Robber
**Difficulty Mix:** Easy / Medium

---

## DP Framework

```
Step 1: Define the state
  dp[i] = answer for subproblem of size i

Step 2: Find the recurrence
  dp[i] = f(dp[i-1], dp[i-2], ...)

Step 3: Establish base cases
  dp[0] = ?, dp[1] = ?

Step 4: Order of computation
  Usually left to right (smaller to larger)

Step 5: Extract the answer
  Usually dp[n] or max(dp)
```

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Climbing Stairs](Climbing-Stairs.md) | LeetCode 70 | Easy | [LeetCode](https://leetcode.com/problems/climbing-stairs/)
- [ ] [House Robber](House-Robber.md) | LeetCode 198 | Medium | [LeetCode](https://leetcode.com/problems/house-robber/)
- [ ] [House Robber II (Circular)](House-Robber-II-Circular.md) | LeetCode 213 | Medium | [LeetCode](https://leetcode.com/problems/house-robber-ii/)
- [ ] [Jump Game](Jump-Game.md) | LeetCode 55 | Medium | [LeetCode](https://leetcode.com/problems/jump-game/)
- [ ] [Jump Game II (Min Jumps)](Jump-Game-II-Min-Jumps.md) | LeetCode 45 | Medium | [LeetCode](https://leetcode.com/problems/jump-game-ii/)
- [ ] [Decode Ways](Decode-Ways.md) | LeetCode 91 | Medium | [LeetCode](https://leetcode.com/problems/decode-ways/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Climbing Stairs | Recursive choices of 1 or 2 steps. O(2^n). | Memoization or DP array. O(n) space. | Fibonacci rolling variables. O(n), O(1). |
| House Robber | Try rob/skip recursively. O(2^n). | DP array where dp[i] is best till house i. O(n) space. | Two rolling values: prev2 and prev1. O(n), O(1). |
| House Robber II | Try circular choices recursively. Exponential. | Run linear House Robber twice with DP arrays. | Run rolling DP on ranges [0..n-2] and [1..n-1]. O(n), O(1). |
| Jump Game | Recursively try every jump. Exponential. | DP reachable from each index. O(n^2). | Greedy farthest reachable index. O(n). |
| Jump Game II | Recursively try all jump paths. Exponential. | DP min jumps for every index. O(n^2). | Greedy BFS-level window. O(n). |
| Decode Ways | Recursively split into 1-char/2-char decodes. Exponential. | Memoization or DP array. O(n). | Two rolling DP values. O(n), O(1). |

---

## 1D DP Common Patterns

| Pattern | Recurrence |
|---------|-----------|
| Fibonacci / Staircase | `dp[i] = dp[i-1] + dp[i-2]` |
| Max/Min subproblem | `dp[i] = max(dp[i-1], dp[i-2] + cost[i])` |
| Partition | `dp[i] = dp[i-1] or dp[i-2] based on condition` |
| Greedy + DP hybrid | Jump Game, Coin Change |

#sde-sheet #dynamic-programming #day26
