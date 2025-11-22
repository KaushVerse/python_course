class Shape:
    """Base class for polymorphism."""
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def __repr__(self):
        return f"{self.__class__.__name__}"


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Method overloading (via default args)
class Calculator:
    def add(self, a, b, c=0):
        """Add 2 or 3 numbers."""
        return a + b + c


# Operator overloading
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    # Polymorphism: same method, different behavior
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
    
    for shape in shapes:
        print(f"{shape} area: {shape.area():.2f}")

    # Method overloading
    calc = Calculator()
    print(f"\nCalculator.add(2, 3) = {calc.add(2, 3)}")
    print(f"Calculator.add(2, 3, 4) = {calc.add(2, 3, 4)}")

    # Operator overloading
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(f"\n{v1} + {v2} = {v3}")