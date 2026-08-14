# Two Sum — Example

**Problem:**
- Title: Two Sum
- Link: https://leetcode.com/problems/two-sum/
- Difficulty: Easy

**Goal (one line):** Find indices of two numbers that add up to target.

**Intuition (explain like I'm 5):**
- Try all pairs to see which add to target (slow).
- Use a map to remember numbers we've seen so we can find complements quickly.

**Visual Guide:**
- Diagram: array indices with pointers and a hashmap snapshot.

**Approaches (ordered):**
1. Brute Force — check all pairs (O(n^2), O(1)).
2. Two-pass Hash Map — build map then find complements (O(n), O(n)).
3. One-pass Hash Map (optimal) — build and check in single loop (O(n), O(n)).

**Pseudocode (one-pass):**
- For i from 0 to n-1:
  - complement = target - nums[i]
  - if complement in map: return [map[complement], i]
  - store nums[i] -> i in map

**Step-by-step walkthrough (example: nums=[2,7,11,15], target=9):**
- i=0: map={}, complement=7 -> not found -> map={2:0}
- i=1: complement=2 -> found at index 0 -> return [0,1]

**Complexity:**
- Time: O(n)
- Space: O(n)

**Edge Cases:**
- No solution (depends on problem constraints — here guaranteed one solution).
- Negative numbers, zeros, duplicates.

**Tests (examples):**
- [2,7,11,15], 9 -> [0,1]
- [3,2,4], 6 -> [1,2]

**Implementation (Java):**
```java
import java.util.*;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (seen.containsKey(comp)) {
                return new int[] { seen.get(comp), i };
            }
            seen.put(nums[i], i);
        }
        return new int[0];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] res = s.twoSum(new int[]{2,7,11,15}, 9);
        System.out.println(Arrays.toString(res));
    }
}
```

**Visualization ideas / links:**
- Embedded image (works in Obsidian):

- `![](../assets/two-sum/step-1.svg)` — relative path from this file's folder `Templates` to the `assets` folder.
- Obsidian-style embed also supported: `![[../assets/two-sum/step-1.svg]]`.
- Notebook: `notebooks/two-sum-visual.ipynb` with an animated pointer.

**Inline fallback (renders in Obsidian preview if external image doesn't):**

<svg xmlns="http://www.w3.org/2000/svg" width="720" height="140">
    <style>text{font-family: Arial, sans-serif; font-size:14px}</style>
    <rect x="10" y="10" width="700" height="120" fill="#f8f9fb" stroke="#d1d7e0" rx="8"/>
    <g transform="translate(30,30)">
        <rect x="0" y="0" width="64" height="64" fill="#ffffff" stroke="#4b6cc1"/>
        <text x="32" y="40" text-anchor="middle" fill="#111">2</text>
        <rect x="84" y="0" width="64" height="64" fill="#ffffff" stroke="#4b6cc1"/>
        <text x="116" y="40" text-anchor="middle" fill="#111">7</text>
        <rect x="168" y="0" width="64" height="64" fill="#ffffff" stroke="#4b6cc1"/>
        <text x="200" y="40" text-anchor="middle" fill="#111">11</text>
        <rect x="252" y="0" width="64" height="64" fill="#ffffff" stroke="#4b6cc1"/>
        <text x="284" y="40" text-anchor="middle" fill="#111">15</text>
        <text x="360" y="22" fill="#333">Map snapshot:</text>
        <rect x="440" y="0" width="160" height="64" fill="#fff6e6" stroke="#d4a017"/>
        <text x="520" y="28" text-anchor="middle" fill="#333">{ }</text>
    </g>
    <text x="28" y="120" fill="#666">Initial array and empty hashmap (example step)</text>
</svg>

**Further reading / related problems:**
- `Two Sum II` (sorted array + two pointers)

**Study tips for beginners:**
- Practice tracing the algorithm on small arrays by hand.
- Sketch the hashmap state after each iteration.