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


# employees = [
#     Employee('emp01', 'John Doe', 5000000, 20, 'it', 1.5, 300, 1)
# ]


def create_menu():
    menu = '\n1. Hiển thị danh sách nhân viên.'
    menu += '\n2. Hiển thị danh sách bộ phận.'
    menu += '\n3. Thêm nhân viên mới.'
    menu += '\n4. Xóa nhân viên theo ID.'
    menu += '\n5. Xóa bộ phận theo ID.'
    menu += '\n6. Hiển thị bảng lương.'
    menu += '\n7. Thoát.'
    menu += '\n\nMời bạn nhập chức năng mong muốn: '
    return menu


def main():
    while True:
        try:
            inp = int(input(create_menu()))
        except ValueError:

            print('\nNhập sai.\nVui lòng nhập một số từ 1 đến 7 để lựa chọn menu!')
            continue

        print(f'\nYour input: {inp}')

        if inp == 7:
            print('\nThank you! See you soon. Bye!')
            exit()

        if inp == 1:
            print('Bạn đã lựa chọn "Hiển thị danh sách nhân viên"')
        if inp == 2:
            print('Bạn đã lựa chọn "Hiển thị danh sách bộ phận."\n')
            for dep in departments:
                print(dep)
        if inp == 3:
            print('Bạn đã lựa chọn "Thêm nhân viên mới."')
        if inp == 4:
            print('Bạn đã lựa chọn "Xóa nhân viên theo ID"')
        if inp == 5:
            print('Bạn đã lựa chọn "Xóa bộ phận theo ID."')
        if inp == 6:
            print('Bạn đã lựa chọn "Hiển thị bảng lương."')


if __name__ == '__main__':
    main()
