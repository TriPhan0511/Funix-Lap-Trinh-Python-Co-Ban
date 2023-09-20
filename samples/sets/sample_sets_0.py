# Links:
# https://www.w3schools.com/python/python_sets.asp
# https://www.datacamp.com/tutorial/sets-in-python

##
# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
#


# ======= Example =======

# my_set = {'apple', 'banana', 'cherry'}
# print(type(my_set))  # <class 'set'>

# ======= Set Items =======

# Set items are unordered, unchangeable, and do not allow duplicate values.


# ======= Unorderd =======

# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# ======= Unchangeable =======

# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# ======= Duplicates Not Allowed =======

# Sets cannot have two items with the same value.

# my_set = {'apple', 'banana', 'cherry', 'apple'}
# print(len(my_set))  # 3
# print(my_set)  # {'cherry', 'banana', 'apple'}

# Note: The values True and 1 are considered the same value in sets,
# and are treated as duplicates:

# my_set = {'apple', 'banana', 'cherry', 1, 2, True}
# print(len(my_set))  # 5
# print(my_set)  # {1, 2, 'banana', 'apple', 'cherry'}

# my_set = {'apple', 'banana', 'cherry', True, 1, 2}
# print(len(my_set))  # 5
# print(my_set)  # {True, 2, 'apple', 'banana', 'cherry'}

# Note: The values False and 0 are considered the same value in sets,
# and are treated as duplicates:

# my_set = {'apple', 'banana', 'cherry', False, 0, 2}
# print(len(my_set))  # 5
# print(my_set)  # {False, 'banana', 2, 'cherry', 'apple'}

# ======= Get the Length of a Set =======

# my_set = {'apple', 'banana', 'cherry'}
# print(len(my_set))  # 3

# ======= Set Items - Data Types =======

# Set items can be of any data type:

# # Example: String, int and boolean data types:
# set1 = {'apple', 'banana', 'cherry'}
# set2 = {1, 34, 5}
# set3 = {True, False, True}

# # A set can contain different data types:
# set4 = {'apple', 1, True}

# ======= The set() Constructor =======

# It is also possible to use the set() constructor to make a set.

# my_set = set((1, 3, 2,))  # pass a tuple as a argument
# print(type(my_set))  # <class 'set'>


# my_set = set([1, 3, 4])  # pass a list as a argument
# print(type(my_set))  # <class 'set'>

# ======= Advantages of a Python Set =======

# Because sets cannot have multiple occurrences of the same element,
# it makes sets highly useful to efficiently remove duplicate values
# from a list or tuple and to perform common math operations like unions
# and intersections.

# ======= Add Values to a Python Set =======

# graphic_designer = {'InDesign', 'Photoshop'}
# graphic_designer.add('Illustrator')
# print(len(graphic_designer))  # 3

# Note:
# It is important to note that you can only add a value that
# is immutable (like a string or a tuple) to a set.
# For example, you would get a TypeError if you try to add a list to a set.

# graphic_designer.add(['Power Point', 'Blender']) #TypeError: unhashable type: 'list'

# ======= Removes Values to a Python Set =======

# # Option 1: You can use the remove method to remove a value from a set.

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# graphic_designer.remove('Illustrator')
# print(len(graphic_designer))  # 2

# The drawback of this method is that if you try to remove a value that is not in your set,
# you will get a KeyError.
# graphic_designer.remove('Muse')  # KeyError: 'Muse'

# --------------

# # Option 2: You can use the discard method to remove a value from a set.

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# graphic_designer.discard('Illustrator')
# print(len(graphic_designer))  # 2

# # The benefit of this approach over the remove method is if
# # you try to remove a value that is not part of the set,
# # you will not get a KeyError.

# graphic_designer.discard('Muse')
# --------------

# Option 3: You can also use the pop method to
# remove and return an arbitrary value from a set.

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# removed_item = graphic_designer.pop()
# print(removed_item)
# print(len(graphic_designer))  # 2

# # Note:
# # It is important to note that the method raises a KeyError if the set is empty.
# my_set = set()
# my_set.pop()  # KeyError: 'pop from an empty set'

# ======= Removes All Values to a Python Set =======

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# graphic_designer.clear()
# print(len(graphic_designer))  # 0

# ======= Update Python Set Values =======

# The update method adds the elements from a set to a set.
# It requires a single argument that can be a set, list, tuples, or dictionary.
# The .update() method automatically converts other data types into sets and adds them to the set.

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# graphic_designer.update({'Adobe', 'Figma'})
# print(len(graphic_designer))  # 5

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# graphic_designer.update(['Adobe', 'Sketch'])
# print(len(graphic_designer))  # 5

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# graphic_designer.update(('Adobe', 'Figma'))
# print(len(graphic_designer))  # 5

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# graphic_designer.update({'Adobe': 5, 'Figma': 4})
# print(len(graphic_designer))  # 5
# print(graphic_designer)
# # {'Figma', 'Illustrator', 'Photoshop', 'Adobe', 'InDesign'}

# ======= Iterate through a Python Set =======

# Like many standard python data types, it is possible to iterate through a set.

# graphic_designer = {'InDesign', 'Photoshop', 'Illustrator'}
# for skill in graphic_designer:
#     print(skill)

# ======= Transform a Python Set into Ordered Values =======

# Use the sorted function

# unordered_set = {4, 1, 5, 7, 2}
# ascending_ordered_numbers = sorted(unordered_set)
# print(type(ascending_ordered_numbers))  # <class 'list'>
# print(ascending_ordered_numbers)  # [1, 2, 4, 5, 7]
# print(ascending_ordered_numbers[0])  # 1

# unordered_set = {'banana', 'apple', 'lemon', 'cherry'}
# descending_ordered_list = sorted(unordered_set, reverse=True)
# print(descending_ordered_list)  # ['lemon', 'cherry', 'banana', 'apple']

# ======= Remove Duplicates from a List in Python =======


# numbers = [2, 1, 3, 5, 2, 3, 4]
# numbers = list(set(numbers))
# print(numbers)  # [1, 2, 3, 4, 5]

