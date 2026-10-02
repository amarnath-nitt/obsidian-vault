# Day 14 — Stack & Queue II

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Stack & Queue — Advanced Problems
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [LRU Cache](LRU-Cache.md) | LeetCode 146 | Medium | [LeetCode](https://leetcode.com/problems/lru-cache/)
- [ ] [Sliding Window Maximum](Sliding-Window-Maximum.md) | LeetCode 239 | Hard | [LeetCode](https://leetcode.com/problems/sliding-window-maximum/)
- [ ] [Daily Temperatures](Daily-Temperatures.md) | LeetCode 739 | Medium | [LeetCode](https://leetcode.com/problems/daily-temperatures/)
- [ ] [Celebrity Problem](Celebrity-Problem.md) | LeetCode — | Medium | [LeetCode search](https://leetcode.com/problemset/?search=Celebrity+Problem)
- [ ] [Stock Span Problem](Stock-Span-Problem.md) | LeetCode 901 | Medium | [LeetCode](https://leetcode.com/problems/online-stock-span/)
- [ ] [Rotten Oranges (BFS + Queue)](Rotten-Oranges-BFS-Queue.md) | LeetCode 994 | Medium | [LeetCode](https://leetcode.com/problems/rotting-oranges/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| LRU Cache | Store entries in a list and scan on get/put. O(n). | Use LinkedHashMap. O(1) average. | HashMap plus doubly linked list for explicit O(1) get/put. |
| Sliding Window Maximum | Compute max for every window. O(n*k). | Max-heap with lazy removal. O(n log k). | Monotonic deque of indexes. O(n). |
| Daily Temperatures | For each day, scan forward for warmer day. O(n^2). | Jump using previously computed answers. O(n) typical. | Monotonic decreasing stack of indexes. O(n). |
| Celebrity Problem | Check every candidate against everyone. O(n^2). | Stack elimination. O(n). | Two-pointer/candidate elimination plus verification. O(n), O(1). |
| Stock Span Problem | For each price, scan backward while prices are smaller. O(n^2). | Store previous greater index jumps. | Monotonic stack of price/index pairs. O(n). |
| Rotten Oranges | Scan the whole grid minute by minute. O((m*n)^2). | BFS from rotten oranges individually. | Multi-source BFS from all rotten oranges. O(m*n). |

---

## Key Design Patterns

| DS Design | Approach |
|-----------|----------|
| LRU Cache | HashMap + DLL |
| LFU Cache | HashMap + freq-bucketed DLL |
| Min Stack | Two stacks |
| Max Queue | Two stacks with max tracking |
| Sliding window max | Monotonic deque |

#sde-sheet #stack #queue #lru #day14
