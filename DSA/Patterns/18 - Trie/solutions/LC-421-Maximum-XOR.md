# Maximum XOR of Two Numbers in an Array (LC 421)

**Difficulty**: Medium  
**Pattern**: Trie / Bit Manipulation  
**LeetCode**: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

## Problem Statement
Given an integer array `nums`, return the maximum result of `nums[i] XOR nums[j]`.

**Example:**
```
Input: nums = [3,10,5,25,2,8]
Output: 28
```

## Approach: Trie (Binary)

### Intuition
To maximize XOR for a number `num`, we want to find another number that has opposite bits at MSB positions.
1. Insert all numbers into binary Trie (MSB to LSB).
2. For each number, traverse Trie attempting to go "opposite" direction.
   - If `bit` is 0, try to go to child 1.
   - If `bit` is 1, try to go to child 0.
   - If preferred child exists, add `1 << bitPosition` to current XOR result.
   - Else, go to the other child.

### Java Code
```java
class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[2];
    }
    
    public int findMaximumXOR(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        TrieNode root = new TrieNode();
        
        // 1. Build Trie
        for (int num : nums) {
            TrieNode curr = root;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (curr.children[bit] == null) {
                    curr.children[bit] = new TrieNode();
                }
                curr = curr.children[bit];
            }
        }
        
        // 2. Query Max XOR
        int maxXor = 0;
        for (int num : nums) {
            TrieNode curr = root;
            int currentXor = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                // Want opposite bit
                if (curr.children[1 - bit] != null) {
                    currentXor |= (1 << i);
                    curr = curr.children[1 - bit];
                } else {
                    curr = curr.children[bit];
                }
            }
            maxXor = Math.max(maxXor, currentXor);
        }
        
        return maxXor;
    }
}
```

### Complexity
- **Time**: O(N * 32) = O(N)
- **Space**: O(N * 32) = O(N)

## Key Takeaways
- Trie can store binary representations
- "Greedy" bit choices from MSB to LSB maximize value
