from tinhtoan_diemtongket import get_full_path
import pprint


def compute_gpa(marks):
    """Compute the gpa (grade point average) of each student"""
    # Sample marks:
    # [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]

    result = ((marks[0] + marks[4] + marks[5]) * 2.0 + (marks[1] +
              marks[2] + marks[3] + marks[6] + marks[7]) * 1.0) / 11.0

    return round(result, 2)


def check_marks(marks, criteria):
    """Check whether or not every mark of a student meet a creteria."""
    for m in marks:
        if m < criteria:
            return False
    return True


def grade(marks):
    """Categorize students based on their marks"""
    gpa = compute_gpa(marks)
    if (gpa > 9 and check_marks(marks, 8)):
        result = 'Xuat sac'
    elif (gpa > 8 and check_marks(marks, 6.5)):
        result = 'Gioi'
    elif (gpa > 6.5 and check_marks(marks, 5)):
        result = 'Kha'
    elif (gpa > 6.0 and check_marks(marks, 4.5)):
        result = 'TB Kha'
    else:
        result = 'TB'
    return result


def xeploai_hocsinh(file_name):
    """Categorize students from the information contained in a file"""
    # Sample input:
    # Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia
    # 1; 7.6;5.85;6.95;6.65;8.1;6.75;8.1;7.05
    # 2; 6.4;4.75;7.35;4.35;5.15;5.95;6.6;6.1

    # Sample output:
    # {'1': 'Kha', '2': 'TB'}

    # Open the file for reading
    try:
        fhand = open(get_full_path(file_name))
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


def grade2(mark, criteria, level):
    if mark >= criteria[0]:
        return level[0]
    elif mark >= criteria[1]:
        return level[1]
    elif mark >= criteria[2]:
        return level[2]
    else:
        return level[3]


def grade3(marks):
    # Sample marks:
    # [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]

    level = (1, 2, 3, 4)
    criteria_a_a1_b = (24, 18, 12)
    criteria_c = (21, 15, 12)
    criteria_d = (32, 24, 20)
    mark_a = marks[0] + marks[1] + marks[2]  # A(Toán, Lý Hóa)
    mark_a1 = marks[0] + marks[1] + marks[5]  # A1(Toán, Lý, Anh)
    mark_b = marks[0] + marks[2] + marks[3]  # B(Toán, Hóa, Sinh)
    mark_c = marks[4] + marks[6] + marks[7]  # C(Văn, Sử Địa)
    mark_d = marks[0] + marks[4] + marks[5] * 2  # D(Toán, Văn, Anh x 2)

    return (grade2(mark_a, criteria_a_a1_b, level), grade2(mark_a1, criteria_a_a1_b, level), grade2(mark_b, criteria_a_a1_b, level), grade2(mark_c, criteria_c, level), grade2(mark_d, criteria_d, level),)


# def grade_natural(marks, flag='a'):
#     # Sample marks:
#     # [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]

#     flag = flag.lower()
#     if flag == 'a':
#         total = marks[0] + marks[1] + marks[2]  # A(Toán, Lý Hóa)
#     elif flag == 'a1':
#         total = marks[0] + marks[1] + marks[5]  # A1(Toán, Lý, Anh)
#     else:
#         total = marks[0] + marks[2] + marks[3]  # B(Toán, Hóa, Sinh)
#     if total >= 24:
#         return 1
#     elif total >= 18:
#         return 2
#     elif total >= 12:
#         return 3
#     else:
#         return 4


# def grade_social(marks):
#     # Sample marks:
#     # [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]

#     total = marks[4] + marks[6] + marks[7]  # C(Văn, Sử Địa)
#     if total >= 21:
#         return 1
#     elif total >= 15:
#         return 2
#     elif total >= 12:
#         return 3
#     else:
#         return 4


# def grade_basic(marks):
#     # Sample marks:
#     # [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]

#     total = marks[0] + marks[4] + marks[5] * 2  # D(Toán, Văn, Anh x 2)
#     if total >= 32:
#         return 1
#     elif total >= 24:
#         return 2
#     elif total >= 20:
#         return 3
#     else:
#         return 4


def xeploai_thidaihoc_hocsinh(file_name):
    # Open the file for reading
    try:
        fhand = open(get_full_path(file_name))
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
        result[id] = grade3(marks)
        # result[id] = [grade_natural(marks, 'a'), grade_natural(
        #     marks, 'a1'), grade_natural(marks, 'b'), grade_social(marks), grade_basic(marks)]

    print(result)
    return result


def luudiem_danhgia(input_file, output_file):
    # Open the file for writing
    try:
        fout = open(get_full_path(output_file), 'w')
    except:
        print('Something went wrong when writing to a file.')
        exit()

    # First line
    first_line = 'Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B, xeploai_C, xeploai_D\n'
    fout.write(first_line)

    # Next lines
    d1 = xeploai_hocsinh(input_file)
    d2 = xeploai_thidaihoc_hocsinh(input_file)
    ids = list(d1.keys())
    for id in ids:
        s = f'{id}; {d1[id]}; '
        print(type(d2[id]))
        lst = [str(i) for i in d2[id]]
        print(type(lst))
        s += '; '.join(lst) + '\n'
        fout.write(s)

    print(f'Finished writing to file named "{output_file}"!')


# def main():
#     # sample marks: [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia] Kha
#     marks = [7.6, 5.85, 6.95, 10, 8.1, 6.75, 8.1, 4]
#     # marks = [7.6, 5.85, 6.95, 6.65, 8.1, 6.75, 8.1, 7.05]
#     gpa = compute_gpa(marks)
#     print(gpa)
#     print(grade(marks))

def main():
    # input_file = 'diem_trungbinh.txt'
    # output_file = 'danhgia_hocsinh.txt'
    # luudiem_danhgia(input_file, output_file)

    


if __name__ == '__main__':
    main()
