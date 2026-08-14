# Remove Duplicates Maintaining Order

**Concept tested**: `LinkedHashSet`, Stream `distinct`

## Solution
```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 4, 1, 5, 3);

List<Integer> unique = new ArrayList<>(new LinkedHashSet<>(numbers));

List<Integer> uniqueWithStream = numbers.stream()
    .distinct()
    .collect(Collectors.toList());
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Interview Explanation
`LinkedHashSet` removes duplicates while preserving insertion order. Stream `distinct()` also preserves encounter order for ordered streams.
