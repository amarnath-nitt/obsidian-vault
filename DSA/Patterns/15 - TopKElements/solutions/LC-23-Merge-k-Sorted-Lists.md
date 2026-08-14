# Merge k Sorted Lists (LC 23)

**Difficulty**: Hard  
**Pattern**: Top K Elements / Merge  
**LeetCode**: https://leetcode.com/problems/merge-k-sorted-lists/

## Problem Statement
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

**Example:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

## Approach 1: Min-Heap (Priority Queue)

### Intuition
Is equivalent to finding the minimum among `k` heads at each step.
Use a Min-Heap to keep track of the current head of each list.
1. Push head of every list into heap.
2. While heap not empty:
   - Pop min node, attach to result.
   - If popped node has next, push next into heap.

### Java Code
```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        
        for (ListNode node : lists) {
            if (node != null) pq.offer(node);
        }
        
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        
        while (!pq.isEmpty()) {
            ListNode node = pq.poll();
            tail.next = node;
            tail = node;
            
            if (node.next != null) {
                pq.offer(node.next);
            }
        }
        
        return dummy.next;
    }
}
```

### Complexity
- **Time**: O(N log k) where N is total nodes, k is number of lists.
- **Space**: O(k) for heap.

## Approach 2: Divide and Conquer

### Intuition
Pair up lists and merge them. Repeat until 1 list remains.
Merge(l1, l2), Merge(l3, l4) ...
Reduces problem size by half each step.

### Key Takeaways
- Classic Heap application
- Similar to "Merge Sorted Array" but for k arrays
- O(N log k) is optimal comparison-based sort for this structure
