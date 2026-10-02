---
solved: false
difficulty: Hard
pattern: Bit Manipulation
lc_number: 421
date_solved: 
tags:
  - dsa
  - bit-manipulation
  - hard
---
# Maximum XOR of Two Numbers in an Array

[Problem Link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

## Problem Statement
Given an integer array `nums`, return the maximum result of `nums[i] XOR nums[j]`, where `0 <= i <= j < n`.

## Approach
Trie (Prefix Tree) / Greedy Bitwise.
1.  Insert all numbers into a binary Trie (from MSB to LSB).
2.  For each number, find the "best" XOR partner in the Trie.
    - To maximize XOR, we want a bit '1' if current bit is '0', and '0' if current bit is '1'.
    - If preferred path exists, take it (bit becomes 1).
    - Else, take the other path (bit becomes 0).
3.  Track the maximum XOR found.

## Time and Space Complexity
- **Time Complexity:** O(N * L), where L is number of bits (31 or 32).
- **Space Complexity:** O(N * L) for Trie.

## Code
```java
class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[2];
    }
    
    public int findMaximumXOR(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        
        TrieNode root = new TrieNode();
        
        // Build Trie
        for (int num : nums) {
            TrieNode node = root;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (node.children[bit] == null) {
                    node.children[bit] = new TrieNode();
                }
                node = node.children[bit];
            }
        }
        
        int maxXor = 0;
        
        for (int num : nums) {
            TrieNode node = root;
            int currentXor = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                // We want the opposite bit to maximize XOR
                if (node.children[1 - bit] != null) {
                    currentXor |= (1 << i);
                    node = node.children[1 - bit];
                } else {
                    node = node.children[bit];
                }
            }
            maxXor = Math.max(maxXor, currentXor);
        }
        
        return maxXor;
    }
}
```
