# Day 14 — Stack & Queue II

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Stack & Queue — Advanced Problems
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#LRU Cache]] | 146 | Medium | ⬜ |
| 2 | [[#Sliding Window Maximum]] | 239 | Hard | ⬜ |
| 3 | [[#Daily Temperatures]] | 739 | Medium | ⬜ |
| 4 | [[#Celebrity Problem]] | — | Medium | ⬜ |
| 5 | [[#Stock Span Problem]] | 901 | Medium | ⬜ |
| 6 | [[#Rotten Oranges (BFS + Queue)]] | 994 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| LRU Cache | Store entries in a list and scan on get/put. O(n). | Use LinkedHashMap. O(1) average. | HashMap plus doubly linked list for explicit O(1) get/put. |
| Sliding Window Maximum | Compute max for every window. O(n*k). | Max-heap with lazy removal. O(n log k). | Monotonic deque of indexes. O(n). |
| Daily Temperatures | For each day, scan forward for warmer day. O(n^2). | Jump using previously computed answers. O(n) typical. | Monotonic decreasing stack of indexes. O(n). |
| Celebrity Problem | Check every candidate against everyone. O(n^2). | Stack elimination. O(n). | Two-pointer/candidate elimination plus verification. O(n), O(1). |
| Stock Span Problem | For each price, scan backward while prices are smaller. O(n^2). | Store previous greater index jumps. | Monotonic stack of price/index pairs. O(n). |
| Rotten Oranges | Scan the whole grid minute by minute. O((m*n)^2). | BFS from rotten oranges individually. | Multi-source BFS from all rotten oranges. O(m*n). |

---

## LRU Cache

**LeetCode 146** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/lru-cache/)

### Problem
Design a Least Recently Used (LRU) cache with `get` and `put` in O(1).

### Approach (HashMap + Doubly Linked List)

- **HashMap:** `key → node` for O(1) lookup
- **DLL:** maintains order (most recent at head, least recent at tail)
- On `get` or `put`: move accessed node to head
- On capacity overflow: remove tail node

### Java Solution

```java
class LRUCache {
    class Node {
        int key, val;
        Node prev, next;
        Node(int k, int v) { key = k; val = v; }
    }

    int capacity;
    Map<Integer, Node> map = new HashMap<>();
    Node head = new Node(0, 0); // dummy head (most recent)
    Node tail = new Node(0, 0); // dummy tail (least recent)

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void insertFront(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }

    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        Node node = map.get(key);
        remove(node);
        insertFront(node);
        return node.val;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) remove(map.get(key));
        Node node = new Node(key, value);
        insertFront(node);
        map.put(key, node);
        if (map.size() > capacity) {
            Node lru = tail.prev;
            remove(lru);
            map.remove(lru.key);
        }
    }
}
```

**Complexity:** get/put O(1)

> **Java shortcut:** `LinkedHashMap` with `accessOrder=true` and override `removeEldestEntry`

---

## Sliding Window Maximum

**LeetCode 239** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/sliding-window-maximum/)

### Problem
Given array and window size k, find max in each window.

### Approach (Monotonic Deque)

- Maintain a **deque of indices** in decreasing order of values
- Remove indices outside the window from the front
- Remove smaller elements from the back (they can never be maximum)

### Java Solution

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> dq = new ArrayDeque<>(); // stores indices

        for (int i = 0; i < n; i++) {
            // Remove out-of-window indices
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1) dq.pollFirst();

            // Remove smaller elements from back
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) dq.pollLast();

            dq.offerLast(i);

            if (i >= k - 1) result[i - k + 1] = nums[dq.peekFirst()];
        }
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(k)

---

## Daily Temperatures

**LeetCode 739** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/daily-temperatures/)

### Problem
For each day, find how many days until a warmer temperature.

### Approach (Monotonic Decreasing Stack of indices)

- While current temp > stack top → that's the warmer day for stack top
- `result[idx] = i - idx`

### Java Solution

```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int idx = stack.pop();
                result[idx] = i - idx;
            }
            stack.push(i);
        }
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(n)

---

## Celebrity Problem

**Problem:** N people, a celebrity is known by all but knows nobody. Find the celebrity.

### Approach (Stack Elimination)

1. Push all people on stack
2. Pop two people `a, b`: if `a knows b` → a can't be celebrity (pop a, keep b); else b can't be
3. Last person on stack is the **candidate**
4. Verify: all others know candidate, candidate knows no one

### Java Solution

```java
// knows(a, b) returns true if a knows b (given as API)
public int findCelebrity(int n) {
    // Find candidate
    int candidate = 0;
    for (int i = 1; i < n; i++)
        if (knows(candidate, i)) candidate = i;

    // Verify candidate
    for (int i = 0; i < n; i++) {
        if (i == candidate) continue;
        if (knows(candidate, i) || !knows(i, candidate)) return -1;
    }
    return candidate;
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Stock Span Problem

**LeetCode 901** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/online-stock-span/)

### Problem
For each day's price, find the number of consecutive days (including today) where price ≤ today's price.

### Approach (Monotonic Stack)

- Stack stores `(price, span)` pairs
- When today's price ≥ stack top → absorb its span

### Java Solution

```java
class StockSpanner {
    Deque<int[]> stack = new ArrayDeque<>(); // [price, span]

    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            span += stack.pop()[1]; // absorb previous spans
        }
        stack.push(new int[]{price, span});
        return span;
    }
}
```

**Complexity:** Amortized O(1) per call

---

## Rotten Oranges (BFS + Queue)

**LeetCode 994** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/rotting-oranges/)

### Problem
Grid with fresh(1), rotten(2), empty(0) oranges. Each minute, rotten spreads to adjacent fresh. Find minimum minutes to rot all, or -1 if impossible.

### Approach (Multi-source BFS)

1. Add all initially rotten oranges to queue
2. BFS level by level (each level = 1 minute)
3. Count remaining fresh; if > 0 → return -1

### Java Solution

```java
class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) queue.offer(new int[]{i, j});
                if (grid[i][j] == 1) fresh++;
            }

        if (fresh == 0) return 0;

        int minutes = 0;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!queue.isEmpty()) {
            minutes++;
            for (int size = queue.size(); size > 0; size--) {
                int[] curr = queue.poll();
                for (int[] d : dirs) {
                    int r = curr[0] + d[0], c = curr[1] + d[1];
                    if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == 1) {
                        grid[r][c] = 2;
                        fresh--;
                        queue.offer(new int[]{r, c});
                    }
                }
            }
        }
        return fresh == 0 ? minutes - 1 : -1;
    }
}
```

**Complexity:** Time O(m×n) · Space O(m×n)

---

## Key Design Patterns

| DS Design | Approach |
|-----------|----------|
| LRU Cache | HashMap + DLL |
| LFU Cache | HashMap + freq-bucketed DLL |
| Min Stack | Two stacks |
| Max Queue | Two stacks with max tracking |
| Sliding window max | Monotonic deque |

#sde-sheet #stack #queue #lru #day14
