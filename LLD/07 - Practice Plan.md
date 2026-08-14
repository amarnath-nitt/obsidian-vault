# 7. LLD Practice Plan

This practice plan is designed to help you systematically approach LLD problems, building from foundational concepts to more complex design challenges.

#### 14-Day LLD Foundation Plan

| Day | Focus | Output |
|---|---|---|
| 1 | **SOLID Principles Deep Dive** | Explain each principle with a small code example, identifying violations and corrections. |
| 2 | **Creational Design Patterns** | Implement Singleton, Factory Method, and Builder patterns. Discuss their use cases. |
| 3 | **Structural Design Patterns** | Implement Adapter, Decorator, and Facade patterns. Explain how they structure code. |
| 4 | **Behavioral Design Patterns** | Implement Strategy, Observer, and Command patterns. Discuss their benefits for flexibility. |
| 5 | **OOP Concepts in Practice** | Refactor a simple class hierarchy to demonstrate encapsulation, abstraction, inheritance, and polymorphism. |
| 6 | **Composition vs. Inheritance** | Redesign a system component using composition where inheritance might have been initially considered. Justify the choice. |
| 7 | **UML Class Diagrams** | Draw a class diagram for a simple system (e.g., Library Management, ATM). |
| 8 | **UML Sequence Diagrams** | Draw a sequence diagram for a key use case in the system designed on Day 7. |
| 9 | **Design Principles (DRY, KISS, YAGNI)** | Review existing code (or write new code) and identify opportunities to apply these principles. |
| 10 | **Vending Machine LLD (Review)** | Re-implement the Vending Machine problem, focusing on state management and extensibility. |
| 11 | **Parking Lot LLD (Initial Draft)** | Design the core classes and interactions for a Parking Lot system. |
| 12 | **Elevator System LLD (Initial Draft)** | Design the core classes and interactions for an Elevator system. |
| 13 | **Traffic Light System LLD (Initial Draft)** | Design the core classes and interactions for a Traffic Light system. |
| 14 | **Mock LLD Interview** | Present one of your designs (Vending Machine, Parking Lot, etc.) and be prepared to discuss trade-offs and extensions. |

#### Advanced Practice Projects

Once you're comfortable with the foundational concepts, tackle these more complex LLD problems. Focus on identifying appropriate design patterns, applying SOLID principles, and discussing scalability and extensibility.

1.  **Parking Lot System**:
    *   **Core Features**: Park/unpark vehicles (cars, bikes, trucks), assign spots, calculate fees.
    *   **Advanced**: Different vehicle types, different parking spot sizes, payment integration, real-time availability, multi-level parking.
    *   **Key LLD Concepts**: Strategy (for fee calculation), Factory (for vehicle creation), Observer (for spot availability), State (for parking spot status), concurrency.

2.  **Elevator System**:
    *   **Core Features**: Call elevator, go to floor, open/close doors.
    *   **Advanced**: Multiple elevators, optimize movement, handle requests from multiple floors, emergency stops.
    *   **Key LLD Concepts**: State (for elevator/door status), Command (for floor requests), Observer (for elevator status updates), Producer-Consumer (for requests).

3.  **Traffic Light System**:
    *   **Core Features**: Cycle through red, yellow, green.
    *   **Advanced**: Multiple intersections, synchronized lights, pedestrian crossings, dynamic timing based on traffic flow.
    *   **Key LLD Concepts**: State (for light colors), Strategy (for timing algorithms), Observer (for intersection synchronization).

---
## 🔗 Related
- [[00 - Roadmap]]