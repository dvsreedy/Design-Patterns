# 🧠 Singleton Design Pattern

## 📘 Definition

The **Singleton Pattern** ensures that only one instance of a class exists throughout the application and provides a single global access point to that instance.

---

## 🎯 Intent

* Restrict instantiation of a class to a **single object**.
* Provide a **global access point** to that object.
* Maintain **shared state or configuration** across the application.

---

## 🧩 Real-World Analogy

A **printer spooler**, **database connection manager**, or **application configuration manager** is typically implemented as a Singleton — because multiple instances could lead to conflicts or inconsistent state.

---

## ⚙️ Key Characteristics

* **Single Instance:** Only one object is created.
* **Global Access:** Accessible via a static access method.
* **Lazy Initialization (optional):** Instance created only when needed.
* **Thread-Safety (optional):** Ensures no race conditions during creation.

---

## ✅ When to Use

Use the Singleton pattern when:

* Exactly **one object** is required to coordinate system-wide actions.
* You want to **control resource usage** and avoid redundant object creation.
* The same instance should be **accessible globally**.

Avoid Singleton when:

* Multiple instances are actually needed.
* You want to keep your system **loosely coupled** and **testable**.
* Hidden dependencies could lead to maintenance challenges.

---

## ⚖️ Pros and Cons

| **Pros**                                                    | **Cons**                                                                       |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Guarantees a single instance across the application.        | Introduces **global state**, making testing and debugging harder.              |
| Provides controlled access to shared resources.             | Can **violate Single Responsibility Principle** by managing its own lifecycle. |
| Enables **lazy initialization** to optimize resource usage. | Thread safety must be handled carefully in multithreaded environments.         |
| Simplifies access to configuration or shared data.          | Can lead to **tight coupling** between classes.                                |

---

## 🧱 Variants

* **Lazy Initialization:** Instance created on first use.
* **Eager Initialization:** Instance created at program start.
* **Thread-Safe Singleton:** Uses synchronization to ensure safety.
* **Meyers Singleton (Modern C++11):** Simplest and safest variant using static local variables.

---

## 🧩 Related Patterns

* **Factory Method:** Often uses Singleton to manage object creation.
* **Facade:** May depend on Singleton to coordinate subsystem operations.

---

## 🧾 Assignment

**Task:**
Create a **thread-safe Singleton Logger** that writes log messages to a file.

**Requirements:**

* Must use lazy initialization.
* Should ensure thread safety with synchronization.
* Demonstrate multiple threads writing concurrently to the same log file.


