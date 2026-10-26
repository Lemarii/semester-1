# Another bad class implementation

# What does the runtime error mean?
# The runtime error is AttributeError: 'Point' object has no attribute 'x' so the constructor is using x_coordinate and y_coordinate to create local variables, but it does not store them on the Point instance.
# How do we fix the code?
# Fix the code by using self.x and self.y:
class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
