# Course Schedule

[Problem Link](https://leetcode.com/problems/course-schedule/)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.
Return `true` if you can finish all courses. Otherwise, return `false`.

## Approach
Topological Sort (Kahn's Algorithm) or DFS Cycle Detection.
Kahn's Algorithm:
1.  Calculate in-degrees.
2.  Queue all 0 in-degree nodes.
3.  Process queue, increment visited count.
4.  If visited count == numCourses, true.

## Time and Space Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V + E).

## Code
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        
        int[] inDegree = new int[numCourses];
        for (int[] p : prerequisites) {
            graph.get(p[1]).add(p[0]);
            inDegree[p[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        int count = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            count++;
            
            for (int neighbor : graph.get(node)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        return count == numCourses;
    }
}
```
