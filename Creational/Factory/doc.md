# Factory Method Design Pattern

## Overview

The **Factory Method Design Pattern** is a creational pattern that defines an interface for creating objects in a superclass, while allowing subclasses to decide which specific class to instantiate. This provides flexibility in object creation and supports scalable, maintainable code structures.

## Why Factory Method?

The pattern is particularly useful when:

* The exact type of object to be created isn't known until runtime.
* Object creation involves complex logic or requires encapsulation.
* You want to avoid tightly coupling your code to specific concrete classes.
* You need to adhere to the **Open/Closed Principle** — open for extension, closed for modification.

## Key Benefits

### 1. **Encapsulation of Object Creation**

Instead of scattering `new` calls across your codebase, the creation logic is centralized.

### 2. **Promotes Loose Coupling**

Clients depend on abstractions (interfaces or base classes), not concrete implementations.

### 3. **Extensibility**

New product types can be added by extending the factory, without modifying existing client logic.

### 4. **Supports Runtime Decision-Making**

Factory methods allow object creation based on runtime parameters or configuration.

## Why Not Just Use If/Else or Switch Statements?

While simple conditional logic can work for very small systems, it becomes problematic as the codebase grows.

### **Problems with If/Else Object Creation:**

* **Violates Open/Closed Principle**: Every time a new type is added, you must modify existing conditional blocks.
* **Hard to Maintain**: Conditionals grow into long, error-prone structures as requirements expand.
* **Tight Coupling**: The client code becomes dependent on concrete classes, making testing and changes harder.
* **No Encapsulation**: Creation logic is duplicated or scattered, making debugging difficult.
* **Difficult to Scale**: Adding logging, validation, caching, or additional steps during creation becomes messy.

### Example Problem (Without Factory)

```python
shape_type = "circle"

if shape_type == "circle":
    shape = Circle()
elif shape_type == "square":
    shape = Square()
# More types require more elif blocks...
```

Issues:

* Adding `Triangle` means modifying this block.
* Logic is inside client code.
* Hard to extend or test.

## Where the Factory Method Helps

Using a factory method moves object creation to a dedicated class or method:

* New types? Just create a new subclass and override the factory method.
* Client code stays unchanged.
* Logical creation steps (logging, preprocessing, parameter validation) stay in one place.

## When to Use the Factory Method

Use it when:

* You anticipate future growth in object types.
* The system should be loosely coupled to specific implementations.
* You need different implementations based on configuration or runtime input.
* Object initialization is complex and should be centralized.

## Summary

The Factory Method Pattern helps write cleaner, more modular, and extensible code. It shifts the object creation responsibility from client code to dedicated factory classes or methods. This avoids rigid if/else structures, improves maintainability, and supports scalable system design.

If you'd like, I can add diagrams, examples in multiple languages (Python, Go, C++, Java), or a comparison with Abstract Factory.
