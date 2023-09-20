# ======= Tuples are immutable =======

# t = 'a',
# print(type(t))  # <class 'tuple'>

# t = ('a',)
# print(type(t))  # <class 'tuple'>

# t = tuple()
# print(type(t))  # <class 'tuple'>
# print(len(t))  # 0

# t = tuple([1, 2, 3])
# print(t)  # (1, 2, 3)
# print(type(t))  # <class 'tuple'>

# t = tuple('lupins')
# print(t)  # ('l', 'u', 'p', 'i', 'n', 's')
# print(type(t))  # <class 'tuple'>


# t = 'a', 'b', 'c'
# print(type(t))  # <class 'tuple'>

# t = ('a', 'd', 'c')

# print(type(t))  # <class 'tuple'>
# print(t[0])  # a
# print(t[-1])  # c
# # print(t[10])  # IndexError: tuple index out of range

# t[0] = 100  # TypeError: 'tuple' object does not support item assignment

# sorted_list = sorted(t)
# print(sorted_list)  # ['a', 'c', 'd']
# print(type(sorted_list))  # <class 'list'>

# print(t[:1])  # ('a',)
# print(type(t[:1]))  # <class 'tuple'>

# t = ('a', 'b', 'c', 'd', 'e')

# print(t[0])  # a
# print(t[1:3])  # ('b', 'c')

# t[0] = 'A'  # TypeError: 'tuple' object does not support item assignment

# t = ('A',) + t[1:]
# print(t)  # ('A', 'b', 'c', 'd', 'e'

# ======= Comparing tuples =======

# The comparison operators work with tuples and other sequences. Python starts by
# comparing the first element from each sequence. If they are equal, it goes on to the
# next element, and so on, until it finds elements that differ. Subsequent elements
# are not considered (even if they are really big).

# print((0, 1, 2) < (0, 3, 4))  # True
# print((0, 1, 200000000) < (0, 3, 4))  # True

# DSU:
# Decorate a sequence by building a list of tuples with one or more sort keys
# preceding the elements from the sequence,
# Sort the list of tuples using the Python built-in sort, and
# Undecorate by extracting the sorted elements of the sequence.

# Example:
# Suppose you have a list of words and you want to sort them from
# longest to shortest:

# txt = 'but soft what light in yonder window breaks'

# words = txt.split(' ')
# lst = [(len(w), w) for w in words]
# lst.sort(reverse=True)
# result = [w for (l, w) in lst]

# print(result)
# # ['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']
# print(' '.join(result))
# # yonder window breaks light what soft but in

# ======= Tuple assignment =======

# # a, b = (1, 20)
# a, b = [1, 3]
# a, b = {1, 4}
# print(a)
# print(b)


# m = ['have', 'fun']
# a, b = m
# print(a)  # have
# print(b)  # fun

# m = ['have', 'fun']
# (a, b) = m
# print(a)  # have
# print(b)  # fun


# # Swap the values of two variables in a single statement:
# a = 1
# b = 2
# (a, b) = (b, a)
# print(a)  # 2
# print(b)  # 1

# The number of variables on the left and the number of values on the right must be
# the same:
# (a, b, c) = (1, 2)  # ValueError: not enough values to unpack (expected 3, got 2)
# (a, b) = (1, 2, 3)  # ValueError: too many values to unpack (expected 2)

# More generally, the right side can be any kind of sequence (string, list, or tuple).
# For example, to split an email address into a user name and a domain, you could
# write:

# addr = 'monty@python.org'
# uname, domain = addr.split('@')
# print(uname)  # monty
# print(domain)  # python.org

# ======= Dictionaries and tuples =======

# Dictionaries have a method called items that returns a list of tuples, where each
# tuple is a key-value pair:

# d = {'a': 10, 'b': 1, 'c': 22}
# t = list(d.items())
# print(t)  # [('a', 10), ('b', 1), ('c', 22)]

# As you should expect from a dictionary, the items are in no particular order.

# However, since the list of tuples is a list, and tuples are comparable, we can now
# sort the list of tuples. Converting a dictionary to a list of tuples is a way for us to
# output the contents of a dictionary sorted by key:

# d = {'a': 10, 'e': 1, 'c': 22}

# t = list(d.items())
# print(t)  # [('a', 10), ('e', 1), ('c', 22)]

# t.sort()
# print(t)  # [('a', 10), ('c', 22), ('e', 1)]

# The new list is sorted in ascending alphabetical order by the key value.

# ======= Multiple assignment with dictionaries =======

# Combining items, tuple assignment, and for, you can see a nice code pattern for
# traversing the keys and values of a dictionary in a single loop:

# d = {'a': 10, 'b': 1, 'c': 22}
# for key, value in d.items():
#     print(value, key)


# # Print out the contents of a dictionary sorted by the value stored in each key-value pair.
# d = {'a': 10, 'b': 1, 'c': 22}

# lst = [(v, k) for k, v in list(d.items())]
# lst.sort(reverse=True)

# print(lst)  # [(22, 'c'), (10, 'a'), (1, 'b')]

# ======= Using tuples as keys in dictionaries =======

# Because tuples are hashable and lists are not, if we want to create a composite key
# to use in a dictionary we must use a tuple as the key.

# We would encounter a composite key if we wanted to create a telephone directory
# that maps from last-name, first-name pairs to telephone numbers. Assuming that
# we have defined the variables last, first, and number, we could write a dictionary
# assignment statement as follows:

# last = 'Rose'
# first = 'Mary'
# number = '0905111111'

# directory = {}
# directory[last, first] = number

# # The expression in brackets is a tuple. We could use tuple assignment in a for loop
# # to traverse this dictionary.

# for last, first in directory:
#     print(first, last, directory[last, first])
# # Mary Rose 0905111111

# t = (3, 2, 4, 1)
# lst = sorted(t)
# print(lst)
# lst = list(reversed(lst))
# print(lst)

# d = {1: 'one'}
# print(type(d))

# d = {'two': 2}
# print(type(d))

# --------------------------------------------------------------------------

# t = ('a', 'b', 'c', 'd')
# print(t[3])
# --------------------------------------------------------------------------

car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red'
} 

inp = input()
if inp in car:
    print(car[inp])