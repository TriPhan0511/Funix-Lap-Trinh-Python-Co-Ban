'''
Lab 4:  Vòng lặp với Python (từ bài 31 đến 36)
Link: https://codelearn.io/learning/python-co-ban
'''

##
# Task 31
# Write a program that takes an integer n from the user
# and displays the sum of numbers from 1 to n on the screen.

# For example, if n = 5, the program will produce the following result:
# 15
# Because 1 + 2 + 3 + 4 + 5 = 15.
#

# inp = int(input())
# print(sum(list(range(inp + 1))))

# --------------------------------------------------------------------

##
# Task 32
# Write a program that accepts two integers a and b from the user
# and displays the sum of odd numbers between a and b on the screen (b > a).

# For example, if a = 3, b = 9, the output should be:
# 24
# Because 3 + 5 + 7 + 9 = 24.
#

# a = int(input())
# b = int(input())

# total = 0
# for num in range(a, b + 1):
#     if num % 2 == 0:
#         continue
#     total += num
# print(total)

# --------------------------------------------------------------------

##
# Task 33
# Write a program that takes a string s from the keyboard
# and displays characters which are not 'y' in string s on the screen.

# For example, if s = "databasesystem", the output should be:

# Current character: d
# Current character: a
# Current character: t
# Current character: a
# Current character: b
# Current character: a
# Current character: s
# Current character: e
# Current character: s
# Current character: s
# Current character: t
# Current character: e
# Current character: m
#

# s = input()
# for c in s:
#     if c == 'y':
#         continue
#     print("Current character:", c)

# --------------------------------------------------------------------

##
# Task 34
# Write a program that takes an integer a from the keyboard
# and displays products of a and numbers from 1 to 5 on the screen.

# For example, if a = 10, the program will produce the following result:

# 10 * 1 = 10
# 10 * 2 = 20
# 10 * 3 = 30
# 10 * 4 = 40
# 10 * 5 = 50
# If a = 5, the program will produce the following result:

# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
#

# n = int(input())
# b = 1

# while b <= 5:
#     print(f'{n} * {b} = {n * b}')
#     b += 1

# --------------------------------------------------------------------

##
# Task 35
# Write a program that takes two integers a and b from the user
# and displays the following information on the screen:

# Number of even numbers: {P1}
# Number of odd numbers: {P2}
# Where {P1} is the number of even numbers and {P2} is the number of odd numbers in range [a, b].

# For example, if a = 1, b = 10, the program will produce the following result:

# Number of even numbers: 5
# Number of odd numbers: 5
# If a = 14, b = 24, the program will produce the following result:

# Number of even numbers: 6
# Number of odd numbers: 5
#

# #Input
# a = int(input())
# b = int(input())
# count_odd = 0
# count_even = 0

# for num in list(range(a, b+1)):
#     if num % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1

# print("Number of even numbers:", count_even)
# print("Number of odd numbers:", count_odd)

# --------------------------------------------------------------------

##
# Task 35
# Write a program that takes an integer n from the keyboard
# and displays the result of this expression: 1/2 + 2/3 + ... + n/n+1

# Note: Keep only two decimals of the result.

# Example:

# For n = 10, the output should be 7.98
# For n = 20, the output should be 17.35
#

# n = int(input())
# result = 0
# for i in range(1, n+1):
#     result += i / (i+1)
# print((round(result, 2)))

# --------------------------------------------------------------------
