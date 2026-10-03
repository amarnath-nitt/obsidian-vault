# Composition - Practice

## Key Concepts
- **Strong "owns-a"** — the whole creates, controls and destroys its parts
- **Lifetime test:** if the whole dies, the part dies → composition ◆──
- Never hand a composed part to another object

## Common Composition Moves in LLD
1. **Create parts internally** — `slides.add(new Slide(title))`
2. **Return unmodifiable views** — don't leak the owned collection
3. **Destroy with the whole** — no external references keeping parts alive
4. **Draw the filled diamond** ◆ on the whole side of the diagram

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Slide Deck](solutions/Design-Slide-Deck.md) — AlgoMaster · easy · Composition — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-slide-deck)

### Medium
- [ ] [Design Computer Workshop](solutions/Design-Computer-Workshop.md) — AlgoMaster · medium · Composition — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-computer-workshop)

### Hard
- [ ] [Design Video Editor](solutions/Design-Video-Editor.md) — AlgoMaster · hard · Composition — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-video-editor)

---

## Extra Practice (self-study)

- [ ] Model `Order ◆── OrderLine` and explain why order lines don't outlive the order
- [ ] Convert an inheritance hierarchy into composition

## Tips
- Answer with the **lifetime question** — fastest way to show mastery
- Composition is the **default** for reuse; inheritance must justify itself
- A composed part must never be **shared**
