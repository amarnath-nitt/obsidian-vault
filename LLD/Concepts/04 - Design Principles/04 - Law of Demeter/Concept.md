# Law of Demeter — Concept

## What Is It?

**Talk to your friends, not strangers.** A method should only call methods on: itself, its own
fields, its parameters, objects it creates, or its immediate components — never on objects
*returned* by those calls.

| | |
|---|---|
| **Principle** | Law of Demeter |
| **One-liner** | Don't reach through — ask your immediate collaborator |

---

## When to Use

> **Trigger keywords:** long navigation chains, "changes deep in the object graph break this class"

| Smell | Move |
|-------|------|
| `order.getCustomer().getAddress().getCity()` | add a delegating method on `Order` |
| `a.getB().getC().doSomething()` | `a.doSomething()` |
| A class knows the internal structure of a graph | have the owner answer the question |

---

## In Java

```java
// ❌ Reaching through four objects
String city = building.getRoom("r1").getThermostat().getSensor().getCity();

// ✅ One friend: the building answers
String city = building.cityOf("r1");
```

---

## The fix: **delegating methods**

```java
class Room {
    private final Thermostat thermostat;
    double temperature() { return thermostat.currentTemperature(); }  // Room asks, not the caller
}
```

Each object hides its internals and answers its own questions, so callers hold **one** dependency
instead of a chain.

---

## Notes

- Violating Demeter creates ** shotgun surgery**: an internal change ripples to every caller.
- It's about *object* navigation, not about number of lines.
- Sometimes called the "one dot" rule in its strictest form.

---

## Common Mistakes

1. Adding getters just to build a longer chain elsewhere.
2. Forgetting that a **value object** (`ShippingInfo`) can bundle what the caller needs.
3. Treating it as dogma — a local, owned component's methods are fine.

---

## Related

- [[../00 - Index|Design Principles Index]]
- [[../../00 - Index|Concepts Index]]
- [[../../../00 - Index|LLD Main Index]]

---

#design-principles #law-of-demeter #lld #concept
