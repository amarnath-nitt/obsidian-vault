# Pascal's Triangle

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
