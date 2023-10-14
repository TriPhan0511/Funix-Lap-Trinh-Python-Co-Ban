from department import Department
from employee import Employee
from manager import Manager
from utilities import format_currency,  write_data_to_file, display_list
from utilities_2 import fetch_departments_and_employees
from utilities_3 import add_employee, delete_employee, delete_department

JSON_FILE_NAME = 'sample.json'


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


# Quit the program
def quit_program(departments, employees, success_msg, error_msg):
    d = {
        'departments': departments,
        'employees': employees
    }
    res = write_data_to_file(JSON_FILE_NAME, d)
    if res:
        print(success_msg)
    else:
        print(error_msg)
    exit()


def main():
    depts, emps = fetch_departments_and_employees(JSON_FILE_NAME)
    changed = False
    while True:
        inp = get_input()
        if inp == 1:
            display_list(
                emps, '\n********** Danh sách nhân viên **********\n', 'Danh sách không có nhân viên nào.')
        if inp == 2:
            display_list(
                depts, '\n********** Danh sách bộ phận **********\n', 'Danh sách không có bộ phận nào.')
        if inp == 3:
            print('\n********** Thêm nhân viên mới **********\n')
            add_employee(depts, emps)
        if inp == 4:
            print('\n********** Xóa nhân viên theo ID **********\n')
            delete_employee(emps)
        if inp == 5:
            print('\n********** Xóa bộ phận theo ID **********\n')
            delete_department(depts, emps)
        if inp == 6:
            display_salaries_table(
                emps, depts, '\n********** Hiển thị bảng lương **********\n')
        if inp == 7:
            quit_program(depts, emps,
                         f'\nĐã lưu dữ liệu vào file "{JSON_FILE_NAME}".', '\nĐã có lỗi xảy ra trong quá trình lưu dữ liệu.')


if __name__ == '__main__':
    main()
