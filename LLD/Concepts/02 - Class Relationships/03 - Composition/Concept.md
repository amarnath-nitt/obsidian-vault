# Composition — Concept

## What Is It?

A **strong "owns-a"**: the whole *creates, controls and destroys* its parts. Parts are exclusive —
they are never handed out to another object, and they do not outlive the whole.

| | |
|---|---|
| **Relationship** | Composition (`◆──`) |
| **One-liner** | Whole owns an exclusive part; the part dies with the whole |

---

## When to Use

> **Trigger keywords:** "consists of", "made up of", "rows belong to the order", "never shared"

| Trigger | Move |
|---------|------|
| Parts are created inside the whole | composition |
| The part has no meaning without the whole | composition |
| Parts must never be shared | composition |

---

## In Java

```java
class SlideDeck {
    private final List<Slide> slides = new ArrayList<>();   // created here...

    void addSlide(String title) { slides.add(new Slide(title)); }   // ...and owned here

    List<Slide> slides() { return Collections.unmodifiableList(slides); }  // never handed out
}
// ...destroyed with the deck. A Slide has no purpose outside its deck.
```

---

## The lifetime test

> **"If the whole is destroyed, does the part still make sense?"**
> **No → composition. Yes → aggregation.**

| | Aggregation `◇──` | Composition `◆──` |
|---|---|---|
| Ownership | weak — shared | strong — exclusive |
| Lifetime | part survives the whole | part dies with the whole |
| Java | reference passed in | created internally |
| Example | Team ◇── Player | Order ◆── OrderLine |

---

## Notes

- Composition is the default answer to **"prefer composition over inheritance"**.
- Return **unmodifiable views** — never expose the owned list for mutation.
- In UML it's a filled diamond on the whole side.

---

## Common Mistakes

1. Handing a composed part to another object (breaks exclusive ownership).
2. Creating a part outside and injecting it while claiming composition.
3. Choosing inheritance where composition was intended.

---

## Related

- [[../00 - Index|Class Relationships Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]
- [[../02 - Aggregation/Concept|Aggregation]] · [[../01 - Association/Concept|Association]]

---

#relationships #composition #lld #concept
