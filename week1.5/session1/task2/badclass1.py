# A bad class implementation

# What does the runtime error mean?
# the error means that the attributes x and y are not defined for the instance of the Point class. In the __init__ method, we are assigning values to local variables x and y instead of instance variables self.x and self.y.
# How do we fix the code?
# We can fix the code by using self.x and self.y to assign the values of x_coordinate and y_coordinate to the instance variables. This way, the attributes will be properly defined for the instance of the Point class.
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
