# 🎯 Design Patterns in C++

This repository is dedicated to learning, understanding, and implementing **Design Patterns** in C++.
It includes theoretical explanations, example implementations, and practical exercises for each pattern.

---

## 🧱 Object-Oriented Programming (OOP) Principles

OOP forms the foundation for understanding and applying design patterns effectively.

| Principle         | Description                                                                 | Pros                                              | Cons                                               |
| ----------------- | --------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Encapsulation** | Binding data and methods that operate on that data within one unit (class). | Protects data integrity, improves modularity.     | Can lead to over-abstraction if misused.           |
| **Abstraction**   | Hiding internal details and showing only the necessary features.            | Simplifies complexity, enhances code readability. | Too much abstraction may make debugging harder.    |
| **Inheritance**   | Deriving new classes from existing ones to reuse functionality.             | Promotes reusability, reduces redundancy.         | Tight coupling, may introduce fragile hierarchies. |
| **Polymorphism**  | Ability to process objects differently based on their type.                 | Improves flexibility and scalability.             | May increase runtime overhead, complex debugging.  |

---

## 🧭 Key Design & Development Principles

### **KISS – Keep It Simple, Stupid**

* **Definition:** Aim for simplicity in design and implementation. Avoid unnecessary complexity.
* **Where used:** Everywhere – especially in system and API design.
* **Pros:** Easier to read, maintain, and test.
* **Cons:** Over-simplification can reduce flexibility.

### **YAGNI – You Aren’t Gonna Need It**

* **Definition:** Don’t add functionality until it’s necessary.
* **Where used:** During feature planning, refactoring, and code reviews.
* **Pros:** Reduces over-engineering and maintenance cost.
* **Cons:** May lead to rework if requirements expand later.

### **SOLID Principles**

| Principle                               | Description                                                                 | Example Usage                                                 | Benefit                                            |
| --------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------- |
| **S – Single Responsibility Principle** | A class should have one and only one reason to change.                      | Logger class handles only logging, not file rotation.         | Easier maintenance, better separation of concerns. |
| **O – Open/Closed Principle**           | Software entities should be open for extension but closed for modification. | Add new shapes without modifying Shape base class.            | Enables flexibility, reduces regression bugs.      |
| **L – Liskov Substitution Principle**   | Subclasses must be substitutable for their base classes.                    | Derived class should not break base class behavior.           | Ensures consistency in polymorphism.               |
| **I – Interface Segregation Principle** | No client should be forced to depend on interfaces it doesn’t use.          | Smaller interfaces like `IReadable`, `IWritable`.             | Improves modularity and reusability.               |
| **D – Dependency Inversion Principle**  | Depend on abstractions, not concretions.                                    | High-level modules depend on interfaces, not implementations. | Enhances flexibility, testability.                 |

**Pros:** Improves maintainability, scalability, and extensibility.
**Cons:** Can lead to more classes/interfaces and initial complexity.

---

## 🧩 What Are Design Patterns?

Design patterns are **proven, reusable solutions** to common software design problems.
They act as templates for solving recurring issues in system architecture and object interaction.

### **Why Are Design Patterns Used?**

* Promote **code reusability** and **consistency**.
* Improve **communication** between developers (shared vocabulary).
* Enable **scalability** and **flexible architecture**.
* Help follow **SOLID principles** effectively.

---

## 💡 Why Design Patterns Are Important

* They **standardize** the way problems are solved in software engineering.
* Provide **time-tested best practices** to avoid reinventing the wheel.
* Improve **readability**, **maintainability**, and **testability** of code.
* Make it easier to **refactor** or extend functionality without breaking existing systems.
* Boost your **interview readiness** by showcasing architectural thinking.

---

## 🧠 Types of Design Patterns

Design patterns are broadly categorized into three groups:

| Category       | Description                              | Common Patterns                                                                                  | Example Use Cases                                                |
| -------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **Creational** | Deal with object creation mechanisms.    | Singleton, Factory, Abstract Factory, Builder, Prototype                                         | Managing object creation efficiently, ensuring single instances. |
| **Structural** | Deal with class and object composition.  | Adapter, Bridge, Composite, Decorator, Proxy, Flyweight, Facade                                  | Building flexible and scalable system architectures.             |
| **Behavioral** | Deal with communication between objects. | Strategy, Observer, Command, State, Template Method, Mediator, Iterator, Chain of Responsibility | Handling workflows, event systems, or dynamic behavior changes.  |

---

## 🚀 Repository Structure

```
├── creational/
│   ├── singleton/
│   ├── factory/
│   └── builder/
├── structural/
│   ├── adapter/
│   ├── decorator/
│   └── composite/
├── behavioral/
│   ├── strategy/
│   ├── observer/
│   └── command/
├── assignments/
│   ├── mid_assignment_1/
│   └── final_project/
└── README.md
```

---

## 🧩 How to Use This Repository

1. Each folder contains:

   * **Concept explanation**
   * **C++ implementation**
   * **Test/demo file**
2. Clone the repo:

   ```bash
   git clone https://github.com/<your-username>/cpp-design-patterns.git
   ```
3. Compile & run examples using:

   ```bash
   g++ pattern_name.cpp -o pattern && ./pattern
   ```
4. Track your progress using the **Excel schedule** you created.

---

## 🏁 Goal

By the end of this journey, you’ll:

* Understand the **purpose and structure** of all major design patterns.
* Know **when and where to apply** each pattern in real-world C++ development.
* Be **interview-ready** for architecture and design-related questions.

Would you like me to tailor this README to include your **GitHub repo name**, and maybe add a short section for “Assignments & Progress Tracker” that links to your Excel sheet and code folders?
