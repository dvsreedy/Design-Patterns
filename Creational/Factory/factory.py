from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplementedError("You should implement this method!")

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"


class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "SQUARE":
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Example usage:
if __name__ == "__main__":
    shape1 = ShapeFactory.get_shape("CIRCLE")
    print(shape1.draw())  # Output: Drawing a Circle

    shape2 = ShapeFactory.get_shape("SQUARE")
    print(shape2.draw())  # Output: Drawing a Square