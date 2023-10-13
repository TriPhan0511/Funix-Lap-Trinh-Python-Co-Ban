from utilities_2 import fetch_departments_and_employees
from utilities import display_list


def main():
    json_file_name = 'test.json'
    depts, emps = fetch_departments_and_employees(json_file_name)
    display_list(depts)
    # display_list(emps)


if __name__ == '__main__':
    main()
