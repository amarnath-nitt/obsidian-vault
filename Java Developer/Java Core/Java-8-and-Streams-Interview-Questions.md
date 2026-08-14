# Java 8 and Streams — Interview Questions

Java 8 introduced the functional programming foundation still tested in most Java interviews. Learn these APIs deeply, but write new production examples with modern Java in mind: prefer clear, side-effect-free pipelines and do not force streams where a loop is simpler. Continue with [Modern Java Interview Questions](Modern-Java-Interview-Questions.md) for Java 21–26 features.

## Lambda Expressions

### 1. What are Lambda Expressions?

**Answer:**
Lambda expressions enable functional programming in Java - treating functions as method arguments or code as data. They provide a clear and concise way to implement functional interfaces.

**Syntax:**
```java
(parameters) -> expression
(parameters) -> { statements; }
```

**Examples:**
```java
// Before Java 8
Runnable r1 = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello");
    }
};

// With Lambda
Runnable r2 = () -> System.out.println("Hello");

// With parameters
Comparator<Integer> comp = (a, b) -> a.compareTo(b);

// Multiple statements
BiFunction<Integer, Integer, Integer> add = (a, b) -> {
    int sum = a + b;
    return sum;
};
```

### 2. What is a Functional Interface?

**Answer:**
A functional interface has exactly one abstract method. It can be implemented using lambda expressions.

```java
@FunctionalInterface
interface Calculator {
    int calculate(int a, int b);
    
    // Can have default and static methods
    default void print() {
        System.out.println("Calculator");
    }
}

// Usage
Calculator add = (a, b) -> a + b;
Calculator multiply = (a, b) -> a * b;

System.out.println(add.calculate(5, 3));      // 8
System.out.println(multiply.calculate(5, 3)); // 15
```

**Built-in Functional Interfaces:**
```java
// Predicate<T> - Takes T, returns boolean
Predicate<String> isEmpty = s -> s.isEmpty();

// Function<T, R> - Takes T, returns R
Function<String, Integer> length = s -> s.length();

// Consumer<T> - Takes T, returns void
Consumer<String> print = s -> System.out.println(s);

// Supplier<T> - Takes nothing, returns T
Supplier<Double> random = () -> Math.random();

// BiFunction<T, U, R> - Takes T and U, returns R
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
```

---

## Stream API

### 3. What is Stream API? Why use it?

**Answer:**
Stream API processes collections of objects in a functional style. It supports sequential and parallel operations.

**Benefits:**
- Declarative code (what, not how)
- Easier to parallelize
- Lazy evaluation
- No side effects

**Example:**
```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Without Stream
List<Integer> evenSquares = new ArrayList<>();
for (Integer num : numbers) {
    if (num % 2 == 0) {
        evenSquares.add(num * num);
    }
}

// With Stream
List<Integer> evenSquares = numbers.stream()
    .filter(n -> n % 2 == 0)
    .map(n -> n * n)
    .collect(Collectors.toList());
// Result: [4, 16, 36, 64, 100]
```

### 4. What are intermediate and terminal operations in Streams?

**Answer:**

**Intermediate Operations (Lazy):**
- Return a Stream
- Don't execute until terminal operation called
- Examples: `filter()`, `map()`, `flatMap()`, `distinct()`, `sorted()`, `peek()`

**Terminal Operations (Eager):**
- Trigger stream processing
- Return non-stream result
- Examples: `collect()`, `forEach()`, `reduce()`, `count()`, `anyMatch()`, `findFirst()`

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

names.stream()
    .filter(n -> n.length() > 3)  // Intermediate (lazy)
    .map(String::toUpperCase)      // Intermediate (lazy)
    .sorted()                      // Intermediate (lazy)
    .forEach(System.out::println); // Terminal (triggers execution)
// Output: ALICE, CHARLIE, DAVID
```

### 5. Explain common Stream operations with examples.

**Answer:**

**filter() - Select elements:**
```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6);
List<Integer> evens = nums.stream()
    .filter(n -> n % 2 == 0)
    .collect(Collectors.toList());
// [2, 4, 6]
```

**map() - Transform elements:**
```java
List<String> names = Arrays.asList("alice", "bob", "charlie");
List<String> upper = names.stream()
    .map(String::toUpperCase)
    .collect(Collectors.toList());
// [ALICE, BOB, CHARLIE]
```

**flatMap() - Flatten nested structures:**
```java
List<List<Integer>> nested = Arrays.asList(
    Arrays.asList(1, 2),
    Arrays.asList(3, 4),
    Arrays.asList(5, 6)
);

List<Integer> flat = nested.stream()
    .flatMap(List::stream)
    .collect(Collectors.toList());
