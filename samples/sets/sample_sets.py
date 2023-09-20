# ======= Set Operations =======

# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}

# # Union: |
# # The union operator | combines two sets to form a new one containing items in either.
# print(first | second)
# # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# # Intersection: &
# # The intersection operator & gets items only in both.
# print(first & second)
# # {4, 5, 6}

# # Difference: -
# # The difference operator - gets items in the first set but not in the second.
# print(first - second)
# # {1, 2, 3}

# print(second - first)
# # {7, 8, 9}

# # Symetric difference: ^
# # The symmetric difference operator ^ gets items in either set, but not both.
# print(first ^ second)
# # # {1, 2, 3, 7, 8, 9}


# --------------------------------------------------------

# skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
# job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

# # # print(skills & job_skills)
# # common_skills = skills & job_skills
# # print(common_skills[0])

# lst = list((skills & job_skills))
# print(lst[0])

# --------------------------------------------------------

# a = {1, 2, 3}
# b = {0, 3, 4, 5}
# print(a & b)
