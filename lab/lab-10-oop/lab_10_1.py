"""lab 10.1: Gioi thieu ve OOP"""

##
# Đề bài:
# Hãy hoàn thành các khai báo trong phần init của class Student và phương thức print_diemtk
# để có thể in ra được điểm tổng kết của một bạn học sinh từ input gồm tên của sinh viên
# và bảng điểm thành phần của 3 môn Toán, Lý, Hóa.

# Jelly
# 8.54 9.32 7.32


# Thì chương trình sẽ hiển thị ra:
# The average mark of Jelly is 8.39

# Lưu ý: kết quả được làm tròn đến chữ số thập phân thứ 2.
#


class Student:
    def __init__(self, name, math, physics, chemistry):
        self.name = name
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def print_diemtk(self):
        average_mark = round(
            (self.math + self.physics + self.chemistry) / 3, 2)
        print(f'The average mark of {self.name} is {average_mark}')


def get_name_and_marks():
    '''Get name and marks from user'''
    name = input().strip()
    marks_inp = input().strip()

    if len(name) == 0 or len(marks_inp) == 0:
        print('Name or marks can not be empty!')
        exit()

    masks_str = marks_inp.split()
    if len(masks_str) != 3:
        print('You should enter marks for math, physics and chemistry.')
        exit()

    try:
        marks = [float(i) for i in masks_str]
    except ValueError:
        print('You should enter numbers for marks.')
        exit()

    return (name, marks[0], marks[1], marks[2], )


def main():
    info = get_name_and_marks()
    jelly = Student(info[0], info[1], info[2], info[3])
    jelly.print_diemtk()


if __name__ == '__main__':
    main()
