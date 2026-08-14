# Design HashMap

**LeetCode Problem:** [706. Design HashMap](https://leetcode.com/problems/design-hashmap/)  
**Difficulty:** Easy  
**Topic:** Design, Array, Hash Table, Linked List

---

## Problem Statement

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

- `MyHashMap()` initializes the object with an empty map.
- `void put(int key, int value)` inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
- `int get(int key)` returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- `void remove(key)` removes the key and its corresponding value if the map contains the mapping for the key.

---

## Examples

### Example 1:
```
Input:
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output:
[null, null, null, 1, -1, null, 1, null, -1]

Explanation:
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1
myHashMap.get(3);    // return -1 (not found)
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (update existing)
myHashMap.get(2);    // return 1
myHashMap.remove(2); // remove the mapping for 2, map is now [[1,1]]
myHashMap.get(2);    // return -1 (not found)
```

---

## Approach 1: Array (Simple but Memory Inefficient)

### Key Insights:
- Use array of size based on key range
- Direct indexing: array[key] = value
- Works only for small key ranges

```java
class MyHashMap {
    private int[] map;
    
    public MyHashMap() {
        map = new int[1000001]; // Constraint: 0 <= key <= 10^6
        Arrays.fill(map, -1);
    }
    
    public void put(int key, int value) {
        map[key] = value;
    }
    
    public int get(int key) {
        return map[key];
    }
    
    public void remove(int key) {
        map[key] = -1;
    }
}
```

**Complexity**: 
- Time: O(1) for all operations
- Space: O(keyRange) - wasteful!

---

## Approach 2: Hash Table with Separate Chaining (Recommended)

### Key Insights:
1. **Hash Function**: `key % size` to map key to bucket
2. **Collision Handling**: Use LinkedList at each bucket (separate chaining)
3. **Load Factor**: Keep reasonable number of buckets to minimize collisions

### Algorithm:
- **put**: Hash key to find bucket, update if exists, else add to list
- **get**: Hash key, search in bucket's linked list
- **remove**: Hash key, remove from bucket's linked list

---

## Java Implementation - Approach 2 (Separate Chaining)

```java
class MyHashMap {
    // Node class for linked list
    class Node {
        int key;
        int value;
        Node next;
        
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private static final int SIZE = 10000; // Number of buckets
    private Node[] buckets;
    
    public MyHashMap() {
        buckets = new Node[SIZE];
    }
    
    // Hash function
    private int hash(int key) {
        return key % SIZE;
    }
    
    public void put(int key, int value) {
        int index = hash(key);
        
        if (buckets[index] == null) {
            // Empty bucket, create new node
            buckets[index] = new Node(key, value);
            return;
        }
        
        // Search in the bucket's linked list
        Node current = buckets[index];
        Node prev = null;
        
        while (current != null) {
            if (current.key == key) {
                // Key exists, update value
                current.value = value;
                return;
            }
            prev = current;
            current = current.next;
        }
        
        // Key doesn't exist, add to end of list
        prev.next = new Node(key, value);
    }
    
    public int get(int key) {
        int index = hash(key);
        Node current = buckets[index];
        
        while (current != null) {
            if (current.key == key) {
                return current.value;
            }
            current = current.next;
        }
        
        return -1; // Not found
    }
    
    public void remove(int key) {
        int index = hash(key);
        Node current = buckets[index];
        Node prev = null;
        
        while (current != null) {
            if (current.key == key) {
                // Found the key, remove it
                if (prev == null) {
                    // Remove head of list
                    buckets[index] = current.next;
                } else {
                    prev.next = current.next;
                }
                return;
            }
            prev = current;
            current = current.next;
        }
    }
}
```

---

## Approach 3: Open Addressing with Linear Probing

### Key Insights:
- No linked lists, all entries in array
- On collision, probe next slot: `(hash + i) % size`
- Need to handle deleted entries (use tombstone)

```java
class MyHashMap {
    private static final int SIZE = 10000;
    private static final int EMPTY = -1;
    private static final int DELETED = -2;
    
    private int[] keys;
    private int[] values;
    
    public MyHashMap() {
        keys = new int[SIZE];
        values = new int[SIZE];
        Arrays.fill(keys, EMPTY);
    }
    
    private int hash(int key) {
        return key % SIZE;
    }
    
    public void put(int key, int value) {
        int index = hash(key);
        
        // Linear probing
        while (keys[index] != EMPTY && keys[index] != DELETED && keys[index] != key) {
            index = (index + 1) % SIZE;
        }
        
        keys[index] = key;
        values[index] = value;
    }
    
    public int get(int key) {
        int index = hash(key);
        
        while (keys[index] != EMPTY) {
            if (keys[index] == key) {
                return values[index];
            }
            index = (index + 1) % SIZE;
        }
        
        return -1;
    }
    
    public void remove(int key) {
        int index = hash(key);
        
        while (keys[index] != EMPTY) {
            if (keys[index] == key) {
                keys[index] = DELETED; // Use tombstone
                values[index] = EMPTY;
                return;
            }
            index = (index + 1) % SIZE;
        }
    }
}
```

---

## Complexity Analysis

### Approach 2 (Separate Chaining):
- **Time Complexity**: 
  - Average: O(1) for all operations
  - Worst: O(n) if all keys hash to same bucket
  
- **Space Complexity**: O(n + m)
  - n = number of entries
  - m = number of buckets

### Approach 3 (Linear Probing):
- **Time Complexity**: 
  - Average: O(1) with good load factor
  - Worst: O(n) with clustering
  
- **Space Complexity**: O(m) where m is table size

---

## Comparison of Approaches

| Approach | Pros | Cons | Best Use |
|----------|------|------|----------|
| **Array** | O(1) guaranteed, simple | Huge space waste | Small key range |
| **Separate Chaining** | Easy to implement, handles collisions well | Extra space for pointers | General purpose |
| **Open Addressing** | Cache-friendly, no pointers | Clustering issues, needs tombstones | Memory-constrained |

---

## Key Points for Interviews

1. **Hash Function Choice:**
   - Simple: `key % size`
   - Better: Consider prime numbers for size
   - Best: Use good hash functions (MurmurHash, etc.)

2. **Collision Resolution:**
   - **Separate Chaining**: LinkedList at each bucket
   - **Open Addressing**: Linear probing, quadratic probing, double hashing

3. **Load Factor:**
   - α = n/m (entries / buckets)
   - Keep α < 0.75 for good performance
   - Resize/rehash when load factor too high

4. **Common Mistakes:**
   - Forgetting to update existing keys in put()
   - Not handling empty buckets in get()
   - Off-by-one errors in probing
   - Memory leaks (not clearing removed nodes)

5. **Follow-up Questions:**
   - How would you implement dynamic resizing?
   - What happens with high load factor?
   - How to make it thread-safe?
   - What's the difference between HashMap and HashTable?

6. **Real-World Considerations:**
   - Java's HashMap uses separate chaining with tree-based bins (when chain > 8)
   - Starting capacity: 16, load factor: 0.75
   - Rehashing: doubles size when threshold exceeded

---

## Advanced: With Dynamic Resizing

```java
class MyHashMapWithResize {
    class Node {
        int key, value;
        Node next;
        Node(int k, int v) { key = k; value = v; }
    }
    
    private static final double LOAD_FACTOR = 0.75;
    private int size = 0;
    private int capacity = 1000;
    private Node[] buckets;
    
    public MyHashMapWithResize() {
        buckets = new Node[capacity];
    }
    
    private int hash(int key) {
        return Integer.hashCode(key) % capacity;
    }
    
    public void put(int key, int value) {
        int index = hash(key);
        
        if (buckets[index] == null) {
            buckets[index] = new Node(key, value);
            size++;
        } else {
            Node curr = buckets[index], prev = null;
            while (curr != null) {
                if (curr.key == key) {
                    curr.value = value;
                    return;
                }
                prev = curr;
                curr = curr.next;
            }
            prev.next = new Node(key, value);
            size++;
        }
        
        // Check load factor and resize if needed
        if ((double) size / capacity >= LOAD_FACTOR) {
            resize();
        }
    }
    
    private void resize() {
        capacity *= 2;
        Node[] oldBuckets = buckets;
        buckets = new Node[capacity];
        size = 0;
        
        // Rehash all entries
        for (Node head : oldBuckets) {
            Node curr = head;
            while (curr != null) {
                put(curr.key, curr.value);
                curr = curr.next;
            }
        }
    }
    
    public int get(int key) {
        int index = hash(key);
        Node curr = buckets[index];
        while (curr != null) {
            if (curr.key == key) return curr.value;
            curr = curr.next;
        }
        return -1;
    }
    
    public void remove(int key) {
        int index = hash(key);
        Node curr = buckets[index], prev = null;
        
        while (curr != null) {
            if (curr.key == key) {
                if (prev == null) buckets[index] = curr.next;
                else prev.next = curr.next;
                size--;
                return;
            }
            prev = curr;
            curr = curr.next;
        }
    }
}
```

---

## Related Problems

- [705. Design HashSet](https://leetcode.com/problems/design-hashset/)
- [[LRU-Cache|146. LRU Cache]]
- [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

---

## Tags

`#design` `#hash-table` `#array` `#linked-list` `#easy` `#collision-resolution`
