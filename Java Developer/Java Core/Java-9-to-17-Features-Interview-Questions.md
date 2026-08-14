# Java 9 to 17 Features — Interview Questions

Java 17 is an LTS release and remains common in production. This guide covers stable, interview-relevant features from Java 9 through Java 17. For the current production baseline (Java 21/25) and feature status after Java 17, continue with [Modern Java Interview Questions](Modern-Java-Interview-Questions.md).

## Records (Java 14/16)

### 1. What are Records? Why use them?

**Answer:**
Records are immutable data carriers that reduce boilerplate code for data classes. They automatically provide constructor, getters, `equals()`, `hashCode()`, and `toString()`.

**Without Record:**
```java
public class Person {
    private final String name;
    private final int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() { return name; }
    public int getAge() { return age; }
    
    @Override
    public boolean equals(Object o) {
        // ... boilerplate code
    }
    
    @Override
    public int hashCode() {
        // ... boilerplate code
    }
    
    @Override
    public String toString() {
        // ... boilerplate code
    }
}
```

**With Record:**
```java
public record Person(String name, int age) {
    // That's it! All methods auto-generated
}

// Usage
Person person = new Person("Alice", 25);
System.out.println(person.name());  // Alice (accessor, not getter)
System.out.println(person.age());   // 25
System.out.println(person);         // Person[name=Alice, age=25]
```

**Custom methods and validations:**
```java
public record Person(String name, int age) {
    // Compact constructor for validation
    public Person {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
    }
    
    // Custom methods
    public boolean isAdult() {
        return age >= 18;
    }
    
    // Static factory method
    public static Person of(String name, int age) {
        return new Person(name, age);
    }
}
```

