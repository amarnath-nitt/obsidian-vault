# DSA Patterns - Progress Tracker

A simple index linking to each DSA pattern's Practice page.

> [!tip] How it works
> The table below uses **Obsidian Dataview** to list all pattern directories automatically.
>
> **[Plugin required]** Install Dataview from **Settings → Community plugins → Browse** (search "Dataview") and enable it for a real-time auto-generated table.

---

## Patterns

> ⚠️ **If Dataview is not installed/enabled**, you'll see a plain code block. The static table below works without any plugins.

```dataview
TABLE WITHOUT ID
  " " AS "Done",
  link(file.path, name) AS "Pattern",
  total AS "Total"
FROM "DSA/Patterns"
WHERE file.name = "Practice.md"
FLATTEN length(file.tasks) AS total
FLATTEN regexreplace(file.folder, ".*/", "") AS name
SORT file.path
```

---

## Patterns (Static)

| Done  | Pattern                                                                        | Total |
| :---- | :----------------------------------------------------------------------------- | :---: |
|       | **🟢 Foundational Patterns**                                                   |       |
| - [ ] | [[03 - FrequencyCounting/Practice.md\|1. Frequency Counting]]                  |  11   |
| - [ ] | [[04 - TwoPointers/Practice.md\|2. Two Pointers]]                              |  12   |
| - [ ] | [[06 - SlidingWindow/Practice.md\|3. Sliding Window]]                          |  11   |
| - [ ] | [[02 - PrefixSum/Practice.md\|4. Prefix Sum]]                                  |  10   |
| - [ ] | [[14 - OverlappingIntervals/Practice.md\|5. Merge Intervals]]                  |   7   |
| - [ ] | [[08 - LinkedListReversal/Practice.md\|7. In-place Reversal of a Linked List]] |   8   |
| - [ ] | [[17 - BitManipulation/Practice.md\|8. Bit Manipulation]]                      |  12   |
|       | **🟡 Intermediate Patterns**                                                   |       |
| - [ ] | [[07 - FastSlowPointers/Practice.md\|9. Linked List Fast & Slow Pointers]]     |   7   |
| - [ ] | [[05 - BinaryTreeTraversal/Practice.md\|10. Tree Traversals (BFS & DFS)]]      |   9   |
| - [ ] | [[10 - BreadthFirstSearch/Practice.md\|10a. Breadth First Search]]             |  14   |
| - [ ] | [[11 - DepthFirstSearch/Practice.md\|10b. Depth First Search]]                 |  14   |
| - [ ] | [[12 - MatrixTraversal/Practice.md\|12. Matrix Traversal]]                     |  13   |
| - [ ] | [[01 - Recursion/Practice.md\|11. Recursion & Backtracking]]                   |  15   |
| - [ ] | [[19 - Backtracking/Practice.md\|11a. Backtracking]]                           |  11   |
| - [ ] | [[13 - MonotonicStack/Practice.md\|13. Monotonic Stack]]                       |  11   |
| - [ ] | [[15 - TopKElements/Practice.md\|15. Top 'K' Elements]]                        |  12   |
| - [ ] | [[16 - Greedy/Practice.md\|16. Greedy]]                                        |  15   |
|       | **🔴 Advanced Patterns**                                                       |       |
| - [ ] | [[09 - ModifiedBinarySearch/Practice.md\|18. Modified Binary Search]]          |  12   |
| - [ ] | [[18 - Trie/Practice.md\|19. Tries (Prefix Trees)]]                            |   8   |
| - [ ] | [[20 - DynamicProgramming/Practice.md\|21. Dynamic Programming (DP)]]          |  19   |
| - [ ] | [[21 - ShortestPath/Practice.md\|22. Shortest Path]]                           |   7   |
