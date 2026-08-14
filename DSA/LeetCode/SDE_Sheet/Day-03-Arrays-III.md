# Day 3 — Arrays III

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Arrays — Advanced
**Difficulty Mix:** Medium / Hard

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Search in a 2D Matrix]] | 74 | Medium | ⬜ |
| 2 | [[#Pow(x, n)]] | 50 | Medium | ⬜ |
| 3 | [[#Majority Element (n/2 times)]] | 169 | Easy | ⬜ |
| 4 | [[#Majority Element II (n/3 times)]] | 229 | Medium | ⬜ |
| 5 | [[#Grid Unique Paths]] | 62 | Medium | ⬜ |
| 6 | [[#Reverse Pairs]] | 493 | Hard | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Search in a 2D Matrix | Scan every cell. O(m*n). | Binary search each row. O(m log n). | Treat matrix as a sorted 1D array. O(log(m*n)). |
| Pow(x, n) | Multiply x by itself abs(n) times. O(n). | Recursive divide-and-conquer exponentiation. O(log n). | Iterative binary exponentiation with negative exponent handling. O(log n), O(1). |
| Majority Element | Count every candidate by scanning. O(n^2). | Use a frequency map. O(n) time, O(n) space. | Boyer-Moore voting. O(n) time, O(1) space. |
| Majority Element II | Count every candidate by scanning. O(n^2). | Use a frequency map. O(n) space. | Extended Boyer-Moore with two candidates plus verification. O(n), O(1). |
| Grid Unique Paths | Recursively try right/down paths. Exponential. | DP table over cells. O(m*n). | Combinatorics: choose moves. O(min(m,n)) time, O(1) space. |
| Reverse Pairs | Check every pair. O(n^2). | Fenwick tree with coordinate compression. O(n log n). | Modified merge sort counts cross pairs. O(n log n). |

---

## Search in a 2D Matrix

**LeetCode 74** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/search-a-2d-matrix/)

### Problem
Matrix where each row is sorted and first integer of each row > last integer of previous row.
Search for a target value efficiently.

### Approach

**Key insight:** Treat the matrix as a **flattened sorted array** → apply Binary Search.

- Total elements: `m * n`
- `mid` element at position `p` → `matrix[p/n][p%n]`

### Java Solution

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int lo = 0, hi = m * n - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = matrix[mid / n][mid % n];
            if (val == target) return true;
            else if (val < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }
}
```

**Complexity:** Time O(log(m×n)) · Space O(1)

> **Variant (LC 240):** Each row & column is sorted but not globally → start from top-right corner, move left or down.

---

## Pow(x, n)

**LeetCode 50** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/powx-n/)

### Problem
Implement `pow(x, n)`. Handle negative `n`.

### Approach (Fast Exponentiation / Binary Exponentiation)

- If `n` is even: `x^n = (x^(n/2))^2`
- If `n` is odd: `x^n = x * x^(n-1)`
- If `n < 0`: `x^n = (1/x)^(-n)`

This reduces O(n) multiplications to O(log n).

### Java Solution

```java
class Solution {
    public double myPow(double x, int n) {
        long N = n; // avoid Integer.MIN_VALUE overflow
        if (N < 0) { x = 1 / x; N = -N; }
        return fastPow(x, N);
    }

    private double fastPow(double x, long n) {
        if (n == 0) return 1.0;
        if (n % 2 == 0) {
            double half = fastPow(x, n / 2);
            return half * half;
        }
        return x * fastPow(x, n - 1);
    }
}
```

**Complexity:** Time O(log n) · Space O(log n) recursion stack

---

## Majority Element (n/2 times)

**LeetCode 169** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/majority-element/)

### Problem
Find the element that appears more than `n/2` times. Guaranteed to exist.

### Approach (Boyer-Moore Voting Algorithm)

- Maintain a `candidate` and a `count`
- If count == 0 → new candidate
- If current == candidate → count++
- Else → count--
- The candidate at the end is the majority element

### Java Solution

```java
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = nums[0], count = 1;

        for (int i = 1; i < nums.length; i++) {
            if (count == 0) {
                candidate = nums[i];
                count = 1;
            } else if (nums[i] == candidate) {
                count++;
            } else {
                count--;
            }
        }
        return candidate;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Majority Element II (n/3 times)

**LeetCode 229** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/majority-element-ii/)

### Problem
Find all elements that appear more than `n/3` times. Return as list.

### Approach (Extended Boyer-Moore — 2 candidates)

- At most **2** elements can appear > n/3 times
- Track 2 candidates and 2 counts
- Two-pass: first pass finds candidates, second pass verifies

### Java Solution

```java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int cand1 = 0, cand2 = 0, cnt1 = 0, cnt2 = 0;

        for (int num : nums) {
            if (num == cand1) cnt1++;
            else if (num == cand2) cnt2++;
            else if (cnt1 == 0) { cand1 = num; cnt1 = 1; }
            else if (cnt2 == 0) { cand2 = num; cnt2 = 1; }
            else { cnt1--; cnt2--; }
        }

        cnt1 = 0; cnt2 = 0;
        for (int num : nums) {
            if (num == cand1) cnt1++;
            else if (num == cand2) cnt2++;
        }

        List<Integer> result = new ArrayList<>();
        int threshold = nums.length / 3;
        if (cnt1 > threshold) result.add(cand1);
        if (cnt2 > threshold) result.add(cand2);
        return result;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Grid Unique Paths

**LeetCode 62** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/unique-paths/)

### Problem
Count unique paths in an `m×n` grid from top-left to bottom-right (only right/down moves).

### Approach 1 — DP

- `dp[i][j]` = number of ways to reach cell (i, j)
- `dp[i][j] = dp[i-1][j] + dp[i][j-1]`

### Approach 2 — Combinatorics ✅ Best

- Total moves: `(m-1) + (n-1)` = `m+n-2`
- Choose `m-1` down moves out of total: `C(m+n-2, m-1)`

### Java Solution (DP)

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                dp[j] += dp[j - 1];

        return dp[n - 1];
    }
}
```

**Complexity:** Time O(m×n) · Space O(n)

---

## Reverse Pairs

**LeetCode 493** · Hard
🔗 [LeetCode Link](https://leetcode.com/problems/reverse-pairs/)

### Problem
Count pairs `(i, j)` where `i < j` and `nums[i] > 2 * nums[j]`.

### Approach (Modified Merge Sort)

- Like Count Inversions, but condition is `arr[i] > 2 * arr[j]`
- **Count phase** (before merge): Use two pointers across left and right halves
- **Merge phase**: Standard merge sort

> ⚠️ Count BEFORE merging, because after merging the halves, relative order changes.

### Java Solution

```java
class Solution {
    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length - 1);
    }

    private int mergeSort(int[] nums, int l, int r) {
        if (l >= r) return 0;
        int mid = l + (r - l) / 2;
        int count = mergeSort(nums, l, mid) + mergeSort(nums, mid + 1, r);

        // Count reverse pairs
        int j = mid + 1;
        for (int i = l; i <= mid; i++) {
            while (j <= r && nums[i] > 2L * nums[j]) j++;
            count += (j - mid - 1);
        }

        // Merge
        int[] temp = new int[r - l + 1];
        int i = l, k = 0;
        j = mid + 1;
        while (i <= mid && j <= r)
            temp[k++] = (nums[i] <= nums[j]) ? nums[i++] : nums[j++];
        while (i <= mid) temp[k++] = nums[i++];
        while (j <= r)   temp[k++] = nums[j++];
        for (int x = 0; x < temp.length; x++) nums[l + x] = temp[x];

        return count;
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---

## Interview Tips for Arrays III

> 💡 **2D Matrix → Flatten to 1D** for binary search
> 💡 **Boyer-Moore** works for n/k majority: need k-1 candidates
> 💡 **Merge Sort** solves inversion-type problems in O(n log n)

#sde-sheet #arrays #day3