// [1, 2, 3, 4, 5, 6]
```

**reduce() - Combine elements:**
```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);

int sum = nums.stream()
    .reduce(0, (a, b) -> a + b);
// 15

Optional<Integer> max = nums.stream()
    .reduce(Integer::max);
// Optional[5]
```

**collect() - Accumulate results:**
```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

// To List
List<String> list = names.stream().collect(Collectors.toList());

// To Set
Set<String> set = names.stream().collect(Collectors.toSet());

// To Map
Map<String, Integer> map = names.stream()
    .collect(Collectors.toMap(
        name -> name,
        name -> name.length()
    ));
// {Alice=5, Bob=3, Charlie=7}

// Joining strings
String joined = names.stream()
    .collect(Collectors.joining(", "));
// "Alice, Bob, Charlie"
```

**sorted() - Sort elements:**
```java
List<String> names = Arrays.asList("Charlie", "Alice", "Bob");

List<String> sorted = names.stream()
    .sorted()
    .collect(Collectors.toList());
// [Alice, Bob, Charlie]

List<String> reversed = names.stream()
    .sorted(Comparator.reverseOrder())
    .collect(Collectors.toList());
// [Charlie, Bob, Alice]
```

**distinct() - Remove duplicates:**
```java
List<Integer> nums = Arrays.asList(1, 2, 2, 3, 3, 3, 4);
List<Integer> unique = nums.stream()
    .distinct()
    .collect(Collectors.toList());
// [1, 2, 3, 4]
```

**limit() and skip():**
```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

List<Integer> first5 = nums.stream()
    .limit(5)
    .collect(Collectors.toList());
// [1, 2, 3, 4, 5]

List<Integer> skip5 = nums.stream()
    .skip(5)
    .collect(Collectors.toList());
// [6, 7, 8, 9, 10]
```

**anyMatch(), allMatch(), noneMatch():**
```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);

boolean hasEven = nums.stream().anyMatch(n -> n % 2 == 0);  // true
boolean allPositive = nums.stream().allMatch(n -> n > 0);   // true
boolean noneNegative = nums.stream().noneMatch(n -> n < 0); // true
```

---

## Method References

### 6. What are Method References? What are the types?

**Answer:**
Method references are shorthand for lambda expressions that only call an existing method.

**Syntax:** `ClassName::methodName`

**Types:**

**1. Static Method Reference:**
```java
// Lambda
Function<String, Integer> parser = s -> Integer.parseInt(s);
// Method Reference
Function<String, Integer> parser = Integer::parseInt;
```

**2. Instance Method Reference (on particular object):**
```java
String str = "Hello";
// Lambda
Supplier<String> upper = () -> str.toUpperCase();
// Method Reference
Supplier<String> upper = str::toUpperCase;
```

**3. Instance Method Reference (on arbitrary object):**
```java
List<String> names = Arrays.asList("alice", "bob", "charlie");
// Lambda
names.stream().map(s -> s.toUpperCase());
// Method Reference
names.stream().map(String::toUpperCase);
```

**4. Constructor Reference:**
```java
// Lambda
Supplier<List<String>> listSupplier = () -> new ArrayList<>();
// Constructor Reference
Supplier<List<String>> listSupplier = ArrayList::new;

// With parameters
Function<String, Integer> converter = Integer::new;
```

---

## Optional Class

### 7. What is Optional? Why use it?

**Answer:**
`Optional<T>` is a container that may or may not contain a non-null value. It helps avoid `NullPointerException` and makes null handling explicit.

**Benefits:**
- Explicit handling of absence of value
- Cleaner API design
- Avoids null checks

**Creating Optional:**
```java
Optional<String> empty = Optional.empty();
Optional<String> of = Optional.of("Hello");  // Throws NPE if null
Optional<String> nullable = Optional.ofNullable(null); // OK with null
```

**Using Optional:**
```java
Optional<String> opt = Optional.of("Hello");

// Check if present
if (opt.isPresent()) {
    System.out.println(opt.get());
}

// Better: ifPresent
opt.ifPresent(System.out::println);

// orElse - default value
String value = opt.orElse("Default");

// orElseGet - lazy default
String value = opt.orElseGet(() -> "Default");

// orElseThrow - throw exception
String value = opt.orElseThrow(() -> new RuntimeException("Not found"));

// map - transform value
Optional<Integer> length = opt.map(String::length);

// filter - conditional
Optional<String> filtered = opt.filter(s -> s.length() > 3);
```

**Real-world example:**
```java
// Before Optional
public String getUserEmail(Long userId) {
    User user = userRepository.findById(userId);
    if (user != null) {
        Email email = user.getEmail();
        if (email != null) {
            return email.getAddress();
        }
    }
    return "default@example.com";
}

