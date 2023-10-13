from department import Department
from employee import Employee
from manager import Manager
from utilities import write_data_to_file

JSON_FILE_NAME = 'test.json'


departments = [
    Department('ACCOUNTING', 450000),
    Department('MARKETING', 1000000),
    Department('IT', 650000),
    Department('SALE01', 500000),
    Department('SALE02', 550000),
]

employees = [
    Employee('NV001', 'John Doe', 200000,
             26, 'ACCOUNTING', 1, 500000, 0),
    Manager('NV006', 'Lê Thị Hồng', 200000,
            26, 'SALE02', 1, 500000, 0),
]
# employees = [
#     Employee('NV001', 'John Doe', 200000,
#              26, 'ACCOUNTING', 1, 500000, 0),
#     Employee('NV002', 'Nguyễn Văn A', 200000,
#              26, 'ACCOUNTING', 1, 500000, 0),
#     Employee('NV003', 'Nguyễn Văn A', 200000,
#              26, 'MARKETING', 1, 500000, 0),
#     Employee('NV004', 'Nguyễn Văn A', 200000,
#              26, 'IT', 1, 500000, 0),
#     Employee('NV005', 'Nguyễn Văn A', 200000,
#              26, 'SALE01', 1, 500000, 0),
#     Manager('NV006', 'Lê Thị Hồng', 200000,
#             26, 'SALE02', 1, 500000, 0),
# ]


def exit_program():
    d = {
        'departments': departments,
        'employees': employees
    }
    res = write_data_to_file(JSON_FILE_NAME, d)
    if res:
        print(f'Data was saved into a file named "{JSON_FILE_NAME}"')


def main():
    exit_program()


if __name__ == '__main__':
    main()
