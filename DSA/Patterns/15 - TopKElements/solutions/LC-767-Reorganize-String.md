---
solved: false
difficulty: Medium
pattern: Top KElements
lc_number: 767
date_solved: 
tags:
  - dsa
  - top-kelements
  - medium
---
# Reorganize String (LC 767)

**Difficulty**: Medium  
**Pattern**: Top K Elements / Greedy  
**LeetCode**: https://leetcode.com/problems/reorganize-string/

## Problem Statement
Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.
Return any possible rearrangement of `s` or return `""` if not possible.

**Example:**
```
Input: s = "aab"
Output: "aba"
```

## Approach: Max-Heap (Greedy)

### Intuition
Always pick the most frequent character remaining to place next, BUT we can't place the same char twice in a row.
1. Count frequencies.
2. Put all chars in Max-Heap (by count).
3. Poll most frequent (A). Append to result. S
4. Poll next most frequent (B). Append.
5. Push A back if count > 0.
Basically, "hold" the just-used character and don't put it back in heap until we use a different one.

### Java Code
```java
class Solution {
    public String reorganizeString(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : s.toCharArray()) {
            counts.put(c, counts.getOrDefault(c, 0) + 1);
        }
        
        // If max freq > (n+1)/2, impossible
        int maxFreq = 0;
        for (int count : counts.values()) maxFreq = Math.max(maxFreq, count);
        if (maxFreq > (s.length() + 1) / 2) return "";
        
        PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> counts.get(b) - counts.get(a));
        pq.addAll(counts.keySet());
        
        StringBuilder sb = new StringBuilder();
        
        while (pq.size() >= 2) {
            char a = pq.poll();
            char b = pq.poll();
            
            sb.append(a);
            sb.append(b);
            
            counts.put(a, counts.get(a) - 1);
            counts.put(b, counts.get(b) - 1);
            
            if (counts.get(a) > 0) pq.offer(a);
            if (counts.get(b) > 0) pq.offer(b);
        }
        
        if (!pq.isEmpty()) {
            sb.append(pq.poll());
        }
        
        return sb.toString();
    }
}
```

### Complexity
- **Time**: O(N log A) or O(N) since A=26 is constant.
- **Space**: O(A) = O(1).

## Key Takeaways
- Key condition: Max frequency cannot exceed `(N+1)/2`
- Need to interleave most frequent chars
- "Hold" strategy for heap ensures adjacency constraint
