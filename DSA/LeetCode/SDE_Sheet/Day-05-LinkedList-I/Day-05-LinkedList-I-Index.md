# Day 5 — Linked Lists I

**Sheet:** [SDE Sheet Index](../SDE-Sheet-Index.md)
**Topic:** Linked Lists — Fundamentals
**Difficulty Mix:** Easy / Medium

---

## Problems

> Toggle each checkbox in Obsidian to track your own completion progress.

- [ ] [Reverse a Linked List](Reverse-a-Linked-List.md) | LeetCode 206 | Easy | [LeetCode](https://leetcode.com/problems/reverse-linked-list/)
- [ ] [Find Middle of Linked List](Find-Middle-of-Linked-List.md) | LeetCode 876 | Easy | [LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/)
- [ ] [Merge Two Sorted Linked Lists](Merge-Two-Sorted-Linked-Lists.md) | LeetCode 21 | Easy | [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)
- [ ] [Remove N-th Node from End](Remove-N-th-Node-from-End.md) | LeetCode 19 | Medium | [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [ ] [Delete a Given Node (no head access)](Delete-a-Given-Node-no-head-access.md) | LeetCode 237 | Medium | [LeetCode](https://leetcode.com/problems/delete-node-in-a-linked-list/)
- [ ] [Add Two Numbers as Linked Lists](Add-Two-Numbers-as-Linked-Lists.md) | LeetCode 2 | Medium | [LeetCode](https://leetcode.com/problems/add-two-numbers/)

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Reverse a Linked List | Copy values to a stack/array and rewrite nodes. O(n) space. | Recursive reversal. O(n) call stack. | Iterative three-pointer reversal. O(n) time, O(1) space. |
| Find Middle of Linked List | Count length, then walk to n/2. Two passes. | Store nodes in an array and index the middle. O(n) space. | Slow and fast pointers. One pass, O(1) space. |
| Merge Two Sorted Linked Lists | Collect values, sort, and rebuild. O((m+n) log(m+n)). | Recursive merge. O(m+n) time, O(m+n) stack. | Iterative dummy-node merge. O(m+n), O(1) extra space. |
| Remove N-th Node from End | Count length first, then delete. Two passes. | Push nodes onto a stack. O(n) space. | Two pointers with an n-node gap. One pass, O(1) space. |
| Delete a Given Node | With head access, search previous node. O(n). | Without head, copy next node's value and bypass it. O(1). | Same O(1) trick; valid only if node is not the tail. |
| Add Two Numbers as Linked Lists | Convert lists to numbers, add, rebuild; may overflow. | Use strings/BigInteger or stacks. Extra space. | Digit-by-digit carry simulation. O(max(m,n)), O(1) aside from output. |

---

## Linked List Mental Models

```
Technique              When to Use
──────────────────────────────────────────────
Dummy head             Simplify insert/delete at head
Slow-Fast pointers     Middle, cycle detection, kth from end
Two pointers (gap n)   Remove nth from end
Reverse               Palindrome check, reorder list
```

---

## Interview Tips for Linked Lists I

> 💡 **Always use a dummy node** when the head might change
> 💡 **Slow-fast pointer** is the Swiss army knife of linked lists
> 💡 **Draw the pointer operations** before coding — avoids infinite loops

#sde-sheet #linked-list #day5
