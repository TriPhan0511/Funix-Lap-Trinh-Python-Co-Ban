import timeit


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst_2 = [i for i in lst if i % 2 == 0 and i % 3 == 0]
# lst_3 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, lst))

# print(lst_2)
# print(lst_3)
# -------------------------------------------------------------------------------------------


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Sử dụng list comprehension
stmt1 = "[i for i in lst if i % 2 == 0 and i % 3 == 0]"
time1 = timeit.timeit(stmt1, globals=globals(), number=1000000)

# Sử dụng filter và lambda
stmt2 = "list(filter(lambda x: x % 2 == 0 and x % 3 == 0, lst))"
time2 = timeit.timeit(stmt2, globals=globals(), number=1000000)


print(f'Thời gian cho list comprehension" {time1} giây')
print(f'Thời gian cho filter và lambda" {time2} giây')