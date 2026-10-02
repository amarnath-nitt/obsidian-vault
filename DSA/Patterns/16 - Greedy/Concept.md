# Greedy — Concept

## What Is It?

Greedy makes the **locally optimal choice** at each step, hoping it leads to a globally optimal solution. Unlike DP, greedy doesn't reconsider past decisions. It works when the problem has **greedy choice property** and **optimal substructure**.

---

## When to Use

> **Trigger keywords:** "maximum profit", "minimum cost", "scheduling", "assign", "jump game", "gas station"

| Trigger | Example |
|---------|---------|
| **Activity selection** / scheduling | Meeting Rooms, Task Scheduler |
| **Jump/reach** problems | Jump Game, Jump Game II |
| **Assign** resources optimally | Assign Cookies |
| **Buy/sell** with constraints | Best Time to Buy and Sell Stock |

---

## Template

```java
// Generic greedy: sort, then make locally optimal choice
Arrays.sort(items, comparator);
int result = 0;
for (Item item : items) {
    if (canTake(item)) {
        take(item);
        result++;
    }
}
```

---

## Visual Walkthrough

### Jump Game II: `[2,3,1,1,4]`
```
Position: 0  1  2  3  4
Values:  [2, 3, 1, 1, 4]

From 0: can reach 1 or 2. Best landing = position 1 (val=3, reaches 4)
From 1: can reach 2, 3, or 4. Position 4 is the end!

Jumps: 0 → 1 → 4  =  2 jumps

Greedy: at each step, pick the position that lets you reach farthest.
```

---

## Time/Space Complexity

| Problem Type | Time | Space |
|-------------|------|-------|
| With sorting | O(n log n) | O(1) |
| Single pass | O(n) | O(1) |

---

## Common Mistakes

1. **Applying greedy when DP is needed** → Verify greedy choice property first
2. **Wrong sorting criteria** → Meeting rooms: sort by end time for max meetings
3. **Not proving correctness** → Greedy needs proof; "it seems right" isn't enough

---

## Related Patterns

- [[20 - DynamicProgramming/Concept|Dynamic Programming]] — When greedy fails, try DP
- [[14 - OverlappingIntervals/Concept|Overlapping Intervals]] — Greedy interval selection
- [[09 - ModifiedBinarySearch/Concept|Modified Binary Search]] — Binary search on answer validated by greedy

---

#greedy #dsa #concept
