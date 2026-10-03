# Refactor Login Guard (KISS)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** KISS
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-login-guard)

### Problem

A login guard has accumulated unnecessary indirection — a boolean that inverts a boolean, a
single-use helper, and a redundant lookup. The result is a simple check dressed up as complex code.
Apply **KISS**.

### The Smell (before)

```java
class LoginGuard {
    boolean canLogin(User user) {
        boolean notBlocked = !isBlocked(user);           // double negative
        boolean hasPassword = checkHasPassword(user);
        if (notBlocked == true) {                        // redundant == true
            if (hasPassword) {
                return user.isActive() == true;          // redundant == true
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
    private boolean checkHasPassword(User u) { return u.passwordHash() != null && !u.passwordHash().isBlank(); }
    private boolean isBlocked(User u) { return u.blocked(); }
}
```

### The Fix (after)

```java
class LoginGuard {
    boolean canLogin(User user) {
        return user.isActive()
            && !user.blocked()
            && hasPassword(user);
    }
    private boolean hasPassword(User u) {
        return u.passwordHash() != null && !u.passwordHash().isBlank();
    }
}
```

### Design points
- **One clear expression** — the rule reads like the requirement.
- **No redundant comparisons** — `== true`/`== false` removed.
- **No double negatives** — `!user.blocked()` instead of `!isBlocked`-then-invert.
- **Less indirection** — the single-use helper is inlined.

> **KISS principle:** prefer a short, direct expression over tangled control flow. If you need a
> comment to explain a boolean, the boolean is probably too clever.

**Complexity:** O(1) · Space O(1)

---
#design-principles #kiss #lld #practice