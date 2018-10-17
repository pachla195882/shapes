# coding: utf8
from shape import Shape
import matplotlib.pyplot as plt

class Rectangle(Shape):
    """
    Rectangular shape.
    """

    a = None
    b = None

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def draw(self):
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        rectangle = plt.Rectangle((0, 0), self.a, self.b)
        ax.add_patch(rectangle)
        ax.relim()
        ax.autoscale_view()
        plt.show()


class Square(Rectangle):
    """
    Square shape as a specific rectangle.
    """

    def __init__(self, a):
        super().__init__(a, a)