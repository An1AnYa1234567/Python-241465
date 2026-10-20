# Write a program to demonstrate Abstract Shape Math Engine with Operator Overloading.
from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Geometry(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Vector Class
class Vector(Geometry):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Circle Class
class Circle(Geometry):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"


# Create objects
v1 = Vector(3, 4)
v2 = Vector(2, 1)

# Vector addition
print("Vector 1:", v1)
print("Vector 2:", v2)
print("Vector Addition:", v1 + v2)

# Vector comparison
print("Vectors Equal:", v1 == v2)
print("Vector 2 is smaller than Vector 1:", v2 < v1)

# Circle calculations
c1 = Circle(5)
print("\nCircle:", c1)
print("Circle Area:", round(c1.area(), 2))