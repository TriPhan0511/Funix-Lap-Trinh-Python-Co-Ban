# ======= map function =======

# def add_five(x):
#     return x + 5


# nums = [11, 22, 33, 44, 55]
# # result = list(map(add_five, nums))
# result = list(map(lambda x: x+5, nums))
# print(result)  # [16, 27, 38, 49, 60]

# ======= filter function =======

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)  # [22, 44]
