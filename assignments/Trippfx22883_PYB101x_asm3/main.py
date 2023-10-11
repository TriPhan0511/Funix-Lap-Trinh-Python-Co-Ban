from classes import Department, Employee, Manager
from utilities import get_late_comming_fines
import json


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
    Employee('NV001', 'Nguyễn Văn A', 200000, 26, 'SALE01', 1, 500000, 2),
    Manager('NV002', 'Trần Thị Huệ', 500000, 26, 'MARKETING', 1.5, 700000, 3),
    Employee('NV003', 'Lê Thị Thủy', 300000, 26, 'MARKETING', 1.5, 700000, 3),
]


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


# Hiển thị danh sách bộ phận
# Display a list of departments
def display_list(lst, message):
    print(message)
    for dep in lst:
        print(f'{dep}\n')


def main():
    while True:
        inp = get_input()

        if inp == 7:
            print('\nThank you! See you soon. Bye!')
            exit()

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
            print('Hiển thị bảng lương.')


def compute_fine(lst):
    print(json.dumps(lst, indent=2))

    for d in lst:
        if 'min' in d:
            min = d['min']
        else:
            min = 0

        if 'max' in d:
            max = d['max']
        else:
            max = 31

        if 'value' in d:
            value = d['value']
        else:
            value = 31

        late_days = 4
        print(f'min={min}, max={max}, value={value}, late_days={late_days}')
        # result = 0
        # if min <= late_days < max:
        if min < late_days and late_days < max:
            result = value
            print(f'result={result}')
            return result


if __name__ == '__main__':
    # main()
    lst = get_late_comming_fines(
        'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de')
    ressult = compute_fine(lst)
