# Proxy Pattern - Practice

## Key Concepts
- **Subject** — interface shared by proxy and real subject
- **RealSubject** — the real worker
- **Proxy** — same interface, controls access, delegates
- **Virtual proxy** — lazy initialisation
- **Protection proxy** — access control
- **Dynamic proxy** — runtime-generated (`java.lang.reflect.Proxy`)

## Common Proxy Use Cases
1. **Lazy image loading** — create the heavy object on first use
2. **Access control** — role-based permission checks
3. **Caching** — memoize expensive calls
4. **Logging / auditing** — record every invocation
5. **Remote / RPC stub** — local representative of a remote service
6. **Spring AOP** — `@Transactional`, `@Cacheable`, security

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Medium
- [ ] [Implement a Lazy Image Proxy](solutions/Implement-Lazy-Image-Proxy.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/implement-lazy-image-proxy)
- [ ] [Implement a Secure Report Proxy](solutions/Implement-Secure-Report-Proxy.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/implement-secure-report-proxy)

### Hard
- [ ] [Design a Caching Weather Proxy](solutions/Design-Caching-Weather-Proxy.md) — AlgoMaster · hard (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Logging proxy / dynamic JDK proxy — [reference code](solutions/Proxy-Implementations.md)
- [ ] Protection proxy for a bank account — [reference code](solutions/Proxy-Implementations.md)
- [ ] Thread-safe lazy proxy (double-checked init) — [reference code](solutions/Proxy-Implementations.md)

---

## Tips
- Say it in interviews: **"Proxy = same interface, controls access; Decorator = same interface, adds behaviour; Adapter = changes the interface."**
- A proxy **often creates/owns** its real subject; a decorator is **given** it
- Keep the proxy **faithful** to the Subject contract
- Guard lazy init with **double-checked locking** when threads are involved