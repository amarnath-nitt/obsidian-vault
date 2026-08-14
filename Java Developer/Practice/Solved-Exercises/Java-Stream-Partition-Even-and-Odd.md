# Partition Even and Odd

**Concept tested**: `Collectors.partitioningBy`

## Solution
```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

Map<Boolean, List<Integer>> partitioned = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));

List<Integer> evens = partitioned.get(true);
List<Integer> odds = partitioned.get(false);
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Interview Explanation
`partitioningBy` is a special case of grouping where the key is boolean. It naturally splits the list into matching and non-matching values.
