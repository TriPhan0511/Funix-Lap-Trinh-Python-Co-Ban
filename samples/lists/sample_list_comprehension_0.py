# Link:
# https://www.datacamp.com/tutorial/python-list-comprehension

# List comprehension

# lst = [x for x in range(10)]
# print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# lst = [x * 2 for x in range(10)]
# print(lst)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# # numbers = [1, 3, 2, 4, 5]
# # numbers = {1, 3, 2, 4, 5}
# # numbers = (1, 3, 2, 4, 5)
# numbers = {1: 'one', 3: 'three', 2: 'two', 4: 'four', 5: 'five'}
# t2 = [x*x for x in numbers]
# print(t2)  # [1, 9, 4, 16, 25]

# ---------------------------------------------------------------------------------------

# ======= List Comporehension with Conditionals =======

# print([i for i in range(10) if i % 2 == 0])
# # [0, 2, 4, 6, 8]

# ======= Multiple If Conditions =======

# print([i for i in range(20) if i % 2 == 0 if i % 3 == 0])
# # [0, 6, 12, 18]

# ======= If-Else Conditions =======

# print([i * i if i % 2 == 0 else i for i in range(10)])
# # [0, 1, 4, 3, 16, 5, 36, 7, 64, 9]

# ======= Nested List Comprehensions =======

# # Flatten 'list_of_list'
# list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8]]
# print([i for lst in list_of_list for i in lst])
# # [1, 2, 3, 4, 5, 6, 7, 8]

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([[row[i] for row in matrix] for i in range(3)])
# # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Rewrite the code chunk above to a nested for loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
out = []
for i in range(3):
    temp = []
    for row in matrix:
        temp.append(row[i])
    out.append(temp)
print(out)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# ---------------------------------------------------------------------------------------

# List comprehension as an alternative to: loop, map, filter, reduce

# # loop
# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i * i)
# print(lst) # [0, 4, 16, 36, 64]

# # List comprehension
# numbers = [i * i for i in range(10) if i % 2 == 0]
# print(numbers)  # [0, 4, 16, 36, 64]

# # map function
# numbers = map(lambda x: x * x, range(10))
# print(list(numbers))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# numbers = map(lambda x: x * x if x % 2 == 0 else x, range(10))
# print(list(numbers))  # [0, 1, 4, 3, 16, 5, 36, 7, 64, 9]

# # List comprehension
# numbers = [i * i for i in range(10)]
# print(numbers)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# # List comprehension
# print([i*i if i % 2 == 0 else i for i in range(10)]) # [0, 1, 4, 3, 16, 5, 36, 7, 64, 9]


# # filter function
# numbers = filter(lambda x: x % 2 == 0, range(10))
# print(list(numbers))  # [0, 2, 4, 6, 8]

# # reduce function
# from functools import reduce
# total = reduce(lambda accumulator, current: accumulator + current, range(10))
# print(total)  # 45

# print([x for x in range(20) if x % 2 == 0 if x % 3 == 0])
