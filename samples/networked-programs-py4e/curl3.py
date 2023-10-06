'''
Save an image from a url. 
Sample url:
http://data.pr4e.org/cover3.jpg
'''

import re
import os
from urllib.request import urlopen


def get_full_path(file_name):
    return f'{os.path.dirname(__file__)}/{file_name}'


def get_image_name(url):
    # Get the last "word"
    words = url.strip().split('/')
    return words[-1]


# def get_image_name(url):
#     lst = re.findall('http.*/([a-zA-Z0-9.]+jpg|jpeg|png$)', url)
#     if len(lst) > 0:
#         return lst[0]


def save_image(url):
    # Get image's name from url
    file_name = get_image_name(url)

    # Don't overwrite the file
    if os.path.exists(get_full_path(file_name)):
        if input(f'Replace {file_name} (Y/n)?').lower() != 'y':
            print('Data not copied')
            exit()

    # Save an image
    try:
        img = urlopen(url)
    except:
        print(f'Can not access to {url}')
        exit()
    try:
        fhand = open(get_full_path(file_name), 'wb')
        while True:
            info = img.read(100000)
            if len(info) < 1:
                break
            fhand.write(info)
        fhand.close()
        print('An image was saved.')
    except:
        print('Something went wrong when writing to file.')
        exit()


def main():
    # url = 'http://data.pr4e.org/cover3.jpg'
    url = input()
    save_image(url)


if __name__ == '__main__':
    main()
