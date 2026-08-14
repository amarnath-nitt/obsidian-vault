# 📘 LLD Revision Guide

A rapid-fire revision guide covering all LLD core concepts. Use this to review before interviews — each entry follows a Question → Answer format.

> [!tip] How to use
> Cover the answer, read the question, and try to answer aloud before revealing. This is active recall — the best way to retain LLD concepts.

---

## 🧱 Core OOP Concepts

> [!question] What is the difference between Encapsulation and Abstraction?
> **Encapsulation** is the *mechanism* of bundling data + methods together and controlling access (via `private` fields, getters/setters). **Abstraction** is the *concept* of hiding implementation details and exposing only what's necessary (via `abstract` classes and `interface`s). Encapsulation is *how* you hide; Abstraction is *what* you hide.

> [!question] What is composition over inheritance and why prefer it?
> Prefer **composition** ("has-a") over **inheritance** ("is-a") because it offers looser coupling, greater flexibility, and easier testing. Inheritance creates a rigid parent-child relationship; composition builds objects from interchangeable collaborators (e.g., `Car has-a Engine` rather than `Car extends Engine`).

---

## 🏛️ SOLID Principles

> [!question] What does each letter of SOLID stand for?
> - **S**ingle Responsibility — one class, one reason to change
> - **O**pen/Closed — open for extension, closed for modification
> - **L**iskov Substitution — subclasses must be substitutable for their base class
> - **I**nterface Segregation — many small interfaces > one fat interface
> - **D**ependency Inversion — depend on abstractions, not concretions

> [!question] Give a real example of the Open/Closed Principle (OCP).
> A `DiscountPolicy` interface with `Strategy` implementations (`FestivalDiscount`, `VIPDiscount`). To add a new discount, you create a new class — you don't modify `PricingService`. This is extension without modification.

---

## 🧵 Design Patterns

> [!question] What are the three categories of design patterns?
> - **Creational**: object creation (Singleton, Factory, Abstract Factory, Builder, Prototype)
> - **Structural**: composition of classes/objects (Adapter, Decorator, Facade, Proxy)
> - **Behavioral**: communication between objects (Strategy, Observer, State, Command, Template Method)

> [!question] Explain the Singleton pattern and its thread-safety concern.
> Ensures a class has only **one instance** with a global access point. In multithreaded environments, naive lazy init is unsafe. Use `enum`, `volatile` + double-checked locking, or eager init. Wrong answers use a plain `static` field with lazy init without synchronization.

> [!question] Factory Method vs Abstract Factory — what's the difference?
> **Factory Method**: creates *one* product, deferred to subclasses via an overridable method. **Abstract Factory**: creates a *family* of related products via multiple factory methods (e.g., a UI factory producing buttons + texts for Windows/Mac).

> [!question] When do you use the Strategy pattern over if-else?
> When you have **interchangeable algorithms** that vary at runtime. Encapsulate each algorithm in its own class implementing a common interface; swap them at runtime. This makes code testable and OCP-compliant — avoids long `if-else`/`switch` chains.

> [!question] Explain the Observer pattern.
> Defines a **one-to-many** dependency: when a `Subject` changes state, all registered `Observer`s are notified automatically. Used for event handling, notifications, and GUI listeners. Loose coupling — the subject doesn't know observer details.

> [!question] What is the State pattern and when is it useful?
> Encapsulates state-specific behavior in separate classes; an object's behavior changes when its internal state changes (like a state machine). Useful for complex state transitions (e.g., vending machine, elevator, order status flow).

> [!question] What is the Decorator pattern?
> Adds behavior to an object **dynamically** without modifying its code, by wrapping it. Flexible alternative to subclassing (e.g., Java `BufferedReader` wrapping `FileReader`). Each decorator implements the same interface and delegates + adds behavior.

> [!question] What is the Command pattern?
> Encapsulates a request as an object, allowing you to parameterize, queue, log, and undo operations. Useful for undo/redo, task queues, and decoupling the invoker from the executor.

> [!question] What is the Adapter pattern?
> Converts the interface of a class into another interface clients expect, allowing incompatible interfaces to work together (e.g., an adapter that lets an old `LegacyPrinter` work with a new `Printer` interface).

> [!question] What is the Facade pattern?
> Provides a simplified interface to a complex subsystem. Reduces dependencies and hides complexity (e.g., a `OrderFacade` wrapping inventory, payment, and shipping services).

---

## 📊 UML Diagrams

> [!question] What does a Class Diagram show?
> The **static structure**: classes, attributes, operations, and relationships (association, aggregation, composition, inheritance, realization, dependency). Visibility shown with `+` (public), `-` (private), `#` (protected).

> [!question] Association vs Aggregation vs Composition?
> - **Association**: general "uses/knows" relationship
> - **Aggregation**: whole-part, part can exist independently (`Department` has `Employee`s)
> - **Composition**: strong whole-part, part lifecycle owned by whole (`Order` has `OrderLine`s)

> [!question] When do you use a Sequence Diagram?
> To model **dynamic interaction** between objects over time for a specific use case — showing method calls and message flow in time order. Useful for documenting and debugging interactions.

---

## 🧠 Core Design Principles

> [!question] What is DRY?
> **Don't Repeat Yourself** — each piece of knowledge/logic should have a single, authoritative representation. Avoid duplicate code by using inheritance, composition, utility classes, and patterns.

> [!question] What is KISS?
> **Keep It Simple** — choose the simplest solution that meets requirements. Avoid over-engineering. Simple code is easier to understand, test, and maintain.

> [!question] What is YAGNI?
> **You Ain't Gonna Need It** — don't build features until they're actually required. Avoid speculative complexity that may never be used.

---

## 🛠️ Common LLD Problem Patterns

> [!question] How do you approach an LLD interview problem?
> 1. **Clarify requirements** (functional + non-functional)
> 2. **Identify core entities/classes**
> 3. **Draw the class diagram** (attributes + relationships)
> 4. **Choose design patterns** where appropriate
> 5. **Apply SOLID**
> 6. **Handle concurrency/edge cases**
> 7. **Write key code** (state transitions, methods)

> [!question] What design patterns are commonly used in a Parking Lot?
> - **Factory** — create vehicle types / spot types
> - **Strategy** — fee calculation variations
> - **Observer** — display board / notification updates
> - **Singleton** — the parking lot itself (typically one instance)

> [!question] How do you make an LLD system thread-safe?
> Use appropriate synchronization, `ConcurrentHashMap`, locks, atomic operations, or a central scheduler that serializes state changes. Identify which parts are shared mutable state and protect those.

---

## ✅ Quick Self-Check

Before your LLD interview, can you answer these aloud?

- [ ] Can you explain all 4 OOP pillars with code examples?
- [ ] Can you state all 5 SOLID principles and give an example each?
- [ ] Can you name + explain 5 design patterns (2 creational, 1 structural, 2 behavioral)?
- [ ] Can you draw a class diagram for Parking Lot / Vending Machine / Elevator?
- [ ] Can you explain Association vs Aggregation vs Composition?
- [ ] Can you explain DRY, KISS, YAGNI?
- [ ] Can you describe how you'd approach any LLD problem step-by-step?

---

## 🔗 Related
- [[00 - Roadmap]]
- [[01 - Introduction]]
- [[02 - SOLID Principles]]
- [[03 - Design Patterns]]
- [[09 - Rapid-Fire Concepts]]
- [[Problems/Parking-Lot]]
- [[Problems/Vending-Machine]]
- [[Problems/Elevator-System]]