# Filter and Transform

**Concept tested**: Stream filtering, mapping, sorting  
**Input**: `[1,2,3,4,5,6,7,8,9,10]`  
**Expected output**: `[100,64,36,16,4]`

## Solution
```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

List<Integer> result = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .sorted(Comparator.reverseOrder())
    .collect(Collectors.toList());
```

## Complexity
- **Time**: O(n log n), because of sorting
- **Space**: O(n)

## Interview Explanation
First filter only even numbers, then transform each number into its square. Finally sort in descending order and collect the stream into a list.
