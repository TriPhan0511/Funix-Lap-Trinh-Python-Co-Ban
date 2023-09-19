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

s = 'bRontosaurus'
d = {}
for letter in s:
    letter = letter.lower()
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] += 1
print(d)
