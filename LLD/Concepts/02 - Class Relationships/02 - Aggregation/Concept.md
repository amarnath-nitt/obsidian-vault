# Aggregation — Concept

## What Is It?

A **weak "has-a"**: the whole *shares* parts that can exist, be reused, and outlive it. The classic
tell-tale is a collection whose elements were *passed in*, not *created inside*.

| | |
|---|---|
| **Relationship** | Aggregation (`◇──`) |
| **One-liner** | Whole shares a part; the part can outlive the whole |

---

## When to Use

> **Trigger keywords:** "contains", "groups", "catalog", "shared", "can be reused elsewhere"

| Trigger | Move |
|---------|------|
| A whole holds parts that can be shared | aggregation |
| The part arrives from outside (constructor/setter) | aggregation |
| Destroying the whole would not destroy the parts | aggregation |

---

## In Java

```java
class Library {
    private final List<Playlist> playlists;      // playlists can exist without this library

    Library(List<Playlist> playlists) {          // passed in -> shared, not owned
        this.playlists = List.copyOf(playlists);
    }
}
```

---

## Aggregation vs Composition — the deciding test

> **"If the whole is destroyed, does the part still make sense?"**
> **Yes → aggregation. No → composition.**

| | Aggregation `◇──` | Composition `◆──` |
|---|---|---|
| Ownership | weak — shared | strong — exclusive |
| Lifetime | part survives the whole | part dies with the whole |
| Java | store a reference passed in | create the part internally |
| Example | Library ◇── Playlist | SlideDeck ◆── Slide |

---

## Notes

- Aggregation means the whole does **not** control the part's lifetime.
- Parts are typically **injected** via constructor or setter.
- In UML it's a hollow diamond on the whole side.

---

## Common Mistakes

1. Creating parts inside the whole and calling it aggregation (that's composition).
2. Sharing a *composed* part with another object.
3. Getting the lifetime question backwards — ask it explicitly.

---

## Related

- [[../00 - Index|Class Relationships Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../03 - Composition/Concept|Composition]] · [[../01 - Association/Concept|Association]]

---

#relationships #aggregation #lld #concept
