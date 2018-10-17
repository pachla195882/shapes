# coding: utf8
import rectangles
import triangles
import circles

square2 = rectangles.Square(2)

print(square2.summary())

square2.draw()

triangle1 = triangles.Triangle(3, 3, 3)

print(triangle1.summary())

triangle1.draw()

circle1 = circles.Circle(5)

print(circle1.summary())

circle1.draw()
