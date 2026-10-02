---
solved: true
difficulty: Medium
pattern: Frequency Counting
lc_number: 347
date_solved: 
tags:
  - dsa
  - frequency-counting
  - medium
---
# Top K Frequent Elements (LC 347)

**Difficulty**: Medium  
**Pattern**: Frequency Counting / Top K Elements  
**LeetCode**: https://leetcode.com/problems/top-k-frequent-elements/

## Existing Solution
This problem is solved in Blind75: → [Solution](../../../LeetCode/Blind75/Arrays-Hashing/Top-K-Frequent-Elements.md)

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

**Example:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

## Approach 1: HashMap + Sorting

### Java Code
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        
        List<Integer> unique = new ArrayList<>(count.keySet());
        unique.sort((a, b) -> count.get(b) - count.get(a));
        
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = unique.get(i);
        }
        return result;
    }
}
```

### Complexity
- **Time**: O(n log n)
- **Space**: O(n)

## Approach 2: Bucket Sort (Optimized)

### Java Code
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        
        // Bucket sort: index = frequency
        List<Integer>[] bucket = new List[nums.length + 1];
        for (int num : count.keySet()) {
            int freq = count.get(num);
            if (bucket[freq] == null) {
                bucket[freq] = new ArrayList<>();
            }
            bucket[freq].add(num);
        }
        
        // Collect top k
        int[] result = new int[k];
        int idx = 0;
        for (int i = bucket.length - 1; i >= 0 && idx < k; i--) {
            if (bucket[i] != null) {
                for (int num : bucket[i]) {
                    result[idx++] = num;
                    if (idx == k) break;
                }
            }
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Takeaways
- Bucket sort achieves O(n) by using frequency as index
- Heap solution is O(n log k) - good for small k
- Most elegant solution for this specific problem
