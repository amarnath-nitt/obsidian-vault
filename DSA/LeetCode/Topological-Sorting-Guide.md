# Topological Sorting - Complete Guide

**Category:** Graph Algorithms  
**Difficulty Level:** Medium to Hard  
**Common Use Cases:** Task scheduling, dependency resolution, build systems

---

## 📚 What is Topological Sorting?

Topological sorting is a **linear ordering of vertices** in a Directed Acyclic Graph (DAG) such that for every directed edge `(u, v)`, vertex `u` comes before vertex `v` in the ordering.

### Key Properties
- ✅ Only works on **Directed Acyclic Graphs (DAG)**
- ✅ If the graph has a cycle, topological sorting is **impossible**
- ✅ A DAG can have **multiple valid topological orderings**

### Real-World Applications
1. **Course Prerequisites** - Determine valid course ordering
2. **Build Systems** - Compile dependencies in correct order
3. **Task Scheduling** - Execute tasks respecting dependencies
4. **Package Managers** - Resolve installation order
5. **Compilation** - Determine file compilation order

---

## 🔍 Two Main Approaches

### 1. DFS-Based Approach (Using Stack)

**Algorithm:**
1. Perform DFS traversal
2. After visiting all neighbors, **push to stack**
3. Final ordering = pop elements from stack

**Pseudocode:**
```
function topologicalSort(graph):
    stack = []
    visited = set()
    
    for each vertex in graph:
        if vertex not in visited:
            dfs(vertex, visited, stack)
    
    return reverse(stack)

function dfs(vertex, visited, stack):
    visited.add(vertex)
    
    for each neighbor of vertex:
        if neighbor not in visited:
            dfs(neighbor, visited, stack)
    
    stack.push(vertex)  // Key: push after processing all neighbors
```

**When to Use:**
- Need to detect cycles
- Simpler recursive implementation
- Memory is not constrained (recursion stack)

---

### 2. Kahn's Algorithm (BFS-Based)

**Algorithm:**
1. Calculate **in-degree** for each vertex
2. Add all vertices with in-degree = 0 to queue
3. Process queue:
   - Remove vertex, add to result
   - Decrease in-degree of neighbors
   - If neighbor's in-degree becomes 0, add to queue
4. If result contains all vertices → valid topological order
5. Otherwise → **cycle detected**

**Pseudocode:**
```
function kahnTopologicalSort(graph):
    inDegree = calculate in-degrees for all vertices
    queue = []
    result = []
    
    // Add all vertices with in-degree 0
    for each vertex in graph:
        if inDegree[vertex] == 0:
            queue.add(vertex)
    
    while queue is not empty:
        vertex = queue.remove()
        result.add(vertex)
        
        for each neighbor of vertex:
            inDegree[neighbor]--
            if inDegree[neighbor] == 0:
                queue.add(neighbor)
    
    // If result doesn't contain all vertices, cycle exists
    return result if result.size == V else []
```

**When to Use:**
- Need explicit cycle detection
- Prefer iterative over recursive
- Want to process nodes level-by-level
- Building actual ordering (not just checking validity)

---

## 🆚 DFS vs Kahn's Algorithm

| Feature | DFS Approach | Kahn's Algorithm |
|---------|-------------|------------------|
| **Implementation** | Recursive | Iterative (BFS) |
| **Cycle Detection** | Requires extra state tracking | Built-in (check result size) |
| **Space Complexity** | O(V) stack space | O(V) queue space |
| **Intuition** | "Finish last, appears first" | "Process nodes with no dependencies" |
| **Output Order** | Reverse post-order | Natural order |

---

## 💡 Key Patterns & Tips

### Pattern 1: Cycle Detection
```java
// DFS with 3 states: 0=unvisited, 1=visiting, 2=visited
int[] state = new int[n];

boolean hasCycle(int node) {
    if (state[node] == 1) return true;  // Back edge = cycle
    if (state[node] == 2) return false; // Already processed
    
    state[node] = 1;  // Mark as visiting
    for (int neighbor : graph[node]) {
        if (hasCycle(neighbor)) return true;
    }
    state[node] = 2;  // Mark as visited
    return false;
}
```

### Pattern 2: Building Graph from Prerequisites
```java
// prerequisites[i] = [a, b] means b → a (b must come before a)
List<List<Integer>> graph = new ArrayList<>();
for (int i = 0; i < n; i++) {
    graph.add(new ArrayList<>());
}

for (int[] prereq : prerequisites) {
    graph.get(prereq[1]).add(prereq[0]);
}
```

### Pattern 3: In-Degree Calculation
```java
int[] inDegree = new int[n];
for (int i = 0; i < n; i++) {
    for (int neighbor : graph.get(i)) {
        inDegree[neighbor]++;
    }
}
```

---

## 🎯 Common Problem Types

### Type 1: Is Topological Sort Possible?
- Check if course schedule is valid
- Detect circular dependencies
- **Approach:** Either DFS cycle detection or Kahn's algorithm

### Type 2: Find All Possible Orders
- Generate all valid topological orderings
- **Approach:** Backtracking with topological constraints

### Type 3: Lexicographically Smallest Order
- Among multiple valid orders, find smallest
- **Approach:** Kahn's with PriorityQueue instead of regular queue

### Type 4: Find Specific Ordering
- Alien dictionary character ordering
- **Approach:** Build graph from constraints, then topological sort

---

## 🧩 Practice Problem Checklist

- [ ] [Course Schedule](Course-Schedule.md) - Basic cycle detection
- [ ] [Course Schedule II](Course-Schedule-II.md) - Return actual ordering
- [ ] [Course Schedule IV](Course-Schedule-IV.md) - Query prerequisites
- [ ] [Alien Dictionary](Alien-Dictionary.md) - Build graph from words
- [ ] [Minimum Height Trees](Minimum-Height-Trees.md) - Reverse topo sort
- [ ] [Sequence Reconstruction](Sequence-Reconstruction.md) - Validate unique order
- [ ] [Parallel Courses](Parallel-Courses.md) - Minimum semesters
- [ ] [Find All Recipes](Find-All-Recipes.md) - Multiple dependencies

---

## 📌 Interview Tips

1. **Always Ask:** Is the graph guaranteed to be a DAG?
2. **Clarify:** Do we need the actual ordering or just validation?
3. **Consider:** Are there multiple valid orderings? Which one to return?
4. **Edge Cases:**
   - Empty graph
   - Single node
   - Disconnected components
   - Self-loops (immediate cycle)
   - Duplicate edges

---

## 🔗 Related Concepts

- **Strongly Connected Components** - Kosaraju's/Tarjan's Algorithm
- **Union-Find** - Cycle detection in undirected graphs
- **Dependency Resolution** - Package managers, build systems
- **Critical Path Method** - Project management
- **Scheduling Problems** - Task dependencies

---

## Tags
#topological-sort #graphs #dfs #bfs #dag #cycle-detection #kahns-algorithm #scheduling
