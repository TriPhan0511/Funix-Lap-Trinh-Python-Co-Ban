'''
Lab 3: Câu lệnh lựa chọn (từ bài 26 đến 30)
Link: https://codelearn.io/learning/python-co-ban
'''

##
# Task 26
# Given an integer age which is the age of a cat.
# Write a program that takes an integer age from the user
# and checks whether the cat is young or old.
# If the cat is less than 5 years old (age < 5), print "Your cat is young".
# If the cat is more than or equal to 5 years old (age >= 5), print "Your cat is old".

# For age = 3, the output should be:
# Your cat is young

# For age = 5, the output should be:
# Your cat is old
#

# age = int(input())
# if age < 5:
#     print('Your cat is young');
# else:
#     print('Your cat is old')

# --------------------------------------------------------------------

##
# Task 27
# Given a natural number temperature which is entered from the keyboard.

# Check the temperature for the below conditions then print the answer on the screen:

# If temperature >= 100, print the text Stay at home and enjoy a good movie on the screen.
# If temperature >= 92, print the text Stay at home on the screen.
# If temperature = 75, print the text Go outside and enjoy the weather on the screen.
# If temperature < 0, print the text It's cool outside on the screen.
# For other conditions, print the text Let's go to school on the screen.
# Example:

# For temperature = 130, the output should be Stay at home and enjoy a good movie.
# For temperature = 93, the output should be Stay at home.
# For temperature = 75, the output should be Go outside and enjoy the weather.
# For temperature = -10, the output should be It's cool outside.
# For temperature = 20, the output should be Let's go to school.
#

# temperature = int(input())

# if temperature >= 100:
#     print('Stay at home and enjoy a good movie')
# elif temperature >= 92:
#     print('Stay at home')
# elif temperature == 75:
#     print('Go outside and enjoy the weather')
# elif temperature < 0:
#     print('It\'s cool outside')
# else:
#     print('Let\'s go to school')

# --------------------------------------------------------------------

##
# Task 28
# Write a program that takes 3 integers x, y, z from the user and checks If x is even or odd.

# If x is an even number, check whether y is greater than or equal to 20.
# If y >= 20, print "y is greater than or equal to 20", print "y is less than 20" otherwise.
# If x is an odd number, check whether z is greater than or equal to 30.
# If z >= 30, print "z is greater than or equal to 30", print "z is less than 30" otherwise.

# Example:

# For x = 20, y = 33, z = 15, the output should be "y is greater than or equal to 20".
# Because x % 2 = 0 and y > 20
# For x = 15, y =23, z = 20, the output should be "z is less than 30".
# Because x % 2 != 0 and z < 30
#

# x = int(input())
# y = int(input())
# z = int(input())

# if x % 2 == 0 and y >= 20:
#     print('y is greater than or equal to 20')
# if x % 2 == 0 and y < 20:
#     print('y is less than 20')
# if x % 2 != 0 and z >= 30:
#     print('z is greater than or equal to 30')
# if x % 2 != 0 and z < 30:
#     print('z is less than 30')

# --------------------------------------------------------------------

##
# Task 29
# Write a program that accepts 3 natural numbers a, b, c from the user
# and calculates the average (avg) of those numbers.
# Check the avarage for the following conditions:

# If avg > a and avg > b, print The average value is greater than both a and b on the screen.
# If avg > a and avg > c, print The average value is greater than both a and c on the screen.
# If avg > b and avg > c, print The average value is greater than both b and c on the screen.
# If avg is greater than a and only a, print The average value is greater than a on the screen.
# If avg is greater than b and only b, print The average value is greater than b on the screen.
# If avg is greater than c and only c, print The average value is greater than c on the screen.
# Example:

# If a = 10, b = 20, c = 20, the output should be The average is greater than a
# Because avg = (10+20+20)/3 = 20 so that the avg is greater than a and only a.
#

# a = int(input())
# b = int(input())
# c = int(input())
# avg = (a + b + c) / 3

# if avg > a and avg > b:
#     print('The average value is greater than both a and b')
# if avg > a and avg > c:
#     print('The average value is greater than both a and c')
# if avg > b and avg > c:
#     print('The average value is greater than both b and c')
# if a < avg <= b and avg <= c:
#     print('The average value is greater than a')
# if b < avg <= a and avg <= c:
#     print('The average value is greater than b')
# if c < avg <= a and avg <= b:
#     print('The average value is greater than c')

# --------------------------------------------------------------------

##
# Task 30
# Given an integer age which is the age of your pet.
# Write a Python program to compare your pet's age to a human's age using the following conditions:

# If age <= 0, print "This can hardly be true" on the screen.
# If age == 1, print "About 1 human year" on the screen.
# If age == 2, print "About 2 human years" on the screen.
# If age > 2, print "Over 5 human years" on the screen.
# Example:

# If age = 3, the output should be "Over 5 human years"
# If age = 1, the output should be "About 1 human year"
#

# age = int(input())

# if age <= 0:
#     print('This can hardly be true')
# elif age == 1:
#     print('About 1 human year')
# elif age == 2:
#     print('About 2 human years')
# else:
#     print('Over 5 human years')


# --------------------------------------------------------------------
