# Flatten Nested Lists

**Concept tested**: `flatMap`

## Solution
```java
List<List<Integer>> nested = Arrays.asList(
    Arrays.asList(1, 2),
    Arrays.asList(3, 4),
    Arrays.asList(5, 6, 7)
);

List<Integer> flat = nested.stream()
    .flatMap(List::stream)
    .collect(Collectors.toList());
```

## Complexity
- **Time**: O(n), where `n` is the total number of integers
- **Space**: O(n)

## Interview Explanation
Each inner list is converted into a stream, and `flatMap` merges those streams into one stream before collecting.
