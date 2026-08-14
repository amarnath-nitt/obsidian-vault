# Course Schedule II

[Problem Link](https://leetcode.com/problems/course-schedule-ii/)

## Problem Statement
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## Approach
Topological Sort (Kahn's Algorithm).
1.  Build graph and calculate in-degrees.
2.  Queue for nodes with 0 in-degree.
3.  Process queue: add to result, decrement neighbor in-degrees.
4.  If result size == numCourses, valid. Else cycle exists.

## Time and Space Complexity
- **Time Complexity:** O(V + E).
- **Space Complexity:** O(V + E).

## Code
```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
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
        
        int[] result = new int[numCourses];
        int index = 0;
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            result[index++] = node;
            
            for (int neighbor : graph.get(node)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        return index == numCourses ? result : new int[0];
    }
}
```
