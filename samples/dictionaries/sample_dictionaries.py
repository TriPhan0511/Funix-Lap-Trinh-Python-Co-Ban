import string
import os

# eng2sp = dict()

# # print(eng2sp)  # {}
# # print(type(eng2sp))  # <class 'dict'>

# eng2sp['one'] = 'uno'
# print(eng2sp)  # {'one': 'uno'}

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

# print(eng2sp)  # {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp['two'])  # dos
# # print(eng2sp['four'])  # KeyError: 'four'

# print(len(eng2sp))  # 3

# # The in operator works on dictionaries; it tells you whether something appears as
# # a key in the dictionary (appearing as a value is not good enough).
# print('one' in eng2sp)  # True
# print('uno' in eng2sp)  # False

# To see whether something appears as a value in a dictionary, you can use the
# method values, which returns the values as a type that can be converted to a list,
# and then use the in operator:

# vals = list(eng2sp.values())
# print('uno' in vals)  # True

# ======= Dictionary as a set of counters =======

# s = 'bRontosaurus'
# d = {}
# for letter in s:
#     letter = letter.lower()
#     if letter not in d:
#         d[letter] = 1
#     else:
#         d[letter] += 1

# print(d)

# Dictionaries have a method called get that takes a key and a default value. If the
# key appears in the dictionary, get returns the corresponding value; otherwise it
# returns the default value. For example:

# counts = {'chuck': 1, 'annie': 42, 'jan': 100}
# print(counts.get('jan', 0))  # 100
# print(counts.get('tim', 0))  # 0

# We can use get to write our histogram loop more concisely. Because the get
# method automatically handles the case where a key is not in a dictionary, we can
# reduce five lines down to two and eliminate the if statement.

# s = 'bRontosaurus'
# d = dict()
# for c in s:
#     c = c.lower()
#     d[c] = d.get(c, 0) + 1

# print(d)

# ======= Dictionaries and files =======

# romeo.txt:

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

# We will write a Python program to read through the lines of the file, break each
# line into a list of words, and then loop through each of the words in the line and
# count each word using a dictionary.


# def count_words(file_name):
#     # Get the current path of this .py file and open the file
#     try:
#         absolute_path = os.path.dirname(__file__)
#         fhand = open(f'{absolute_path}/{file_name}')
#     except:
#         print(f'File cannot be opend: {file_name}')
#         exit()

#     # Count words in the file and returnt the reusult in a dictionary
#     # Option 1:
#     counts = dict()
#     for line in fhand:
#         line = line.strip()
#         words = line.split()
#         for w in words:
#             counts[w] = counts.get(w, 0) + 1
#     return counts

#     # # Count words in the file and returnt the reusult in a dictionary
#     # # Option 2:
#     # counts = dict()
#     # list_of_list = [line.strip().split() for line in fhand]
#     # words = [word for lst in list_of_list for word in lst]
#     # for w in words:
#     #     counts[w] = counts.get(w, 0) + 1
#     # return counts

# # Run:
# file_name = 'romeo.txt'
# # file_name = input('Enter the file name: ')
# print(count_words(file_name))

# -------------------------------

# It is a bit inconvenient to look through the dictionary to find the most common
# words and their counts, so we need to add some more Python code to get us the
# output that will be more helpful.


# def find_common_words(d):
#     result = []
#     for k, v in d.items():
#         result.append((v, k))
#     result.sort(reverse=True)
#     return result


# # # Run:
# # file_name = input('Enter the file name: ')
# # file_name = 'romeo222.txt'
# file_name = 'romeo.txt'
# d = count_words(file_name)
# lst = find_common_words(d)
# for count, word in lst:
#     print(f'The word "{word}" appears {count} times.')
# # ->
# # The word "the" appears 3 times.
# # The word "is" appears 3 times.
# # The word "and" appears 3 times.
# # The word "sun" appears 2 times.
# # The word "yonder" appears 1 times.
# # The word "with" appears 1 times.

# ======= Looping and dictionaries =======

# If you use a dictionary as the sequence in a for statement, it traverses the keys of
# the dictionary. This loop prints each key and the corresponding value:

# counts = {'chuck': 1, 'annie': 42, 'jan': 100}

# for key in counts:
#     print(f'{key} {counts[key]}')

# chuck 1
# annie 42
# jan 100


# If you want to print the keys in alphabetical order, you first make a list of the keys
# in the dictionary using the keys method available in dictionary objects, and then
# sort that list and loop through the sorted list, looking up each key and printing
# out key-value pairs in sorted order as follows:

# counts = {'chuck': 1, 'annie': 42, 'jan': 100}

# keys = list(counts.keys())
# keys.sort()
# for key in keys:
#     print(f'{key} {counts[key]}')

# annie 42
# chuck 1
# jan 100

# ======= Advanced text parsing =======

# romeo.txt:

# But, soft! what light through yonder window breaks?
# It is the east, and Juliet is the sun.
# Arise, fair sun, and kill the envious moon,
# Who is already sick and pale with grief,

# We can solve problems such as punctuation, capitalization by using
# the string methods lower, punctuation, and translate.
# The translate is the most subtle of the methods. Here is the documentation for translate:

# line.translate(str.maketrans(fromstr, tostr, deletestr))

# Replace the characters in fromstr with the character in the same position in tostr
# and delete all characters that are in deletestr. The fromstr and tostr can be
# empty strings and the deletestr parameter can be omitted.

# We will not specify the tostr but we will use the deletestr parameter to delete
# all of the punctuation. We will even let Python tell us the list of characters that
# it considers “punctuation”:

# # import string

# print(string.punctuation)
# # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# def count_words(file_name):
#     try:
#         absolute_path = os.path.dirname(__file__)
#         fhand = open(f'{absolute_path}/{file_name}')
#     except:
#         print(f'File cannot be opened: {file_name}')
#         exit()
#     counts = {}
#     for line in fhand:
#         line = line.strip()
#         line = line.lower()
#         line = line.translate(line.maketrans(
#             '', '', string.punctuation))  # Remove punctuations
#         words = line.split()
#         for w in words:
#             counts[w] = counts.get(w, 0) + 1
#     return counts
# ---------------------------------------------------------------------

# Use tuple and dictionary

def count_words(file_name):
    try:
        absolute_path = os.path.dirname(__file__)
        fhand = open(f'{absolute_path}/{file_name}')
    except:
        print(f'File cannot be opened: {file_name}')
        exit()

    counts = {}
    for line in fhand:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans(
            '', '', string.punctuation))  # Remove punctuations
        words = line.split()
        for w in words:
            counts[w] = counts.get(w, 0) + 1

    lst = [(value, key) for key, value in counts.items()]  # List comprehension
    lst.sort(reverse=True)

    return lst


# # file_name = 'romeo-full222.txt'
# file_name = 'romeo-full.txt'
# lst = count_words(file_name)
# print('\nTen most common words:\n')
# for k, v in lst[:10]:
#     print(f'{k} {v}')

file_name = 'romeo-full.txt'
absolute_path = os.path.dirname(__file__)
fhand = open(f'{absolute_path}/{file_name}')
