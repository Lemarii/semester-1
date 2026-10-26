# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
# The Point class should have a constructor that creates fields to represent the x & y coordinates of a point, and methods distance() and distance_to() that return the distance of the point from the origin and from another point, respectively.

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point with x and y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self):
        """
        Returns the distance from the Point to the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, other_point):
        """
        Returns the distance from this Point to another Point.
        """
        return math.hypot(self.x - other_point.x, self.y - other_point.y)


# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
# The centre should be represented as a Point object, and the radius should be a float. The constructor should allow the centre to be omitted, in which case it should default to the origin. 
# The constructor should allow the centre to be omitted, in which case it should default to the origin.
# Method area() should return the area of the circle, calculated using the formula π * radius^2.
# Method perimeter() should return the perimeter of the circle, calculated using the formula 2 * π * radius.

class Circle:
    """
    A circle with a radius and centre coordinates.
    """

    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """
        Creates a Circle with a radius and an optional centre Point.
        """
        self.radius = radius
        self.centre = centre

    def area(self):
        """
        Returns the area of the Circle.
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        Returns the perimeter of the Circle.
        """
        return 2.0 * math.pi * self.radius


# Don't add any testing code to this file!
