# Refactor Profile Service (Separation of Concerns)

**Source:** AlgoMaster · Low-Level Design Practice · **medium (premium)** · **Principle:** Separation of Concerns
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-profile-service)

### Problem

A `ProfileService` parses incoming request data, validates it, loads/saves from the database, and
renders a response — four concerns tangled in one class. Apply **Separation of Concerns**: split the
HTTP, domain, and persistence concerns.

### The Smell (before)

```java
// ❌ HTTP parsing + validation + persistence + rendering all in one place
class ProfileService {
    String handle(String rawBody) {
        String[] parts = rawBody.split("&");                 // parsing (HTTP concern)
        String name = parts[0].split("=")[1];
        String bio  = parts[1].split("=")[1];

        if (name.isBlank()) return "{\"error\":\"name required\"}";   // validation (domain)
        if (bio.length() > 200) return "{\"error\":\"bio too long\"}";

        System.out.println("UPDATE profiles SET name='" + name + "'"); // persistence
        return "{\"name\":\"" + name + "\",\"bio\":\"" + bio + "\"}";  // rendering (HTTP concern)
    }
}
```

### The Fix (after)

```java
import java.util.*;

// Domain model
record Profile(String name, String bio) {}

// Concern 1: parsing the request body
class ProfileRequestParser {
    Profile parse(String rawBody) {
        Map<String, String> fields = new HashMap<>();
        for (String pair : rawBody.split("&")) {
            String[] kv = pair.split("=", 2);
            fields.put(kv[0], kv.length > 1 ? kv[1] : "");
        }
        return new Profile(fields.getOrDefault("name", ""), fields.getOrDefault("bio", ""));
    }
}

// Concern 2: domain validation
class ProfileValidator {
    void validate(Profile profile) {
        if (profile.name().isBlank())   throw new IllegalArgumentException("name required");
        if (profile.bio().length() > 200) throw new IllegalArgumentException("bio too long");
    }
}

// Concern 3: persistence
interface ProfileRepository { void save(Profile profile); }
class InMemoryProfileRepository implements ProfileRepository {
    public void save(Profile profile) { System.out.println("Saved " + profile.name()); }
}

// Concern 4: rendering the response
class ProfileResponseWriter {
    String ok(Profile p) { return "{\"name\":\"" + p.name() + "\",\"bio\":\"" + p.bio() + "\"}"; }
    String error(String msg) { return "{\"error\":\"" + msg + "\"}"; }
}

// Coordinator — no concern of its own
class ProfileService {
    private final ProfileRequestParser parser;
    private final ProfileValidator validator;
    private final ProfileRepository repository;
    private final ProfileResponseWriter writer;

    ProfileService(ProfileRequestParser parser, ProfileValidator validator,
                   ProfileRepository repository, ProfileResponseWriter writer) {
        this.parser = parser; this.validator = validator;
        this.repository = repository; this.writer = writer;
    }

    String handle(String rawBody) {
        try {
            Profile profile = parser.parse(rawBody);
            validator.validate(profile);
            repository.save(profile);
            return writer.ok(profile);
        } catch (IllegalArgumentException e) {
            return writer.error(e.getMessage());
        }
    }
}
```

### Design points
- **HTTP concern** — parsing/writing live in their own classes.
- **Domain concern** — validation is pure and testable without HTTP or a database.
- **Persistence concern** — behind a `ProfileRepository` interface (also **DIP**).
- **Coordinator only** — `ProfileService` wires the pieces; it holds no rules.

**Complexity:** O(fields) per request · Space O(1)

---
#design-principles #separation-of-concerns #lld #practice