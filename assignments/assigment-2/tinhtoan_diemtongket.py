import os


def get_full_path(file_name):
    """Get the path of the file."""
    path = os.path.dirname(__file__)
    return f'{path}/{file_name}'


def compute_average_mark_of_natural_science(lst):
    """Compute average mark of a natural science."""
    return round(0.05*lst[0] + 0.1*lst[1] + 0.15*lst[2] + 0.7*lst[3], 2)


def compute_average_mark_of_social_science(lst):
    """Compute average mark of a social science."""
    return round(0.05*lst[0] + 0.1*lst[1] + 0.1*lst[2] + 0.15*lst[3] + 0.6*lst[4], 2)


def tinhdiem_trungbinh(file_name):
    """Compute average mark of every subject of all students in a file."""

    # Sample input file:
    # Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia
    # 1; 5,7,7,8;5,5,6,6;8,6,7,7;4,8,5,7;7,7,6,7,9;7,5,8,6,7;7,8,8,5,9;5,8,6,8,7
    # 2; 8,6,8,6;5,5,8,4;4,9,9,7;4,9,3,4;6,7,7,7,4;8,9,6,7,5;5,7,7,9,6;6,6,4,4,7

    # Ouput Format:
    # {‘Ma HS’: {‘Mon hoc’: Điểm TB}

    # Sample output:
    # {'1': {'Toan': 7.6, 'Ly': 5.85, 'Hoa': 6.95, 'Sinh': 6.65, 'Van': 8.1, 'Anh': 6.75, 'Su': 8.1, 'Dia': 7.05},
    # '2': {'Toan': 6.4, 'Ly': 4.75, 'Hoa': 7.35, 'Sinh': 4.35, 'Van': 5.15, 'Anh': 5.95, 'Su': 6.6, 'Dia': 6.1}}

    # Open the file for reading
    try:
        fhand = open(get_full_path(file_name))
    except:
        print(f'File cannot be opened: {file_name}')
        exit()

    # Read lines in the file, compute average mark of every subject of all students
    # and return result as format: {‘Ma HS’: {‘Mon hoc’: Điểm TB}
    result = dict()
    for line in fhand:
        # Remove the 'new line' character ('\n') at the end of line
        line = line.rstrip()
        # Get the name of subjects ('Toan', 'Ly', 'Hoa', 'Sinh', 'Van', 'Anh', 'Su', 'Dia')
        if ';' not in line:
            subjects = tuple(line.split(', ')[1:])
            continue
        # Get ids and marks of students and return the result
        student_info = line.split(';')
        subjects_and_marks = dict()
        for i in range(len(student_info)):
            if i == 0:
                id = student_info[i]
            else:
                marks = student_info[i].lstrip().split(',')
                # If a mark cannot be casted to a float,
                # the subject has that mark is removed from the result.
                try:
                    marks = [float(m) for m in marks]
                except:
                    continue

                if i <= 4:
                    avg = compute_average_mark_of_natural_science(
                        marks)
                    subjects_and_marks[subjects[i - 1]] = avg
                else:
                    avg = compute_average_mark_of_social_science(marks)
                    subjects_and_marks[subjects[i - 1]] = avg
            result[id] = subjects_and_marks

    return result


def luudiem_trungbinh(file_name, d):
    """Save the ids and the average marks of students to a file."""

    # Sample output file:
    # Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia
    # 1; 7.6;5.85;6.95;6.65;8.1;6.75;8.1;7.05
    # 2; 6.4;4.75;7.35;4.35;5.15;5.95;6.6;6.1

    # Open the file for writing
    try:
        fout = open(get_full_path(file_name), 'w')
    except:
        print('Something went wrong when writing to a file.')
        exit()

    # First line
    subjects = list(d['1'].keys())
    first_line = f"Ma HS, {', '.join(subjects)}"
    fout.write(f'{first_line}\n')

    # Next lines
    ids = list(d.keys())
    for id in ids:
        info = d[id]
        out = ''
        for s in subjects:
            out += f'{info[s]};'
        fout.write(f'{id}; {out[:len(out) - 1]}\n')

    print(f'Finished writing to file named "{file_name}"!')


def main():
    input_file = 'diem_chitiet.txt'
    output_file = 'diem_trungbinh.txt'
    ids_and_marks = tinhdiem_trungbinh(input_file)
    luudiem_trungbinh(output_file, ids_and_marks)


if __name__ == '__main__':
    main()
