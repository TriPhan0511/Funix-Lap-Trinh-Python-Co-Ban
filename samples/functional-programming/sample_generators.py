# Generators are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
# They can be created using functions and the yield statement.

# Note:
# The yield statement is used to define a generator,
# replacing the return of a function to provide a result to its caller
# without destroying local variables.

# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i -= 1


# for i in countdown():
#     print(i)

# # output:
# # 5
# # 4
# # 3
# # 2
# # 1

# print(type(countdown()))  # <class 'generator'>

# --------------------------------------------------------

# Due to the fact that they yield one item at a time,
# generators don't have the memory restrictions of lists.
# In fact, they can be infinite!


# In short, generators allow you to declare a function that behaves like an iterator,
# i.e. it can be used in a for loop.

# --------------------------------------------------------


# Sample:
# Finding prime numbers is a common coding interview task.
# The given code defines a function isPrime(x), which returns True if x is prime.
# You need to create a generator function primeGenerator(),
# that will take two numbers as arguments, and use the isPrime() function
# to output the prime numbers in the given range (between the two arguments).

# Sample Input
# 10
# 20

# Sample Output
# [11, 13, 17, 19]


def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def primeGenerator(a, b):
    # your code goes here
    for i in range(a, b):
        if (isPrime(i)):
            yield i


f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))
