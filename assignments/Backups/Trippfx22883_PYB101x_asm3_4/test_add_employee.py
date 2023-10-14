from department import Department
from employee import Employee
from manager import Manager
from utilities_2 import fetch_departments_and_employees

# Add a new employee


def add_employee(depts, emps):
    dept_ids = [dept.id for dept in depts]
    emp_ids = [emp.id for emp in emps]
    print(f'\ndept_ids:\n{dept_ids}')
    print(f'\nemp_ids:\n{emp_ids}')


def main():
    depts, emps = fetch_departments_and_employees('test.json')
    print(depts)


if __name__ == '__main__':
    main()
