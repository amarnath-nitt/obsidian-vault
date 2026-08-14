# Reverse Linked List

**Difficulty:** Easy  
**Category:** Linked Lists  
**LeetCode Link:** [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

---

## Problem Statement

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**
```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**
```
Input: head = []
Output: []
```

**Constraints:**
- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

---

## Intuition

To reverse a linked list, we need to change the direction of all `next` pointers. We can do this iteratively or recursively.

---

## Approach 1: Iterative (Optimized Solution)

### Algorithm
1. Use three pointers: `prev`, `current`, `next`
2. Iterate through the list
3. For each node, reverse its `next` pointer
4. Move all pointers forward
5. Return `prev` as the new head

### Java Code
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        
        while (current != null) {
            ListNode next = current.next;  // Save next node
            current.next = prev;           // Reverse pointer
            prev = current;                // Move prev forward
            current = next;                // Move current forward
        }
        
        return prev;  // New head
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Visit each node once
- **Space Complexity:** O(1) - Only using pointers

---

## Approach 2: Recursive

### Algorithm
1. Base case: if head is null or only one node, return head
2. Recursively reverse the rest of the list
3. Fix the pointers for current node
4. Return the new head

### Java Code
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        // Base case
        if (head == null || head.next == null) {
            return head;
        }
        
        // Reverse the rest of the list
        ListNode newHead = reverseList(head.next);
        
        // Fix pointers
        head.next.next = head;  // Make next node point back to current
        head.next = null;        // Current node points to null
        
        return newHead;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n) - Visit each node once
- **Space Complexity:** O(n) - Recursion stack

### Why Iterative is Better
- ✅ O(1) space vs O(n) space
- ✅ No risk of stack overflow
- ✅ More efficient in practice
- ✅ Easier to understand

---

## Key Takeaways

1. **Pattern:** Three-pointer technique for linked list reversal
2. **Iterative vs Recursive:** Iterative is more space-efficient
3. **Pointer manipulation:** Carefully save next before changing pointers
4. **Return value:** Return prev, not current (current is null at end)

---

## Step-by-Step Example

For `1 → 2 → 3 → null`:

```
Initial: prev=null, current=1→2→3→null

Step 1: next=2, 1→null, prev=1, current=2→3→null
Step 2: next=3, 2→1→null, prev=2, current=3→null
Step 3: next=null, 3→2→1→null, prev=3, current=null

Return prev = 3→2→1→null
```

---

## Edge Cases

- Empty list: `null` → `null`
- Single node: `[1]` → `[1]`
- Two nodes: `[1,2]` → `[2,1]`

---

## Related Problems
- [[Reverse-Linked-List-II]] - Reverse portion of list
- [[Palindrome-Linked-List]] - Uses reversal
- [[Reorder-List]] - Uses reversal technique

---

## Tags
#linked-lists #two-pointers #recursion #easy #blind75

---

## Visualization

- Embed: `![](../assets/reverse-linked-list/step-1.svg)`
- Obsidian embed: `![[../assets/reverse-linked-list/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="720" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="28" fill="#222">Linked list reversal (iterative steps)</text>
    <g transform="translate(20,50)">
        <rect x="0" y="0" width="48" height="24" fill="#fff" stroke="#4b6cc1"/>
        <text x="24" y="16" text-anchor="middle">1</text>
        <rect x="60" y="0" width="48" height="24" fill="#fff" stroke="#4b6cc1"/>
        <text x="84" y="16" text-anchor="middle">2</text>
        <rect x="120" y="0" width="48" height="24" fill="#fff" stroke="#4b6cc1"/>
        <text x="144" y="16" text-anchor="middle">3</text>
    </g>
</svg>
