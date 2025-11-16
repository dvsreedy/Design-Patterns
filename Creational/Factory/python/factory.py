from abc import ABC, abstractmethod

class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()

class SquareFactory(ShapeFactory):
    def create_shape(self):
        return Square()

class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

# Example usage:
if __name__ == "__main__":
    factory = CircleFactory()
    shape = factory.create_shape()
    print(shape.draw())  # Output: Drawing a Circle
    factory = SquareFactory()
    shape = factory.create_shape()
    print(shape.draw())  # Output: Drawing a Square
