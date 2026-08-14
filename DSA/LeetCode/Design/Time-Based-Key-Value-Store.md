# Time Based Key-Value Store

**LeetCode Problem:** [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)  
**Difficulty:** Medium  
**Topic:** Design, Hash Table, String, Binary Search

---

## Problem Statement

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

**Note:** All timestamps of `set` are strictly increasing.

---

## Examples

### Example 1:
```
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output:
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store key="foo", value="bar", timestamp=1
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar" (latest timestamp <= 3 is 1)
timeMap.set("foo", "bar2", 4); // store key="foo", value="bar2", timestamp=4
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2" (latest timestamp <= 5 is 4)
```

---

## Approach

### Key Insights:
1. **HashMap + List**: Store key -> list of (timestamp, value) pairs
2. **Sorted Timestamps**: Since timestamps are strictly increasing, list is naturally sorted
3. **Binary Search**: Use binary search to find largest timestamp <= given timestamp
4. **Data Structure**:
   - `HashMap<String, List<Pair>>`
   - Each Pair contains (timestamp, value)

### Algorithm:

**set(key, value, timestamp)**:
1. Get list for key (create if doesn't exist)
2. Append (timestamp, value) to list
3. Time: O(1)

**get(key, timestamp)**:
1. Get list for key
2. Binary search for largest timestamp <= given timestamp
3. Return corresponding value
4. Time: O(log n) where n is number of values for that key

---

## Java Implementation - Approach 1 (Using Custom Pair)

```java
class TimeMap {
    // Pair class to store timestamp and value
    class Pair {
        int timestamp;
        String value;
        
        Pair(int timestamp, String value) {
            this.timestamp = timestamp;
            this.value = value;
        }
    }
    
    private HashMap<String, List<Pair>> map;
    
    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.putIfAbsent(key, new ArrayList<>());
        map.get(key).add(new Pair(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }
        
        List<Pair> list = map.get(key);
        return binarySearch(list, timestamp);
    }
    
    private String binarySearch(List<Pair> list, int timestamp) {
        int left = 0, right = list.size() - 1;
        String result = "";
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (list.get(mid).timestamp <= timestamp) {
                result = list.get(mid).value;
                left = mid + 1; // Look for larger timestamp
            } else {
                right = mid - 1;
            }
        }
        
        return result;
    }
}
```

---

## Java Implementation - Approach 2 (Using TreeMap)

**Alternative using TreeMap for automatic sorting**

```java
class TimeMap {
    private HashMap<String, TreeMap<Integer, String>> map;
    
    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.putIfAbsent(key, new TreeMap<>());
        map.get(key).put(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }
        
        TreeMap<Integer, String> treeMap = map.get(key);
        
        // floorEntry returns entry with largest key <= timestamp
        Map.Entry<Integer, String> entry = treeMap.floorEntry(timestamp);
        
        return entry == null ? "" : entry.getValue();
    }
}
```

---

## Java Implementation - Approach 3 (Two ArrayLists)

**More memory efficient, separate lists for timestamps and values**

```java
class TimeMap {
    private HashMap<String, List<Integer>> timestampMap;
    private HashMap<String, List<String>> valueMap;
    
    public TimeMap() {
        timestampMap = new HashMap<>();
        valueMap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        timestampMap.putIfAbsent(key, new ArrayList<>());
        valueMap.putIfAbsent(key, new ArrayList<>());
        
        timestampMap.get(key).add(timestamp);
        valueMap.get(key).add(value);
    }
    
    public String get(String key, int timestamp) {
        if (!timestampMap.containsKey(key)) {
            return "";
        }
        
        List<Integer> timestamps = timestampMap.get(key);
        List<String> values = valueMap.get(key);
        
        // Binary search for largest timestamp <= given timestamp
        int left = 0, right = timestamps.size() - 1;
        int index = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (timestamps.get(mid) <= timestamp) {
                index = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return index == -1 ? "" : values.get(index);
    }
}
```

---

## Complexity Analysis

### Approach 1 & 3 (ArrayList + Binary Search):
- **set(key, value, timestamp)**: O(1)
  - ArrayList add is O(1) amortized
  
- **get(key, timestamp)**: O(log n)
  - Binary search on list of n timestamps
  
- **Space**: O(N)
  - N = total number of set operations

### Approach 2 (TreeMap):
- **set(key, value, timestamp)**: O(log n)
  - TreeMap insertion is O(log n)
  
- **get(key, timestamp)**: O(log n)
  - TreeMap floorEntry is O(log n)
  
- **Space**: O(N)
  - TreeMap overhead is higher than ArrayList

---

## Comparison of Approaches

| Approach | Set Time | Get Time | Space | Pros | Cons |
|----------|----------|----------|-------|------|------|
| **ArrayList + Pair** | O(1) | O(log n) | Low | Simple, cache-friendly | Need custom Pair class |
| **TreeMap** | O(log n) | O(log n) | Medium | Clean API, auto-sorted | Slower set, more memory |
| **Two ArrayLists** | O(1) | O(log n) | Lowest | Memory efficient | Two separate lists to maintain |

**Recommendation**: Use **Approach 1** (ArrayList + Pair) for best balance of simplicity and performance.

---

## Binary Search Template Explanation

```java
// Find largest timestamp <= target
int left = 0, right = list.size() - 1;
String result = "";

while (left <= right) {
    int mid = left + (right - left) / 2;
    
    if (list.get(mid).timestamp <= target) {
        result = list.get(mid).value;  // Valid candidate
        left = mid + 1;                // Look for larger
    } else {
        right = mid - 1;               // Too large, go left
    }
}

return result;
```

**Key Points:**
- We're looking for **largest value <= target**
- If `mid` timestamp is valid, save it and search right half
- If `mid` timestamp is too large, search left half
- Result stores the last valid value found

---

## Key Points for Interviews

1. **Why Binary Search?**
   - Timestamps are strictly increasing (sorted)
   - Linear search would be O(n)
   - Binary search gives O(log n)

2. **Why Not Just Use HashMap?**
   - HashMap stores single value per key
   - Need to store **multiple values** with different timestamps
   - Need to efficiently find **closest timestamp**

3. **Edge Cases:**
   - Key doesn't exist → return ""
   - All timestamps > target → return ""
   - Empty list → return ""
   - Single element

4. **Common Mistakes:**
   - Using wrong binary search variant (need "largest <=", not exact match)
   - Forgetting to check if key exists
   - Not initializing result to ""
   - Using regular HashMap instead of TreeMap (if applicable)

5. **Follow-up Questions:**
   - What if timestamps are not strictly increasing?
   - How would you handle delete operations?
   - How to support range queries (get all values in time range)?
   - How would you optimize for space?

6. **Real-World Applications:**
   - Version control systems (Git)
   - Database snapshots
   - Time-series databases
   - Audit logs

---

## Test Cases

```java
public class TimeMapTest {
    public static void main(String[] args) {
        TimeMap timeMap = new TimeMap();
        
        // Test 1: Basic operations
        timeMap.set("foo", "bar", 1);
        System.out.println(timeMap.get("foo", 1));  // "bar"
        System.out.println(timeMap.get("foo", 3));  // "bar"
        
        timeMap.set("foo", "bar2", 4);
        System.out.println(timeMap.get("foo", 4));  // "bar2"
        System.out.println(timeMap.get("foo", 5));  // "bar2"
        
        // Test 2: Edge cases
        System.out.println(timeMap.get("nonexistent", 1));  // ""
        System.out.println(timeMap.get("foo", 0));          // ""
        
        // Test 3: Multiple keys
        timeMap.set("bar", "value1", 2);
        timeMap.set("bar", "value2", 5);
        System.out.println(timeMap.get("bar", 3));  // "value1"
        System.out.println(timeMap.get("bar", 6));  // "value2"
    }
}
```

---

## Visual Example

```
After operations:
set("foo", "bar", 1)
set("foo", "bar2", 4)
set("foo", "bar3", 7)

Data structure:
{
  "foo": [
    (1, "bar"),
    (4, "bar2"),
    (7, "bar3")
  ]
}

get("foo", 5):
Binary search for largest timestamp <= 5
Found: timestamp=4, value="bar2"
Return: "bar2"
```

---

## Related Problems

- [[Design-HashMap|706. Design HashMap]]
- [1244. Design A Leaderboard](https://leetcode.com/problems/design-a-leaderboard/)
- [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/)

---

## Tags

`#design` `#hash-table` `#binary-search` `#timestamp` `#medium` `#time-series`
