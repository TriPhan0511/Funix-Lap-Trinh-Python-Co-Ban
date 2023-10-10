'''
Lab 6: String với Python (từ bài 42 đến 45)
Link: https://codelearn.io/learning/python-co-ban
'''

##
# Task 42
# Write a program that accepts a string s from the user
# and converts all lowercase characters in s into uppercase characters
# then prints the converted string on the screen.

# Example:

# For s = "Codelearn", the output should be CODELEARN
# For s = "abc123", the output should be ABC123
#

# s = input()
# s = s.upper()
# print(s)

# --------------------------------------------------------------------

##
# Task 43
# Write a Python program that accepts a string s from the user
# and creates a string containing the first 2 characters and the last 2 characters of string s
# then displays this string on the screen. If the length of string s is less than 2, print an empty string.

# Example:

# For s = "Codelearn.io", the output should be "Coio"
# For s = "uno", the output should be "unno"
# For s = "a", the output should be "" (empty string)
#

# s = input()
# if len(s) < 2:
#     print('')
# else:
#     print(f'{s[:2]}{s[-2:]}')

# --------------------------------------------------------------------

##
# Task 44
# Write a Python program that accepts 2 trings s1 and s2 from the user
# and swaps the first two characters of 2 given strings then print a new string s1 + " " + s2 on the screen.

# Example:

# For s1 = "sun", s2 = "moon", the output should be "mon suon"
# For s1 = "apple", s2 = "banana", the output should be "baple apnana"
#

# s1 = input()
# s2 = input()

# first_two_1 = s1[:2]
# first_two_2 = s2[:2]

# s1 = first_two_2 + s1[2:]
# s2 = first_two_1 + s2[2:]

# print(f'{s1} {s2}')

# --------------------------------------------------------------------

##
# Task 45
# Given the string s entered from the keyboard,
# write a program to reverse the order of the words appearing in the string s
# and then display the result to the screen.

# Example:

# For s = "Python Exercises", the output should be "Exercises Python"
# For s = "This is an apple", the output should be "apple an is This"
#

# s = input()
# words = s.split(' ')
# words.reverse()
# result = ' '.join(words)
# print(result)

# --------------------------------------------------------------------
