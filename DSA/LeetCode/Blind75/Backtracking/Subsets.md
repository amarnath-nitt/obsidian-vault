# Subsets

**Difficulty:** Medium  
**Category:** Backtracking  
**LeetCode Link:** [Subsets](https://leetcode.com/problems/subsets/)

---

## Approach: Backtracking

### Java Code
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] nums, int start, List<Integer> current, List<List<Integer>> result) {
        result.add(new ArrayList<>(current));
        
        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);
            backtrack(nums, i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
}
```

### Complexity
- **Time:** O(2^n)
- **Space:** O(n)

---

## Tags
#backtracking #medium #blind75

---

## Visualization

- Embed: `![](../assets/subsets/step-1.svg)`
- Obsidian embed: `![[../assets/subsets/step-1.svg]]`

<svg xmlns="http://www.w3.org/2000/svg" width="720" height="120">
    <style>text{font-family: Arial, sans-serif; font-size:13px}</style>
    <text x="20" y="24" fill="#222">Backtracking tree (subsets)</text>
    <g transform="translate(20,40)">
        <circle cx="40" cy="0" r="12" fill="#fff" stroke="#4b6cc1"/>
        <text x="40" y="4" text-anchor="middle">[]</text>
        <circle cx="120" cy="-20" r="12" fill="#fff" stroke="#4b6cc1"/>
        <text x="120" y="-16" text-anchor="middle">[1]</text>
        <circle cx="120" cy="20" r="12" fill="#fff" stroke="#4b6cc1"/>
        <text x="120" y="24" text-anchor="middle">[2]</text>
    </g>
</svg>