// With Optional
public String getUserEmail(Long userId) {
    return userRepository.findById(userId)
        .map(User::getEmail)
        .map(Email::getAddress)
        .orElse("default@example.com");
}
```

---

## Default and Static Methods in Interfaces

### 8. What are default methods in interfaces?

**Answer:**
Default methods allow adding new methods to interfaces without breaking existing implementations.

```java
interface Vehicle {
    // Abstract method
    void start();
    
    // Default method
    default void stop() {
        System.out.println("Vehicle stopped");
    }
    
    // Static method
    static void repair() {
        System.out.println("Vehicle repaired");
    }
}

class Car implements Vehicle {
    @Override
    public void start() {
        System.out.println("Car started");
    }
    
    // Can optionally override default method
    @Override
    public void stop() {
        System.out.println("Car stopped");
    }
}

// Usage
Car car = new Car();
car.start();    // Car started
car.stop();     // Car stopped
Vehicle.repair(); // Static call
```

**Diamond Problem Resolution:**
```java
interface A {
    default void show() { System.out.println("A"); }
}

interface B {
    default void show() { System.out.println("B"); }
}

class C implements A, B {
    @Override
    public void show() {
        A.super.show(); // Explicitly call A's version
        // Or provide own implementation
    }
}
```

---

## Date and Time API

### 9. What's new in Date and Time API (java.time)?

**Answer:**
Java 8 introduced `java.time` package to replace the old `java.util.Date` and `Calendar` classes.

**Key Classes:**

**LocalDate - Date without time:**
```java
LocalDate today = LocalDate.now();
LocalDate birthday = LocalDate.of(1990, Month.JANUARY, 15);
LocalDate tomorrow = today.plusDays(1);

int year = today.getYear();
Month month = today.getMonth();
int day = today.getDayOfMonth();
```

**LocalTime - Time without date:**
```java
LocalTime now = LocalTime.now();
LocalTime meetingTime = LocalTime.of(14, 30); // 2:30 PM
LocalTime later = now.plusHours(2);
```

**LocalDateTime - Date and time:**
```java
LocalDateTime now = LocalDateTime.now();
LocalDateTime specific = LocalDateTime.of(2024, 1, 15, 14, 30);
```

**ZonedDateTime - Date and time with timezone:**
```java
ZonedDateTime nowInNY = ZonedDateTime.now(ZoneId.of("America/New_York"));
ZonedDateTime nowInTokyo = ZonedDateTime.now(ZoneId.of("Asia/Tokyo"));
```

**Period and Duration:**
```java
// Period - Date-based
LocalDate start = LocalDate.of(2020, 1, 1);
LocalDate end = LocalDate.of(2024, 1, 1);
Period period = Period.between(start, end);
// 4 years

// Duration - Time-based
LocalTime startTime = LocalTime.of(9, 0);
LocalTime endTime = LocalTime.of(17, 0);
Duration duration = Duration.between(startTime, endTime);
// 8 hours
```

**Formatting:**
```java
LocalDateTime now = LocalDateTime.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
String formatted = now.format(formatter);
// "22-01-2024 14:30:45"

LocalDateTime parsed = LocalDateTime.parse("22-01-2024 14:30:45", formatter);
```

---

## Collectors

### 10. What are Collectors? Explain common Collectors.

**Answer:**
Collectors are used with `collect()` terminal operation to accumulate stream elements into collections or other results.

**Common Collectors:**

**toList(), toSet():**
```java
List<String> list = stream.collect(Collectors.toList());
Set<String> set = stream.collect(Collectors.toSet());
```

**toMap():**
```java
List<Person> people = Arrays.asList(
    new Person("Alice", 25),
    new Person("Bob", 30)
);

Map<String, Integer> nameToAge = people.stream()
    .collect(Collectors.toMap(
        Person::getName,
        Person::getAge
    ));
// {Alice=25, Bob=30}
```

**groupingBy() - Group elements:**
```java
List<Person> people = Arrays.asList(
    new Person("Alice", 25),
    new Person("Bob", 30),
    new Person("Charlie", 25)
);

Map<Integer, List<Person>> byAge = people.stream()
    .collect(Collectors.groupingBy(Person::getAge));
// {25=[Alice, Charlie], 30=[Bob]}

// GroupingBy with counting
Map<Integer, Long> countByAge = people.stream()
    .collect(Collectors.groupingBy(
        Person::getAge,
        Collectors.counting()
    ));
