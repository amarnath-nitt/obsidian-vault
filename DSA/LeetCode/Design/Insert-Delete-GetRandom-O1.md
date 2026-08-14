# Insert Delete GetRandom O(1)

**LeetCode Problem:** [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)  
**Difficulty:** Medium  
**Topic:** Design, Array, Hash Table, Randomized

---

## Problem Statement

Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average O(1)** time complexity.

---

## Examples

### Example 1:
```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]

Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```

---

## Approach: HashMap + ArrayList

### Key Insights:
1.  **O(1) Insert/Remove**: HashMap allows O(1) checks and removal *by key*.
2.  **O(1) GetRandom**: ArrayList allows O(1) access *by index*.
3.  **Synchronization**: We need to keep both data structures in sync.
4.  **The Trick for O(1) Remove**:
    -   To remove from an ArrayList in O(1), we can't remove from the middle (which is O(N) due to shifting).
    -   Instead, **swap the element to be removed with the last element**, then remove the last element.
    -   Update the HashMap with the new index of the swapped element.

### Data Structures:
-   `ArrayList<Integer> nums`: Stores the actual values. Used for `getRandom`.
-   `HashMap<Integer, Integer> map`: Stores `val -> index` mapping. Used for O(1) lookup and finding index for removal.

### Algorithm:

**insert(val)**:
1.  Check map. If exists, return false.
2.  Add `val` to end of `nums`.
3.  Put `(val, last_index)` into `map`.
4.  Return true.

**remove(val)**:
1.  Check map. If not exists, return false.
2.  Get `index` of `val` from map.
3.  Get `lastElement` from `nums` (at `size - 1`).
4.  **Overwrite** `nums[index]` with `lastElement`.
5.  Update `map` for `lastElement`: set its index to `index`.
6.  Remove the actual last element from `nums` (O(1)).
7.  Remove `val` from `map`.
8.  Return true.

**getRandom()**:
1.  Generate random index between 0 and `size - 1`.
2.  Return `nums[randomIndex]`.

---

## Java Implementation

```java
import java.util.*;

class RandomizedSet {
    private ArrayList<Integer> nums;
    private HashMap<Integer, Integer> map;
    private Random rand;

    public RandomizedSet() {
        nums = new ArrayList<>();
        map = new HashMap<>();
        rand = new Random();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) {
            return false;
        }
        
        // Add to list and map
        map.put(val, nums.size());
        nums.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        }
        
        // Get index of element to remove
        int index = map.get(val);
        int lastElement = nums.get(nums.size() - 1);
        
        // Move last element to the hole left by removing val
        nums.set(index, lastElement);
        map.put(lastElement, index);
        
        // Remove the last element (which is now a duplicate)
        nums.remove(nums.size() - 1);
        map.remove(val);
        
        return true;
    }
    
    public int getRandom() {
        return nums.get(rand.nextInt(nums.size()));
    }
}
```

---

## Complexity Analysis

### Time Complexity:
-   **insert(val)**: O(1)
    -   HashMap put: O(1)
    -   ArrayList add: O(1)
-   **remove(val)**: O(1)
    -   HashMap get/remove: O(1)
    -   ArrayList set/remove(last): O(1)
-   **getRandom()**: O(1)
    -   Random generation: O(1)
    -   ArrayList access: O(1)

### Space Complexity:
-   **O(N)**: where N is the number of elements. We store each element once in the ArrayList and once in the HashMap.

---

## Key Points for Interviews

1.  **Why ArrayList + HashMap?**
    -   HashMap gives O(1) `insert` and `remove` check, but `getRandom` is O(N) (needs conversion to array/list keys).
    -   ArrayList gives O(1) `getRandom` and `insert`, but `remove` is O(N) (searching or shifting).
    -   Combining them gives the best of both worlds.

2.  **The "Swap with Last" Trick:**
    -   This is the standard technique for O(1) removal from an unsorted array when index is known.
    -   Crucial to mention that order does not matter in a Set.

3.  **Edge Cases:**
    -   Removing the last element itself (swap with itself is fine).
    -   Set with 1 element.
    -   Insert existing / Remove non-existing.

4.  **Follow-up: With Duplicates?**
    -   [381. Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)
    -   Solution: `HashMap<Integer, Set<Integer>>` to store *all* indices for a value.

---

## Related Problems

-   [381. Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)
-   [[Design-HashMap|Design HashMap]]

---

## Tags

`#design` `#array` `#hash-table` `#randomized` `#medium` `#google`
