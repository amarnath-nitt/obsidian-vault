# Extend Grading Policy (Open/Closed)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Principle:** Open/Closed
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/extend-grading-policy)

### Problem

A grading service converts a numeric score to a letter grade using a growing `if/else` chain. Adding a
new grading scheme (e.g. pass/fail, curved grades) means editing the method. Refactor it so new
policies can be **added without modifying** existing code.

### The Smell (before)

```java
// ❌ Every new policy edits this method (violates Open/Closed)
class GradingService {
    String grade(int score, String policy) {
        if (policy.equals("letter")) {
            if (score >= 90) return "A";
            if (score >= 80) return "B";
            return "C";
        } else if (policy.equals("passfail")) {
            return score >= 50 ? "PASS" : "FAIL";
        }
        // ... more branches added over time
        throw new IllegalArgumentException("unknown policy");
    }
}
```

### The Fix (after)

```java
// The extension point — open for extension, closed for modification
interface GradingPolicy {
    String grade(int score);
    String name();
}

class LetterGradePolicy implements GradingPolicy {
    public String name()  { return "letter"; }
    public String grade(int score) {
        if (score >= 90) return "A";
        if (score >= 80) return "B";
        if (score >= 70) return "C";
        return "F";
    }
}

class PassFailPolicy implements GradingPolicy {
    public String name()  { return "passfail"; }
    public String grade(int score) { return score >= 50 ? "PASS" : "FAIL"; }
}

class GradingService {
    private final Map<String, GradingPolicy> policies = new HashMap<>();

    void register(GradingPolicy policy) { policies.put(policy.name(), policy); }

    String grade(int score, String policyName) {
        GradingPolicy policy = policies.get(policyName);
        if (policy == null) throw new IllegalArgumentException("unknown policy: " + policyName);
        return policy.grade(score);                 // never edited when a policy is added
    }
}
```

**Usage**
```java
GradingService service = new GradingService();
service.register(new LetterGradePolicy());
service.register(new PassFailPolicy());

service.grade(85, "letter");    // "B"
service.grade(85, "passfail");  // "PASS"

// New policy — NO change to GradingService:
service.register(score -> score >= 95 ? "A+" : "A-" ...);   // a lambda policy
```

### Design points
- **Closed for modification** — `GradingService` never changes when a policy is added.
- **Open for extension** — a new `GradingPolicy` (or a lambda) plugs straight in.
- **Polymorphism replaces branching** — the `if/else` chain is gone.

**Complexity:** O(1) per grade · Space O(policies)

---
#solid #ocp #lld #practice