# Find Common Elements

**Concept tested**: Set lookup, collection operations

## Solution
```java
List<Integer> list1 = Arrays.asList(1, 2, 3, 4, 5);
List<Integer> list2 = Arrays.asList(4, 5, 6, 7, 8);

Set<Integer> lookup = new HashSet<>(list2);

List<Integer> common = list1.stream()
    .filter(lookup::contains)
    .collect(Collectors.toList());
```

## Complexity
- **Time**: O(n + m)
- **Space**: O(m)

## Interview Explanation
Convert one list to a set so membership checks are O(1) average time. Then filter the other list against that set.
