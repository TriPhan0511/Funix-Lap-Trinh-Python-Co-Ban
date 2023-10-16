from utilities import write_data_to_file, display_list
from utilities_fetch_departments_and_employees_from_json_file import fetch_departments_and_employees
from utilities_2 import add_employee, delete_employee, delete_department, display_salaries_table, edit_employee

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
        '7. Chỉnh sửa nhân viên.',
        '8. Thoát.',
        '\nMời bạn nhập chức năng mong muốn: '
    ]
    return ('\n'.join(items))


# Get choice from user
def get_input(start=1, end=8):
    err_msg = f'\nNhập sai.\nVui lòng nhập một số từ {start} đến {end} để lựa chọn menu!'
    while True:
        try:
            inp = int(input(f'\n{create_menu()}'))
        except ValueError:
            print(err_msg)
            continue
        if inp < start or inp > end:
            print(err_msg)
            continue
        return inp


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
    while True:
        inp = get_input(1, 8)
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
            print('\n********** Chỉnh sửa nhân viên **********\n')
            edit_employee(emps)
                
        if inp == 8:
            quit_program(depts, emps,
                         f'\nĐã lưu dữ liệu vào file "{JSON_FILE_NAME}"\n.', '\nĐã có lỗi xảy ra trong quá trình lưu dữ liệu.\n')


if __name__ == '__main__':
    main()


