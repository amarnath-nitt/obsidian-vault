# Activity Selection / Minimum Arrows to Burst Balloons

**LeetCode 452** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

### Problem
Balloons represented as intervals. Minimum arrows to burst all (arrow at x bursts all balloons spanning x).

### Approach (Activity Selection / Greedy)

- Sort by **end coordinate**
- Shoot an arrow at the end of the first balloon
- Skip all balloons the arrow hits
- Next arrow at the next unpopped balloon's end

### Java Solution

```java
class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));

        int arrows = 1;
        int arrowPos = points[0][1];

        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > arrowPos) { // balloon starts after current arrow
                arrows++;
                arrowPos = points[i][1];
            }
        }
        return arrows;
    }
}
```

**Complexity:** Time O(n log n) · Space O(1)

---
