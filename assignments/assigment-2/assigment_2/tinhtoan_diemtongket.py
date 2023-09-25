import os
from functools import reduce

FILE_NAME = 'diem_chitiet.txt'


def get_full_path(file_name):
    # This function returns the path of the file
    absolute_path = os.path.dirname(__file__)
    relative_path = ''
    # relative_path = 'src/lib'
    full_path = os.path.join(absolute_path, relative_path)
    return f'{full_path}/{file_name}'

# a. Hàm tinhdiem_trungbinh

# Output:
# {‘Ma HS’: {‘Mon hoc’: Điểm TB}
# (‘Ma HS’ thay bằng mã học sinh,
# ‘Mon hoc’ thay thế bằng tên môn học,
# Điểm TB thay thế bằng điểm TB của môn đấy).


def tinh_diem_tb_mon_tu_nhien(t):
    return round(0.05*t[0] + 0.1*t[1] + 0.15*t[2] + 0.7*t[3], 2)


def tinh_diem_tb_mon_xa_hoi(t):
    return round(0.05*t[0] + 0.1*t[1] + 0.1*t[2] + 0.15*t[3] + 0.6*t[4], 2)


def tinhdiem_trungbinh(file_name):
    try:
        fhand = open(get_full_path(file_name))
    except:
        print(f'File cannot be opened: {file_name}')

    out = dict()
    subjects = tuple()
    for line in fhand:
        # Remove the 'new line' character ('\n')
        line = line.rstrip()

        # Get the name of subjects ('Toan', 'Ly', 'Hoa', 'Sinh', 'Van', 'Anh', 'Su', 'Dia')
        if ';' not in line:
            subs = line.split(', ')
            subjects = tuple(subs[1:])
            continue

        # Get all marks
        student_info = line.split(';')
        # ['1', ' 5,7,7,8', '5,5,6,6', '8,6,7,7', '4,8,5,7', '7,7,6,7,9', '7,5,8,6,7', '7,8,8,5,9', '5,8,6,8,7']
        id = ''
        marks = dict()
        ids_and_marks = dict()
        for i in range(len(student_info)):
            if i == 0:
                id = student_info[i]
            else:
                subject_marks = student_info[i].lstrip().split(',')
                # [5.0, 7.0, 7.0, 8.0]
                subject_marks = [float(m) for m in subject_marks]
                if i <= 4:
                    avg = tinh_diem_tb_mon_tu_nhien(subject_marks)
                    marks[subjects[i - 1]] = avg
                    # print(f'marks: {subject_marks}')
                    # print(f'Diem tb mon tu nhien: {avg}')
                    # print(f'ids_and_marks: {marks}')
                else:
                    avg = tinh_diem_tb_mon_xa_hoi(subject_marks)
                    marks[subjects[i - 1]] = avg
                    # print(f'marks: {subject_marks}')
                    # print(f'Diem tb mon xa hoi: {avg}')
                    # print(f'ids_and_marks: {marks}')

            ids_and_marks[id] = marks
            print(f'ids_and_marks: {ids_and_marks}')
        print('*******************')


def main():
    tinhdiem_trungbinh(FILE_NAME)


if __name__ == '__main__':
    main()
