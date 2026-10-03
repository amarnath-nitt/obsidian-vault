# Class Diagram - Practice

## Key Concepts
- **Box format** — name + attributes (`-` private, `+` public, `#` protected) + operations
- **Relationships** — inheritance `──▷`, realisation `╌╌▷`, association `──`, aggregation `◇──`, composition `◆──`, dependency `╌╌▶`
- **Multiplicity** — `1`, `0..1`, `*`, `1..*` at the ends; the design lives in the relationships, not the boxes

## Common Triggers in Interviews
| Trigger | Response |
|---------|----------|
| "design the classes" / "show relationships" | draw the class diagram **first** |
| "who owns what" / "extend" / "use" / "contain" | pick the relationship: is-a vs has-a vs owns-a vs uses |
| "does the part die with the whole?" → yes | **composition** `◆──` |
| "does the part outlive the whole?" → yes | **aggregation** `◇──` |

---

## Exercises (self-study)

> UML has no AlgoMaster exercise — this package is the core LLD deliverable. Work these by hand (or Mermaid), then reuse the skill in every Problems package.

- [ ] **Draw the box** — a `ParkingSpot` class with 3 attributes and 2 operations in correct box format with visibilities
- [ ] **Name the relationship** — for each pair, pick inheritance / realisation / association / aggregation / composition / dependency: `Car–Vehicle`, `CreditCard–PaymentMethod`, `Order–OrderLine`, `Department–Professor`, `Order–InvoiceService`
- [ ] **Add multiplicity** — `Order–OrderLine`, `Customer–Order`, `ParkingLot–Floor–Spot`: write the correct `1`, `*`, `1..*` at each end
- [ ] **Mermaid drill** — reproduce the PaymentMethod / CreditCard / Upi + Order composition diagram from Concept.md in Mermaid without looking

---

## Extra Practice

- [ ] Take any Easy problem (e.g. Parking Lot) and draw its full class diagram before writing code
- [ ] Review a class diagram and delete every class not referenced by a use case — over-modelling check

## Tips
- **Relationships are the design** — boxes without relationships score nothing
- Say *"composition or aggregation?"* out loud and answer with the dies-with-the-whole test
- Always label multiplicity — `Order` has `1..*` lines, not an unbounded list
