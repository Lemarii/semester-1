# Week 1.5, Session 1: Task 3

import math


class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        """
        Creates a Point with x and y coordinates.
        """
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        """
        Returns the distance from the Point to the origin.
        """
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other_point):
        """
        Returns the distance from this Point to another Point.
        """
        return math.hypot(self.x - other_point.x, self.y - other_point.y)


# Finally, add code here to demonstrate use of Point
first_point = Point(3, 4)
second_point = Point(6, 8)

print("First point x:", first_point.x)
print("First point y:", first_point.y)
print("Distance from origin:", first_point.distance())
print("Distance between points:", first_point.distance_to(second_point))
