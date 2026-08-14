# 🚗 LLD Problem: Design a Parking Lot

This document outlines the Low-Level Design for a parking lot system, a common interview problem that tests OOP principles, design patterns, and requirement analysis.

## 1. Requirements Gathering

Before we design, let's define what the system must do. It's always a good practice to separate functional (what it does) from non-functional (how it does it) requirements.

### Functional Requirements

1.  **Vehicle Entry & Parking**:
    *   The system should be able to park vehicles of different types (e.g., `Motorcycle`, `Car`, `Truck`).
    *   It must issue a `Ticket` upon entry, containing details like vehicle number, spot number, and entry time.
    *   It should find the first available parking spot suitable for the vehicle type.
    *   If the parking lot is full for a specific vehicle type, it should notify the user.

2.  **Vehicle Exit & Payment**:
    *   Upon exit, the system should calculate the parking fee based on the duration of the stay.
    *   It should process payments (we can assume a simple payment model for now).
    *   After successful payment, the parking spot should be marked as `vacant`.

3.  **System Administration & Display**:
    *   The system should be able to add/remove parking floors.
    *   It should be able to add/remove parking spots on each floor.
    *   There should be a display board showing the number of free spots for each vehicle type on each floor.

### Non-Functional Requirements & Assumptions

1.  **Scope**: We are designing for a single parking lot, not a chain of lots.
2.  **Structure**: The parking lot can have multiple floors.
3.  **Spot Types**: Each floor can have different types of parking spots (`SMALL` for motorcycles, `MEDIUM` for cars, `LARGE` for trucks).
4.  **Fee Calculation**: The fee calculation strategy is based on time. For now, let's assume a simple hourly rate that might differ per vehicle type.
5.  **Extensibility**: The design should be flexible enough to easily add new vehicle types (e.g., `ElectricCar` with charging) or new fee calculation strategies (e.g., daily rates, weekend rates) in the future.
6.  **Concurrency**: The system must handle multiple vehicles entering and exiting concurrently without conflicts (e.g., assigning the same spot to two vehicles).

---

These requirements give us a solid foundation. What do you think? Do these seem reasonable, or is there anything you'd like to add or change?

Once we agree on the requirements, the next logical step is to identify the core classes (or entities) of our system.