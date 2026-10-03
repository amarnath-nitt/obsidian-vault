# Design Input Validator (Interfaces)

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Topic:** Interfaces
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-input-validator)

### Problem

Design a validation framework where **individual validation rules** (not empty, minimum length, valid
email) can be combined freely. Callers should depend on a single `Validator` interface and be able to
compose rules without the framework knowing the concrete rules.

### Approach

- Define a `Validator` interface returning an optional error message.
- Provide concrete validators.
- Compose several validators with a `ValidatorChain` (itself a `Validator` — Composite).

### Java Solution

```java
import java.util.*;

@FunctionalInterface
public interface Validator {
    /** Returns an error message, or empty if the input is valid. */
    Optional<String> validate(String input);
}

class NotEmptyValidator implements Validator {
    public Optional<String> validate(String input) {
        return (input == null || input.isBlank()) ? Optional.of("must not be empty") : Optional.empty();
    }
}
class MinLengthValidator implements Validator {
    private final int min;
    MinLengthValidator(int min) { this.min = min; }
    public Optional<String> validate(String input) {
        return (input != null && input.length() >= min) ? Optional.empty()
                : Optional.of("must be at least " + min + " characters");
    }
}
class EmailValidator implements Validator {
    public Optional<String> validate(String input) {
        return (input != null && input.matches("^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$")) ? Optional.empty()
                : Optional.of("must be a valid email");
    }
}

/** Composes several validators; itself a Validator (Composite). */
class ValidatorChain implements Validator {
    private final List<Validator> validators = new ArrayList<>();
    ValidatorChain add(Validator v) { validators.add(v); return this; }

    public Optional<String> validate(String input) {
        for (Validator v : validators) {
            Optional<String> error = v.validate(input);
            if (error.isPresent()) return error;      // first failure wins
        }
        return Optional.empty();
    }
}
```

**Usage**
```java
Validator emailField = new ValidatorChain()
        .add(new NotEmptyValidator())
        .add(new MinLengthValidator(5))
        .add(new EmailValidator());

emailField.validate("a@b.com");     // Optional.empty (valid)
emailField.validate("a@b");         // Optional["must be a valid email"]
```

### Design points
- **Program to an interface** — callers use `Validator`, never concrete rules.
- **Composable** — `ValidatorChain` is itself a `Validator`, so chains can nest.
- **Open/Closed** — add a `MaxLengthValidator` without changing the framework.

**Complexity:** O(rules) per validation · Space O(rules)

---
#oop #interfaces #lld #practice