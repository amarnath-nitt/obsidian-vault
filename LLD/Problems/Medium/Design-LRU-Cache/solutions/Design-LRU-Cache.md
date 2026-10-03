# Design LRU Cache (Medium)

**Difficulty:** Medium · **Patterns:** (Data structure)
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design a fixed-capacity LRU cache: O(1) `get`/`put`, evict least-recently-used past capacity.

**Functional**
- `get` returns value + refreshes recency; miss returns −1.
- `put` inserts/updates + refreshes; evicts LRU past capacity.

**Non-functional**
- O(1) both ops; thread-safe variant; eviction policy swappable.

### The failure, before

```java
// ❌ LinkedHashMap alone with manual scans, or a queue + map that desync —
// refresh-on-get forgotten, eviction scans O(n), concurrent puts corrupt the order.
public int get(int k) { return map.getOrDefault(k, -1); }  // recency never updated
```

### The Fix (after)

HashMap key → node plus sentinel-based doubly-linked list; every access splices to head.

```java
import java.util.*;
import java.util.concurrent.locks.ReentrantLock;

class LRUCache {
    class Node {
        int key, val; Node prev, next;
        Node(int k, int v) { key = k; val = v; }
    }
    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(-1, -1);   // sentinels: never null checks
    private final Node tail = new Node(-1, -1);
    private final ReentrantLock lock = new ReentrantLock();

    LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail; tail.prev = head;
    }
    private void detach(Node n) { n.prev.next = n.next; n.next.prev = n.prev; }
    private void attachHead(Node n) {
        n.next = head.next; n.prev = head;
        head.next.prev = n; head.next = n;
    }
    public int get(int key) {
        lock.lock();
        try {
            Node n = map.get(key);
            if (n == null) return -1;
            detach(n); attachHead(n);              // refresh recency
            return n.val;
        } finally { lock.unlock(); }
    }
    public void put(int key, int val) {
        lock.lock();
        try {
            Node n = map.get(key);
            if (n != null) { n.val = val; detach(n); attachHead(n); return; }
            n = new Node(key, val);
            map.put(key, n); attachHead(n);
            if (map.size() > capacity) {           // evict-after-insert: one place
                Node lru = tail.prev;
                detach(lru); map.remove(lru.key);  // key in node: map stays in sync
            }
        } finally { lock.unlock(); }
    }
}
```

**Usage**
```java
LRUCache c = new LRUCache(2);
c.put(1, 10); c.put(2, 20); c.get(1);  // 1 is now MRU
c.put(3, 30);                           // evicts 2
c.get(2);                               // -1 (miss)
```

### Design points
- **Key lives in the node** — tail eviction deletes from the map with no reverse lookup.
- **Sentinels remove branches** — detach/attach never null-check; splice bugs vanish.
- **Refresh on both paths** — get and put-update splice identically; one helper, no drift.
- **One lock, whole op** — get = lookup + splice is atomic; striped locks only if scale is demanded.

**Complexity:** get/put O(1) · Space O(capacity).

---
#lld #machine-coding #lru-cache #medium #practice
