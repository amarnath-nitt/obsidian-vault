# Day 2 — Arrays II

**Sheet:** [[SDE-Sheet-Index|SDE Sheet Index]]
**Topic:** Arrays — Intermediate
**Difficulty Mix:** Easy / Medium

---

## Problems

| # | Problem | LC # | Difficulty | Status |
|---|---------|------|------------|--------|
| 1 | [[#Rotate Matrix (Image)]] | 48 | Medium | ⬜ |
| 2 | [[#Merge Overlapping Intervals]] | 56 | Medium | ⬜ |
| 3 | [[#Merge Two Sorted Arrays Without Extra Space]] | 88 | Medium | ⬜ |
| 4 | [[#Find Duplicate in Array]] | 287 | Medium | ⬜ |
| 5 | [[#Repeat and Missing Number]] | — | Medium | ⬜ |
| 6 | [[#Count Inversions in Array]] | — | Medium | ⬜ |

## Approach Ladder

| Problem | Brute Force | Better | Optimized |
|---|---|---|---|
| Rotate Matrix | Copy each cell to its rotated position in another matrix. O(n^2) space. | Rotate layer by layer using 4-way swaps. O(1) space. | Transpose, then reverse every row. O(n^2) time, O(1) space. |
| Merge Overlapping Intervals | Repeatedly compare and merge overlapping pairs. O(n^2). | Sort by start and merge in one pass. O(n log n). | Same sorted merge, reusing output list/in-place where possible. |
| Merge Two Sorted Arrays | Combine both arrays and sort. O((m+n) log(m+n)). | Use an extra merged array. O(m+n) space. | Fill from the back of nums1 with three pointers. O(m+n), O(1). |
| Find Duplicate in Array | Compare every pair. O(n^2). | Use sorting or a frequency set. O(n log n) or O(n) extra space. | Floyd cycle detection on index-to-value links. O(n), O(1). |
| Repeat and Missing Number | Count each number by scanning the array. O(n^2). | Use a frequency array. O(n) time, O(n) space. | Use math equations or XOR. O(n) time, O(1) space. |
| Count Inversions in Array | Check every pair. O(n^2). | Use Fenwick tree with coordinate compression. O(n log n). | Count during merge sort. O(n log n), O(n) space. |

---

## Rotate Matrix (Image)

**LeetCode 48** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/rotate-image/)

### Problem
Rotate an `n×n` matrix 90° clockwise in-place.

### Approach

**Key insight:** Rotating 90° clockwise = **Transpose + Reverse each row**

1. **Transpose:** `matrix[i][j] ↔ matrix[j][i]`
2. **Reverse each row**

### Java Solution

```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        // Step 1: Transpose
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }

        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            int left = 0, right = n - 1;
            while (left < right) {
                int tmp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = tmp;
                left++; right--;
            }
        }
    }
}
```

**Complexity:** Time O(n²) · Space O(1)

> **Counter-clockwise 90°** = Transpose + Reverse each **column**

---

## Merge Overlapping Intervals

**LeetCode 56** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/merge-intervals/)

### Problem
Given a list of intervals, merge all overlapping intervals.

### Approach

1. **Sort** intervals by start time
2. Iterate and compare current interval's start with last merged interval's end:
   - If `current.start <= last.end` → merge by extending end: `Math.max(last.end, current.end)`
   - Else → add a new interval

### Java Solution

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> merged = new ArrayList<>();

        for (int[] interval : intervals) {
            if (merged.isEmpty() || merged.get(merged.size()-1)[1] < interval[0]) {
                merged.add(interval);
            } else {
                merged.get(merged.size()-1)[1] =
                    Math.max(merged.get(merged.size()-1)[1], interval[1]);
            }
        }
        return merged.toArray(new int[0][]);
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---

## Merge Two Sorted Arrays Without Extra Space

**LeetCode 88** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/merge-sorted-array/)

### Problem
Merge `nums2` into `nums1` in-place. `nums1` has enough space at the end.

### Approach

- Start filling from the **end** of `nums1` (avoid overwriting)
- Use three pointers: `i = m-1`, `j = n-1`, `k = m+n-1`
- Compare `nums1[i]` and `nums2[j]`, place the larger at `k`

### Java Solution

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;

        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }

        // Remaining nums2 elements
        while (j >= 0) nums1[k--] = nums2[j--];
    }
}
```

**Complexity:** Time O(m+n) · Space O(1)

---

## Find Duplicate in Array

**LeetCode 287** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/find-the-duplicate-number/)

### Problem
Array of `n+1` integers in range `[1,n]`. Find the one duplicate without modifying the array. O(1) extra space.

### Approach (Floyd's Cycle Detection)

- Treat array as a **linked list** where `index → nums[index]`
- Since there's a duplicate, there must be a cycle
- Use **slow/fast pointers** to detect cycle entry point

```
Phase 1: Find intersection inside cycle
  slow = nums[slow], fast = nums[nums[fast]]
Phase 2: Find cycle entry (= duplicate)
  Move slow from head, keep fast at intersection, both move 1 step
```

### Java Solution

```java
class Solution {
    public int findDuplicate(int[] nums) {
        // Phase 1: Detect cycle
        int slow = nums[0], fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Phase 2: Find entry point
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Repeat and Missing Number

**Problem:** Given array of size N with values 1 to N, one number is repeated and one is missing. Find both.

### Approach (Math)

Let:
- `S` = sum of array, `S_n` = n*(n+1)/2
- `S2` = sum of squares of array, `S2_n` = n*(n+1)*(2n+1)/6

Then:
- `S - S_n = repeat - missing` → equation 1
- `S2 - S2_n = repeat² - missing²` → divide by eq1 → `repeat + missing` → equation 2

Solve two equations for repeat and missing.

### Java Solution

```java
public int[] findMissingRepeating(int[] arr) {
    long n = arr.length;
    long S = 0, S2 = 0;
    for (int x : arr) { S += x; S2 += (long)x*x; }

    long Sn = n*(n+1)/2;
    long S2n = n*(n+1)*(2*n+1)/6;

    long diff = S - Sn;          // repeat - missing
    long diff2 = (S2 - S2n) / diff; // repeat + missing

    long repeat = (diff + diff2) / 2;
    long missing = repeat - diff;

    return new int[]{(int)repeat, (int)missing};
}
```

**Complexity:** Time O(n) · Space O(1)

---

## Count Inversions in Array

**Problem:** Count pairs (i, j) where `i < j` but `arr[i] > arr[j]`.

### Approach (Modified Merge Sort)

- During merge step, when `arr[right] < arr[left]`:
  - All remaining elements in left half form inversions with `arr[right]`
  - Count += `mid - left + 1`

### Java Solution

```java
class Solution {
    static long count = 0;

    public static long inversionCount(long[] arr) {
        count = 0;
        mergeSort(arr, 0, arr.length - 1);
        return count;
    }

    static void mergeSort(long[] arr, int l, int r) {
        if (l >= r) return;
        int mid = (l + r) / 2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }

    static void merge(long[] arr, int l, int mid, int r) {
        long[] temp = new long[r - l + 1];
        int i = l, j = mid + 1, k = 0;

        while (i <= mid && j <= r) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                count += (mid - i + 1); // all remaining left-half form inversions
                temp[k++] = arr[j++];
            }
        }
        while (i <= mid) temp[k++] = arr[i++];
        while (j <= r)   temp[k++] = arr[j++];
        for (int x = 0; x < temp.length; x++) arr[l + x] = temp[x];
    }
}
```

**Complexity:** Time O(n log n) · Space O(n)

---

## Interview Tips for Arrays II

> 💡 **Rotate = Transpose + Reverse** (remember this forever)
> 💡 **Inversions → Modified Merge Sort** (classic divide and conquer)
> 💡 **Floyd's Cycle** works whenever you can model the problem as a linked list

#sde-sheet #arrays #day2
