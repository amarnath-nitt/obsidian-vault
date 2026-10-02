# Merge K Sorted Lists

**Difficulty:** Hard
**Category:** Linked Lists / Heap
**LeetCode Link:** [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## Problem Statement

Given an array of `k` sorted linked lists, merge them all into one sorted linked list and return it.

**Example:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

---

## Intuition

At each step we need the smallest element among the current heads of all k lists. A min heap gives us O(log k) access to the minimum — much better than scanning all k heads each time (O(k)).

---

## Approach 1: Min Heap (Optimal)

### Algorithm
1. Add the first node of each list to a min heap
2. Poll the minimum node, add to result
3. If that node has a next, push it to the heap
4. Repeat until heap is empty

### Java Code
```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);

        for (ListNode list : lists) {
            if (list != null) minHeap.offer(list);
        }

        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (!minHeap.isEmpty()) {
            ListNode node = minHeap.poll();
            current.next = node;
            current = current.next;

            if (node.next != null) minHeap.offer(node.next);
        }

        return dummy.next;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(N log k) — N total nodes, each heap operation is O(log k)
- **Space Complexity:** O(k) — heap holds at most k nodes

---

## Approach 2: Divide and Conquer

### Algorithm
Repeatedly merge pairs of lists. Each round halves the number of lists. Total rounds = log k.

### Java Code
```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        int interval = 1;

        while (interval < lists.length) {
            for (int i = 0; i + interval < lists.length; i += interval * 2) {
                lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }

        return lists[0];
    }

    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) { curr.next = l1; l1 = l1.next; }
            else { curr.next = l2; l2 = l2.next; }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(N log k)
- **Space Complexity:** O(1) — in-place merging

---

## Key Takeaways

1. **Min heap:** Always gives the global minimum in O(log k) — ideal for k-way merge
2. **Divide and conquer:** Avoids heap overhead; same time complexity
3. **Both are O(N log k):** Heap is simpler to code; D&C is more space efficient

---

## Tags
#linked-lists #heap #divide-and-conquer #hard #blind75
