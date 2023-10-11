# #
# Bạn cần tạo một Menu để người dùng có thể lựa chọn các chức năng như sau:

# 1. Hiển thị danh sách nhân viên.
# 2. Hiển thị danh sách bộ phận.
# 3. Thêm nhân viên mới.
# 4. Xóa nhân viên theo ID.
# 5. Xóa bộ phân theo ID
# 6. Hiển thị bảng lương.
# 7. Thoát.
# Mời bạn nhập chức năng mong muốn:

# Người dùng sẽ được lựa chọn chức năng (từ 1 --> 7),
# tương ứng với mỗi chức năng sẽ có các thao tác như sau:

# 1. "Hiển thị danh sách nhân viên"
#


from classes import Department, Employee

departments = [
    Department('accounting', 450000),
    Department('marketing', 1000000),
    Department('it', 650000),
    Department('sale01', 500000),
    Department('sale02', 550000),
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
def display_departments(departments, message):
    print(message)
    for dep in departments:
        print(f'{dep}\n')


def main():
    while True:
        inp = get_input()

        if inp == 7:
            print('\nThank you! See you soon. Bye!')
            exit()

        if inp == 1:
            print('Bạn đã lựa chọn "Hiển thị danh sách nhân viên"')
        if inp == 2:
            display_departments(departments, '\n===== Danh sách bộ phận =====\n')
        if inp == 3:
            print('Thêm nhân viên mới.')
        if inp == 4:
            print('Xóa nhân viên theo ID')
        if inp == 5:
            print('Xóa bộ phận theo ID.')
        if inp == 6:
            print('Hiển thị bảng lương.')


if __name__ == '__main__':
    main()
