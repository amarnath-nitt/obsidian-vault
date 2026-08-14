# Sort Items by Groups Respecting Dependencies

**Difficulty:** Hard  
**Category:** Graphs / Topological Sort  
**LeetCode Link:** [Sort Items by Groups](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/)

---

## Problem Statement

There are `n` items each belonging to zero or one of `m` groups where `group[i]` is the group that the i-th item belongs to. If `group[i] = -1`, the i-th item belongs to no group.

Given the items, the group they belong to, and a list indicating which items come before others, return a sorted list of items. If there is no solution, return an empty list.

**Example:**
```
Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], 
       beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
```

---

## Intuition

This is a **two-level topological sort** problem:

1. **Group-level topological sort** - Order the groups
2. **Item-level topological sort** - Order items within each group

Key insight: If group A must come before group B, then ALL items in A must come before ALL items in B.

---

## Approach: Double Topological Sort

### Algorithm
1. Assign unique group IDs to ungrouped items (-1)
2. Build TWO graphs:
   - **Group graph**: dependencies between groups
   - **Item graph**: dependencies between items
3. Perform topological sort on groups
4. Perform topological sort on items within each group
5. Combine results respecting group order

### Java Code
```java
class Solution {
    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        // Assign unique groups to ungrouped items
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                group[i] = m++;
            }
        }
        
        // Build graphs
        List<List<Integer>> itemGraph = new ArrayList<>();
        List<List<Integer>> groupGraph = new ArrayList<>();
        int[] itemInDegree = new int[n];
        int[] groupInDegree = new int[m];
        
        for (int i = 0; i < n; i++) {
            itemGraph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            groupGraph.add(new ArrayList<>());
        }
        
        // Build edges
        for (int i = 0; i < n; i++) {
            for (int before : beforeItems.get(i)) {
                // Item graph edge
                itemGraph.get(before).add(i);
                itemInDegree[i]++;
                
                // Group graph edge (if different groups)
                if (group[before] != group[i]) {
                    int fromGroup = group[before];
                    int toGroup = group[i];
                    
                    // Avoid duplicate edges
                    if (!groupGraph.get(fromGroup).contains(toGroup)) {
                        groupGraph.get(fromGroup).add(toGroup);
                        groupInDegree[toGroup]++;
                    }
                }
            }
        }
        
        // Topological sort for groups
        List<Integer> groupOrder = topologicalSort(groupGraph, groupInDegree, m);
        if (groupOrder.isEmpty()) return new int[0];
        
        // Topological sort for items
        List<Integer> itemOrder = topologicalSort(itemGraph, itemInDegree, n);
        if (itemOrder.isEmpty()) return new int[0];
        
        // Group items by their group
        Map<Integer, List<Integer>> groupToItems = new HashMap<>();
        for (int item : itemOrder) {
            int g = group[item];
            groupToItems.computeIfAbsent(g, k -> new ArrayList<>()).add(item);
        }
        
        // Build final result
        List<Integer> result = new ArrayList<>();
        for (int g : groupOrder) {
            if (groupToItems.containsKey(g)) {
                result.addAll(groupToItems.get(g));
            }
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
    
    private List<Integer> topologicalSort(List<List<Integer>> graph, int[] inDegree, int count) {
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < count; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        List<Integer> result = new ArrayList<>();
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            result.add(node);
            
            for (int neighbor : graph.get(node)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        return result.size() == count ? result : new ArrayList<>();
    }
}
```

### Complexity
- **Time:** O(n + m + edges) - Two topological sorts
- **Space:** O(n + m + edges)

---

## Key Insights

1. **Two-level sorting** - Groups first, then items within groups
2. **Handle ungrouped items** - Assign unique group IDs
3. **Avoid duplicate group edges** - Multiple items can create same group dependency
4. **Validate both sorts** - Either can fail due to cycles

---

## Common Pitfalls

❌ Forgetting to assign groups to -1 items  
❌ Not handling duplicate group edges  
❌ Sorting items before considering group order  
❌ Not validating group-level topological sort

---

## Visual Example

```
Items: [0,1,2,3]
Groups: [0,0,1,1]
Dependencies: 0→1, 2→3, 0→2

Step 1: Group dependencies
  Group 0 → Group 1 (because 0→2)

Step 2: Group order
  [0, 1]

Step 3: Item order within groups
  Group 0: [0, 1]
  Group 1: [2, 3]

Result: [0, 1, 2, 3]
```

---

## Pattern Template

```java
// Two-level topological sort pattern
1. Normalize groups (handle -1)
2. Build item graph + group graph simultaneously
3. Topological sort groups
4. Topological sort items
5. Combine: for each group in order, add its items
```

---

## Tags
#topological-sort #graphs #kahns-algorithm #two-level-sort #hard #complex-constraints
