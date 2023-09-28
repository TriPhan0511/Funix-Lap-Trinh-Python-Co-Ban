from operator import attrgetter

##
# This sample demonstrates how to sort a list of objects using an attribute in Python.
#

# ======= 1. Using list.sort() function =======

# This function sorts the list in-place and produces a stable sort.

# It accepts two optional keyword-only arguments: "key" and "reverse".
# The "key" argument specifies a single-arg function to extract a comparison key from each list object.
# When the "reverse" argument is True, the list will be sorted in reversed order.

# Sample:
# Sort a list of "Employee" objects using the "name" attribute in natural order,
# followed by the reverse order.


# class Employee:
#     def __init__(self, name, dept, age):
#         self.name = name
#         self.dept = dept
#         self.age = age

#     def __repr__(self):
#         return f'{{ {self.name} {self.dept} {self.age} }}'


# def main():
#     employees = [
#         Employee('John', 'IT', 28),
#         Employee('Sam', 'Banking', 20),
#         Employee('Joe', 'Finance', 25),
#     ]

#     # # Sort list by "name" in the natural order
#     # employees.sort(key=lambda x: x.name)

#     # # Output: [{ Joe Finance 25 }, { John IT 28 }, { Sam Banking 20 }]
#     # print(employees)

#     # # Sort list by "name" in reverse order
#     # employees.sort(key=lambda x: x.name, reverse=True)

#     # # Output: [{ Sam Banking 20 }, { John IT 28 }, { Joe Finance 25 }]
#     # print(employees)

#     # You can also use the operator.attrgetter() function to produce value for the "key" attribute.
#     # It returns a callable object that fetches a specified attribute from its operand.
#     employees.sort(key=attrgetter('name'))

#     # Output: [{ Joe Finance 25 }, { John IT 28 }, { Sam Banking 20 }]
#     print(employees)


# if __name__ == '__main__':
#     main()

# ======= 2. Using sorted function =======

# The list.sort() function does not return the sorted sequence but modifies the list in-place.
# To return a new sorted list instance, you can use the sorted() built-in function.
# Like the list.sort() function, it accepts two optional keyword-only arguments - "key"
# and "reverse" - that have the same meaning

class Employee:
    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age

    def __repr__(self):
        return f'{{ {self.name} {self.dept} {self.age} }}'


def main():
    employees = [
        Employee('John', 'IT', 28),
        Employee('Sam', 'Banking', 20),
        Employee('Joe', 'Finance', 25),
    ]

    sorted_by_name = sorted(employees, key=attrgetter('name'))
    # sorted_by_name = sorted(employees, key=lambda x: x.name)

    # Output: [{ Joe Finance 25 }, { John IT 28 }, { Sam Banking 20 }]
    print(sorted_by_name)


if __name__ == '__main__':
    main()
