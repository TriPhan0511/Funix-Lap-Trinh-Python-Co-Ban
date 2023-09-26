import tinhtoan_diemtongket
import pprint


def compute_standard_average_mark(marks):
    # marks = [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]
    result = ((marks[0] + marks[4] + marks[5]) * 2.0 + (marks[1] +
              marks[2] + marks[3] + marks[6] + marks[7]) * 1.0) / 11.0

    return round(result, 2)


def check_marks(marks, criteria):
    for m in marks:
        if m < criteria:
            return False
    return True


def grade(marks):
    standard_average_mark = compute_standard_average_mark(marks)
    if (standard_average_mark > 9 and check_marks(marks, 8)):
        result = 'Xuat sac'
    elif (standard_average_mark > 8 and check_marks(marks, 6.5)):
        result = 'Gioi'
    elif (standard_average_mark > 6.5 and check_marks(marks, 5)):
        result = 'Kha'
    elif (standard_average_mark > 6.0 and check_marks(marks, 4.5)):
        result = 'TB Kha'
    else:
        result = 'TB'
    return result


def xeploai_hocsinh(file_name):
    # Open the file for reading
    try:
        fhand = open(tinhtoan_diemtongket.get_full_path(file_name))
    except:
        print(f'File cannot be opened: {file_name}')
        exit()

    result = dict()
    for line in fhand:
        line = line.rstrip()
        if ';' not in line:
            continue
        lst = line.split(';')
        id = lst[0]
        lst = [i.lstrip() for i in lst[1: len(lst)]]
        marks = [float(m) for m in lst]
        result[id] = grade(marks)

    return result


def grade_natural(marks, flag='a'):
    # marks = [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]
    flag = flag.lower()
    if flag == 'a':
        total = marks[0] + marks[1] + marks[2]  # A(Toán, Lý Hóa)
    elif flag == 'a1':
        total = marks[0] + marks[1] + marks[5]  # A1(Toán, Lý, Anh)
    else:  # B(Toán, Hóa, Sinh)
        total = marks[0] + marks[2] + marks[3]  # B(Toán, Hóa, Sinh)
    if total >= 24:
        return 1
    elif total >= 18:
        return 2
    elif total >= 12:
        return 3
    else:
        return 4


def grade_social(marks):
    # marks = [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]
    total = marks[4] + marks[6] + marks[7]  # C(Văn, Sử Địa)
    if total >= 21:
        return 1
    elif total >= 15:
        return 2
    elif total >= 12:
        return 3
    else:
        return 4


def grade_basic(marks):
    # marks = [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]
    total = marks[0] + marks[4] + marks[5] * 2  # D(Toán, Văn, Anh x 2)
    if total >= 32:
        return 1
    elif total >= 24:
        return 2
    elif total >= 20:
        return 3
    else:
        return 4


def xeploai_thidaihoc_hocsinh(file_name):
    # Open the file for reading
    try:
        fhand = open(tinhtoan_diemtongket.get_full_path(file_name))
    except:
        print(f'File cannot be opened: {file_name}')
        exit()

    result = dict()
    for line in fhand:
        line = line.rstrip()
        if ';' not in line:
            continue
        lst = line.split(';')
        id = lst[0]
        lst = [i.lstrip() for i in lst[1: len(lst)]]
        marks = [float(m) for m in lst]
        result[id] = [grade_natural(marks, 'a'), grade_natural(
            marks, 'a1'), grade_natural(marks, 'b'), grade_social(marks), grade_basic(marks)]

    return result


def luudiem_danhgia(file_name):
    # def luudiem_danhgia(file_name, d):
    # Open the file for writing
    try:
        fout = open(tinhtoan_diemtongket.get_full_path(file_name), 'w')
    except:
        print('Something went wrong when writing to a file.')
        exit()

    # First line
    first_line = 'Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B, xeploai_C, xeploai_D\n'
    fout.write(first_line)

    # subjects = list(d['1'].keys())
    # subjects_str = reduce(lambda x, y: f'{x}, {y}', subjects)
    # first_line = f'Ma HS, {subjects_str}'
    # fout.write(f'{first_line}\n')

    # # Next lines
    # ids = list(d.keys())
    # for id in ids:
    #     info = d[id]
    #     out = ''
    #     for s in subjects:
    #         out += f'{info[s]};'
    #     fout.write(f'{id}; {out[:len(out) - 1]}\n')

    print('Done!')

# “Nguyen Hai Nam; Gioi; 1; 1; 1; 3; 2”


def main():
    # file_name = 'diem_trungbinh.txt'
    # pprint.pprint(xeploai_hocsinh(file_name))
    # pprint.pprint(xeploai_thidaihoc_hocsinh(file_name))

    input_file = 'diem_trungbinh.txt'
    output_file = 'danhgia_hocsinh.txt'
    luudiem_danhgia(output_file)


if __name__ == '__main__':
    main()

# {'1': 'Kha', '2': 'TB', '3': 'TB Kha', '4': 'Kha', '5': 'TB Kha', '6': 'Kha'}

# {'1': [2, 2, 2, 1, 2],
#  '2': [2, 3, 2, 2, 3],
#  '3': [2, 2, 2, 2, 2],
#  '4': [2, 2, 2, 1, 2],
#  '5': [3, 2, 2, 2, 2],
#  '6': [2, 2, 2, 1, 2]}
