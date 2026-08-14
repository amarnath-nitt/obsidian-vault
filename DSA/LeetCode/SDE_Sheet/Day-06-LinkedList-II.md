# Day 6 — Linked Lists II

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Linked Lists — Advanced
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Linked List Cycle Detection]] | 141/142 | Medium | ⬜ |
| 2 | [[#Intersection of Two Linked Lists]] | 160 | Easy | ⬜ |
| 3 | [[#Reverse Linked List in Groups of K]] | 25 | Hard | ⬜ |
| 4 | [[#Check if Linked List is Palindrome]] | 234 | Easy | ⬜ |
| 5 | [[#Flatten a Multilevel Doubly Linked List]] | 430 | Medium | ⬜ |
| 6 | [[#Rotate Linked List]] | 61 | Medium | ⬜ |

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

## Linked List Cycle Detection

**LeetCode 141** (Detect) · **142** (Find start) · Medium
🔗 [LC 141](https://leetcode.com/problems/linked-list-cycle/) · [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/)

### Problem
- 141: Does the list have a cycle?
- 142: If yes, return the node where the cycle begins.

### Approach (Floyd's Cycle Detection)

**Step 1:** Use slow/fast pointers. If they meet → cycle exists.

**Step 2 (find start):** After meeting:
- Move `slow` back to `head`
- Move both `slow` and `fast` one step at a time
- They will meet at the **cycle start**

**Why does this work?**
If fast traveled `2d` and slow traveled `d`, and cycle length is `c`:
`d = n*c` for some integer n → distance from head to cycle start = distance from meeting point to cycle start.

### Java Solution

```java
// LC 141 — Detect
public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}

// LC 142 — Find cycle start
public ListNode detectCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            slow = head;
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next;
            }
            return slow;
        }
    }
    return null;
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Intersection of Two Linked Lists

**LeetCode 160** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/intersection-of-two-linked-lists/)

### Problem
Find the node where two linked lists intersect. Return null if they don't intersect.

### Approach (Two Pointer — Equalize Distance)

- `pA` starts at `headA`, `pB` starts at `headB`
- When `pA` reaches end → redirect to `headB`
- When `pB` reaches end → redirect to `headA`
- They will meet at intersection (or both reach null)

**Why?** Both traverse `lenA + lenB` steps total — they equalize the "head distance" gap.

### Java Solution

```java
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        while (a != b) {
            a = (a == null) ? headB : a.next;
            b = (b == null) ? headA : b.next;
        }
        return a;
    }
}
```

**Complexity:** Time O(m+n) · Space O(1)

---

## Reverse Linked List in Groups of K

**LeetCode 25** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/reverse-nodes-in-k-group/)

### Problem
Reverse the list k nodes at a time. If remaining < k, leave as is.

### Approach

1. Check if k nodes exist ahead
2. Reverse k nodes (standard reverse with 3 pointers)
3. Connect the reversed segment to the rest
4. Recurse/iterate for next group

### Java Solution

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int count = 0;

        // Check if k nodes exist
        while (curr != null && count < k) { curr = curr.next; count++; }
        if (count < k) return head;

        // Reverse k nodes
        ListNode prev = null; curr = head;
        for (int i = 0; i < k; i++) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // head is now the tail of reversed group
        head.next = reverseKGroup(curr, k);
        return prev; // prev is new head
    }
}
```

**Complexity:** Time O(n) · Space O(n/k) recursive stack

---

## Check if Linked List is Palindrome

**LeetCode 234** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/palindrome-linked-list/)

### Problem
Determine if the linked list is a palindrome. O(n) time, O(1) space.

### Approach (3 steps)

1. **Find middle** using slow-fast pointers
2. **Reverse** the second half
3. **Compare** first half with reversed second half
4. (Optional) Restore the list

### Java Solution

```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        // Step 1: Find middle
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse second half
        ListNode prev = null, curr = slow;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // Step 3: Compare
        ListNode left = head, right = prev;
        while (right != null) {
            if (left.val != right.val) return false;
            left = left.next;
            right = right.next;
        }
        return true;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Flatten a Multilevel Doubly Linked List

**LeetCode 430** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

### Problem
Flatten a doubly linked list where each node can have a `child` pointer.

### Approach

- When we encounter a node with a `child`:
  1. Save the current `next`
  2. Connect current node to child
  3. Traverse to the **end of the child list**
  4. Connect end of child list to saved `next`

### Java Solution

```java
class Solution {
    public Node flatten(Node head) {
        Node curr = head;
        while (curr != null) {
            if (curr.child != null) {
                Node child = curr.child;
                Node next = curr.next;

                curr.next = child;
                child.prev = curr;
                curr.child = null;

                // Find tail of child list
                Node tail = child;
                while (tail.next != null) tail = tail.next;

                tail.next = next;
                if (next != null) next.prev = tail;
            }
            curr = curr.next;
        }
        return head;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Rotate Linked List

**LeetCode 61** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/rotate-list/)

### Problem
Rotate the list to the right by k places.

### Approach

1. Find **length** and connect tail to head (make circular)
2. Effective rotation = `k % length`
3. Move to `(length - k%length - 1)` position → that's the new tail
4. Break the circle there

### Java Solution

```java
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;

        // Find length and tail
        ListNode tail = head;
        int len = 1;
        while (tail.next != null) { tail = tail.next; len++; }

        // Make circular
        tail.next = head;

        // Find new tail (position len - k%len - 1)
        int stepsToNewTail = len - k % len - 1;
        ListNode newTail = head;
        for (int i = 0; i < stepsToNewTail; i++) newTail = newTail.next;

        ListNode newHead = newTail.next;
        newTail.next = null;
        return newHead;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Interview Tips for Linked Lists II

> 💡 **Cycle problems → Floyd's algorithm** (slow-fast)
> 💡 **Intersection → equalize total traversal distance**
> 💡 **K-group reverse → check count before reversing, recurse rest**
> 💡 **Palindrome LL → find middle + reverse second half**

#sde-sheet #linked-list #day6
