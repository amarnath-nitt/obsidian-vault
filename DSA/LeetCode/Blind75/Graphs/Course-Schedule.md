# Course Schedule

**Difficulty:** Medium
**Category:** Graphs
**LeetCode Link:** [Course Schedule](https://leetcode.com/problems/course-schedule/)

---

## Problem Statement

There are `numCourses` courses labeled `0` to `numCourses-1`. Given `prerequisites[i] = [a, b]` meaning you must take course `b` before `a`, determine if it's possible to finish all courses.

**Example:**
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false  (cycle: 0 → 1 → 0)
```

---

## Intuition

This is a cycle detection problem on a directed graph. If there's a cycle in the prerequisite graph, it's impossible to finish all courses. Use DFS with 3-color marking: unvisited (0), currently visiting (1), fully processed (2).

---

## Approach 1: DFS Cycle Detection (3-color)

### Algorithm
1. Build adjacency list from prerequisites
2. For each unvisited node, run DFS
3. Mark node as "visiting" (1) when entering, "visited" (2) when done
4. If we reach a node marked "visiting", we found a cycle

### Java Code
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());

        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
        }

        int[] visited = new int[numCourses]; // 0=unvisited, 1=visiting, 2=done

        for (int i = 0; i < numCourses; i++) {
            if (hasCycle(graph, visited, i)) return false;
        }

        return true;
    }

    private boolean hasCycle(List<List<Integer>> graph, int[] visited, int course) {
        if (visited[course] == 1) return true;  // Back edge = cycle
        if (visited[course] == 2) return false; // Already fully processed

        visited[course] = 1;

        for (int next : graph.get(course)) {
            if (hasCycle(graph, visited, next)) return true;
        }

        visited[course] = 2;
        return false;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(V + E) — visit every node and edge
- **Space Complexity:** O(V + E) — graph + visited array

---

## Approach 2: Kahn's Algorithm (BFS Topological Sort)

### Algorithm
1. Compute in-degrees for all nodes
2. Add all nodes with in-degree 0 to queue
3. Process queue: reduce neighbors' in-degrees; add to queue if in-degree becomes 0
4. If processed count == numCourses, no cycle

### Java Code
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());

        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
            inDegree[prereq[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) queue.offer(i);
        }

        int processed = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            processed++;
            for (int next : graph.get(course)) {
                if (--inDegree[next] == 0) queue.offer(next);
            }
        }

        return processed == numCourses;
    }
}
```

### Complexity Analysis
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V + E)

---

## Key Takeaways

1. **Pattern:** Cycle detection in directed graph = course scheduling
2. **3-color DFS:** 0=unvisited, 1=in-stack (visiting), 2=done
3. **Kahn's BFS:** Topological sort — if all nodes processed, no cycle

---

## Tags
#graphs #topological-sort #dfs #medium #blind75
