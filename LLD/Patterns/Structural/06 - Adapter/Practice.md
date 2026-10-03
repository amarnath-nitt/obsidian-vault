# Adapter Pattern - Practice

## Key Concepts
- **Target** — the interface the client wants
- **Adaptee** — the existing incompatible class
- **Adapter** — implements Target, delegates to Adaptee
- **Object Adapter** — composition (preferred)
- **Class Adapter** — inheritance (rare in Java)

## Common Adapter Use Cases
1. **Payment gateways** — unify Stripe / PayPal / Razorpay behind one interface
2. **Logging libraries** — adapt SLF4J/Log4j behind your `AppLogger`
3. **Media players** — play MP4/VLC through a common `MediaPlayer`
4. **Data formats** — adapt an XML/CSV parser to a JSON model
5. **Legacy services** — wrap an old SOAP service as a REST-like client

---

## Problems (AlgoMaster)

> Real AlgoMaster exercises — each links to its own solution note **and** to the original problem.
> Toggle the checkbox to track your own completion progress.

### Easy
- [ ] [Implement Temperature Adapter](solutions/Implement-Temperature-Adapter.md) — AlgoMaster · easy — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/implement-temperature-adapter)

### Medium
- [ ] [Implement a Legacy Payment Adapter](solutions/Implement-Legacy-Payment-Adapter.md) — AlgoMaster · medium — [🔗 AlgoMaster](https://algomaster.io/practice/low-level-design/implement-legacy-payment-adapter)
- [ ] [Implement Notification Adapter](solutions/Implement-Notification-Adapter.md) — AlgoMaster · medium (premium) — [🔗 AlgoMaster index](https://algomaster.io/practice/low-level-design)

---

## Extra Practice (self-study)

- [ ] Media player adapter (MP4/VLC behind one player) — [reference code](solutions/Adapter-Implementations.md)
- [ ] Two-way adapter / class adapter — [reference code](solutions/Adapter-Implementations.md)
- [ ] Multi-gateway payment hub — [reference code](solutions/Adapter-Implementations.md)

---

## Tips
- **Object adapter (composition) is preferred** — it can wrap any subtype and is testable
- The adapter must **translate data**, not add behaviour
- Keep the **adaptee private** — never leak it through the Target API
- Say it in interviews: "Adapter = convert one interface; Facade = simplify a subsystem; Decorator = add behaviour"