# LFU Cache

**LeetCode Problem:** [460. LFU Cache](https://leetcode.com/problems/lfu-cache/)  
**Difficulty:** Hard  
**Topic:** Design, Hash Table, Linked List, Doubly-Linked List

---

## Problem Statement

Design and implement a data structure for a **Least Frequently Used (LFU)** cache.

Implement the `LFUCache` class:

- `LFUCache(int capacity)` Initializes the object with the capacity of the data structure.
- `int get(int key)` Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- `void put(int key, int value)` Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** key would be invalidated.

To determine the least frequently used key, a **use counter** is maintained for each key in the cache. The key with the smallest **use counter** is the least frequently used key.

When a key is first inserted into the cache, its **use counter** is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions `get` and `put` must each run in **O(1)** average time complexity.

---

## Examples

### Example 1:
```
Input:
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation:
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1, cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3, cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3, cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4, cache=[4,3], cnt(4)=2, cnt(3)=3
```

---

## Approach

### Key Insights:
1. **Three Hash Maps Required**:
   - `keyToVal`: Maps key -> value
   - `keyToFreq`: Maps key -> frequency count
   - `freqToKeys`: Maps frequency -> LinkedHashSet of keys with that frequency
   
2. **LinkedHashSet for LRU within Same Frequency**:
   - Maintains insertion order
   - When frequency is same, first inserted is LRU

3. **Track Minimum Frequency**: 
   - `minFreq` variable to quickly find which frequency bucket to evict from

### Algorithm:

**get(key)**:
1. If key doesn't exist, return -1
2. Get value, increment frequency
3. Update all hash maps
4. Return value

**put(key, value)**:
1. If key exists:
   - Update value
   - Increment frequency (same as get)
2. If key doesn't exist:
   - Check capacity
   - If full, evict LFU key (use minFreq to find bucket, remove first from LinkedHashSet)
   - Insert new key with frequency 1
   - Set minFreq = 1

---

## Java Implementation

```java
class LFUCache {
    // Node class to store key-value-frequency
    class Node {
        int key;
        int val;
        int freq;
        
        Node(int key, int val) {
            this.key = key;
            this.val = val;
            this.freq = 1;
        }
    }
    
    private int capacity;
    private int minFreq;
    private HashMap<Integer, Node> keyToNode;
    private HashMap<Integer, LinkedHashSet<Integer>> freqToKeys;
    
    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minFreq = 0;
        this.keyToNode = new HashMap<>();
        this.freqToKeys = new HashMap<>();
    }
    
    public int get(int key) {
        if (!keyToNode.containsKey(key)) {
            return -1;
        }
        
        Node node = keyToNode.get(key);
        updateFreq(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if (capacity == 0) return;
        
        if (keyToNode.containsKey(key)) {
            // Update existing key
            Node node = keyToNode.get(key);
            node.val = value;
            updateFreq(node);
        } else {
            // Add new key
            if (keyToNode.size() >= capacity) {
                // Evict LFU (and LRU if tie)
                evict();
            }
            
            // Insert new node
            Node newNode = new Node(key, value);
            keyToNode.put(key, newNode);
            freqToKeys.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
            minFreq = 1;
        }
    }
    
    // Helper: Update frequency when key is accessed
    private void updateFreq(Node node) {
        int key = node.key;
        int oldFreq = node.freq;
        
        // Remove from old frequency bucket
        freqToKeys.get(oldFreq).remove(key);
        
        // If this was the only key with minFreq, increment minFreq
        if (oldFreq == minFreq && freqToKeys.get(oldFreq).isEmpty()) {
            minFreq++;
        }
        
        // Increment frequency and add to new bucket
        node.freq++;
        freqToKeys.computeIfAbsent(node.freq, k -> new LinkedHashSet<>()).add(key);
    }
    
    // Helper: Evict least frequently used (and LRU if tie)
    private void evict() {
        // Get the LRU key from minFreq bucket
        LinkedHashSet<Integer> keys = freqToKeys.get(minFreq);
        int keyToEvict = keys.iterator().next(); // First key (LRU)
        
        // Remove from all data structures
        keys.remove(keyToEvict);
        keyToNode.remove(keyToEvict);
    }
}
```

---

## Alternative Implementation (More Explicit)

```java
class LFUCache {
    private int capacity;
    private int minFreq;
    private HashMap<Integer, Integer> keyToVal;
    private HashMap<Integer, Integer> keyToFreq;
    private HashMap<Integer, LinkedHashSet<Integer>> freqToKeys;
    
    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minFreq = 0;
        this.keyToVal = new HashMap<>();
        this.keyToFreq = new HashMap<>();
        this.freqToKeys = new HashMap<>();
    }
    
    public int get(int key) {
        if (!keyToVal.containsKey(key)) {
            return -1;
        }
        
        // Increase frequency
        increaseFreq(key);
        return keyToVal.get(key);
    }
    
    public void put(int key, int value) {
        if (capacity <= 0) return;
        
        if (keyToVal.containsKey(key)) {
            // Update value
            keyToVal.put(key, value);
            increaseFreq(key);
            return;
        }
        
        // Check capacity
        if (keyToVal.size() >= capacity) {
            removeLFU();
        }
        
        // Add new key
        keyToVal.put(key, value);
        keyToFreq.put(key, 1);
        freqToKeys.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
        minFreq = 1;
    }
    
    private void increaseFreq(int key) {
        int freq = keyToFreq.get(key);
        
        // Remove from old frequency list
        freqToKeys.get(freq).remove(key);
        
        // Update minFreq if needed
        if (freq == minFreq && freqToKeys.get(freq).isEmpty()) {
            minFreq++;
        }
        
        // Add to new frequency list
        int newFreq = freq + 1;
        keyToFreq.put(key, newFreq);
        freqToKeys.computeIfAbsent(newFreq, k -> new LinkedHashSet<>()).add(key);
    }
    
    private void removeLFU() {
        // Get keys with minimum frequency
        LinkedHashSet<Integer> keys = freqToKeys.get(minFreq);
        
        // Remove the first key (LRU among same frequency)
        int keyToRemove = keys.iterator().next();
        keys.remove(keyToRemove);
        
        // Clean up if empty
        if (keys.isEmpty()) {
            freqToKeys.remove(minFreq);
        }
        
        // Remove from other maps
        keyToVal.remove(keyToRemove);
        keyToFreq.remove(keyToRemove);
    }
}
```

---

## Complexity Analysis

### Time Complexity:
- **get(key)**: O(1)
  - HashMap lookup: O(1)
  - Update frequency: O(1)
  
- **put(key, value)**: O(1)
  - HashMap operations: O(1)
  - Eviction (if needed): O(1)
  - LinkedHashSet add/remove: O(1)

### Space Complexity:
- **O(capacity)**: Three hash maps storing at most `capacity` entries

---

## Key Points for Interviews

1. **Why Three Hash Maps?**
   - `keyToVal` (or `keyToNode`): Quick value lookup
   - `keyToFreq`: Track frequency for each key
   - `freqToKeys`: Group keys by frequency, enables O(1) eviction

2. **Why LinkedHashSet?**
   - Maintains insertion order (for LRU tie-breaking)
   - O(1) add, remove, and iteration to get first element
   - Cannot use HashSet (no order), cannot use List (O(n) removal)

3. **Critical: minFreq Tracking**
   - Always points to lowest frequency bucket
   - Only increments when last key of that frequency is removed
   - Reset to 1 when new key is inserted

4. **Common Mistakes:**
   - Not handling LRU tie-breaking (must use LinkedHashSet, not HashSet)
   - Forgetting to update minFreq when frequency bucket becomes empty
   - Not resetting minFreq to 1 when inserting new key
   - Trying to use TreeMap (O(log n), not O(1))

5. **LFU vs LRU:**
   - LRU: Evicts least recently used
   - LFU: Evicts least frequently used (with LRU as tie-breaker)
   - LFU is more complex but better for access pattern-based caching

6. **Follow-up Questions:**
   - What if we want to support both LRU and LFU policies?
   - How would you handle time-to-live (TTL)?
   - Can you make this thread-safe?

---

## Visual Example

```
Initial: capacity=2
put(1,1): freq[1]={1}, minFreq=1
put(2,2): freq[1]={1,2}, minFreq=1
get(1):   freq[1]={2}, freq[2]={1}, minFreq=1
put(3,3): evict key=2 (minFreq=1, LRU in that bucket)
          freq[2]={1}, freq[1]={3}, minFreq=1
```

---

## Related Problems

- [[LRU-Cache|146. LRU Cache]]
- [[Min-Stack|155. Min Stack]]
- [Design HashMap](https://leetcode.com/problems/design-hashmap/)

---

## Tags

`#design` `#hash-table` `#linked-list` `#lfu-cache` `#hard` `#linked-hash-set`
