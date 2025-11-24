# Abstract Factory Design Pattern

## Overview

The **Abstract Factory** is a creational design pattern that provides an interface for creating **families of related or dependent objects** without specifying their concrete classes. It ensures that objects created from the same family are compatible with each other.

This pattern is widely used when a system needs to remain platform-independent or theme-independent.

---

## When to Use

Use the Abstract Factory pattern when:

* Your system must create **multiple related products** (e.g., Button + Checkbox + Menu).
* You need to ensure **consistency** across products from the same family.
* You want to **switch families of objects at runtime**.
* You want to avoid tight coupling between client code and concrete implementations.

---

## Real-World Example

A cross-platform UI framework that supports multiple operating systems:

* **Windows UI** components
* **Mac UI** components
* **Linux UI** components

Each platform has its own versions of:

* Buttons
* Checkboxes
* Dropdowns

Abstract Factory ensures that if the user selects the Mac UI theme, *all components* come from the Mac family.

---

## Structure

```
AbstractFactory
│── create_button()
│── create_checkbox()
│
├── ConcreteFactoryA  →  creates ProductA1, ProductA2
└── ConcreteFactoryB  →  creates ProductB1, ProductB2

AbstractProductA
│── ConcreteProductA1
└── ConcreteProductA2

AbstractProductB
│── ConcreteProductB1
└── ConcreteProductB2
```

---

## Participants

### **1. AbstractFactory**

Declares methods for creating each type of product.

### **2. ConcreteFactory**

Creates concrete variants of products. Each factory corresponds to one product family.

### **3. AbstractProduct**

Declares the interface for each product.

### **4. ConcreteProduct**

Actual implementations of products.

### **5. Client**

Works with AbstractFactory and AbstractProduct interfaces and doesn’t depend on concrete classes.

---

## Benefits

* Ensures **compatibility** across related products.
* Helps maintain **loose coupling**.
* Easy to **switch product families**.
* Adding new product families is easy through new factories.

---

## Drawbacks

* Adding a new **product type** requires updating all factories.
* Increases code complexity due to multiple interfaces and classes.

---

## UML Diagram (Text Representation)

```
Client → AbstractFactory
        ↑           ↑
        │           │
ConcreteFactoryA   ConcreteFactoryB
        │           │
ProductA1, ProductB1   ProductA2, ProductB2
```

---

## Python Example

```python
from abc import ABC, abstractmethod

# --- Abstract Products ---
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def toggle(self):
        pass

# --- Concrete Products (Windows Variant) ---
class WinButton(Button):
    def click(self):
        print("Windows Button Clicked")

class WinCheckbox(Checkbox):
    def toggle(self):
        print("Windows Checkbox Toggled")

# --- Concrete Products (Mac Variant) ---
class MacButton(Button):
    def click(self):
        print("Mac Button Pressed")

class MacCheckbox(Checkbox):
    def toggle(self):
        print("Mac Checkbox Toggled")

# --- Abstract Factory ---
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# --- Concrete Factories ---
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# --- Client Code ---
def render_ui(factory: GUIFactory):
    btn = factory.create_button()
    cb = factory.create_checkbox()

    btn.click()
    cb.toggle()

# Example Usage
factory = MacFactory()
render_ui(factory)
```

---

## Output

```
Mac Button Pressed
Mac Checkbox Toggled
```

---

## Summary

The **Abstract Factory** pattern is ideal for creating **families of related objects** while ensuring compatibility and maintaining loose coupling. It's widely used in UI frameworks, game development, OS-level components, and any system that requires interchangeable object families.
