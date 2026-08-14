# Assign Cookies (LC 455)

**Difficulty**: Easy  
**Pattern**: Greedy  
**LeetCode**: https://leetcode.com/problems/assign-cookies/

## Problem Statement
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

**Example:**
```
Input: g = [1,2,3], s = [1,1]
Output: 1
```

## Approach: Sort and Match

### Intuition
Sort children `g` and cookies `s`.
Give the smallest cookie that satisfies content child.
Greedily satisfy easiest-to-satisfy children first using smallest sufficient resources.

### Java Code
```java
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        
        int child = 0;
        int cookie = 0;
        
        while (child < g.length && cookie < s.length) {
            if (s[cookie] >= g[child]) {
                child++;
            }
            cookie++;
        }
        
        return child;
    }
}
```

### Complexity
- **Time**: O(N log N + M log M)
- **Space**: O(log N) sorting

## Key Takeaways
- Basic Greedy sorting strategy