**Key Points:**
- Records are implicitly `final` (can't be extended)
- All fields are `final`
- No setters (immutable)
- Can implement interfaces
- Can have static methods and fields

---

## Sealed Classes (Java 17)

### 2. What are Sealed Classes?

**Answer:**
Sealed classes restrict which classes can extend or implement them, providing better control over inheritance hierarchy.

**Syntax:**
```java
// Define sealed class with permitted subclasses
public sealed class Shape 
    permits Circle, Rectangle, Triangle {
}

// Permitted classes must be: final, sealed, or non-sealed
public final class Circle extends Shape {
    private double radius;
}

public final class Rectangle extends Shape {
    private double width, height;
}

public sealed class Triangle extends Shape 
    permits EquilateralTriangle {
}

public final class EquilateralTriangle extends Triangle {
}

// Non-sealed allows open extension
public non-sealed class CustomShape extends Shape {
}

public class AnyShape extends CustomShape {
    // Can extend non-sealed class
}
```

**Benefits:**
1. **Exhaustive switch** statements (compiler knows all subtypes)
2. **Better encapsulation** and API control
3. **Pattern matching** improvements

**Exhaustive switch with sealed classes:**
```java
public sealed interface Payment 
    permits CreditCard, DebitCard, Cash {
}

public record CreditCard(String number) implements Payment {}
public record DebitCard(String number) implements Payment {}
public record Cash(double amount) implements Payment {}

// Exhaustive - no default needed
public double processPayment(Payment payment) {
    return switch (payment) {
        case CreditCard cc -> cc.number().length() * 1.0;
        case DebitCard dc -> dc.number().length() * 0.5;
        case Cash cash -> cash.amount();
        // No default needed - compiler knows all types
    };
}
```

---

## Pattern Matching for instanceof (Java 16)

### 3. What is Pattern Matching for instanceof?

**Answer:**
Eliminates casting after `instanceof` check by binding the variable directly.

**Before Java 16:**
```java
if (obj instanceof String) {
    String str = (String) obj;  // Redundant cast
    System.out.println(str.length());
}
```

**With Pattern Matching:**
```java
if (obj instanceof String str) {
    System.out.println(str.length());  // str already String
}

// Works in expressions
if (obj instanceof String str && str.length() > 5) {
    System.out.println(str.toUpperCase());
}
```

**Complex example:**
```java
public String formatValue(Object obj) {
    if (obj instanceof Integer i) {
        return "Integer: " + i;
    } else if (obj instanceof String s && s.length() > 0) {
        return "String: " + s.toUpperCase();
    } else if (obj instanceof List<?> list && !list.isEmpty()) {
        return "List of size: " + list.size();
    } else {
        return "Unknown type";
    }
}
```

---

## Switch Expressions (Java 14)

### 4. What are Switch Expressions?

**Answer:**
Switch can now be used as an expression that returns a value, with improved syntax and exhaustiveness checking.

**Traditional Switch:**
```java
String day = "MONDAY";
int numLetters;

switch (day) {
    case "MONDAY":
    case "FRIDAY":
    case "SUNDAY":
        numLetters = 6;
        break;
    case "TUESDAY":
        numLetters = 7;
        break;
    case "THURSDAY":
    case "SATURDAY":
        numLetters = 8;
        break;
    case "WEDNESDAY":
        numLetters = 9;
        break;
    default:
        throw new IllegalArgumentException("Invalid day");
}
```

**Switch Expression:**
```java
String day = "MONDAY";

int numLetters = switch (day) {
    case "MONDAY", "FRIDAY", "SUNDAY" -> 6;
    case "TUESDAY" -> 7;
    case "THURSDAY", "SATURDAY" -> 8;
    case "WEDNESDAY" -> 9;
    default -> throw new IllegalArgumentException("Invalid day");
};
```

**With blocks:**
```java
int result = switch (value) {
    case 1, 2, 3 -> {
        System.out.println("Processing small value");
        yield value * 10;  // yield returns value from block
    }
    case 4, 5 -> value * 20;
    default -> 0;
};
```

**Pattern matching in switch (Preview in Java 17):**
```java
public String format(Object obj) {
    return switch (obj) {
        case Integer i -> String.format("int %d", i);
        case Long l -> String.format("long %d", l);
        case Double d -> String.format("double %f", d);
        case String s -> String.format("String %s", s);
        default -> obj.toString();
    };
}
```

---

## Text Blocks (Java 15)

### 5. What are Text Blocks?

**Answer:**
Text blocks provide multi-line string literals without escape sequences, making code more readable.

**Before Text Blocks:**
```java
String json = "{\n" +
              "  \"name\": \"John\",\n" +
              "  \"age\": 30,\n" +
              "  \"city\": \"New York\"\n" +
              "}";

String sql = "SELECT id, name, email\n" +
             "FROM users\n" +
             "WHERE status = 'active'\n" +
             "ORDER BY name";
```

**With Text Blocks:**
```java
String json = """
    {
      "name": "John",
      "age": 30,
      "city": "New York"
    }
    """;

String sql = """
    SELECT id, name, email
    FROM users
    WHERE status = 'active'
    ORDER BY name
    """;
```

**Features:**
- Automatically handles new lines
- Preserves indentation relative to closing `"""`
- No need to escape quotes
- Can include expressions with `\s` and `\` for formatting

```java
String html = """
    <html>
        <body>
            <h1>Hello, World!</h1>
        </body>
    </html>
    """;

// With variables
String name = "Alice";
String greeting = """
    Hello, %s!
    Welcome to our application.
    """.formatted(name);
```

---

## Module System (Java 9)

### 6. What is the Java Module System (JPMS)?

**Answer:**
The Java Platform Module System (Project Jigsaw) allows creating modular applications with explicit dependencies.

**module-info.java:**
```java
module com.example.myapp {
    // Exports package to other modules
    exports com.example.myapp.api;
    
    // Requires another module
    requires java.sql;
    requires java.logging;
    
    // Requires and re-exports (transitive)
    requires transitive java.xml;
    
    // Opens package for reflection
    opens com.example.myapp.internal to com.example.framework;
    
    // Provides service implementation
    provides com.example.service.MyService 
        with com.example.service.impl.MyServiceImpl;
    
    // Uses service
    uses com.example.service.MyService;
}
```

**Benefits:**
1. **Strong Encapsulation**: Internal packages are truly hidden
2. **Explicit Dependencies**: Clear module requirements
3. **Smaller Runtime**: Only required modules included
4. **Better Performance**: Optimized class loading

---

## var Keyword (Java 10)

### 7. What is the var keyword? When to use it?

**Answer:**
`var` enables local variable type inference - the compiler infers the type from the initializer.

**Usage:**
```java
// Instead of
String message = "Hello";
List<String> names = new ArrayList<>();
Map<String, Integer> scores = new HashMap<>();

// Can use var
var message = "Hello";              // String
var names = new ArrayList<String>();  // ArrayList<String>
var scores = new HashMap<String, Integer>(); // HashMap<String, Integer>
```

**Restrictions:**
```java
// ❌ Cannot use without initializer
var x;  // Error

// ❌ Cannot use with null
var y = null;  // Error

// ❌ Cannot use for fields, parameters, or return types
class Example {
    var field = 10;  // Error - only for local variables
    
    var method() {   // Error
        return 0;
    }
}

// ❌ Cannot use with lambda without explicit type
var lambda = () -> {};  // Error
var lambda = (Runnable) () -> {};  // OK
```

**Best Practices:**
```java
// ✅ Good - type is obvious
var list = new ArrayList<String>();
var path = Paths.get("/tmp/file.txt");
var user = userService.findById(123);

// ❌ Avoid - type not clear
var result = calculate();  // What type is this?
var data = getData();      // Unclear

// ✅ Good in loops
for (var entry : map.entrySet()) {
    var key = entry.getKey();
    var value = entry.getValue();
}
```

---

## Private Methods in Interfaces (Java 9)

### 8. What are private methods in interfaces?

**Answer:**
Java 9 allows private methods in interfaces to share code between default methods without exposing helper methods.

```java
public interface Calculator {
    default int addAndDouble(int a, int b) {
        return doubleValue(a + b);
    }
    
    default int subtractAndDouble(int a, int b) {
        return doubleValue(a - b);
    }
    
    // Private helper method
    private int doubleValue(int value) {
        return value * 2;
    }
    
    // Private static method
    private static void log(String message) {
        System.out.println("Calculator: " + message);
    }
}
```

---

## Enhanced NullPointerException Messages (Java 14)

### 9. What are helpful NullPointerException messages?

**Answer:**
Java 14+ provides detailed NPE messages showing exactly which variable was null.

**Before:**
```java
String city = person.getAddress().getCity();
// NullPointerException at line 5
```

**Java 14+:**
```java
String city = person.getAddress().getCity();
// NullPointerException: Cannot invoke "Address.getCity()" 
// because the return value of "Person.getAddress()" is null
```

Enable with: `-XX:+ShowCodeDetailsInExceptionMessages`

---

## Other Important Features

### 10. What are some other important features in Java 9-17?

**Answer:**

**HTTP Client API (Java 11):**
```java
HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.example.com/data"))
    .GET()
    .build();

HttpResponse<String> response = client.send(request, 
    HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

**Collection Factory Methods (Java 9):**
```java
// Immutable collections
List<String> list = List.of("A", "B", "C");
Set<Integer> set = Set.of(1, 2, 3);
Map<String, Integer> map = Map.of("A", 1, "B", 2);

// Also: Map.ofEntries()
Map<String, Integer> map = Map.ofEntries(
    Map.entry("A", 1),
    Map.entry("B", 2)
);
```

**Stream API Enhancements:**
```java
// takeWhile (Java 9)
Stream.of(1, 2, 3, 4, 5, 1, 2)
    .takeWhile(n -> n < 4)
    .forEach(System.out::println);  // 1, 2, 3

// dropWhile (Java 9)
Stream.of(1, 2, 3, 4, 5)
    .dropWhile(n -> n < 3)
    .forEach(System.out::println);  // 3, 4, 5

// iterate with predicate (Java 9)
Stream.iterate(1, n -> n < 10, n -> n + 1)
    .forEach(System.out::println);  // 1 to 9

// ofNullable (Java 9)
Stream.ofNullable(getValue())  // Empty stream if null
    .forEach(System.out::println);

// teeing (Java 12) - combine two collectors
var result = list.stream()
    .collect(Collectors.teeing(
        Collectors.summingInt(Integer::intValue),
        Collectors.counting(),
        (sum, count) -> sum / count
    ));
```

**String Methods (Java 11):**
```java
" ".isBlank();              // true
"  text  ".strip();         // "text" (Unicode-aware)
"text".repeat(3);           // "texttexttext"
"A\nB\nC".lines().count();  // 3 (Stream<String>)
```

**Files.readString() and Files.writeString() (Java 11):**
```java
String content = Files.readString(Path.of("file.txt"));
Files.writeString(Path.of("file.txt"), "content");
```

---

## Comparison Table

### 11. Quick comparison of Java versions

| Feature | Version | Description |
|---------|---------|-------------|
| Modules (JPMS) | Java 9 | Module system for better encapsulation |
| var keyword | Java 10 | Local variable type inference |
| String methods | Java 11 | isBlank(), strip(), repeat(), lines() |
| HTTP Client | Java 11 | Modern HTTP client API |
| Switch Expressions | Java 14 | Switch as expression with -> syntax |
| Text Blocks | Java 15 | Multi-line strings with """ |
| Records | Java 16 | Immutable data carriers |
| Pattern Matching instanceof | Java 16 | Eliminate casting after instanceof |
| Sealed Classes | Java 17 | Restrict inheritance hierarchy |
