'''
Lab 2.2: Toán tử cơ bản (từ bài 19 đến 25)
Link: https://codelearn.io/learning/python-co-ban
'''

##
# Task 19
# Write a Python program that takes the height h and base a of a triangle (where h and a are integers)
# from the user and calculates its area.
# Print the text "The area of triangle is {P}" (P is the area of the given triangle) on the screen.

# If a = 10, h = 12, the screen will display as below:
# The area of triangle is 60
#

# h = int(input())
# a = int(input())

# area = a * h * 0.5

# print(f'The area of triangle is {area}')

# --------------------------------------------------------------------

##
# Task 20
# Write a program that takes two integers a and b from the user
# then prints the result of ab on the screen.

# For example, if a = 2, b = 3, the program will produce the following result:
# 8
#

# a = int(input())
# b = int(input())
# print(a**b)

# --------------------------------------------------------------------

##
# Task 21
# Write a program that takes two integers x and y from the user
# and checks if x is greater than y.
# If x is greater than y, print "x > y: True" on the screen,
# if x is less than y, print "x > y: False" on the screen.

# For example, if x = 10, y = 5, the output should be:
# x > y: True

# If x = 2, y = 8, the output should be:
# x > y: False
#

# x = int(input())
# y = int(input())

# if x > y:
#     print('x > y: True')
# else:
#     print('x > y: False')

# --------------------------------------------------------------------

##
# Task 22
# Write a program that takes two natural numbers a and Total from the user.
# Use assignment operators to assign the value of the first variable to the second variable
# then print the assigned values of Total in seperate lines as below:

# The Value of the Total after using += Operator is: {A}
# The Value of the Total after using -= Operator is: {B}
# The Value of the Total after using *= Operator is: {C}
# The Value of the Total after using //= Operator is: {D}
# The Value of the Total after using **= Operator is: {E}
# The Value of the Total after using /= Operator is: {F}
# The Value of the Total after using %= Operator is: {G}

# Where A, B, C, D, E, F, G are the values of Total
# after using the operators +=, -=, *=, //=, **=, /=, %= respectively

# For example, if a = 7, Total = 21, the program will produce the following result:

# The Value of the Total after using += Operator is: 28
# The Value of the Total after using -= Operator is: 21
# The Value of the Total after using *= Operator is: 147
# The Value of the Total after using //= Operator is: 21
# The Value of the Total after using **= Operator is: 1801088541
# The Value of the Total after using /= Operator is: 257298363.0
# The Value of the Total after using %= Operator is: 0.0
#

# a = int(input())
# Total = int(input())

# Total += a  # Using += Operator
# print('The Value of the Total after using += Operator is:', Total)
# Total -= a  # Using -= Operator
# print('The Value of the Total after using -= Operator is:', Total)
# Total *= a  # Using *= Operator
# print('The Value of the Total after using *= Operator is:', Total)
# Total //= a  # Using //= Operator
# print('The Value of the Total after using //= Operator is:', Total)
# Total **= a  # Using **= Operator
# print('The Value of the Total after using **= Operator is:', Total)
# Total /= a  # Using /= Operator
# print('The Value of the Total after using /= Operator is:', Total)
# Total %= a  # Using %= Operator
# print('The Value of the Total after using %= Operator is:', Total)

# --------------------------------------------------------------------

##
# Task 23
# Write a program that takes a string x from the user
# and checks if the string x contains character 'H' or not.
# Return True if string x contains 'H' and print False otherwise.

# For example, if x = "PYTHON", the output should be:
# True

# If x = "Codelearn", the output should be:
# False
#

# x = input()
# print('H' in x)

# --------------------------------------------------------------------

##
# Task 24
# Write a program that takes two integers a and b from the user
# and check if a and b have the same value or not.
# Return True if they share the same value, return False otherwise.

# If a = 10, b = 10, the output should be:
# True

# If a = 5, b = 7, the output should be:
# False
#

# a = int(input())
# b = int(input())

# print(a == b)

# --------------------------------------------------------------------

##
# Task 25
# Write a Python program that takes 4 integers x, y, z, and t from the user
# and checks if these 4 numbers satisfy the conditions: x > y and z < t.

# Print "Result evaluation is True" if the integers satisfy the conditions, print "Result evaluation is False" otherwise.

# For x = 5, y = 6, z = 8, t = 3, the output should be:
# Result evaluation is False

# For x = 10, y = 3, z = 7, t = 13, the output should be:
# Result evaluation is True
#

# x = int(input())
# y = int(input())
# z = int(input())
# t = int(input())

# print("Result evaluation is", (x > y) and (z < t))
