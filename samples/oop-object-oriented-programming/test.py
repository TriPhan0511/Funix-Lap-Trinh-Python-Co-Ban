# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def intro(self):
#         print(f'My name\'s {self.name}')

#     def __str__(self):
#         return f'My name is {self.name}'


# j = Animal('Jim')
# # j.intro()
# print(j)

# ----------------------------------------------------------------

# ======== __add__ method ========

# class One:
#     def __init__(self, a):
#         self.a = a

#     def __add__(self, object2):
#         return self.a + object2.a


# class Two:
#     def __init__(self, a):
#         self.a = a

#     def __add__(self, object2):
#         return self.a + object2.a


# a_instance = One(10)
# b_instance = Two(20)
# print(a_instance + b_instance)

# ----------------------------------------------------------------

# ======== Class Variables and Instance Variables ========


class Point:
    printed_rep = '*'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_printed_rep(self):
        return self.printed_rep


p = Point(5, 10)
print(p.get_printed_rep())
