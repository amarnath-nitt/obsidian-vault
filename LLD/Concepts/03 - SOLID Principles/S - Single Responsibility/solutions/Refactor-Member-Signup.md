# Refactor Member Signup (Single Responsibility)

**Source:** AlgoMaster · Low-Level Design Practice · **hard** · **Principle:** Single Responsibility
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/refactor-member-signup)

### Problem

A `MemberSignup` service does everything: validates the form, hashes the password, checks for
duplicate emails, saves the member, and sends a welcome email. Each of those is a separate reason to
change. Refactor into focused collaborators with one orchestrator.

### The Smell (before)

```java
// ❌ A god class: validation + security + persistence + notification
class MemberSignup {
    void signup(String email, String password, String name) {
        if (!email.contains("@")) throw new IllegalArgumentException("bad email");
        if (password.length() < 8) throw new IllegalArgumentException("weak password");

        String hash = Integer.toHexString(password.hashCode());        // "hashing"
        System.out.println("Checking duplicates for " + email);        // duplicate check
        System.out.println("Saving member " + name);                   // persistence
        System.out.println("Sending welcome to " + email);             // notification
    }
}
```

### The Fix (after)

```java
record Member(String id, String email, String name, String passwordHash) {}

class SignupValidator {                                 // one job: validate input
    void validate(String email, String password) {
        if (email == null || !email.contains("@")) throw new IllegalArgumentException("bad email");
        if (password == null || password.length() < 8) throw new IllegalArgumentException("weak password");
    }
}

interface PasswordHasher {                              // one job: hash (abstraction → DIP)
    String hash(String raw);
}
class SimpleHasher implements PasswordHasher {
    public String hash(String raw) { return Integer.toHexString(raw.hashCode()); }
}

interface MemberRepository {                            // one job: persistence
    boolean existsByEmail(String email);
    Member save(Member member);
}
class InMemoryMemberRepository implements MemberRepository {
    private final java.util.Map<String, Member> byEmail = new java.util.HashMap<>();
    private int seq = 0;
    public boolean existsByEmail(String email) { return byEmail.containsKey(email); }
    public Member save(Member member) {
        Member saved = new Member("M" + (++seq), member.email(), member.name(), member.passwordHash());
        byEmail.put(saved.email(), saved);
        return saved;
    }
}

interface WelcomeNotifier { void sendWelcome(Member member); }   // one job: notify
class EmailWelcomeNotifier implements WelcomeNotifier {
    public void sendWelcome(Member m) { System.out.println("Sent welcome to " + m.email()); }
}

// Orchestrator — no business rules of its own
class MemberSignup {
    private final SignupValidator validator;
    private final PasswordHasher hasher;
    private final MemberRepository repository;
    private final WelcomeNotifier notifier;

    MemberSignup(SignupValidator validator, PasswordHasher hasher,
                 MemberRepository repository, WelcomeNotifier notifier) {
        this.validator = validator; this.hasher = hasher;
        this.repository = repository; this.notifier = notifier;
    }

    Member signup(String email, String password, String name) {
        validator.validate(email, password);
        if (repository.existsByEmail(email)) throw new IllegalStateException("email already registered");
        Member member = repository.save(new Member(null, email, name, hasher.hash(password)));
        notifier.sendWelcome(member);
        return member;
    }
}
```

**Usage**
```java
MemberSignup signup = new MemberSignup(
        new SignupValidator(), new SimpleHasher(),
        new InMemoryMemberRepository(), new EmailWelcomeNotifier());

signup.signup("alice@example.com", "password123", "Alice");
```

### Design points
- **One responsibility each** — validation, hashing, persistence, and notification are separate.
- **Orchestrator, not a god class** — `MemberSignup` coordinates but implements no rules.
- **DIP for free** — every collaborator is an interface injected in, so it is mockable.
- **Focused tests** — test the validator, hasher, and notifier independently.

**Complexity:** O(1) per signup (repository-dependent) · Space O(members)

---
#solid #srp #lld #practice