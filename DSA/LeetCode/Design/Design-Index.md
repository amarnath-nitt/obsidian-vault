# LeetCode Design Problems - Index

A curated collection of essential LeetCode design problems for technical interview preparation. Each problem includes detailed implementations in Java with multiple approaches, complexity analysis, and interview tips.

---

## 🎯 Difficulty Roadmap

### 🟢 Easy

- [x] **706** · [[Design-HashMap|Design HashMap]] — Hash function, collision handling, resizing

### 🟡 Medium

- [x] **155** · [[Min-Stack|Min Stack]] — Auxiliary stack, constant-time min
- [x] **208** · [[Implement-Trie|Implement Trie]] — Prefix tree, node representation
- [x] **211** · [[Add-and-Search-Words|Add and Search Words]] — Trie + DFS wildcard matching
- [x] **380** · [[Insert-Delete-GetRandom-O1|Insert Delete GetRandom O(1)]] — HashMap + ArrayList, swap-remove
- [x] **379** · [[Design-Phone-Directory|Design Phone Directory]] — Queue + HashSet / BitSet
- [x] **981** · [[Time-Based-Key-Value-Store|Time Based Key-Value Store]] — Timestamp indexing, binary search
- [x] **1472** · [[Design-Browser-History|Design Browser History]] — Two stacks, list pointer, history truncation
- [x] **355** · [[Design-Twitter|Design Twitter]] — Heap, k-way merge, social graph

### 🔴 Hard

- [x] **146** · [[LRU-Cache|LRU Cache]] — HashMap + doubly linked list
- [x] **460** · [[LFU-Cache|LFU Cache]] — Frequency buckets, LRU tie-break

### Recommended Order

1. Design HashMap
2. Min Stack
3. Implement Trie
4. Add and Search Words
5. Insert Delete GetRandom O(1)
6. Time Based Key-Value Store
7. Design Browser History
8. LRU Cache
9. LFU Cache
10. Design Twitter

---

## Cache Design Problems

Master cache eviction policies and understand the differences between LRU and LFU.

| # | Problem | Difficulty | Key Concepts |
|---|---------|------------|-------------|
| 146 | [[LRU-Cache\|LRU Cache]] | Medium | HashMap + Doubly Linked List, O(1) operations |
| 460 | [[LFU-Cache\|LFU Cache]] | Hard | HashMap + LinkedHashSet, Frequency tracking |

---

## Stack & Queue Design

Fundamental stack and queue variations.

| # | Problem | Difficulty | Key Concepts |
|---|---------|------------|-------------|
| 155 | [[Min-Stack\|Min Stack]] | Medium | Two stacks, Constant time getMin |
| 1472 | [[Design-Browser-History\|Design Browser History]] | Medium | Stacks vs Doubly Linked List vs Array |

---

## Core Data Structure Design

Fundamental data structures every engineer should know how to implement from scratch.

| # | Problem | Difficulty | Key Concepts |
|---|---------|------------|-------------|
| 208 | [[Implement-Trie\|Implement Trie]] | Medium | Prefix tree, Array vs HashMap approaches |
| 706 | [[Design-HashMap\|Design HashMap]] | Easy | Hash function, Collision resolution, Chaining |
| 211 | [[Add-and-Search-Words\|Add and Search Words]] | Medium | Trie + DFS, Wildcard matching, Backtracking |
| 380 | [[Insert-Delete-GetRandom-O1\|Insert Delete GetRandom O(1)]] | Medium | HashMap + ArrayList, Swap-remove technique |
| 379 | [[Design-Phone-Directory\|Design Phone Directory]] | Medium | Queue + HashSet vs BitSet, Lazy Loading |

---

## Advanced System Design

Real-world system design problems that test your ability to combine multiple data structures.

| # | Problem | Difficulty | Key Concepts |
|---|---------|------------|-------------|
| 981 | [[Time-Based-Key-Value-Store\|Time Based Key-Value Store]] | Medium | Binary search, Timestamp indexing, TreeMap |
| 355 | [[Design-Twitter\|Design Twitter]] | Medium | Max heap, K-way merge, Social graph |

---

## Key Concepts by Category

### Cache Systems
- **LRU (Least Recently Used)**: Evicts least recently accessed item
  - HashMap for O(1) lookup
  - Doubly linked list for O(1) insertion/deletion
  - Move accessed items to head
  
- **LFU (Least Frequently Used)**: Evicts least frequently accessed item
  - Three HashMaps: key→value, key→frequency, frequency→keys
  - LinkedHashSet for LRU tie-breaking
  - Track minimum frequency

### Array & HashMap Tricks
- **O(1) Remove from Array**: Swap element with last element, then pop back.
- **Random Access**: Use ArrayList for O(1) by index access (needed for `getRandom`).
- **Pool Management**: Use Queue to store available items, HashSet/BitSet to track usage (Phone Directory).

