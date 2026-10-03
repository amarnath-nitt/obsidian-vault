# Builder — Implementations & Examples

**Pattern:** Builder (Creational) · **Skill:** constructing complex / immutable objects fluently

### Approach

- Make the product's **constructor private** and its fields `final`.
- Provide a **static nested `Builder`** with one fluent method per field (each returns `this`).
- `build()` validates required fields and returns the immutable product.

### Java Solutions

**1. Pizza Builder (fluent nested builder)**
```java
import java.util.*;

public final class Pizza {
    private final String size;                 // required
    private final boolean cheese;
    private final boolean pepperoni;
    private final List<String> toppings;

    private Pizza(Builder b) {
        this.size = b.size;
        this.cheese = b.cheese;
        this.pepperoni = b.pepperoni;
        this.toppings = List.copyOf(b.toppings);
    }

    public String size()       { return size; }
    public boolean cheese()    { return cheese; }
    public boolean pepperoni() { return pepperoni; }
    public List<String> toppings() { return toppings; }

    public static Builder builder() { return new Builder(); }

    public static final class Builder {
        private String size;
        private boolean cheese, pepperoni;
        private final List<String> toppings = new ArrayList<>();

        public Builder size(String size)          { this.size = size; return this; }
        public Builder cheese(boolean v)          { this.cheese = v; return this; }
        public Builder pepperoni(boolean v)       { this.pepperoni = v; return this; }
        public Builder addTopping(String t)       { toppings.add(t); return this; }

        public Pizza build() {
            if (size == null || size.isBlank())
                throw new IllegalStateException("size is required");
            return new Pizza(this);
        }
    }
}
// usage
Pizza p = Pizza.builder().size("LARGE").cheese(true).addTopping("olives").build();
```

**2. HttpRequest Builder (headers + defaults)**
```java
import java.util.*;

public final class HttpRequest {
    private final String url, method, body;
    private final int timeoutSeconds;
    private final Map<String, String> headers;

    private HttpRequest(Builder b) {
        this.url = b.url;
        this.method = b.method;
        this.body = b.body;
        this.timeoutSeconds = b.timeoutSeconds;
        this.headers = Map.copyOf(b.headers);
    }

    public static Builder builder() { return new Builder(); }

    public static final class Builder {
        private String url, method = "GET", body;
        private int timeoutSeconds = 30;
        private final Map<String, String> headers = new HashMap<>();

        public Builder url(String url)            { this.url = url; return this; }
        public Builder method(String m)           { this.method = m; return this; }
        public Builder body(String b)             { this.body = b; return this; }
        public Builder timeout(int s)             { this.timeoutSeconds = s; return this; }
        public Builder header(String k, String v) { headers.put(k, v); return this; }

        public HttpRequest build() {
            if (url == null || url.isBlank())
                throw new IllegalStateException("url is required");
            return new HttpRequest(this);
        }
    }
}
```

**3. Classic GoF — Director + Builder**
```java
interface DocumentBuilder { void addTitle(String t); void addBody(String b); String render(); }

class HtmlDocumentBuilder implements DocumentBuilder {
    private final StringBuilder sb = new StringBuilder();
    public void addTitle(String t) { sb.append("<h1>").append(t).append("</h1>\n"); }
    public void addBody(String b)  { sb.append("<p>").append(b).append("</p>\n"); }
    public String render()         { return sb.toString(); }
}

class Director {                                  // encodes the reusable sequence
    void build(DocumentBuilder b) {
        b.addTitle("Report");
        b.addBody("Quarterly results");
    }
}
```

**4. `toBuilder()` (Derived Copy)**
```java
// start from an existing immutable object, change one field, build a new one
HttpRequest modified = existing.toBuilder().timeout(60).build();
```

**Complexity:** construction O(n) in the number of configured fields · Space O(1) extra beyond the product

**Note:** always create a **fresh** builder per object — reusing a builder leaks state between builds.