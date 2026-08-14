# Partition Labels (LC 763)

**Difficulty**: Medium  
**Pattern**: Greedy  
**LeetCode**: https://leetcode.com/problems/partition-labels/

## Problem Statement
You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.
Return a list of integers representing the size of these parts.

**Example:**
```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
```

## Approach: Greedy Expansion

### Intuition
For each character in a partition, the partition must extend at least to the last occurrence of that character.
1. Record last occurrence index for every char.
2. Iterate string. Maintain `end` of current partition.
   `end = max(end, last_index[char])`.
3. If `i == end`, partition complete. Push size `i - start + 1`.

### Java Code
```java
class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }
        
        List<Integer> partitions = new ArrayList<>();
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            
            if (i == end) {
                partitions.add(end - start + 1);
                start = end + 1;
            }
        }
        
        return partitions;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(1) (size 26 map)

## Key Takeaways
- Precompute "constraints" (last indices)
- Expand partition eagerly based on constraints
