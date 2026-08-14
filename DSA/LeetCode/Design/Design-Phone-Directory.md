# Design Phone Directory

**LeetCode Problem:** [379. Design Phone Directory](https://leetcode.com/problems/design-phone-directory/)  
**Difficulty:** Medium  
**Topic:** Design, Array, Hash Table, Linked List, Queue

---

## Problem Statement

Design a Phone Directory which supports the following operations:

1.  `get`: Provide a number which is not assigned to anyone.
2.  `check`: Check if a number is available or not.
3.  `release`: Recycle or release a number.

Implement the `PhoneDirectory` class:
-   `PhoneDirectory(int maxNumbers)` Initializes the phone directory with the number of available slots `maxNumbers`.
-   `int get()` Provides a number that is not assigned to anyone. Returns -1 if no number is available.
-   `bool check(int number)` Returns `true` if the number is available, and `false` otherwise.
-   `void release(int number)` Recycles or releases the number.

---

## Examples

### Example 1:
```
Input
["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
[[3], [], [], [2], [], [2], [2], [2]]

Output
[null, 0, 1, true, 2, false, null, true]

Explanation
PhoneDirectory directory = new PhoneDirectory(3);
directory.get();     // It can return any available phone number. Here we assume it returns 0.
directory.get();     // Assume it returns 1.
directory.check(2);  // The number 2 is available, so return true.
directory.get();     // It returns 2, the only number that is left.
directory.check(2);  // The number 2 is no longer available, so return false.
directory.release(2); // Release number 2 back to the pool.
directory.check(2);  // Number 2 is available again, return true.
```

---

## Approach 1: Queue + HashSet (Standard Pool Pattern)

### Key Insights:
1.  **Queue**: Efficiently provides the "next" available number in O(1).
2.  **HashSet**: Efficiently checks availability in O(1) and prevents duplicates in the Queue when releasing.
3.  **Initialization**: We can pre-fill the queue with all numbers `0` to `maxNumbers - 1`.

### Algorithm:
-   **Init**: Create a Queue and a HashSet. Add all numbers from `0` to `maxNumbers - 1` to both.
-   **get()**: Poll from Queue. Remove from HashSet.
-   **check(num)**: Return `set.contains(num)`.
-   **release(num)**: If `!set.contains(num)`, add to Queue and Set.

### Java Implementation

```java
class PhoneDirectory {
    private Set<Integer> available;
    private Queue<Integer> queue;
    private int max;

    public PhoneDirectory(int maxNumbers) {
        max = maxNumbers;
        available = new HashSet<>();
        queue = new LinkedList<>();
        
        // Pre-fill with all numbers
        for (int i = 0; i < maxNumbers; i++) {
            queue.offer(i);
            available.add(i);
        }
    }
    
    public int get() {
        if (queue.isEmpty()) {
            return -1;
        }
        
        int num = queue.poll();
        available.remove(num);
        return num;
    }
    
    public boolean check(int number) {
        if (number < 0 || number >= max) {
            return false;
        }
        return available.contains(number);
    }
    
    public void release(int number) {
        // Only release if it's currently used (not available)
        if (number >= 0 && number < max && !available.contains(number)) {
            available.add(number);
            queue.offer(number);
        }
    }
}
```

**Complexity**:
-   **Time**: O(N) for constructor, O(1) for all other operations.
-   **Space**: O(N) to store all numbers.

---

## Approach 2: BitSet (Space Optimized)

### Key Insights:
-   If `maxNumbers` is large, storing all Integers in a Set/Queue is heavy memory-wise.
-   A `BitSet` (or boolean array) uses 1 bit per number.
-   We still need a way to quickly find the *next* free number. We can iterate (slow) or use a Queue for *only recycled* numbers + a pointer for fresh numbers.

### Algorithm (BitSet + Lazy Load):
1.  `next`: Pointer to the next "fresh" number (never provided before).
2.  `recycled`: Queue of numbers that were released.
3.  `used`: BitSet marking numbers currently in use.

-   **get()**: 
    -   If `recycled` is not empty, pop one.
    -   Else if `next < maxNumbers`, return `next++`.
    -   Else return -1.
    -   Mark returned number as true in BitSet.
-   **check(num)**: Return `!bitset.get(num)`.
-   **release(num)**:
    -   If `bitset.get(num)` is true (it's used):
        -   Mark false in BitSet.
        -   Add to `recycled` queue.

### Java Implementation

```java
class PhoneDirectory {
    private BitSet used;
    private Queue<Integer> recycled;
    private int next;
    private int max;

    public PhoneDirectory(int maxNumbers) {
        max = maxNumbers;
        used = new BitSet(maxNumbers); // All false by default (available)
        recycled = new LinkedList<>();
        next = 0;
    }
    
    public int get() {
        if (!recycled.isEmpty()) {
            int num = recycled.poll();
            used.set(num);
            return num;
        }
        
        if (next < max) {
            int num = next;
            next++;
            used.set(num);
            return num;
        }
        
        return -1;
    }
    
    public boolean check(int number) {
        if (number < 0 || number >= max) {
            return false;
        }
        return !used.get(number);
    }
    
    public void release(int number) {
        if (number >= 0 && number < max && used.get(number)) {
            used.clear(number);
            recycled.offer(number);
        }
    }
}
```

**Complexity**:
-   **Time**: O(1) for all operations (Constructor is O(1) too!).
-   **Space**: O(N/8) for BitSet + O(K) for recycled numbers. Much lighter.

---

## Key Points for Interviews

1.  **Lazy Loading**: The second approach is better because it doesn't allocate O(N) memory/time upfront. It only tracks what's necessary.
2.  **Concurrency**: If accessed by multiple threads, which approach is better?
    -   Queue is not thread-safe. Use `ConcurrentLinkedQueue` and `atomic` operations or `synchronized` blocks.
3.  **Why HashSet vs BitSet?**
    -   HashSet<Integer> overhead is huge (Object header + Integer object + HashMap entry). 
    -   BitSet is extremely compact.
4.  **Edge Cases**:
    -   Releasing a number that is already free (already released).
    -   Requesting when pool is full.

---

## Related Problems

-   [Design Compressed String Iterator](https://leetcode.com/problems/design-compressed-string-iterator/)
-   [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

---

## Tags

`#design` `#queue` `#hash-set` `#bit-manipulation` `#medium`
