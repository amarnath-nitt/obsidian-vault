# Find All Recipes From Given Supplies

**Difficulty:** Medium  
**Category:** Graphs / Topological Sort  
**LeetCode Link:** [Find All Recipes](https://leetcode.com/problems/find-all-recipes-from-given-supplies/)

---

## Problem Statement

You have information about `n` different recipes. You are given a string array `recipes` and a 2D string array `ingredients`. The ith recipe has the name `recipes[i]`, and you can create it if you have all the needed ingredients from `ingredients[i]`. Ingredients to a recipe may need to be created from other recipes.

You are also given a string array `supplies` containing all the ingredients that you initially have.

Return a list of all the recipes that you can create. You may return the answer in any order.

**Example:**
```
Input: 
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]

Output: ["bread","sandwich","burger"]

Explanation:
- We can create "bread" since we have "yeast" and "flour"
- We can create "sandwich" since we have "bread" and "meat"
- We can create "burger" since we have "sandwich", "meat", and "bread"
```

---

## Intuition

This is a **dependency resolution** problem - perfect for topological sort!

Think of it as:
- **Recipes** = nodes we want to reach
- **Ingredients** = dependencies
- **Supplies** = starting nodes (in-degree 0)

Key insight: A recipe can be made if all its ingredient dependencies are resolved.

---

## Approach: Kahn's Algorithm with Initial Supplies

### Algorithm
1. Build graph: ingredient → recipes that need it
2. Calculate in-degrees (number of ingredients needed)
3. Start with supplies (already available ingredients)
4. Process queue: mark ingredients as available
5. When a recipe's in-degree reaches 0, it can be made

### Java Code
```java
class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        // Build graph and in-degree map
        Map<String, List<String>> graph = new HashMap<>();
        Map<String, Integer> inDegree = new HashMap<>();
        Set<String> recipeSet = new HashSet<>(Arrays.asList(recipes));
        
        // Initialize recipes
        for (int i = 0; i < recipes.length; i++) {
            String recipe = recipes[i];
            inDegree.put(recipe, 0);
            
            for (String ingredient : ingredients.get(i)) {
                // Only count ingredients that are recipes (dependencies)
                if (recipeSet.contains(ingredient)) {
                    inDegree.put(recipe, inDegree.get(recipe) + 1);
                    graph.computeIfAbsent(ingredient, k -> new ArrayList<>()).add(recipe);
                }
            }
        }
        
        // Start with supplies - these are "free" ingredients
        Queue<String> queue = new LinkedList<>();
        
        // Also add recipes that have no dependencies
        for (String recipe : recipes) {
            if (inDegree.get(recipe) == 0) {
                queue.offer(recipe);
            }
        }
        
        // Add supplies to queue (they enable recipes)
        Set<String> available = new HashSet<>(Arrays.asList(supplies));
        for (String supply : supplies) {
            if (graph.containsKey(supply)) {
                for (String recipe : graph.get(supply)) {
                    inDegree.put(recipe, inDegree.get(recipe) - 1);
                    if (inDegree.get(recipe) == 0) {
                        queue.offer(recipe);
                    }
                }
            }
        }
        
        List<String> result = new ArrayList<>();
        
        while (!queue.isEmpty()) {
            String recipe = queue.poll();
            result.add(recipe);
            
            // This recipe is now available as an ingredient
            if (graph.containsKey(recipe)) {
                for (String nextRecipe : graph.get(recipe)) {
                    inDegree.put(nextRecipe, inDegree.get(nextRecipe) - 1);
                    if (inDegree.get(nextRecipe) == 0) {
                        queue.offer(nextRecipe);
                    }
                }
            }
        }
        
        return result;
    }
}
```

### Complexity
- **Time:** O(R + I) where R = recipes, I = total ingredients
- **Space:** O(R + I)

---

## Cleaner Implementation

```java
class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, 
                                       String[] supplies) {
        Map<String, Set<String>> graph = new HashMap<>();
        Map<String, Integer> inDegree = new HashMap<>();
        
        // Build graph
        for (int i = 0; i < recipes.length; i++) {
            String recipe = recipes[i];
            inDegree.put(recipe, ingredients.get(i).size());
            
            for (String ing : ingredients.get(i)) {
                graph.computeIfAbsent(ing, k -> new HashSet<>()).add(recipe);
            }
        }
        
        // BFS with supplies
        Queue<String> queue = new LinkedList<>(Arrays.asList(supplies));
        List<String> result = new ArrayList<>();
        
        while (!queue.isEmpty()) {
            String item = queue.poll();
            
            if (inDegree.containsKey(item) && inDegree.get(item) == 0) {
                result.add(item);
            }
            
            if (graph.containsKey(item)) {
                for (String recipe : graph.get(item)) {
                    inDegree.put(recipe, inDegree.get(recipe) - 1);
                    if (inDegree.get(recipe) == 0) {
                        queue.offer(recipe);
                    }
                }
            }
        }
        
        return result;
    }
}
```

---

## Key Insights

1. **Multi-level dependencies** - Recipes can depend on other recipes
2. **Initial available nodes** - Unlike classic topological sort, we start with supplies
3. **Only recipes are nodes** - Supplies are just enablers
4. **In-degree = ingredients needed** - Recipe ready when in-degree = 0

---

## Pattern Recognition

This is **Kahn's Algorithm with multiple starting points**:
- Classic: Start with nodes having in-degree = 0
- Here: Start with **supplies** (pre-available ingredients)

Similar problems:
- Package dependency resolution
- Task scheduling with initial resources
- Build systems with pre-compiled modules

---

## Edge Cases

- Recipe needs only supplies → in-degree = 0 initially
- Recipe needs another recipe that can't be made → never added to result
- Circular dependencies → some recipes won't be made
- Empty supplies → only recipes with no dependencies can be made

---

## Tags
#topological-sort #graphs #kahns-algorithm #dependency-resolution #medium #bfs
