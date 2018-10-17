from shape import Shape
import numpy as np
import matplotlib.pyplot as plt

class Triangle(Shape):

    a = None
    b = None
    c = None

    def __init__(self,a,b,c):
        super().__init__()
        if a > b + c:
            raise ValueError("Triangle condition is not satisfied! A is greater than the sum of B and C")
        elif b > a + c:
            raise ValueError("Triangle condition is not satisfied! B is greater than the sum of A and C")
        elif c > a + b:
            raise ValueError("Triangle condition is not satisfied! C is greater than the sum of A and B")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a+self.b+self.c

    def calc_angles(self):
        alpha = np.arccos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2. * self.b * self.c))
        beta = np.arccos((-self.b ** 2 + self.c ** 2 + self.a ** 2) / (2. * self.a * self.c))
        gamma = np.pi - alpha - beta
        return alpha, beta, gamma

    def calc_point(self, alpha, beta, c):
        x = (c * np.tan(beta)) / (np.tan(alpha) + np.tan(beta))
        y = x * np.tan(alpha)
        return x, y

    def get_triangle(self):
        z = np.array([self.a, self.b, self.c])
        while z[-1] != z.max():
            z = z[[2, 0, 1]]  # make sure last entry is largest
        alpha, beta, _ = self.calc_angles()
        x, y = self.calc_point(alpha, beta, z[-1])
        return [(0, 0), (z[-1], 0), (x, y)]

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5  # Heron's formula

    def draw(self):
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        triangle = plt.Polygon(self.get_triangle())
        ax.add_patch(triangle)
        ax.relim()
        ax.autoscale_view()
        plt.show()