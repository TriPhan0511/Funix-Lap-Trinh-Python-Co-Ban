import json
from utilities import read_json_file
from department import Department
from employee import Employee


def display_list(lst):
    for i in lst:
        print(type(i))
        print(i)


def create_department(values):
    return Department(values[0], values[1])


def create_employee(v):
    return Employee(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7])


def fetch_departments_and_employees():
    JSON_FILE_NAME = 'sample.json'
    departments = []
    employees = []

    res = read_json_file(JSON_FILE_NAME)
    if res is not None:
        departments = res.get('departments', [])
        employees = res.get('employees', [])

    # display_list(departments)
    # display_list(employees)
    depts = []
    emps = []
    for dept in departments:
        values = list(dept.values())
        d = create_department(values)
        depts.append(d)
    for emp in employees:
        values = list(emp.values())
        d = create_employee(values)
        emps.append(d)

    return (depts, emps)


def main():
    depts, emps = fetch_departments_and_employees()
    # display_list(depts)
    display_list(emps)


if __name__ == '__main__':
    main()
