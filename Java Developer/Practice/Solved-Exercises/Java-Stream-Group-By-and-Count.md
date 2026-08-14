# Group By and Count

**Concept tested**: `Collectors.groupingBy`, `Collectors.counting`

## Solution
```java
List<String> fruits = Arrays.asList("apple", "banana", "apple", "orange", "banana", "apple");

Map<String, Long> count = fruits.stream()
    .collect(Collectors.groupingBy(
        Function.identity(),
        Collectors.counting()
    ));
```

## Complexity
- **Time**: O(n)
- **Space**: O(k), where `k` is the number of distinct strings

## Interview Explanation
`groupingBy` creates a map by key. `Function.identity()` uses each fruit as its own key, and `counting()` counts how many values fall into each group.
