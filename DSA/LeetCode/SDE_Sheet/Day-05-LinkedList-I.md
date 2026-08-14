# Day 5 — Linked Lists I

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Linked Lists — Fundamentals
**Difficulty Mix:** Easy / Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Reverse a Linked List]] | 206 | Easy | ⬜ |
| 2 | [[#Find Middle of Linked List]] | 876 | Easy | ⬜ |
| 3 | [[#Merge Two Sorted Linked Lists]] | 21 | Easy | ⬜ |
| 4 | [[#Remove N-th Node from End]] | 19 | Medium | ⬜ |
| 5 | [[#Delete a Given Node (no head access)]] | 237 | Medium | ⬜ |
| 6 | [[#Add Two Numbers as Linked Lists]] | 2 | Medium | ⬜ |

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

## Reverse a Linked List

**LeetCode 206** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/reverse-linked-list/)

### Problem
Reverse a singly linked list.

### Approach (Iterative — 3 Pointers)

- Maintain `prev = null`, `curr = head`, `next = null`
- At each step: save next, reverse the pointer, move forward

### Java Solution

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, curr = head;

        while (curr != null) {
            ListNode next = curr.next; // save next
            curr.next = prev;          // reverse pointer
            prev = curr;               // move prev
            curr = next;               // move curr
        }
        return prev;
    }
}
```

**Recursive:**
```java
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode rest = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return rest;
}
```

**Complexity:** Time O(n) · Space O(1) iterative / O(n) recursive

---

## Find Middle of Linked List

**LeetCode 876** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/middle-of-the-linked-list/)

### Problem
Find the middle node of a linked list. If two middles, return the second.

### Approach (Slow-Fast Pointers / Floyd's)

- `slow` moves 1 step, `fast` moves 2 steps
- When `fast` reaches end, `slow` is at the middle

### Java Solution

```java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Merge Two Sorted Linked Lists

**LeetCode 21** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/merge-two-sorted-lists/)

### Problem
Merge two sorted linked lists into one sorted list.

### Approach

- Use a **dummy head** to simplify edge cases
- Compare list1 and list2 node by node, attach smaller one
- Attach remaining list at end

### Java Solution

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) { curr.next = l1; l1 = l1.next; }
            else                  { curr.next = l2; l2 = l2.next; }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
```

**Complexity:** Time O(m+n) · Space O(1)

---

## Remove N-th Node from End

**LeetCode 19** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

### Problem
Remove the n-th node from the end of the list in one pass.

### Approach (Two Pointers — Gap of N)

- Move `fast` pointer n+1 steps ahead
- Move both `slow` and `fast` until `fast` is null
- `slow` now points to the node **before** the one to delete

### Java Solution

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode slow = dummy, fast = dummy;

        // Move fast n+1 steps
        for (int i = 0; i <= n; i++) fast = fast.next;

        // Move both until fast is null
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Delete a Given Node (no head access)

**LeetCode 237** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/delete-node-in-a-linked-list/)

### Problem
Delete a node given only access to that node (not the head). Not the tail.

### Approach

- **Copy** the next node's value into current node
- Then **skip** the next node

> We can't actually delete the current node, so we make it "become" the next node.

### Java Solution

```java
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```

**Complexity:** Time O(1) · Space O(1)

---

## Add Two Numbers as Linked Lists

**LeetCode 2** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/add-two-numbers/)

### Problem
Two non-empty linked lists represent non-negative integers in **reverse order**. Add them.

### Approach

- Simulate grade-school addition digit by digit
- Track `carry` across iterations
- Create new nodes for the result

### Java Solution

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry;
            if (l1 != null) { sum += l1.val; l1 = l1.next; }
            if (l2 != null) { sum += l2.val; l2 = l2.next; }
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
        }
        return dummy.next;
    }
}
```

**Complexity:** Time O(max(m,n)) · Space O(max(m,n))

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
