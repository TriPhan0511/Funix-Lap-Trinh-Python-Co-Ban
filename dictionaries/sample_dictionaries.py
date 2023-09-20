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


def count_words(file_name):
    # Get the current path of this .py file and open the file
    try:
        absolute_path = os.path.dirname(__file__)
        fhand = open(f'{absolute_path}/{file_name}')
    except:
        print(f'File cannot be opend: {file_name}')
        exit()

    # Count words in the file
    counts = dict()
    for line in fhand:
        line = line.strip()
        words = line.split()
        for w in words:
            counts[w] = counts.get(w, 0) + 1
    return counts

    # # Count words in the file and returnt the reusult in a dictionary
    # counts = dict()
    # list_of_list = [line.strip().split() for line in fhand]
    # words = [word for lst in list_of_list for word in lst]
    # for w in words:
    #     counts[w] = counts.get(w, 0) + 1
    # return counts


# file_name = 'romeo.txt'
# # file_name = input('Enter the file name: ')
# print(count_words(file_name))

# It is a bit inconvenient to look through the dictionary to find the most common
# words and their counts, so we need to add some more Python code to get us the
# output that will be more helpful.

def find_common_words(d):
    

file_name = 'romeo.txt'
# file_name = input('Enter the file name: ')
print(count_words(file_name))
