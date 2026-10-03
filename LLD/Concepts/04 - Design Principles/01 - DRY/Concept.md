# DRY — Concept

## What Is It?

**Don't Repeat Yourself.** Every piece of *knowledge* should have a single, authoritative
representation in the system. Duplication means a change must be applied in several places — and
eventually one is missed.

| | |
|---|---|
| **Principle** | DRY — Don't Repeat Yourself |
| **One-liner** | One home for each piece of knowledge |

---

## When to Use

> **Trigger keywords:** "copy-pasted", "the same rule in three places", "we updated one and forgot the other"

| Smell | Move |
|-------|------|
| The same validation appears in several methods | extract one validator |
| Magic numbers duplicated across classes | one constant / price book |
| Two code paths implement the same business rule | one shared rule object |

---

## In Java

```java
// ❌ Same tax rule duplicated
double usTotal = price * 1.07;
double caTotal = price * 1.07;   // copy-pasted — change one, forget the other

// ✅ One home for the rule
static final double TAX_RATE = 1.07;
double total = price * TAX_RATE;
```

---

## Notes

- **DRY is about *knowledge*, not *text*.** Two identical-looking lines that change for *different
  reasons* should stay separate — merging them is premature abstraction.
- Extract when the *why* is shared; keep separate when only the *what* happens to match today.
- The opposite smell is **Shotgun Surgery** (one change, many files) — DRY's usual symptom.

---

## Common Mistakes

1. DRY-ing unrelated code that merely looks alike (over-abstraction).
2. Sharing a method whose two callers will diverge, forcing `if (caller == ...)` branches.
3. Waiting for the *third* duplication before abstracting (rule of three).

---

## Related

- [[../00 - Index|Design Principles Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#design-principles #dry #lld #concept
