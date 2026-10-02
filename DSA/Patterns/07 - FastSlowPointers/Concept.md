# Fast & Slow Pointers — Concept

## What Is It?

Fast & Slow Pointers (Floyd's Tortoise and Hare) uses two pointers moving at **different speeds** through a linked list or sequence. The fast pointer moves 2× speed of the slow pointer, enabling cycle detection and middle-finding in O(n) time.

---

## When to Use

> **Trigger keywords:** "linked list cycle", "find middle", "palindrome linked list", "duplicate number", "happy number"

| Trigger | Example |
|---------|---------|
| **Detect cycle** in linked list | Linked List Cycle |
| **Find the start** of a cycle | Linked List Cycle II |
| Find the **middle node** | Middle of Linked List |
| Check **palindrome** linked list | Palindrome Linked List |

---

## Variants

### 1. Cycle Detection
```java
boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}
```

### 2. Find Cycle Start
```java
ListNode findCycleStart(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            slow = head;  // reset slow to head
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next;  // both move at same speed
            }
            return slow;  // cycle start
        }
    }
    return null;
}
```

### 3. Find Middle
```java
ListNode findMiddle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow; // middle node
}
```

---

## Visual Walkthrough

### Cycle Detection
```
1 → 2 → 3 → 4 → 5
              ↑       ↓
              8 ← 7 ← 6

Step 1: slow=1, fast=1
Step 2: slow=2, fast=3
Step 3: slow=3, fast=5
Step 4: slow=4, fast=7
Step 5: slow=5, fast=3  (fast lapped!)
Step 6: slow=6, fast=5
Step 7: slow=7, fast=7  ← MEET! Cycle exists.

Find start: reset slow=head
slow=1, fast=7 → slow=2, fast=8 → slow=3, fast=3 ← MEET at cycle start!
```

---

## Time/Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Cycle detection | O(n) | O(1) |
| Find cycle start | O(n) | O(1) |
| Find middle | O(n/2) | O(1) |

---

## Common Mistakes

1. **NullPointerException** → Always check `fast != null && fast.next != null`
2. **Confusing cycle start algorithm** → After meeting, reset ONE pointer to head, then both move at speed 1
3. **Middle node definition** → For even-length lists, this returns the second middle node

---

## Related Patterns

- [[08 - LinkedListReversal/Concept|Linked List Reversal]] — Often combined: find middle, then reverse second half
- [[04 - TwoPointers/Concept|Two Pointers]] — Fast & Slow is a variant of two pointers

---

#fast-slow-pointers #linked-list #dsa #concept
