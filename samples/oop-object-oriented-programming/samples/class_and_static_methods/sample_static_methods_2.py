
# The given code takes 2 numbers as input and calls the static area() method of the Shape class,
# to output the area of the shape, which is equal to the height multiplied by the width.

# To make the code work, you need to define the Shape class,
# and the static area() method, which should return the multiplication of its two arguments

# Note:
# Use the @staticmethod decorator to define a static method.

class Shape:
    @staticmethod
    def area(width, height):
        return width * height


w = int(input())
h = int(input())

print(Shape.area(w, h))
