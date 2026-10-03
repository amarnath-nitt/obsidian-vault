# Association - Practice

## Key Concepts
- A **peer link** — both ends exist independently, no ownership
- Give the link its own class when it **carries data** (`role`, `since`, `grade`)
- Many-to-many links are usually an **association class**

## Common Association Moves in LLD
1. **Model the link** — `Enrollment`, `Follow`, `Booking` instead of a bare reference list
2. **Store both ends** — the association object holds references to each peer
3. **Put the link's attributes on the link** — not on either peer
4. **Draw `-->`** on the class diagram — the relationship is part of the design

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Course Registry](solutions/Design-Course-Registry.md) — AlgoMaster · easy · Association — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-course-registry)

### Medium
- [ ] [Design Follow Graph](solutions/Design-Follow-Graph.md) — AlgoMaster · medium · Association — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-follow-graph)

---

## Extra Practice (self-study)

- [ ] Model `Student --> Course` with an `Enrollment` association class
- [ ] Decide for each link: does either end own the other? (usually no)

## Tips
- Say **"peer link, no ownership"** — it's what distinguishes association from aggregation/composition
- If the relationship has fields, it's a **class**, not a pointer
- Association is the baseline; the others add ownership on top
