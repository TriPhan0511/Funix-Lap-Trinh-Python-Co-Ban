import os
import json


def get_full_path(file_name):
    # This function returns the path of the file
    absolute_path = os.path.dirname(__file__)
    return f'{absolute_path}/{file_name}'


# # Solution 1: Use json.dumps()
# # The function json.dumps() converts a Python object to a JSON object
# def write_to_json_file(file_name, data):
#     # Serialize json
#     json_object = json.dumps(data, indent=4)
#     # Write to sample.json
#     with open(get_full_path(file_name), 'w') as fhand:
#         fhand.write(json_object)

#     print('DONE')

# Solution 1: Use json.dumps()
# The function json.dumps() converts a Python object to a JSON object
def write_data_to_json_file(file_name, data):
    try:
        # Serialize json
        json_object = json.dumps(data, indent=4)
    except Exception as err:
        print(f'Something went wrong: {err}')
        return False
    # Write to sample.json
    try:
        fhand = open(get_full_path(file_name), 'w')
        fhand.write(json_object)
    except FileNotFoundError:
        print(f'File can not be opened for writing: {file_name}')
        return False
    except Exception:
        print(f'Something went wrong when writing to file: {file_name}')
        return False
    fhand.close()
    return True


# Solution : Use json.dump()
def write_to_json_file_2(file_name, data):
    with open(get_full_path(file_name), 'w') as fhand:
        json.dump(data, fhand)

    print('DONE')


def main():
    data = {
        "id": "001",
        "x": "2",
        "name": "Chuck"
    }

    # content = [
    #     {
    #         "id": "001",
    #         "x": "2",
    #         "name": "Chuck"
    #     },
    #     {
    #         "id": "009",
    #         "x": "7",
    #         "name": "Brent"
    #     }
    # ]

    file_name = 'sample.json'
    # write_to_json_file_2(file_name, content)
    res = write_data_to_json_file(file_name, data)
    if res:
        print('Saved data to a json file!')


if __name__ == '__main__':
    main()