### Trie (Prefix Tree)
- Efficient prefix-based operations
- O(m) search where m is word length
- Applications: autocomplete, spell check, dictionary
- Array-based (faster) vs HashMap-based (flexible)

### Hash Table Design
- **Hash Function**: Distribute keys uniformly
- **Collision Resolution**:
  - Separate chaining (linked list at each bucket)
  - Open addressing (linear probing, quadratic probing)
- **Load Factor**: Keep α < 0.75 for good performance
- **Dynamic Resizing**: Double capacity when threshold exceeded

### Time-Series Data
- Store multiple values per key with timestamps
- Binary search for closest timestamp
- TreeMap.floorEntry() for O(log n) lookup
- Applications: versioning, audit logs, snapshots

---

## Interview Strategy

### 1. Clarify Requirements
- Input constraints (key/value types, size limits)
- Expected operations and their frequencies
- Time/space complexity requirements
- Edge cases to handle

### 2. Choose Right Data Structures
- Quick lookup → HashMap
- Ordered data → TreeMap, sorted list
- Fast insertion/deletion at ends → Doubly linked list
- Prefix operations → Trie
- Top K elements → Heap
- Random access → ArrayList
- Availability Pool → Queue + BitSet

### 3. Common Patterns
- **HashMap + LinkedList/Set**: LRU, LFU caches
- **HashMap + TreeMap**: Time-based storage
- **Trie + DFS**: Wildcard search
- **Heap + HashMap**: Priority-based systems
- **HashMap + ArrayList**: O(1) Randomized Set
- **BitSet + Queue**: Resource Pools

### 4. Optimization Tips
- Use dummy nodes to simplify edge cases
- Consider load factor for hash tables
- Use primitive types to save memory
- Profile before optimizing
- Use BitSets for dense integer ranges

---

## Complexity Cheat Sheet

| Data Structure | Access | Search | Insert | Delete | Space |
|----------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| HashMap | O(1)* | O(1)* | O(1)* | O(1)* | O(n) |
| TreeMap | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Doubly Linked List | O(n) | O(n) | O(1)** | O(1)** | O(n) |
| Trie | O(m) | O(m) | O(m) | O(m) | O(ALPHABET × m × n) |
| Heap | O(1)† | O(n) | O(log n) | O(log n) | O(n) |
| BitSet | O(1) | O(1) | O(1) | O(1) | O(n/8) |

\* Average case, O(n) worst case  
\*\* With reference to node  
† Only peek/top operation

---

## Common Mistakes to Avoid

1. **LRU Cache**
   - Using singly linked list (can't delete in O(1))
   - Not moving accessed nodes to head
   - Forgetting dummy head/tail nodes

2. **LFU Cache**
   - Using HashSet instead of LinkedHashSet (loses LRU order)
   - Not updating minFreq when frequency bucket empties
   - Not resetting minFreq to 1 for new keys

3. **Trie**
   - Forgetting to mark end of word
   - Wrong index calculation (ch - 'a')
   - Not checking null before recursing

4. **HashMap**
   - Not handling collisions properly
   - Using val < current instead of val <= current
   - Forgetting to update existing keys

5. **Time-Based Storage**
   - Wrong binary search variant (need largest <=, not exact)
   - Not checking if key exists
   - Using min heap instead of binary search

6. **O(1) Remove**
   - Forgetting to update the index in map after swapping
   - Not handling removal of last element correctly (edge case)

---

## Study Tips

1. **Start with Core Data Structures**
   - Implement Trie and HashMap first
   - Understand hash collisions deeply
   - Master binary search variations

2. **Progress to Cache Problems**
   - LRU before LFU
   - Understand eviction policies
   - Practice with different capacities

3. **Tackle System Design Last**
   - Combine multiple data structures
   - Think about scalability
   - Consider real-world constraints

4. **Practice Implementation**
   - Code from scratch without IDE
   - Write test cases
   - Analyze time/space complexity

5. **Review Regularly**
   - Re-implement after 1 week
   - Compare different approaches
   - Optimize based on constraints

---

## Related Topics

- **Graph Algorithms**: For social network features
- **String Matching**: For search and autocomplete
- **Priority Queues**: For ranking and recommendations
- **Database Indexing**: Similar to Trie structures

---

## Resources

- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Designing Data-Intensive Applications](https://dataintensive.net/)
- Java Collections Framework documentation

---

## 🔗 Related Notes

- [[../00 - Index|LeetCode Master Index]]
- [[../Blind75/Top-75-Index|Top 75 Index]]
- [[../../Patterns/00 - Index|Patterns Index]]

---

*Last Updated: October 2, 2026*
