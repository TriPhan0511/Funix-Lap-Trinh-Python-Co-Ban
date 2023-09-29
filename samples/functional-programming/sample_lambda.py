# def my_func(f, arg):
#     return f(arg)


# print(my_func(lambda x: 2*x*x, 5))  # 50

# --------------------------------------------------------

# # named function
# def polynomial(x):
#     return x**2 + 5*x + 4


# print(polynomial(-4))  # 0
# # lambda function
# print((lambda x: x**2 + 5*x + 4)(-4))  # 0

# --------------------------------------------------------

# Input:
# 50
# 10
# Output:
5.0

price = int(input())
perc = int(input())

res = (lambda x,y: x*y/100)(price, perc)

print(res)
