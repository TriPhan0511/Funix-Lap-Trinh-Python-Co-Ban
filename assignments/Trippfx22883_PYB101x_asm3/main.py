from department import Department
from employee import Employee
from manager import Manager
from utilities import format_currency, read_json_file, write_data_to_file
import json

JSON_FILE_NAME = 'sample.json'


departments = [
    Department('ACCOUNTING', 450000),
    Department('MARKETING', 1000000),
    Department('IT', 650000),
    Department('SALE01', 500000),
    Department('SALE02', 550000),
]


# Mã số: NV001
# Mã bộ phận: SALE001
# Chức vụ: Nhân viên
# Họ và tên: Nguyễn Văn A
# Hệ số lương: 200,000 (VND)
# Số ngày làm việc: 26 (ngày)
# Hệ số hiệu quả: 1
# Thưởng: 500,000 (VND)
# Số ngày đi muộn: 2
employees = [
    Employee('NV001', 'Nguyễn Văn A', 200000,
             26, 'ACCOUNTING', 1, 500000, 0),
    Employee('NV002', 'Nguyễn Văn A', 200000,
             26, 'MARKETING', 1, 500000, 0),
    Employee('NV003', 'Nguyễn Văn A', 200000,
             26, 'IT', 1, 500000, 0),
    Employee('NV004', 'Nguyễn Văn A', 200000,
             26, 'SALE01', 1, 500000, 0),
    Manager('NV005', 'Nguyễn Văn A', 200000,
            26, 'SALE02', 1, 500000, 0),
]


# employees = [
#     Employee('NV001', 'Nguyễn Văn A', 200000, 26, 'SALE01', 1, 500000, 2),
#     Employee('NV003', 'Lê Thị Thủy', 300000, 26, 'MARKETING', 1.5, 700000, 3),
#     # Manager('NV002', 'Trần Thị Huệ', 500000, 26, 'MARKETING', 1.5, 700000, 3),
# ]


# Create a list of options
def create_menu():
    items = [
        '1. Hiển thị danh sách nhân viên.',
        '2. Hiển thị danh sách bộ phận.',
        '3. Thêm nhân viên mới.',
        '4. Xóa nhân viên theo ID.',
        '5. Xóa bộ phận theo ID.',
        '6. Hiển thị bảng lương.',
        '7. Thoát.',
        '\nMời bạn nhập chức năng mong muốn: '
    ]
    return ('\n'.join(items))


# Get choice from user
def get_input():
    while True:
        try:
            inp = int(input(f'\n{create_menu()}'))
        except ValueError:
            print('\nNhập sai.\nVui lòng nhập một số từ 1 đến 7 để lựa chọn menu!')
            continue
        if inp < 1 or inp > 7:
            print('\nNhập sai.\nVui lòng nhập một số từ 1 đến 7 để lựa chọn menu!')
            continue
        return inp


# Display departments or employees
def display_list(lst, msg='Display list'):
    print(msg)
    for dep in lst:
        print(f'{dep}\n')


# Display id and salary of an employee
# Sample output:
# Mã số: NV001
# Thu nhập thực nhận: 4,961,880 (VND)
def display_salary(emp, depts):
    out = f'Mã số: {emp.id}'
    out += f'\nThu nhập thực nhận: {format_currency(emp.compute_salary(depts))}'
    print(f'{out}\n')


# Display all of employees' salaries
def display_salaries_table(emps, depts, msg='Salaries Table'):
    print(msg)
    for emp in emps:
        display_salary(emp, depts)


def quit_program():
    d = {
        'departments': departments,
        'employees': employees
    }
    res = write_data_to_file(JSON_FILE_NAME, d)
    if res:
        msg = f'\nData was saved into a file named "{JSON_FILE_NAME}"'
    else:
        msg = '\nSomething went wrong when saving data into a file!!!'
    msg += '\nThank you! See you soon. Bye!'
    print(msg)
    exit()


def main():
    while True:
        inp = get_input()

        if inp == 7:
            quit_program()

        if inp == 1:
            display_list(
                employees, '\n********** Danh sách nhân viên **********\n')
        if inp == 2:
            display_list(
                departments, '\n********** Danh sách bộ phận **********\n')
        if inp == 3:
            print('Thêm nhân viên mới.')
        if inp == 4:
            print('Xóa nhân viên theo ID')
        if inp == 5:
            print('Xóa bộ phận theo ID.')
        if inp == 6:
            display_salaries_table(
                employees, departments, '\n********** Hiển thị bảng lương **********\n')


if __name__ == '__main__':
    main()
