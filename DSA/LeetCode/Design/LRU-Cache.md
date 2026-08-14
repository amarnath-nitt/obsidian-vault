# LRU Cache

**LeetCode Problem:** [146. LRU Cache](https://leetcode.com/problems/lru-cache/)  
**Difficulty:** Medium  
**Topic:** Design, Hash Table, Linked List, Doubly-Linked List

---

## Problem Statement

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.
- `int get(int key)` Return the value of the key if the key exists, otherwise return -1.
- `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions `get` and `put` must each run in **O(1)** average time complexity.

---

## Examples

### Example 1:
```
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

---

## Approach

### Key Insights:
1. **O(1) Get and Put**: We need fast lookup (HashMap) and fast removal/insertion (Doubly Linked List)
2. **HashMap + Doubly Linked List**: 
   - HashMap: stores key -> node mapping for O(1) lookup
   - Doubly Linked List: maintains order of usage (most recent at head, least recent at tail)
3. **Node Structure**: Each node contains key, value, prev, and next pointers
4. **Dummy Nodes**: Use dummy head and tail to simplify edge cases

### Algorithm:
1. **get(key)**:
   - If key exists in HashMap, move the node to head (most recently used)
   - Return the value
   - If key doesn't exist, return -1

2. **put(key, value)**:
   - If key exists, update value and move to head
   - If key doesn't exist:
     - Create new node and add to head
     - Add to HashMap
     - If cache exceeds capacity, remove tail node (LRU) and remove from HashMap

### Data Structure:
- **HashMap<Integer, Node>**: Maps key to its node in the doubly linked list
- **Doubly Linked List**: Maintains access order with dummy head and tail

---

## Java Implementation

```java
class LRUCache {
    // Node class for doubly linked list
    class Node {
        int key;
        int value;
        Node prev;
        Node next;
        
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private HashMap<Integer, Node> cache;
    private int capacity;
    private Node head; // Dummy head (most recently used)
    private Node tail; // Dummy tail (least recently used)
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        
        // Initialize dummy head and tail
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        
        Node node = cache.get(key);
        // Move to head (most recently used)
        moveToHead(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            // Update existing key
            Node node = cache.get(key);
            node.value = value;
            moveToHead(node);
        } else {
            // Add new key
            Node newNode = new Node(key, value);
            cache.put(key, newNode);
            addToHead(newNode);
            
            // Check if capacity exceeded
            if (cache.size() > capacity) {
                // Remove LRU (tail node)
                Node lru = removeTail();
                cache.remove(lru.key);
            }
        }
    }
    
    // Helper method: Add node right after head
    private void addToHead(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
    
    // Helper method: Remove node from its current position
    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    // Helper method: Move node to head
    private void moveToHead(Node node) {
        removeNode(node);
        addToHead(node);
    }
    
    // Helper method: Remove and return tail node (LRU)
    private Node removeTail() {
        Node lru = tail.prev;
        removeNode(lru);
        return lru;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

---

## Complexity Analysis

### Time Complexity:
- **get(key)**: O(1)
  - HashMap lookup: O(1)
  - Move to head (remove + add): O(1)
  
- **put(key, value)**: O(1)
  - HashMap lookup/insert: O(1)
  - Add to head or move to head: O(1)
  - Remove tail: O(1)

### Space Complexity:
- **O(capacity)**: HashMap stores at most `capacity` entries, and doubly linked list has at most `capacity` nodes

---

## Key Points for Interviews

1. **Why HashMap + Doubly Linked List?**
   - HashMap provides O(1) lookup
   - Doubly Linked List allows O(1) insertion and deletion at both ends
   - Singly linked list won't work because we can't delete a node in O(1) without reference to previous node

2. **Why Dummy Head and Tail?**
   - Simplifies edge cases (empty list, single element)
   - No need to check for null when adding/removing nodes

3. **Key Operations:**
   - `addToHead()`: Add node right after dummy head (most recent)
   - `removeNode()`: Remove node from current position
   - `moveToHead()`: Remove + add to head (mark as recently used)
   - `removeTail()`: Remove LRU element before dummy tail

4. **Common Mistakes:**
   - Forgetting to update both HashMap and linked list
   - Not moving accessed nodes to head in `get()`
   - Not handling capacity overflow correctly
   - Using singly linked list (can't achieve O(1) deletion)

5. **Follow-up Questions:**
   - What if we need LFU (Least Frequently Used) instead?
   - How would you make this thread-safe?
   - How would you implement TTL (Time To Live)?

---

## Related Problems

- [[Min-Stack|155. Min Stack]]
- [460. LFU Cache](https://leetcode.com/problems/lfu-cache/)
- [Design HashMap](https://leetcode.com/problems/design-hashmap/)

---

## Tags

`#design` `#hash-table` `#linked-list` `#doubly-linked-list` `#lru-cache` `#medium`
