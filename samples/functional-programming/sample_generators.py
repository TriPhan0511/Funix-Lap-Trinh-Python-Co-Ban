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

# Sample: Create a prime number generator

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# def get_primes():
#     num = 2
#     while True:
#         if is_prime(num):
#             yield num
#         num += 1

# # for i in get_primes():
# #     print(i)

# --------------------------------------------------------

# # Sample: Create a first 100 prime numbers generator
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# # def get_primes(limit):
# #     num = 2
# #     while True and num <= limit:
# #         if is_prime(num):
# #             yield num
# #         num += 1

# def get_primes(limit):
#     for i in range(2, limit + 1):
#         if is_prime(i):
#             yield i


# for i in get_primes(100):
#     print(i)

# --------------------------------------------------------

# Finite generators can be converted into lists
# by passing them as arguments to the list function.

# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i


# print(list(numbers(11)))
# # [0, 2, 4, 6, 8, 10]
