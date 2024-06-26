

import math

class Circle:
    def __init__(self, radius):
        """Initialize the circle with a given radius."""
        self.radius = radius

    def area(self):
        """Compute the area of the circle."""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """Compute the circumference of the circle."""
        return 2 * math.pi * self.radius

circle = Circle(5)
print(f"Area: {circle.area()}")            
print(f"Circumference: {circle.circumference()}") 