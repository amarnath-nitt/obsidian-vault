# Merge K Sorted Lists

**Difficulty:** Hard  
**Category:** Linked Lists  
**LeetCode Link:** [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## Problem Statement

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Constraints:**
- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`

---

## Intuition

Use a min heap to efficiently find the smallest element among k lists.

---

## Approach: Min Heap

### Algorithm
1. Add first node of each list to min heap
2. Extract minimum, add to result
3. Add next node from that list to heap
4. Repeat until heap is empty

### Java Code
```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);
        
        // Add first node of each list
        for (ListNode list : lists) {
            if (list != null) {
                minHeap.offer(list);
            }
        }
        
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        while (!minHeap.isEmpty()) {
            ListNode node = minHeap.poll();
            current.next = node;
            current = current.next;
            
            if (node.next != null) {
                minHeap.offer(node.next);
            }
        }
        
        return dummy.next;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(N log k) where N = total nodes, k = number of lists
- **Space Complexity:** O(k) - Heap size

---

## Tags
#linked-lists #heap #divide-and-conquer #hard #blind75

---

## Visualization

- Embed: `![](../assets/merge-k-sorted-lists/step-1.svg)`
- Obsidian embed: `![[../assets/merge-k-sorted-lists/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="120">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="24" fill="#222">Min-heap merging k lists</text>
    <g transform="translate(20,40)">
        <circle cx="40" cy="16" r="12" fill="#fff" stroke="#4b6cc1"/>
        <text x="40" y="20" text-anchor="middle">1</text>
        <circle cx="100" cy="16" r="12" fill="#fff" stroke="#4b6cc1"/>
        <text x="100" y="20" text-anchor="middle">1</text>
        <circle cx="160" cy="16" r="12" fill="#fff" stroke="#4b6cc1"/>
        <text x="160" y="20" text-anchor="middle">2</text>
    </g>
</svg>
