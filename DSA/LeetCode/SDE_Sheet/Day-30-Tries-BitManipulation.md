# Day 30 — Tries & Bit Manipulation

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Tries (Prefix Trees) & Bit Manipulation
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Implement Trie (Prefix Tree)]] | 208 | Medium | ⬜ |
| 2 | [[#Maximum XOR of Two Numbers in an Array]] | 421 | Medium | ⬜ |
| 3 | [[#Maximum XOR with an Element From Array]] | 1707 | Hard | ⬜ |
| 4 | [[#Power Set (Subset Generation using Bitmasking)]] | 78 | Medium | ⬜ |
| 5 | [[#Single Number III (Two Non-Repeating Numbers)]] | 260 | Medium | ⬜ |
| 6 | [[#Divide Two Integers]] | 29 | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Implement Trie | Store all words in a list and scan for search/prefix. O(N*L). | HashSet for exact search plus prefix set for startsWith. | Trie nodes by character. O(L) search/insert/prefix. |
| Maximum XOR of Two Numbers | Check every pair. O(n^2). | Greedy prefix-set bit building. O(31*n). | Binary trie choosing opposite bits. O(31*n). |
| Maximum XOR with an Element From Array | For each query, scan all nums <= mi. O(n*q). | Sort nums and filter eligible range per query. Still costly. | Offline sort queries by mi and insert eligible nums into trie. |
| Power Set | Recursive include/exclude generation. O(n*2^n). | Bitmask from 0 to 2^n - 1. | Output-bound; bitmask/backtracking both are optimal. |
| Single Number III | Frequency map counts every number. O(n) space. | Sort and scan singles. O(n log n). | XOR all, split by rightmost set bit, XOR groups. O(n), O(1). |
| Divide Two Integers | Repeated subtraction. O(quotient). | Exponential subtraction by doubling divisor. O(log quotient). | Check high-to-low bit shifts and subtract. O(log dividend), O(1). |

---

## Implement Trie (Prefix Tree)

**LeetCode 208** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/implement-trie-prefix-tree/)

### Approach
- A Trie is an efficient information-retrieval data structure.
- Each node contains an array of children nodes (usually of size 26 for English letters) and a boolean flag `isEnd` indicating if the node marks the end of a word.

### Java Solution

```java
class Trie {
    private class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
    }

    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) {
                curr.children[idx] = new TrieNode();
            }
            curr = curr.children[idx];
        }
        curr.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) return false;
            curr = curr.children[idx];
        }
        return curr.isEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for (char c : prefix.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) return false;
            curr = curr.children[idx];
        }
        return true;
    }
}
```

**Complexity:**
- **Insert:** Time $O(L)$ · Space $O(L \times N)$ (where $L$ is word length, $N$ is number of inserted words)
- **Search / StartsWith:** Time $O(L)$ · Space $O(1)$

---

## Maximum XOR of Two Numbers in an Array

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

## Maximum XOR with an Element From Array

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

## Power Set (Subset Generation using Bitmasking)

**LeetCode 78** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/subsets/)

### Problem
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

### Approach
- An array of size $N$ has $2^N$ subsets.
- We can map each subset to a binary number from $0$ to $2^N - 1$.
- For any number $i$ in this range, if the $j$-th bit of $i$ is set (i.e., `(i >> j) & 1 == 1`), then `nums[j]` is included in that subset.

### Java Solution

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;
        int totalSubsets = 1 << n; // 2^n

        for (int i = 0; i < totalSubsets; i++) {
            List<Integer> subset = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) == 1) {
                    subset.add(nums[j]);
                }
            }
            result.add(subset);
        }
        return result;
    }
}
```

**Complexity:** Time $O(N \times 2^N)$ · Space $O(N \times 2^N)$

---

## Single Number III (Two Non-Repeating Numbers)

**LeetCode 260** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/single-number-iii/)

### Problem
Given an integer array `nums`, in which exactly two elements appear only once and all other elements appear exactly twice. Find the two elements that appear only once.

### Approach
1. XOR all numbers. The result `XOR_total` will be $A \oplus B$ (since all duplicates cancel out).
2. Since $A \neq B$, `XOR_total` must have at least one set bit. Find the lowest set bit: `rightmost_set_bit = XOR_total & -XOR_total`.
3. Use this set bit to divide all numbers in the array into two groups:
   - Group 1: Numbers that have this bit set.
   - Group 2: Numbers that do not have this bit set.
4. XORing all numbers in Group 1 will yield $A$, and XORing Group 2 will yield $B$.

### Java Solution

```java
class Solution {
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }

        // Get the rightmost set bit
        int rightmostSetBit = xor & -xor;

        int a = 0, b = 0;
        for (int num : nums) {
            if ((num & rightmostSetBit) != 0) {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        return new int[]{a, b};
    }
}
```

**Complexity:** Time $O(N)$ · Space $O(1)$

---

## Divide Two Integers

**LeetCode 29** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/divide-two-integers/)

### Problem
Divide two integers without using multiplication, division, and mod operator.

### Approach
- We can find the quotient by shifting the divisor left (`divisor << i`) until it's just under the dividend.
- Subtract `(divisor << i)` from `dividend`, add `(1 << i)` to the quotient, and repeat.
- Handle overflow cases (like `Integer.MIN_VALUE / -1`).

### Java Solution

```java
class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE; // Overflow case
        }

        // Convert to long to prevent overflow during absolute value conversion
        long lDividend = Math.abs((long) dividend);
        long lDivisor = Math.abs((long) divisor);
        int quotient = 0;

        for (int i = 31; i >= 0; i--) {
            if ((lDivisor << i) <= lDividend) {
                lDividend -= (lDivisor << i);
                quotient += (1 << i);
            }
        }

        return (dividend > 0) == (divisor > 0) ? quotient : -quotient;
    }
}
```

**Complexity:** Time $O(\log(\text{dividend}))$ · Space $O(1)$

---

## Bitwise Reference Cheatsheet

```
  Operation             Code                     Use Case
---------------------------------------------------------------------------------
  Get lowest set bit    `x & -x`                 Isolate rightmost set bit
  Clear lowest set bit  `x & (x - 1)`            Check power of 2, count set bits
  Toggle bit            `x ^ (1 << i)`           Toggle i-th bit from right
  Subset Check          `(mask & (1 << i)) != 0` Check if i-th element is in subset
```

#sde-sheet #tries #bit-manipulation #day30
