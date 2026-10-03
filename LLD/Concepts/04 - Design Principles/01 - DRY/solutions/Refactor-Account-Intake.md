# Refactor Account Intake (DRY)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** DRY
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-account-intake)

### Problem

An account intake service validates member details in several places — signup, admin import, and
profile update — each with its own copy of the same rules. When a rule changes, one copy is missed.
Apply **DRY**: give the knowledge a single home.

### The Smell (before)

```java
class AccountIntake {
    void signup(String email, String name) {
        if (email == null || !email.contains("@")) throw new IllegalArgumentException("bad email");
        if (name == null || name.isBlank())        throw new IllegalArgumentException("bad name");
        // ... create account
    }
    void adminImport(String email, String name) {
        if (email == null || !email.contains("@")) throw new IllegalArgumentException("bad email");  // duplicated
        if (name == null || name.isBlank())        throw new IllegalArgumentException("bad name");   // duplicated
        // ... create account
    }
    void updateProfile(String email, String name) {
        if (email == null || !email.contains("@")) throw new IllegalArgumentException("bad email");  // duplicated
        // ...
    }
}
```

### The Fix (after)

Extract the rules into one authoritative place and reuse it everywhere.

```java
// The single home for account-detail rules
final class AccountRules {
    private AccountRules() {}

    static void validateEmail(String email) {
        if (email == null || !email.contains("@"))
            throw new IllegalArgumentException("bad email");
    }
    static void validateName(String name) {
        if (name == null || name.isBlank())
            throw new IllegalArgumentException("bad name");
    }
    static void validateDetails(String email, String name) {
        validateEmail(email);
        validateName(name);
    }
}

class AccountIntake {
    void signup(String email, String name) {
        AccountRules.validateDetails(email, name);
        // ... create account
    }
    void adminImport(String email, String name) {
        AccountRules.validateDetails(email, name);      // no duplication
        // ... create account
    }
    void updateProfile(String email, String name) {
        AccountRules.validateEmail(email);              // reuse just what's needed
        // ...
    }
}
```

### Design points
- **One home for each rule** — change the email rule once; all callers update.
- **Small composable methods** — `validateEmail` / `validateName` reused individually or together.
- **DRY ≠ text** — these genuinely share *knowledge*, so merging is correct.

**Complexity:** O(1) per validation · Space O(1)

---
#design-principles #dry #lld #practice