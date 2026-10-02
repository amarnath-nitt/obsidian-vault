# LRU Cache

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
