def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


# output: 20
print(apply_twice(add_five, 10))

# 15
# 20
