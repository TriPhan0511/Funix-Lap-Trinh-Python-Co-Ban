'''
Lab 5:  Hàm trong Python (từ bài 46 đến 50)
Link: https://codelearn.io/learning/python-co-ban
'''

##
# Task 46
# Write a function that accepts a list lst from the user and returns the sum of elements in lst.

# Example

# For n = 3, lst = [2, 1, 6] the output should be 9.
# For n = 4, lst = [1, 1, 2, 3] the output should be 7.
#

# def sum_of_list(t):
#     total = 0
#     for num in t:
#         total += num
#     return sum(t)

# lst = []
# n = int(input())
# for i in range(n):
#     lst.append(int(input()))
# print(sum_of_list(lst))

# --------------------------------------------------------------------

##
# Task 47
# Write a Python function that accepts 3 integers a,b and c from the user
# and print the largest among the three on the screen.

# Example:

# For a = 3, b = 6, c = 5, the output should be 6
# For a = 2, b = 1, c = 3, the output should be 3
#

# def max3(a, b, c):
#     if a > b and a > c:
#         return a
#     if b > a and b > c:
#         return b
#     return c

# a = int(input())
# b = int(input())
# c = int(input())
# print(max3(a, b, c))

# --------------------------------------------------------------------

##
# Task 48
# Write a Python program that accepts a string s from the user
# and counts the number of uppercase letters and lowercase letters
# then prints the following information on the screen:

# Given string: {P1}
# Number of uppercase letters: {P2}
# Number of lowercase letters: {P3}
# Where:

# {P1} is the given string.

# {P2} is the number of uppercase characters in the string.

# {P3} is the number of lowercase characters in the string.

# Example:

# For s = "You Are Apple In My Eye", the output should be as below:
# Given string: You Are Apple In My Eye
# Number of uppercase letters: 6
# Number of lowercase letters: 12​
#

# def show(st):
#     upper_count = 0
#     lower_count = 0
#     for letter in st:
#         if letter == ' ':
#             continue
#         if letter == letter.upper():
#             upper_count += 1
#         else:
#             lower_count += 1
#     print(f'Given string: {st}')
#     print(f'Number of uppercase letters: {upper_count}')
#     print(f'Number of lowercase letters: {lower_count}')


# s = str(input())
# show(s)

# --------------------------------------------------------------------

##
# Task 49
# Write a function that takes a list as an argument
# and returns a list containing unique values that appear in the list.

# Example:

# For lst = [1,2,3,3,3,3,4,5], the output should be [1,2,3,4,5]
# For lst = [1,1,2,2,3,3,3,3,4,4,4,4,5,5], the output should be [1,2,3,4,5]
# For lst = [1, 1, 1], the output should be [1]
#

# def get_unique_values(lst):
#     result = []
#     for item in lst:
#         if item in result:
#             continue
#         result.append(item)
#     return result


# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# print(get_unique_values(lst))

# --------------------------------------------------------------------

##
# Task 50
# Write a Python program that accepts a natural number n from the user
# and checks whether that number is a prime number.
# If n is a prime number, return True, return False otherwise.

# A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. 2, 3, 5, 7, 11, 13, 17,... are prime numbers.

# Example

# For n = 9, the output should be False
# For n = 3, the output should be True
#

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# n = int(input())
# print(is_prime(n))

# --------------------------------------------------------------------
