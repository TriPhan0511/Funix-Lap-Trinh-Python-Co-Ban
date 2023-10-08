# class Cat:
#     def __init__(self, name):
#         self.name = name


# rose = Cat('Rose')
# print(rose.name)

# --------------------------------------------------------------

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f'Vector x={self.x} y={self.y}'


# a = Vector(1, 5)
# b = Vector(10, 3)
# print(a + b)

# --------------------------------------------------------------

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont

#     def __truediv__(self, other):
#         line = "=" * len(other.cont)
#         return "\n".join([self.cont, line, other.cont])


# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(spam / hello)

# --------------------------------------------------------------

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont

#     def __gt__(self, other):
#         for index in range(len(other.cont)+1):
#             result = other.cont[:index] + ">" + self.cont
#             result += ">" + other.cont[index:]
#             print(result)


# spam = SpecialString("spam")
# eggs = SpecialString("eggs")
# spam > eggs

# --------------------------------------------------------------

# import random


# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont

#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1, 1)]

#     def __len__(self):
#         return random.randint(0, len(self.cont)*2)


# vague_list = VagueList(["A", "B", "C", "D", "E"])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])

# --------------------------------------------------------------

class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width*self.height

    # your code goes here

    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()


w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)
