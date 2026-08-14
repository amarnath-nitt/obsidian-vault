# Sorting Objects

**Concept tested**: Stream API (`sorted`, `comparingDouble`, comparator chaining, nulls handling)

## Problem
Sort a list of products by their price (descending). If prices are equal, resolve the tie by sorting by their rating (descending), and finally by their name (alphabetically). Handle cases where price or rating might be null.

## Solution
```java
public List<Product> sortProducts(List<Product> products) {
    return products.stream()
        .sorted(
            Comparator.comparing(Product::getPrice, Comparator.nullsLast(Comparator.reverseOrder()))
                .thenComparing(Product::getRating, Comparator.nullsLast(Comparator.reverseOrder()))
                .thenComparing(Product::getName, Comparator.nullsLast(Comparator.naturalOrder()))
        )
        .collect(Collectors.toList());
}
```

## Complexity
- **Time Complexity**: $O(N \log N)$ due to the sorting operation.
- **Space Complexity**: $O(N)$ to collect the sorted elements into a new list.

## Interview Explanation
When sorting objects in Java, the `Comparator` utility provides a fluent API for chaining sorting criteria using `thenComparing`. By combining `comparing` or `comparingDouble` with `nullsLast` or `nullsFirst`, we can write robust, null-safe sorting logic. This prevents `NullPointerException`s if any properties are missing, which is a common real-world bug.
