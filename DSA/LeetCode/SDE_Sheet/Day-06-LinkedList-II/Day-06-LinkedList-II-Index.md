# Day 6 — Linked Lists II

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Linked Lists — Advanced
**Difficulty Mix:** Medium / Hard

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Linked List Cycle Detection](Linked-List-Cycle-Detection.md) | LeetCode 141/142 | Medium | [LeetCode](https://leetcode.com/problems/linked-list-cycle/)
- [ ] [Intersection of Two Linked Lists](Intersection-of-Two-Linked-Lists.md) | LeetCode 160 | Easy | [LeetCode](https://leetcode.com/problems/intersection-of-two-linked-lists/)
- [ ] [Reverse Linked List in Groups of K](Reverse-Linked-List-in-Groups-of-K.md) | LeetCode 25 | Hard | [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [ ] [Check if Linked List is Palindrome](Check-if-Linked-List-is-Palindrome.md) | LeetCode 234 | Easy | [LeetCode](https://leetcode.com/problems/palindrome-linked-list/)
- [ ] [Flatten a Multilevel Doubly Linked List](Flatten-a-Multilevel-Doubly-Linked-List.md) | LeetCode 430 | Medium | [LeetCode](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)
- [ ] [Rotate Linked List](Rotate-Linked-List.md) | LeetCode 61 | Medium | [LeetCode](https://leetcode.com/problems/rotate-list/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Linked List Cycle Detection | Store visited nodes in a HashSet. O(n) space. | Mark nodes if mutation is allowed. Unsafe for interviews. | Floyd slow/fast pointers. O(n) time, O(1) space. |
| Intersection of Two Linked Lists | Compare every pair of nodes. O(m*n). | Store nodes of one list in a HashSet. O(m+n) space. | Two pointers switch heads to equalize distance. O(m+n), O(1). |
| Reverse Linked List in Groups of K | Copy nodes/values and reverse chunks. O(n) space. | Recursive chunk reversal. O(n/k) stack. | Iterative pointer rewiring group by group. O(n), O(1). |
| Check if Linked List is Palindrome | Copy values to an array and use two pointers. O(n) space. | Push first half onto a stack. O(n/2) space. | Find middle, reverse second half, compare. O(n), O(1). |
| Flatten a Multilevel Doubly Linked List | DFS collect all nodes, then relink. O(n) space. | Iterative DFS with stack. O(n) worst-case space. | Splice child lists in DFS order while tracking tails. O(n). |
| Rotate Linked List | Move last node to front k times. O(k*n). | Compute length and reduce k modulo n. | Make a cycle, break at new tail. O(n), O(1). |

---

## Interview Tips for Linked Lists II

> 💡 **Cycle problems → Floyd's algorithm** (slow-fast)
> 💡 **Intersection → equalize total traversal distance**
> 💡 **K-group reverse → check count before reversing, recurse rest**
> 💡 **Palindrome LL → find middle + reverse second half**

#sde-sheet #linked-list #day6
