# Separation of Concerns - Practice

## Key Concepts
- **One module, one concern** — parsing, rules, persistence and rendering are separate
- The coordinator holds **no rules of its own**
- Put persistence behind a **repository interface** (also satisfies DIP)

## Common SoC Moves in LLD
1. **Split the layers** — controller → service → repository
2. **Extract the parser** — raw input becomes a domain object on its own
3. **Extract the validator** — pure rules, testable with no I/O
4. **Extract the writer/serializer** — presentation lives at the edge

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Refactor Profile Service](solutions/Refactor-Profile-Service.md) — AlgoMaster · medium (premium) · SoC — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-profile-service)
- [ ] [Refactor Expense Importer](solutions/Refactor-Expense-Importer.md) — AlgoMaster · medium (premium) · SoC — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-expense-importer)

---

## Extra Practice (self-study)

- [ ] Find a class that does parsing + rules + storage and split it into three
- [ ] Write a test for your domain rules that touches neither HTTP nor SQL

## Tips
- **SoC is the parent of SRP** — say "separation of concerns at the layer level, SRP at the class level"
- A thin coordinator with four collaborators is the picture interviewers want
- Each split stage becomes independently **testable**
