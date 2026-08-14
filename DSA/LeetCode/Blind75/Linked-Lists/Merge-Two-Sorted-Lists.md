# Merge Two Sorted Lists

**Difficulty:** Easy  
**Category:** Linked Lists  
**LeetCode Link:** [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Example 1:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**
```
Input: list1 = [], list2 = []
Output: []
```

**Constraints:**
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

---

## Intuition

Since both lists are sorted, we can merge them by comparing the smallest unmerged elements from each list.

---

## Approach 1: Iterative with Dummy Node

### Algorithm
1. Create a dummy node to simplify edge cases
2. Use a pointer to build the merged list
3. Compare heads of both lists, add smaller one
4. Move pointer in the list we took from
5. Append remaining nodes from non-empty list

### Java Code
```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }
        
        // Append remaining nodes
        current.next = (list1 != null) ? list1 : list2;
        
        return dummy.next;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n + m) - Visit all nodes once
- **Space Complexity:** O(1) - Only using pointers

---

## Approach 2: Recursive

### Algorithm
1. Base cases: if either list is null, return the other
2. Compare heads, choose smaller one
3. Recursively merge the rest
4. Return the chosen head

### Java Code
```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Base cases
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        
        // Choose smaller head and recursively merge rest
        if (list1.val <= list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(n + m) - Recursion stack

---

## Key Takeaways

1. **Pattern:** Dummy node simplifies linked list problems
2. **Two pointers:** Track current position in both lists
3. **Remaining nodes:** Don't forget to append leftover nodes
4. **Iterative preferred:** O(1) space vs O(n) space

---

## Tags
#linked-lists #two-pointers #recursion #easy #blind75
