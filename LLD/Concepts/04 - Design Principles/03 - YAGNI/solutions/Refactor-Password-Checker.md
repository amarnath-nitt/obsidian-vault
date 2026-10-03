# Refactor Password Checker (YAGNI)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** YAGNI
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-password-checker)

### Problem

A password checker exposes a pile of configuration options — configurable min/max length, toggles for
every character class, a sets-of-forbidden-passwords hook, a leetspeak normaliser — most of which are
never used. Apply **YAGNI**: keep only the rule the product actually needs.

### The Smell (before)

```java
// ❌ A configurable "framework" for one simple rule
class PasswordChecker {
    private final PasswordPolicy policy;   // minLen, maxLen, requireUpper, requireLower,
                                           // requireDigit, requireSymbol, dictionary, leetspeak...
    boolean isValid(String pw) {
        if (pw == null) return false;
        if (pw.length() < policy.minLength || pw.length() > policy.maxLength) return false;
        if (policy.requireUpper  && pw.equals(pw.toLowerCase())) return false;
        if (policy.requireLower  && pw.equals(pw.toUpperCase())) return false;
        if (policy.requireDigit  && pw.chars().noneMatch(Character::isDigit)) return false;
        if (policy.requireSymbol && pw.chars().allMatch(Character::isLetterOrDigit)) return false;
        if (policy.dictionary != null && policy.dictionary.contains(pw)) return false;
        // ...leetspeak, history, etc. — never configured
        return true;
    }
}
```

### The Fix (after)

```java
// The actual required rule: at least 8 characters and one digit.
class PasswordChecker {
    private static final int MIN_LENGTH = 8;

    boolean isValid(String password) {
        if (password == null) return false;
        return password.length() >= MIN_LENGTH
            && password.chars().anyMatch(Character::isDigit);
    }
}
```

### Design points
- **Remove the configuration surface** — no unused policy object.
- **YAGNI** — implement the stated rule, not a general policy engine.
- **Trivial to read and test** — the requirement is visible at a glance.
- **Add options only when required** — if the product later needs complexity rules, introduce them then.

> **YAGNI principle:** don't build a framework before you have more than one use for it. A policy
> engine is justified by many policies — not by one.

**Complexity:** O(password length) · Space O(1)

---
#design-principles #yagni #lld #practice