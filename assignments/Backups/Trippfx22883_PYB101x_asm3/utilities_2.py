from department import Department
from employee import Employee
from manager import Manager
from utilities import read_json_file


# def display_list_2(lst):
#     for i in lst:
#         print(type(i))
#         print(i)


# Create a Department object from a bunch of information
def create_department(values):
    return Department(values[0], values[1])


# Create an Employee object or a Manager object from a bunch of information
def create_employee(v):
    if len(v) == 9:
        return Manager(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7])
    return Employee(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7])


# Get a list of Deparment objects
# and a list of Employee of objects from a json file.
def fetch_departments_and_employees(json_file_name):
    departments = []
    employees = []
    res = read_json_file(json_file_name)
    if res is not None:
        departments = res.get('departments', [])
        employees = res.get('employees', [])
    departments = [list(dept.values()) for dept in departments]
    departments = [create_department(val) for val in departments]
    employees = [list(emp.values()) for emp in employees]
    employees = [create_employee(val) for val in employees]

    return (departments, employees)
