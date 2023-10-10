'''
Lab 7: List với Python (từ bài 37 đến 41)
Link: https://codelearn.io/learning/python-co-ban
'''

##
# Task 37
# Write a program that takes n and a list lst of n elements
# then returns the smallest number in lst on the screen.

# Example:

# For n = 3, lst = [1, 3, 2] the output should be 1
# Because 1 is the smallest element in lst
# For n = 3, lst = [34, 35, 27] the output should be 27.
#

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))

# lst.sort()
# print(lst[0])

# --------------------------------------------------------------------

##
# Task 38
# Write a program that takes n and a list lst of n elements from the user
# then display the sum of all elements in the list on the screen.

# Example:

# For n = 4, lst = [4, 5, 3, 2], the output should be:
# 14​
# Because 4 + 5 + 3 + 2 = 14
#

# n = int(input())
# total = 0
# for i in range(n):
#     total += int(input())
# print(total)

# --------------------------------------------------------------------

##
# Task 39
# Write a program that takes n and a list lst of n elements from the user,
# sorts all elements in ascending order, and prints the sorted list on the screen.

# Example:

# For n = = 5, lst = [4, 2, 1, 6, 4] the output should be [1, 2, 4, 4, 6]
# For n = 5, lst = [4, 1, 5, 10, 7] the output should be [1, 4, 5, 7, 10].
#

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# lst.sort()
# print(lst)

# --------------------------------------------------------------------

##
# Task 40
# Write a Python program that accepts a list lst of n elements,
# print a list containing all the odd elements of list lst on the screen.

# Example:

# For length = 3 and res = [1, 2, 3], the output should be [1,3]
# For length = 7 and res = [2, 4, 6, 1, 9, 5, 8], the output should be [1,9,5]
#

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# lst = list(filter(lambda e: e % 2 != 0, lst))
# print(lst)

# --------------------------------------------------------------------

##
# Task 41
# Write a Python program that takes a list lst of n elements from the keyboard
# and displays a list containing all element(s) divisible by 5 in the list lst. If there is no such element, print [0].

# Example:

# For length = 4 and res = [5,6,7,8], the output should be [5]
# For length = 3 and res = [1,2,3,4], the output should be  [0]
# For lenghts = 5 and res = [15,5,20,3,7], the output should be [15,5,20]
#

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# lst = list(filter(lambda e: e % 5 == 0, lst))


# if len(lst) == 0:
#     print([0])
# else:
#     print(lst)

# --------------------------------------------------------------------
