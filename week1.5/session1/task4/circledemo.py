# Week 1.5, Session 1: Task 4

from geometry import Circle, Point

x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))
centre = Point(x, y)

radius = float(input("Enter the radius: "))
circle = Circle(radius, centre)

print(f"Area: {circle.area():.4f}")
print(f"Perimeter: {circle.perimeter():.4f}")
