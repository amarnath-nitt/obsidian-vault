# Day 1 — Arrays I

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Arrays — Fundamentals
**Difficulty Mix:** Easy / Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Set Matrix Zeroes]] | 73 | Medium | ⬜ |
| 2 | [[#Pascal's Triangle]] | 118 | Easy | ⬜ |
| 3 | [[#Next Permutation]] | 31 | Medium | ⬜ |
| 4 | [[#Kadane's Algorithm — Maximum Subarray]] | 53 | Medium | ⬜ |
| 5 | [[#Sort an Array of 0s 1s 2s (Dutch National Flag)]] | 75 | Medium | ⬜ |
| 6 | [[#Best Time to Buy and Sell Stock]] | 121 | Easy | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Set Matrix Zeroes | For every zero, scan its full row and column. O(m*n*(m+n)) time. | Keep row and column marker arrays. O(m*n) time, O(m+n) space. | Use first row and first column as markers. O(m*n) time, O(1) space. |
| Pascal's Triangle | Compute every value independently with combinations. Costly repeated work. | Build each row from the previous row. O(n^2) time. | Same output-bound DP; for a single row use rolling nCr values. |
| Next Permutation | Generate all permutations, sort them, pick the next one. O(n!*n). | Find pivot, swap, then sort the suffix. O(n log n). | Find pivot, swap with next greater from suffix, reverse suffix. O(n), O(1). |
| Kadane's Algorithm | Try every subarray and sum it. O(n^3). | Use prefix sums or two loops. O(n^2). | Kadane: keep best subarray ending here. O(n), O(1). |
| Sort 0s 1s 2s | Use library sort. O(n log n). | Count 0s, 1s, 2s, then overwrite. O(n), two passes. | Dutch National Flag with low/mid/high. O(n), one pass, O(1). |
| Best Time to Buy and Sell Stock | Try every buy/sell pair. O(n^2). | Precompute best future selling price. O(n) time, O(n) space. | Track minimum price so far and best profit. O(n), O(1). |

---

## Set Matrix Zeroes

**LeetCode 73** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/set-matrix-zeroes/)

### Problem
Given an `m x n` matrix, if an element is `0`, set its entire row and column to `0`.
Do it **in-place**.

### Approach

**Brute Force — O(m×n×(m+n)) time, O(1) space:**
- For each cell with 0, mark entire row and column with -1 (sentinel)
- Then convert all -1 to 0
- ⚠️ Breaks if original matrix contains -1

**Better — O(m×n) time, O(m+n) space:**
- Use two boolean arrays: `rowZero[m]` and `colZero[n]`
- First pass: mark rows and cols that have a zero
- Second pass: set cells to 0 based on markers

**Optimal — O(m×n) time, O(1) space:** ✅
- Use **first row and first column** as markers
- Track separately if row[0] or col[0] itself has zero

### Java Solution

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;

        // Check if first row has zero
        for (int j = 0; j < n; j++)
            if (matrix[0][j] == 0) firstRowZero = true;

        // Check if first col has zero
        for (int i = 0; i < m; i++)
            if (matrix[i][0] == 0) firstColZero = true;

        // Use first row/col as markers
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }

        // Set zeros based on markers
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;

        // Handle first row
        if (firstRowZero)
            for (int j = 0; j < n; j++) matrix[0][j] = 0;

        // Handle first col
        if (firstColZero)
            for (int i = 0; i < m; i++) matrix[i][0] = 0;
    }
}
```

**Complexity:** Time O(m×n) · Space O(1)

---

## Pascal's Triangle

**LeetCode 118** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/pascals-triangle/)

### Problem
Given `numRows`, return the first `numRows` of Pascal's triangle.

### Approach

- Row `i` has `i+1` elements
- `triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]`
- First and last element of each row is always 1

### Java Solution

```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for (int j = 1; j < i; j++)
                row.add(result.get(i-1).get(j-1) + result.get(i-1).get(j));
            if (i > 0) row.add(1);
            result.add(row);
        }
        return result;
    }
}
```

**Complexity:** Time O(n²) · Space O(n²)

---

## Next Permutation

**LeetCode 31** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/next-permutation/)

### Problem
Rearrange numbers into the lexicographically next greater permutation. If no next permutation exists, sort ascending.

### Approach (3-step in-place)

1. **Find the "dip"**: Scan right-to-left, find index `i` where `nums[i] < nums[i+1]`
2. **Find the swap partner**: Scan right-to-left, find smallest element > `nums[i]`, swap
3. **Reverse the suffix**: Reverse everything after index `i`

> If no dip found → the array is fully descending → reverse the whole array

### Java Solution

```java
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2;

        // Step 1: Find dip
        while (i >= 0 && nums[i] >= nums[i + 1]) i--;

        if (i >= 0) {
            // Step 2: Find swap partner
            int j = n - 1;
            while (nums[j] <= nums[i]) j--;
            int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
        }

        // Step 3: Reverse suffix
        int left = i + 1, right = n - 1;
        while (left < right) {
            int tmp = nums[left]; nums[left] = nums[right]; nums[right] = tmp;
            left++; right--;
        }
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Kadane's Algorithm — Maximum Subarray

**LeetCode 53** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/maximum-subarray/)

### Problem
Find the contiguous subarray with the largest sum.

### Approach

**Key insight:** At each position, decide:
- Extend the existing subarray: `currentSum + nums[i]`
- Start fresh: `nums[i]`
→ Take the maximum of both

Reset `currentSum` to 0 whenever it goes negative.

### Java Solution

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = 0;

        for (int num : nums) {
            currentSum += num;
            maxSum = Math.max(maxSum, currentSum);
            if (currentSum < 0) currentSum = 0;
        }
        return maxSum;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

> **Follow-up:** Print the actual subarray → track `start`, `end`, `tempStart` indices.

---

## Sort an Array of 0s 1s 2s (Dutch National Flag)

**LeetCode 75** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/sort-colors/)

### Problem
Sort an array containing only 0, 1, 2 in-place without using library sort.

### Approach (Dutch National Flag — Dijkstra's 3-way partition)

- Maintain 3 pointers: `low`, `mid`, `high`
- Invariant: `[0..low-1]` = 0s, `[low..mid-1]` = 1s, `[high+1..n-1]` = 2s
- Process `mid` to `high`:
  - `nums[mid] == 0` → swap with `low`, advance both `low` and `mid`
  - `nums[mid] == 1` → advance `mid`
  - `nums[mid] == 2` → swap with `high`, decrease `high` (don't advance `mid`)

### Java Solution

```java
class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                int tmp = nums[low]; nums[low] = nums[mid]; nums[mid] = tmp;
                low++; mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                int tmp = nums[mid]; nums[mid] = nums[high]; nums[high] = tmp;
                high--;
            }
        }
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Best Time to Buy and Sell Stock

**LeetCode 121** · Easy
🔗 [LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### Problem
Given prices array, find the maximum profit from one transaction (buy then sell).

### Approach

- Track `minPrice` seen so far (best day to buy)
- At each day, compute profit = `price - minPrice`
- Track `maxProfit` across all days

### Java Solution

```java
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                maxProfit = Math.max(maxProfit, price - minPrice);
            }
        }
        return maxProfit;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Interview Tips for Arrays

> 💡 **Always clarify:** Can we modify the array? Is there extra space allowed?
> 💡 **Common tricks:** Two pointers, prefix sums, frequency maps, in-place markers
> 💡 **Edge cases:** Empty array, single element, all same elements, all zeros

#sde-sheet #arrays #day1
