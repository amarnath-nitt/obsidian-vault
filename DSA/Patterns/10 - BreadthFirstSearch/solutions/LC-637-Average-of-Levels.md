# Average of Levels in Binary Tree (LC 637)

**Difficulty**: Easy  
**Pattern**: Breadth-First Search  
**LeetCode**: https://leetcode.com/problems/average-of-levels-in-binary-tree/

## Problem Statement
Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array.

**Example:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000, 14.50000, 11.00000]
```

## Approach: BFS

### Intuition
Standard BFS. Compute average for each level.
Use `double` sum to avoid overflow.

### Java Code
```java
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> result = new ArrayList<>();
        if (root == null) return result;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            double sum = 0;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode curr = queue.poll();
                sum += curr.val;
                
                if (curr.left != null) queue.offer(curr.left);
                if (curr.right != null) queue.offer(curr.right);
            }
            result.add(sum / levelSize);
        }
        
        return result;
    }
}
```

### Complexity
- **Time**: O(N)
- **Space**: O(N)

## Key Takeaways
- Simple variation of Level Order
