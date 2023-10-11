# r = Read
# a = Append
# w = Write
# x = Create

# # Read - error if it doesn't exist
# f = open('names.txt')

# # print(f.read())
# # print(f.read(4))  # Read the first 4 characters

# # # Read a line
# # print(f.readline())
# # print(f.readline())

# # Loop through each line
# for line in f:
#     print(line.strip())

# f.close()


# Use try block
try:
    f = open('name_list.txt')
    print(f.read())
except:
    print("The file you want to read doesn't exist.")
else:
    f.close()
