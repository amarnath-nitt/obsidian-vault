# Overlapping Intervals — Concept

## What Is It?

Overlapping Intervals deals with problems where intervals can overlap, and you need to merge, insert, count, or remove them. The key step is almost always **sorting by start time** first.

---

## When to Use

> **Trigger keywords:** "intervals", "merge", "overlap", "meeting rooms", "free time", "insert interval"

---

## Template

### Merge Overlapping Intervals
```java
Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
List<int[]> merged = new ArrayList<>();
merged.add(intervals[0]);

for (int i = 1; i < intervals.length; i++) {
    int[] last = merged.get(merged.size() - 1);
    if (intervals[i][0] <= last[1]) {
        last[1] = Math.max(last[1], intervals[i][1]); // merge
    } else {
        merged.add(intervals[i]); // no overlap
    }
}
```

---

## Visual Walkthrough

```
Input:  [1,3] [2,6] [8,10] [15,18]

  1---3
    2------6
              8--10
                      15--18

After sort (already sorted):
Merge [1,3] + [2,6] → [1,6]  (3 >= 2, overlap!)
Keep [8,10]                   (8 > 6, no overlap)
Keep [15,18]                  (15 > 10, no overlap)

Output: [1,6] [8,10] [15,18]
```

---

## Time/Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Merge intervals | O(n log n) | O(n) |
| Insert interval | O(n) | O(n) |
| Meeting Rooms (can attend?) | O(n log n) | O(1) |
| Meeting Rooms II (min rooms) | O(n log n) | O(n) |

---

## Common Mistakes

1. **Forgetting to sort** → Intervals must be sorted by start time first
2. **Using `>` instead of `>=`** for overlap check → `[1,3]` and `[3,5]` overlap if touching counts
3. **Not updating end time with `max()`** → Merged interval end should be `max(a.end, b.end)`

---

## Related Patterns

- [[04 - TwoPointers/Concept|Two Pointers]] — Sometimes scan with two pointers after sorting
- [[16 - Greedy/Concept|Greedy]] — Non-overlapping intervals uses greedy selection

---

#intervals #sorting #dsa #concept
