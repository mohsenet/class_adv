class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


# Polymorphic function that works with any shape
def calculate_total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()  # Polymorphic call
    return total


# Usage
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Triangle(6, 2)
]

print(f"Total area: {calculate_total_area(shapes)}")
