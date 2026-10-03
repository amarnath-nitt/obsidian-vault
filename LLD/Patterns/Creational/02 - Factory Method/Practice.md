# Factory Method Pattern - Practice

## Key Concepts
- **Product** interface + concrete products
- **Creator** declares the factory method; subclasses decide the concrete product
- **Client** depends only on abstractions
- **Simple Factory** — one class, switch-based (fast, not OCP)
- **Named static factory** — `of()`, `valueOf()`, `getInstance()`

## Common Factory Use Cases
1. **Notification system** — Email / SMS / Push senders
2. **Payment gateways** — Card / UPI / PayPal / Stripe
3. **Document editor** — `open()` returns Word/PDF/Markdown
4. **Parser selection** — parse by file extension
5. **Logger creation** — Console / File / Cloud loggers

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Design Shape Factory](solutions/Design-Shape-Factory.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-shape-factory)

### Medium
- [ ] [Design Plugin System](solutions/Design-Plugin-System.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/design-plugin-system-factory)

---

## Extra Practice (self-study)

- [ ] Notification factory (Email/SMS/Push) — [reference code](solutions/Factory-Method-Implementations.md)
- [ ] Payment gateway factory — [reference code](solutions/Factory-Method-Implementations.md)
- [ ] Registered factory (`Map<Type, Supplier<Product>>`) — [reference code](solutions/Factory-Method-Implementations.md)

---

## Tips
- **Return the interface**, never the concrete class
- **Throw a clear exception** for unknown types
- **Register creators in a `Map<Type, Supplier<Product>>`** to stay OCP
- **Say it in interviews:** "Factory Method = one product; Abstract Factory = a family"