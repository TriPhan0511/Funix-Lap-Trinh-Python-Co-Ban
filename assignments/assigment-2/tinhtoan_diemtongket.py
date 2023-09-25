import os
from functools import reduce
import pprint


def get_full_path(file_name):
    """Get the path of the file."""
    absolute_path = os.path.dirname(__file__)
    relative_path = ''
    # relative_path = 'src/lib'
    full_path = os.path.join(absolute_path, relative_path)
    return f'{full_path}/{file_name}'


def compute_average_mark_of_natural_science(lst):
    """Compute average mark of a natural science."""
    return round(0.05*lst[0] + 0.1*lst[1] + 0.15*lst[2] + 0.7*lst[3], 2)


def compute_average_mark_of_social_science(lst):
    """Compute average mark of a social science."""
    return round(0.05*lst[0] + 0.1*lst[1] + 0.1*lst[2] + 0.15*lst[3] + 0.6*lst[4], 2)


def tinhdiem_trungbinh(file_name):
    """Compute average mark of every subject of all students in a file."""
    # Open the file for reading
    try:
        fhand = open(get_full_path(file_name))
    except:
        print(f'File cannot be opened: {file_name}')

    # Read lines in the file, compute average mark of every subject of all students
    # and return result as format: {‘Ma HS’: {‘Mon hoc’: Điểm TB}
    result = dict()
    for line in fhand:
        # Remove the 'new line' character ('\n')
        line = line.rstrip()

        # Get the name of subjects ('Toan', 'Ly', 'Hoa', 'Sinh', 'Van', 'Anh', 'Su', 'Dia')
        if ';' not in line:
            subs = line.split(', ')
            subjects = tuple(subs[1:])
            continue

        # Get ids and marks of students and return the result
        student_info = line.split(';')
        id = ''
        marks = dict()
        for i in range(len(student_info)):
            if i == 0:
                id = student_info[i]
            else:
                subject_marks = student_info[i].lstrip().split(',')
                # If a mark cannot be casted to a float,
                # the subject has that mark is removed from the result.
                try:
                    subject_marks = [float(m) for m in subject_marks]
                except:
                    continue

                if i <= 4:
                    avg = compute_average_mark_of_natural_science(
                        subject_marks)
                    marks[subjects[i - 1]] = avg
                else:
                    avg = compute_average_mark_of_social_science(subject_marks)
                    marks[subjects[i - 1]] = avg
            result[id] = marks

    return result


def luudiem_trungbinh(file_name, d):
    try:
        fout = open(get_full_path(file_name), 'w')
    except:
        print('Something went wrong when writing to a file.')

    # First line
    subjects = list(d['1'].keys())
    subjects_str = reduce(lambda x, y: f'{x}, {y}', subjects)
    first_line = f'Ma HS, {subjects_str}'
    fout.write(f'{first_line}\n')

    # Next lines
    ids = list(d.keys())
    for id in ids:
        info = d[id]
        out = ''
        for s in subjects:
            out += f'{info[s]};'
        fout.write(f'{id}; {out[:len(out) - 1]}\n')

    print('Done!')


def main():
    input_file = 'diem_chitiet.txt'
    output_file = 'diem_trungbinh.txt'
    ids_and_marks = tinhdiem_trungbinh(input_file)
    # pprint.pprint(ids_and_marks)
    luudiem_trungbinh(output_file, ids_and_marks)


if __name__ == '__main__':
    main()
