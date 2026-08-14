# Find First and Optional

**Concept tested**: `findFirst`, `Optional`

## Solution
```java
List<String> names = Arrays.asList("Bob", "Charlie", "Alice", "Andrew");

Optional<String> result = names.stream()
    .filter(name -> name.startsWith("A"))
    .findFirst();

String firstName = result.orElse("No name found");
```

## Complexity
- **Time**: O(n) worst case
- **Space**: O(1)

## Interview Explanation
`findFirst()` short-circuits as soon as the first matching name is found. Because the result may be absent, Java returns an `Optional` instead of a nullable value.
