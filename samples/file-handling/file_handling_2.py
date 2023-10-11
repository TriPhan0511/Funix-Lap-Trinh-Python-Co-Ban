import os


# # Include absolute_path and relative_path
# def get_full_path(file_name):
#     # This function returns the path of the file
#     absolute_path = os.path.dirname(__file__)
#     relative_path = ''
#     # relative_path = 'src/lib'
#     full_path = os.path.join(absolute_path, relative_path)
#     return f'{full_path}/{file_name}'


def get_full_path(file_name):
    # This function returns the path of the file
    absolute_path = os.path.dirname(__file__)
    return f'{absolute_path}/{file_name}'

# ======= Reading files =======


# Solution 1:
fhand = open(get_full_path('mbox-short.txt'))
# fhand = open(get_full_path('mbox-short.txt'))
# fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count += 1
print(f'Line Count: {count}')  # Line Count: 1910
fhand.close()
# ----------------------------------------------------

# Solution 2: Use the "with" statement
with open(get_full_path('mbox-short.txt')) as fhand:
    count = 0
    for line in fhand:
        count += 1
print(f'Line Count: {count}')  # Line Count: 1910

# fhand = open(get_full_path('mbox-short.txt'))
# # fhand = open('mbox-short.txt')
# inp = fhand.read()  # Read the whole file into a string
# print(type(inp))  # <class 'str'>
# print(len(inp))  # 94626
# print(inp[:20])  # From stephen.marquar


# ======= Searching through a file =======

# fhand = open(get_full_path('mbox-short.txt'))
# # fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)


# fhand = open(get_full_path('mbox-short.txt'))
# # fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.find('@uct.ac.za') == -1:
#         continue
#     print(line.rstrip())

# ======= Letting the user choose the file name =======
# ======= Using try, except, and open =======

# while True:
#     file_name = input('\nEnter a file name:\n')
#     try:
#         fhand = open(file_name)
#     except FileNotFoundError as error:
#         print(f'Something went error: {error}')
#         continue
#     else:
#         count = 0
#         for line in fhand:
#             if not line.startswith('Subject:'):
#                 continue
#             # print(line.rstrip())
#             count += 1
#         fhand.close()
#         break

# print(f'There were {count} subject lines in {file_name}.')


# file_name = input('\nEnter a file name:\n')
# try:
#     fhand = open(file_name)
# except FileNotFoundError:
#     print('\nFile cannot be opened.')
#     exit()
# count = 0
# for line in fhand:
#     if not line.startswith('Subject:'):
#         continue
#     count += 1
# fhand.close()
# print(f'There were {count} subject lines in {file_name}.')

# ======= Writing files =======

# fout = open('output.txt', 'w')

# line1 = "This here's the wattle,\n"
# fout.write(line1)

# line2 = "the emblem of our land.\n"
# fout.write(line2)

# fout.close()

# ======= Debugging =======

# s = '1 2\t 3\n 4'
# print(s)
# print(repr(s))  # '1 2\t 3\n 4'
