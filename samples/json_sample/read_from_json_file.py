import json
import os


def get_full_path(file_name):
    # This function returns the path of the file
    absolute_path = os.path.dirname(__file__)
    return f'{absolute_path}/{file_name}'


def read_from_json_file(file_name):
    try:
        fhand = open(get_full_path(file_name))
    except FileNotFoundError:
        print(f'Can not open file {file_name}')
        exit()
    try:
        result = json.load(fhand)
    except:
        print(f'Can not load file {file_name}')
        exit()
    return result


def main():
    res = read_from_json_file('sample.json')
    print(json.dumps(res, indent=4))


if __name__ == '__main__':
    main()
