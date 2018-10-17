from shape import Shape
import matplotlib.pyplot as plt
import math


class Circle(Shape):

    r = None

    def __init__(self, r):
        super().__init__()
        self.r = r

    def perimeter(self):
        return math.pi*2*self.r

    def area(self):
        return math.pi*self.r**2

    def draw(self):
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        circle = plt.Circle((0, 0), self.r)
        ax.add_patch(circle)
        ax.relim()
        ax.autoscale_view()
        plt.show()