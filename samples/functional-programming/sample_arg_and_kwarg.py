# ========== *args ==========

# Python allows you to have functions with varying numbers of arguments.
# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.
# The arguments are then accessible as the tuple args in the body of the function.

# Notes:
# The parameter *args must come after the named parameters to a function.
# The name args is just a convention; you can choose to use another.

# def my_func(named_arg, *args):
#     print(named_arg)
#     print(args)


# my_func(1, 2, 3, 4, 5)
# # 1
# # (2, 3, 4, 5)

# ========== **kwargs ==========

# **kwargs (standing for keyword arguments) allows you to handle named arguments
# that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names,
# and the values are the argument values.

def my_func(x, y=7, *args, **kwargs):
    print(f'kwargs: {kwargs}')
    print(f'args: {args}')
    print(f'x={x}')
    print(f'y={y}')


my_func(2, 3, 4, 5, 6, a=7, b=8)
# kwargs: {'a': 7, 'b': 8}
# args: (4, 5, 6)
# x=2
# y=3