// {25=2, 30=1}
```

**partitioningBy() - Binary split:**
```java
Map<Boolean, List<Integer>> partitioned = Stream.of(1, 2, 3, 4, 5, 6)
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
// {false=[1, 3, 5], true=[2, 4, 6]}
```

**joining() - Concatenate strings:**
```java
String joined = Stream.of("A", "B", "C")
    .collect(Collectors.joining(", "));
// "A, B, C"

String withPrefixSuffix = Stream.of("A", "B", "C")
    .collect(Collectors.joining(", ", "[", "]"));
// "[A, B, C]"
```

**summarizingInt/Long/Double():**
```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);

IntSummaryStatistics stats = nums.stream()
    .collect(Collectors.summarizingInt(Integer::intValue));

System.out.println("Count: " + stats.getCount());     // 5
System.out.println("Sum: " + stats.getSum());         // 15
System.out.println("Min: " + stats.getMin());         // 1
System.out.println("Max: " + stats.getMax());         // 5
System.out.println("Average: " + stats.getAverage()); // 3.0
```

---

## Advanced Stream Topics

### 11. What is the difference between map() and flatMap()?

**Answer:**
- **map()**: One-to-one mapping (Stream<T> → Stream<R>)
- **flatMap()**: One-to-many mapping, flattens result (Stream<Stream<T>> → Stream<T>)

```java
// map() - transforms each element
List<String> names = Arrays.asList("Alice", "Bob");
List<Integer> lengths = names.stream()
    .map(String::length)
    .collect(Collectors.toList());
// [5, 3]

// flatMap() - flattens nested structures
List<List<Integer>> nested = Arrays.asList(
    Arrays.asList(1, 2),
    Arrays.asList(3, 4)
);

List<Integer> flat = nested.stream()
    .flatMap(List::stream)
    .collect(Collectors.toList());
// [1, 2, 3, 4]

// Practical example: Get all characters from words
List<String> words = Arrays.asList("Hello", "World");

List<String> letters = words.stream()
    .flatMap(word -> Arrays.stream(word.split("")))
    .collect(Collectors.toList());
// [H, e, l, l, o, W, o, r, l, d]
```

### 12. What is parallel stream? When to use it?

**Answer:**
Parallel streams divide data into multiple chunks and process them in parallel using ForkJoinPool.

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8);

// Sequential
long sum = numbers.stream()
    .map(n -> n * n)
    .reduce(0, Integer::sum);

// Parallel
long sum = numbers.parallelStream()
    .map(n -> n * n)
    .reduce(0, Integer::sum);
```

**When to Use:**
✅ Large datasets
✅ CPU-intensive operations
✅ Independent operations (no shared mutable state)

**When NOT to Use:**
❌ Small datasets (overhead outweighs benefit)
❌ I/O operations (not CPU-bound)
❌ Order-dependent operations
❌ Shared mutable state

### 13. Explain forEach() vs forEachOrdered() in parallel streams.

**Answer:**
- **forEach()**: No order guarantee in parallel streams
- **forEachOrdered()**: Maintains encounter order even in parallel streams

```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);

// forEach - order not guaranteed
nums.parallelStream().forEach(System.out::println);
// May print: 3, 1, 5, 2, 4

// forEachOrdered - maintains order
nums.parallelStream().forEachOrdered(System.out::println);
// Prints: 1, 2, 3, 4, 5
```

### 14. How do you create streams from different source types?

**Answer:** Use the stream factory that matches the source. The most common options are `collection.stream()`, `Stream.of(...)`, `Arrays.stream(array)`, primitive streams such as `IntStream.range(...)`, `String.chars()`, `Stream.generate(...)`, and `Stream.iterate(...)`.

```java
Stream<String> values = Stream.of("a", "b", "c");
Stream<String> fromList = List.of("a", "b", "c").stream();
IntStream numbers = Arrays.stream(new int[] {1, 2, 3});
IntStream range = IntStream.rangeClosed(1, 10);
Stream<UUID> generated = Stream.generate(UUID::randomUUID).limit(3);
```

For a `char[]`, Java does not provide `Arrays.stream(char[])`. Create an `IntStream` with `new String(chars).chars()` or `CharBuffer.wrap(chars).chars()`, then use `mapToObj(value -> (char) value)` if you need `Stream<Character>`.

```java
char[] chars = {'a', 'b', 'c'};

Stream<Character> characterStream = new String(chars)
        .chars()
        .mapToObj(value -> (char) value);
```

Do not use `Stream.of(chars)` for this purpose: it creates a stream containing one `char[]` element. See [Java Stream Creation Guide](../Reference/Java-Stream-Creation-Guide.md) for all common standard-library source types, including files, readers, `Optional`, regular expressions, builders, concatenation, and custom `Spliterator` sources.
