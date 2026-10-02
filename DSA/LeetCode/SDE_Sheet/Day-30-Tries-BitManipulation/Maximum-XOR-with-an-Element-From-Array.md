# Maximum XOR with an Element From Array

**LeetCode 1707** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

### Problem
Given an array `nums` and a queries array `queries` where `queries[i] = [xi, mi]`. The answer to the $i$-th query is the maximum bitwise XOR value of $x_i$ with any element in `nums` that is less than or equal to $m_i$. If all elements in `nums` are larger than $m_i$, the answer is `-1`.

### Approach
- Offline Query Processing: Sort both the `nums` array and the `queries` by their limit value $m_i$.
- Keep a pointer in `nums`. For each sorted query, insert all elements from `nums` that are $\le m_i$ into the Trie.
- Then, query the Trie for the maximum XOR with $x_i$.
- Store the results in the original query order using their original indices.

### Java Solution

```java
class Solution {
    private class TrieNode {
        TrieNode[] children = new TrieNode[2];
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
            int targetBit = 1 - bit;
            if (curr.children[targetBit] != null) {
                maxXOR |= (1 << i);
                curr = curr.children[targetBit];
            } else if (curr.children[bit] != null) {
                curr = curr.children[bit];
            } else {
                return -1; // Trie is empty
            }
        }
        return maxXOR;
    }

    public int[] maximizeXor(int[] nums, int[][] queries) {
        int qLen = queries.length;
        int[][] offlineQueries = new int[qLen][3]; // [xi, mi, originalIndex]
        for (int i = 0; i < qLen; i++) {
            offlineQueries[i][0] = queries[i][0];
            offlineQueries[i][1] = queries[i][1];
            offlineQueries[i][2] = i;
        }

        Arrays.sort(nums);
        Arrays.sort(offlineQueries, (a, b) -> Integer.compare(a[1], b[1]));

        TrieNode root = new TrieNode();
        int[] ans = new int[qLen];
        int numIdx = 0;
        int n = nums.length;

        for (int[] query : offlineQueries) {
            int xi = query[0];
            int mi = query[1];
            int originalIdx = query[2];

            while (numIdx < n && nums[numIdx] <= mi) {
                insert(root, nums[numIdx]);
                numIdx++;
            }

            if (numIdx == 0) {
                ans[originalIdx] = -1; // no element in nums <= mi
            } else {
                ans[originalIdx] = getMaxXOR(root, xi);
            }
        }

        return ans;
    }
}
```

**Complexity:** Time $O(N \log N + Q \log Q)$ · Space $O(N)$

---
