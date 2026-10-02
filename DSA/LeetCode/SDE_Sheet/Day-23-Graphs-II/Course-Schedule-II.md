# Course Schedule II

**LeetCode 210** · Medium
🔗 [LeetCode Link](https://leetcode.com/problems/course-schedule-ii/)

### Problem
Return the order to take courses. Return empty if impossible.

### Java Solution (same as Kahn's — collect order)

```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDegree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());

        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]);
            inDegree[pre[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++)
            if (inDegree[i] == 0) queue.offer(i);

        int[] order = new int[numCourses];
        int idx = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            order[idx++] = course;
            for (int next : adj.get(course))
                if (--inDegree[next] == 0) queue.offer(next);
        }
        return idx == numCourses ? order : new int[]{};
    }
}
```

---
