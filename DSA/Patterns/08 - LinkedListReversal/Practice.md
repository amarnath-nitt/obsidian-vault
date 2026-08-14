# LinkedList In-place Reversal - Practice Notes

## Pattern Overview
Reverses a linked list or parts of it without using extra space, by changing the direction of pointers.

## Key Concepts
- **In-place**: O(1) space complexity
- **Three Pointers**: prev, current, next
- **Time Complexity**: O(n)

## Template Code

```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null, curr = head;
    
    while (curr != null) {
        ListNode next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
```

## Practice Problems

### Easy
- [ ] [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (LC 206) → [Solution](solutions/LC-206-Reverse-Linked-List.md)
- [ ] [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (LC 234) → [Solution](solutions/LC-234-Palindrome-Linked-List.md)

### Medium
- [ ] [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) (LC 92) → [Solution](solutions/LC-92-Reverse-Linked-List-II.md)
- [ ] [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (LC 24) → [Solution](solutions/LC-24-Swap-Nodes-in-Pairs.md)
- [ ] [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) (LC 328) → [Solution](solutions/LC-328-Odd-Even-Linked-List.md)
- [ ] [Rotate List](https://leetcode.com/problems/rotate-list/) (LC 61) → [Solution](solutions/LC-61-Rotate-List.md)
- [ ] [Reorder List](https://leetcode.com/problems/reorder-list/) (LC 143) → [Solution](solutions/LC-143-Reorder-List.md)

### Hard
- [ ] [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (LC 25) → [Solution](solutions/LC-25-Reverse-Nodes-k-Group.md)

## Reference
[LeetCode Pattern Guide](https://lnkd.in/gpBNzfpF)
