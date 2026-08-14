# Rotate Image

**Difficulty:** Medium  
**Category:** Matrix  
**LeetCode Link:** [Rotate Image](https://leetcode.com/problems/rotate-image/)

---

## Problem Statement

You are given an `n x n` 2D matrix representing an image, rotate the image by **90 degrees (clockwise)**.

You have to rotate the image **in-place**.

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Constraints:**
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`

---

## Intuition

Rotating 90° clockwise = Transpose + Reverse each row.

---

## Approach: Transpose then Reverse

### Algorithm
1. **Transpose:** Swap matrix[i][j] with matrix[j][i]
2. **Reverse:** Reverse each row

### Java Code
```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        
        // Step 1: Transpose
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            int left = 0, right = n - 1;
            while (left < right) {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left++;
                right--;
            }
        }
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) - In-place

---

## Key Takeaways

1. **Pattern:** Transpose + Reverse = 90° rotation
2. **In-place:** No extra matrix needed
3. **Two steps:** Easier than rotating directly

---

## Tags
#matrix #math #medium #blind75

---

## Visualization

- Embed: `![](../assets/rotate-image/step-1.svg)`
- Obsidian embed: `![[../assets/rotate-image/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="420" height="160">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="24" fill="#222">Matrix transpose + reverse rows</text>
    <g transform="translate(20,40)">
        <rect x="0" y="0" width="30" height="30" fill="#fff" stroke="#4b6cc1"/>
        <rect x="34" y="0" width="30" height="30" fill="#fff" stroke="#4b6cc1"/>
        <rect x="68" y="0" width="30" height="30" fill="#fff" stroke="#4b6cc1"/>
    </g>
</svg>
