# Topological Sorting - Practice Problems

**Quick Navigation:** [Main Guide](../Topological-Sorting-Guide.md)

---

## 📊 Problem Difficulty Distribution

| Difficulty | Count | Problems |
|------------|-------|----------|
| **Easy** | 2 | Find if Path Exists, Build a Matrix |
| **Medium** | 8 | Course Schedule, Course Schedule II, Min Height Trees, Parallel Courses, etc. |
| **Hard** | 4 | Alien Dictionary, Sequence Reconstruction, Sort Items by Groups, etc. |

---

## 🎯 Essential Problems (Must Practice)

### 1. Foundation Problems
- ✅ [Course Schedule](Course-Schedule.md) - **Start Here!**
- ✅ [Course Schedule II](Course-Schedule-II.md)
- [ ] [Alien Dictionary](Alien-Dictionary.md) - **Premium**

### 2. Intermediate
- [ ] Minimum Height Trees (LeetCode 310)
- [ ] Course Schedule IV (LeetCode 1462)
- [ ] Parallel Courses (LeetCode 1136) - **Premium**

### 3. Advanced
- [ ] Sequence Reconstruction (LeetCode 444) - **Premium**
- [ ] Sort Items by Groups (LeetCode 1203)
- [ ] Find All Recipes (LeetCode 2115)

---

## 📝 All Practice Problems

### Cycle Detection Pattern

#### [Course Schedule](Course-Schedule.md)
- **Difficulty:** Medium
- **Focus:** Basic cycle detection using DFS
- **Key Concept:** 3-state coloring (unvisited, visiting, visited)

#### Course Schedule IV (LeetCode 1462)
- **Difficulty:** Medium
- **Focus:** Query prerequisites using topological sort
- **Key Concept:** Reachability in DAG

---

### Build Ordering Pattern

#### [Course Schedule II](Course-Schedule-II.md)
- **Difficulty:** Medium
- **Focus:** Return actual topological ordering
- **Approach:** Kahn's algorithm or DFS with stack

#### Parallel Courses (LeetCode 1136)
- **Difficulty:** Medium
- **Focus:** Minimum semesters to complete all courses
- **Key Concept:** Level-by-level BFS in topological sort

#### Parallel Courses II (LeetCode 1494)
- **Difficulty:** Hard
- **Focus:** Limited capacity per semester
- **Approach:** Bitmask DP + Topological sort

---

### Graph Construction Pattern

#### [Alien Dictionary](Alien-Dictionary.md)
- **Difficulty:** Hard
- **Focus:** Build graph from word ordering
- **Key Concept:** Compare adjacent words to derive character order

#### Sequence Reconstruction (LeetCode 444)
- **Difficulty:** Medium (Premium)
- **Focus:** Check if sequences uniquely determine order
- **Key Concept:** Verify only one valid topological ordering exists

---

### Tree/Graph Variations

#### Minimum Height Trees (LeetCode 310)
- **Difficulty:** Medium
- **Focus:** Find tree centers using reverse topological sort
- **Approach:** Remove leaves layer by layer (like Kahn's in reverse)

#### Find All Recipes (LeetCode 2115)
- **Difficulty:** Medium
- **Focus:** Multiple dependencies with available ingredients
- **Key Concept:** Topological sort with initial available nodes

---

### Complex Constraints

#### Sort Items by Groups Respecting Dependencies (LeetCode 1203)
- **Difficulty:** Hard
- **Focus:** Two-level topological sort
- **Approach:** Sort groups, then sort items within each group

#### Build a Matrix With Conditions (LeetCode 2392)
- **Difficulty:** Hard
- **Focus:** Construct matrix satisfying row/column constraints
- **Approach:** Two separate topological sorts

---

## 🗺️ Learning Path

### Week 1: Foundations
1. Read [Main Guide](../Topological-Sorting-Guide.md)
2. Solve Course Schedule (DFS approach)
3. Solve Course Schedule II (Kahn's approach)
4. Understand both algorithms deeply

### Week 2: Graph Construction
1. Solve Alien Dictionary
2. Practice building graphs from constraints
3. Handle edge cases (invalid orderings)

### Week 3: Advanced Patterns
1. Minimum Height Trees
2. Parallel Courses
3. Find All Recipes

### Week 4: Hard Problems
1. Sort Items by Groups
2. Sequence Reconstruction
3. Build a Matrix With Conditions

---

## 💡 Quick Reference - Algorithm Choice

| Problem Type | Recommended Approach | Why? |
|--------------|---------------------|------|
| Just detect cycle | DFS with 3-state | Simpler implementation |
| Need actual ordering | Kahn's Algorithm | Natural order output |
| Find all orderings | Backtracking | Explore all possibilities |
| Lexicographically smallest | Kahn's + PriorityQueue | Process smallest first |
| Level-wise processing | Kahn's Algorithm | BFS naturally handles levels |

---

## 🔄 Common Patterns & Templates

### Template 1: Kahn's Algorithm
```java
public List<Integer> topologicalSort(List<List<Integer>> graph, int n) {
    int[] inDegree = new int[n];
    for (int i = 0; i < n; i++) {
        for (int neighbor : graph.get(i)) {
            inDegree[neighbor]++;
        }
    }
    
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < n; i++) {
        if (inDegree[i] == 0) queue.offer(i);
    }
    
    List<Integer> result = new ArrayList<>();
    while (!queue.isEmpty()) {
        int node = queue.poll();
        result.add(node);
        
        for (int neighbor : graph.get(node)) {
            if (--inDegree[neighbor] == 0) {
                queue.offer(neighbor);
            }
        }
    }
    
    return result.size() == n ? result : new ArrayList<>();
}
```

### Template 2: DFS Cycle Detection
```java
public boolean hasCycle(List<List<Integer>> graph, int n) {
    int[] state = new int[n];  // 0=white, 1=gray, 2=black
    
    for (int i = 0; i < n; i++) {
        if (dfs(graph, state, i)) return true;
    }
    return false;
}

private boolean dfs(List<List<Integer>> graph, int[] state, int node) {
    if (state[node] == 1) return true;   // Back edge
    if (state[node] == 2) return false;  // Already done
    
    state[node] = 1;
    for (int neighbor : graph.get(node)) {
        if (dfs(graph, state, neighbor)) return true;
    }
    state[node] = 2;
    return false;
}
```

---

## 📈 Progress Tracker

Track your progress:
- [ ] Understand both DFS and Kahn's approaches
- [ ] Solved 3+ foundation problems
- [ ] Can detect cycles reliably
- [ ] Can build graphs from various inputs
- [ ] Solved at least 1 hard problem
- [ ] Can explain when to use which algorithm

---

## Tags
#topological-sort #practice-problems #leetcode #graphs #learning-path
