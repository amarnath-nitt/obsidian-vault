# Course Schedule

**Difficulty:** Medium  
**Category:** Graphs  
**LeetCode Link:** [Course Schedule](https://leetcode.com/problems/course-schedule/)

---

## Approach: Topological Sort (DFS)

### Java Code
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
        }
        
        int[] visited = new int[numCourses];  // 0=unvisited, 1=visiting, 2=visited
        
        for (int i = 0; i < numCourses; i++) {
            if (hasCycle(graph, visited, i)) {
                return false;
            }
        }
        
        return true;
    }
    
    private boolean hasCycle(List<List<Integer>> graph, int[] visited, int course) {
        if (visited[course] == 1) return true;  // Cycle detected
        if (visited[course] == 2) return false;  // Already processed
        
        visited[course] = 1;  // Mark as visiting
        
        for (int next : graph.get(course)) {
            if (hasCycle(graph, visited, next)) {
                return true;
            }
        }
        
        visited[course] = 2;  // Mark as visited
        return false;
    }
}
```

### Complexity
- **Time:** O(V + E)
- **Space:** O(V + E)

---

## Tags
#graphs #topological-sort #dfs #medium #blind75
