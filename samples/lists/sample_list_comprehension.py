# Given a word as input, output a list, containing
# only the letters of the word that are not vowels.

# The vowels are a, e, i, o, u.

# Sample Input:
# awesome

# Sample Output:
# ['w', 's', 'm']

# # word = 'awesome'
# word = input()
# vowels = ['a', 'e', 'i', 'o', 'u']
# out = [c for c in word if c not in vowels]
# print(out)

# ----------------------------------------------------

# Slicing

# lst = [1, 2, 3, 4, 5, 6]
# print(lst[2:5])  # [3, 4, 5]

# tu = (1, 2, 3, 4, 5)
# print(tu[2:5])  # (3, 4, 5)

# s = {1, 2, 3, 4, 5}
# # print(s[2:4])  # TypeError: 'set' object is not subscriptable

# d = {'one': 1, 'two': 2, 'three': 3}
# print(d[:1])  # TypeError: unhashable type: 'slice'
