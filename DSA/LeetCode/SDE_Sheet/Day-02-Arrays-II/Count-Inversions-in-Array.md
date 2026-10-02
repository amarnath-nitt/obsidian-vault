# Count Inversions in Array

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
