# A classic example of a function that is implemented recursively is the factorial function,
# which finds the product of all positive integers below a specified number.

# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120).
# To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on.
# Generally, n! = n * (n-1)!.
# Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials.

# The base case acts as the exit condition of the recursion.
# Not adding a base case results in infinite function calls, crashing the program.

# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)


# print(factorial(5))  # 120

# --------------------------------------------------------

# Recursion can also be indirect.
# One function can call a second, which calls the first, which calls the second, and so on.
# This can occur with any number of functions.

# def is_even(num):
#     if num == 0:
#         return True
#     return is_odd(num-1)


# def is_odd(num):
#     return not is_even(num)


# print(is_odd(17))  # True
# print(is_odd(12))  # False
# print(is_even(23))  # False
# print(is_even(20))  # True

# --------------------------------------------------------

# Sample:
# Convert a number from decimal to binary

# Sample Input
# 8

# Sample Output
# 1000

# def convert(num):
#     if num == 0:
#         return 0
#     return (num % 2 + 10 * convert(num // 2))


# # print(convert(int(input())))

# print(convert(8))

# --------------------------------------------------------

# Sample:

def fib(num):
    if num == 0 or num == 1:
        return 1
    return fib(num-2) + fib(num-1)


print(fib(4))  # 5
