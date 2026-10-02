# Rotate Matrix (Image)

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
