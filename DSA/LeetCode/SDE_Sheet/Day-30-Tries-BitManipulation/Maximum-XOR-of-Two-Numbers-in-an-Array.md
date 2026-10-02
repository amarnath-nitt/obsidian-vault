# Maximum XOR of Two Numbers in an Array

**LeetCode 421** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

### Approach
1. Build a Binary Trie using the binary representation of numbers (from the 31st bit down to the 0th bit).
2. For each number, traverse the Trie. To maximize XOR, at each bit, we want to go in the opposite direction (if current bit is 1, look for 0; if current bit is 0, look for 1).
3. If the opposite direction exists, we take it and add the bit value $(1 \ll i)$ to our current XOR sum. Otherwise, we go in the same direction.

### Java Solution

```java
class Solution {
    private class TrieNode {
        TrieNode[] children = new TrieNode[2]; // 0 and 1
    }

    private void insert(TrieNode root, int num) {
        TrieNode curr = root;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[bit] == null) {
                curr.children[bit] = new TrieNode();
            }
            curr = curr.children[bit];
        }
    }

    private int getMaxXOR(TrieNode root, int num) {
        TrieNode curr = root;
        int maxXOR = 0;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int targetBit = 1 - bit; // opposite bit
            if (curr.children[targetBit] != null) {
                maxXOR |= (1 << i);
                curr = curr.children[targetBit];
            } else {
                curr = curr.children[bit];
            }
        }
        return maxXOR;
    }

    public int findMaximumXOR(int[] nums) {
        TrieNode root = new TrieNode();
        for (int num : nums) {
            insert(root, num);
        }
        
        int maxResult = 0;
        for (int num : nums) {
            maxResult = Math.max(maxResult, getMaxXOR(root, num));
        }
        return maxResult;
    }
}
```

**Complexity:** Time $O(N)$ (since bit length is constant 31) · Space $O(N)$

---
