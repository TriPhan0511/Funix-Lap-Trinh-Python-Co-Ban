'''
Lab 9: Tuple với Python (Bài luyện tập I) (từ bài 51 đến 54)
Link: https://codelearn.io/learning/python-co-ban
'''

# #
# Task 51:
# Given a list res of integers.
# Write a Python program to find the even numbers in the list
# and print the list of even numbers on the screen.

# Example:
# For res = [1,2,3,4,5,6,7,8,9], the output should be [2,4,6,8]
# For res = [10, 22, 33, 45, 79, 81], the output should be [10,22]
# Input: a list of integers entered from the keyboard
# Output: The list of even numbers displays on the screen
# Execution time limit: 1s

# Suggestion
# Write a function to check if the numbers in the list are divisible by 2
# and use the for loop to check all the elements
#

# #Initial list
# res = []

# # Input lengths
# lengths = int(input())

# # Add element
# for i in range(lengths):
#     # Input elements
#     n = int(input())
#     res.append(n)

# def evenNum(res):
#     return [i for i in res if i % 2 == 0]


# res = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # [2, 4, 6, 8]
# # res = [10, 22, 33, 45, 79, 81] # [10, 22]
# print(evenNum(res))

# -----------------------------------------------------------------------------

##
# Task 52
# Given two integers a and b entered from the keyboard.
# Write a Python program to calculate the value of a to the power b (a^b)
# and print the result on the screen.

# Example:
# For a = 3, b = 4, the output should be 81
# Because 3^4 = 81

# For a = 5, b = 2, the output should be 25
# Because 5^2 = 25

# Input: a, b are integers entered from the keyboard
# Output: The result displays on the screen as required

# Execution time limit: 1s

# Suggestion
# Write a function to take the values of a and b and use recursive method to calculate the value of a^b.

# def power(a, b):
#     return a**b

# # a = int(input())
# # b = int(input())
# a = 7
# b = 2

# print(power(a, b))

# -----------------------------------------------------------------------------

##
# Task 53
# Given 2 integers a and b entered from the keyboard.
# Write a Python program to find the greatest common divisor (gcd) of a, b
# and print the result on the screen.

# Example:
# For a = 12, b = 14, the output should be 2
# For a = 16, b = 22, the output should be 2

# Input: a, b are integers entered from the keyboard
# Output: the gcd of 2 integers displays on the screen

# Execution time limit: 1s

# Suggestion
# Write a function to take the values of a and b and use the recursive method to find the gcd of a, b

# def gcd(a, b):
#     divisors1 = set([i for i in range(1, a + 1) if a % i == 0])
#     divisors2 = set([i for i in range(1, b + 1) if b % i == 0])
#     return max(divisors1 & divisors2)


# a = int(input())
# b = int(input())
# # a = 12
# # b = 14
# # a = 14
# # b = 22

# print(gcd(a, b))

# -----------------------------------------------------------------------------

##
# Task 54
# Given 3 integers a, b and c that are 3 sides of a triangle.
# Write a Python program to check whether that triangle is equilateral (đều), isosceles (cân), or scalene (lệch, không đều)
# and print "Equilateral triangle", "Isosceles triangle" or "Scalene triangle" respectively
# on the screen.

# Example:
# For a = 20, b = 20, c = 20, the output should be "Equilateral triangle"
# For a = 33, b = 20, c = 15, the output should be "Scalene triangle"

# Input: 3 integers entered from the keyboard
# Output: the result displays on the screen as required

# Execution time limit: 1s

# Suggestion
# Use if else statement to complete this task.

# Note:

# An equilateral triangle is a triangle in which all three sides are equal.
# An isosceles triangle is a triangle with (at least) two equal sides.
# A scalene triangle is a triangle that has three unequal sides.

# a = int(input())
# b = int(input())
# c = int(input())

# a = 20
# b = 20
# c = 20

# a = 15
# b = 15
# c = 20

# a = 20
# b = 15
# c = 20

# a = 20
# b = 15
# c = 15


a = 33
b = 20
c = 15

triangle = ('Equilateral triangle', 'Isosceles triangle', 'Scalene triangle')

if (a == b) and (a == c):
    print(triangle[0])
elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print(triangle[1])
else:
    print(triangle[2])
