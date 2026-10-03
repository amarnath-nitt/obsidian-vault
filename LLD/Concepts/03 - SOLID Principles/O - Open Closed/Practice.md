# Open/Closed - Practice

## Key Concepts
- **Open for extension, closed for modification** — add, don't edit
- The extension point is an **abstraction** (interface / abstract class)
- Reaches the same goal as **Strategy**, **Template Method** and **Decorator**

## Common OCP Moves in LLD
1. **Replace a `switch`** with polymorphism over the varying dimension
2. **Extract a rule/strategy interface** and register implementations
3. **One writer per format** instead of a format `if/else` chain
4. **Template Method** for "same skeleton, different steps"

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Extend Grading Policy](solutions/Extend-Grading-Policy.md) — AlgoMaster · easy · OCP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/extend-grading-policy)

### Medium
- [ ] [Refactor a Text Pipeline](solutions/Refactor-Text-Pipeline.md) — AlgoMaster · medium · OCP — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/refactor-text-pipeline)

---

## Extra Practice (self-study)

- [ ] Replace a `switch`/`if-else` chain with polymorphism
- [ ] Turn a hard-coded discount rule into a pluggable strategy

## Tips
- Say **"I'd introduce an abstraction here"** — then show the concrete class you'd add
- OCP and **YAGNI** are in tension: design *for* change, don't *pre-build* it
- A growing `switch` on the same value is the classic OCP smell
