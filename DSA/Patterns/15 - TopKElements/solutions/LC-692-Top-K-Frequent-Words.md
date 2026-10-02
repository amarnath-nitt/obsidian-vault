---
solved: false
difficulty: Medium
pattern: Top KElements
lc_number: 692
date_solved: 
tags:
  - dsa
  - top-kelements
  - medium
---
# Top K Frequent Words (LC 692)

**Difficulty**: Medium  
**Pattern**: Top K Elements / Heap  
**LeetCode**: https://leetcode.com/problems/top-k-frequent-words/

## Problem Statement
Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

**Example:**
```
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
```

## Approach: Min-Heap

### Intuition
Count frequencies.
Use Min-Heap to keep top k.
Comparator:
- If counts different: sort by count ascending (to remove smallest count).
- If counts same: sort by word descending (lexicographical reverse, to remove "largest" word which corresponds to least lexicographical priority in top k context? Wait).
Requirement: "highest freq", "same freq -> lexicographical".
Min-Heap removes "Least important".
"Least important" = Lower frequency OR (Same frequency AND Later in dictionary).
So heap order: Count Ascending, then Word Descending.

### Java Code
```java
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap<>();
        for (String w : words) count.put(w, count.getOrDefault(w, 0) + 1);
        
        PriorityQueue<String> minHeap = new PriorityQueue<>((w1, w2) -> {
            int c1 = count.get(w1);
            int c2 = count.get(w2);
            if (c1 != c2) return c1 - c2; // Lower count first (evict first)
            return w2.compareTo(w1);      // Reverse lexicographical (z before a, evict 'z' first to keep 'a')
        });
        
        for (String w : count.keySet()) {
            minHeap.offer(w);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        
        List<String> result = new ArrayList<>();
        while (!minHeap.isEmpty()) {
            result.add(minHeap.poll());
        }
        Collections.reverse(result);
        return result;
    }
}
```

### Complexity
- **Time**: O(N log K)
- **Space**: O(N)

## Key Takeaways
- Custom comparator for Heap
- Careful with lexicographical logic in Min-Heap (reverse logic to Evict the "worst")
