import os
import re


def get_full_path(file_name):
    return f'{os.path.dirname(__file__)}/{file_name}'


def get_file_name_from_url(url):
    # Get the last "word"
    words = url.strip().split('/')
    return words[-1]

# def get_image_name(url):
#     lst = re.findall('http.*/([a-zA-Z0-9.]+jpg|jpeg|png$)', url)
#     if len(lst) > 0:
#         return lst[0]


def overwrite(file_name):
    if os.path.exists(file_name):
        if input(f'Replace {file_name} (Y/n)?').lower() != 'y':
            print('Data not copied')
            return False
    return True


def validate_url(url):
    url = url.strip()
    if not re.search('^http[s]?://.+', url):
        print('The entered link is not an improperly formatted url.')
        return False
    words = url.split('/')
    if len(words) < 4:
        print('Wrong input')
        return False
    return True
