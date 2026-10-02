# Merge K Sorted Lists

**LeetCode 23** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/merge-k-sorted-lists/)

### Problem
Merge k sorted linked lists into one sorted list.

### Approach (Min-Heap)

- Add first node of each list to a min-heap
- Poll the minimum, add to result, push next node from that list

### Java Solution

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> heap = new PriorityQueue<>((a, b) -> a.val - b.val);

        for (ListNode node : lists)
            if (node != null) heap.offer(node);

        ListNode dummy = new ListNode(0), curr = dummy;
        while (!heap.isEmpty()) {
            ListNode node = heap.poll();
            curr.next = node;
            curr = curr.next;
            if (node.next != null) heap.offer(node.next);
        }
        return dummy.next;
    }
}
```

**Complexity:** Time O(N log k) where N = total nodes · Space O(k)

---
