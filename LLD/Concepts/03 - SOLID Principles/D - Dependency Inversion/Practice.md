# Dependency Inversion - Practice

## Key Concepts
- **High-level modules depend on abstractions**, not concretions
- **Constructor injection** is the usual mechanism: pass the collaborator in
- The abstraction should live **with the module that needs it**

## Common DIP Moves in LLD
1. **Extract a port** — `OrderRepository`, `PaymentGateway`, `Clock`
2. **Inject via constructor** — make the dependency explicit and visible
3. **Fake it in tests** — an in-memory implementation behind the same interface
4. **Move the `new` to the edge** — composition root / factory wires concretes

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### AlgoMaster exercise set
> **Note:** AlgoMaster does not currently publish a DIP-labelled low-level-design exercise.
> The DIP refactors appear inside the SRP/OCP/ISP exercises (repositories, gateways and
> injected collaborators) — work those, then return here for self-study.

---

## Extra Practice (self-study)

- [ ] Take a class that `new`s its dependencies and inject them via the constructor
- [ ] Write an in-memory implementation of a repository interface and use it in a test
- [ ] Identify one place where your domain logic imports an infrastructure SDK

## Tips
- **Say "constructor injection"** — it is the concrete answer interviewers want
- An abstraction for every class is noise: introduce interfaces where there is a **real variation**
- ISP + DIP together: *"narrow interfaces are easier to depend on and easier to fake"*
