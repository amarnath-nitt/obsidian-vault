# Course Schedule II

**Difficulty:** Medium  
**Category:** Graphs / Topological Sort  
**LeetCode Link:** [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

---

## Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

**Example 1:**
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are 2 courses. To take course 1, you must first take course 0.
```

**Example 2:**
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] or [0,1,2,3]
```

---

## Approach 1: Kahn's Algorithm (BFS)

### Algorithm
1. Build adjacency list and calculate in-degrees
2. Add all courses with in-degree 0 to queue
3. Process queue, adding to result and reducing neighbors' in-degrees
4. If result size != numCourses, cycle exists

### Java Code
```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // Build graph
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
            inDegree[prereq[0]]++;
        }
        
        // Kahn's algorithm
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        int[] result = new int[numCourses];
        int index = 0;
        
        while (!queue.isEmpty()) {
            int course = queue.poll();
            result[index++] = course;
            
            for (int next : graph.get(course)) {
                inDegree[next]--;
                if (inDegree[next] == 0) {
                    queue.offer(next);
                }
            }
        }
        
        return index == numCourses ? result : new int[0];
    }
}
```

### Complexity
- **Time:** O(V + E)
- **Space:** O(V + E)

---

## Approach 2: DFS with Stack

### Algorithm
1. Build adjacency list
2. Use DFS to detect cycles (3-color marking)
3. Push to stack after processing all neighbors
4. Reverse stack for final order

### Java Code
```java
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
        }
        
        int[] state = new int[numCourses];  // 0=unvisited, 1=visiting, 2=visited
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < numCourses; i++) {
            if (hasCycle(graph, state, i, stack)) {
                return new int[0];
            }
        }
        
        int[] result = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            result[i] = stack.pop();
        }
        
        return result;
    }
    
    private boolean hasCycle(List<List<Integer>> graph, int[] state, int course, Stack<Integer> stack) {
        if (state[course] == 1) return true;   // Cycle detected
        if (state[course] == 2) return false;  // Already processed
        
        state[course] = 1;  // Mark as visiting
        
        for (int next : graph.get(course)) {
            if (hasCycle(graph, state, next, stack)) {
                return true;
            }
        }
        
        state[course] = 2;  // Mark as visited
        stack.push(course);
        return false;
    }
}
```

### Complexity
- **Time:** O(V + E)
- **Space:** O(V + E)

---

## Key Insights
- This is an extension of Course Schedule I - need actual ordering, not just validation
- Kahn's algorithm naturally produces valid order
- DFS approach needs to reverse the stack
- Both approaches have same time/space complexity

---

## Tags
#topological-sort #graphs #bfs #dfs #kahns-algorithm #medium #leetcode-medium
