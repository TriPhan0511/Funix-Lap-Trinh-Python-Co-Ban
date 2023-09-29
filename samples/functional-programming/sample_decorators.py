# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions that you don't want to modify.

# def decor(func):
#     def wrap():
#         print('================')
#         func()
#         print('================')

#     return wrap


# def print_text():
#     print('Hello world!')


# decorated = decor(print_text)
# decorated()
# # ================
# # Hello world!
# # ================

# --------------------------------------------------------

# Python provides support to wrap a function in a decorator
# by pre-pending the function definition with a decorator name and the @ symbol.
# If we are defining a function we can "decorate" it with the @ symbol like:

# def decor(func):
#     def wrap():
#         print('================')
#         func()
#         print('================')
#     return wrap


# @decor
# def print_text():
#     print('Hello world!')


# print_text()
# # ================
# # Hello world!
# # ================

# Note:
# A single function can have multiple decorators.

# def decor(func):
#     def wrap():
#         print('================')
#         func()
#         print('================')
#     return wrap


# def decor2(f):
#     def decorate_with_asterisk():
#         print('*******************')
#         f()
#         print('*******************')
#     return decorate_with_asterisk


# @decor2
# @decor
# def welcome():
#     print('Welcome to our program!')


# welcome()
# # *******************
# # ================
# # Welcome to our program!
# # ================
# # *******************

# --------------------------------------------------------

# Sample:
# You are working on an invoicing system.
# The system has an already defined invoice() function,
# which takes the invoice number as argument and outputs it.
# You need to add a decorator for the invoice() function,
# that will print the invoice in the following format:

# Sample Input
# 42

# Sample Output
# ***
# INVOICE #42
# ***
# END OF PAGE

def decor(f):
    def wrap(*arg, **kwargs):
        print('***')
        f(*arg, **kwargs)
        print('***')
        print('END OF PAGE')
    return wrap


@decor
def invoice(num):
    print("INVOICE #" + num)


invoice(input())
