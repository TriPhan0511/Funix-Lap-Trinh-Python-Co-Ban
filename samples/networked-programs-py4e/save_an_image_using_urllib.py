'''
Save an image from a url. 
Sample url:
http://data.pr4e.org/cover3.jpg
'''

import os
from urllib.request import urlopen
from utilities import get_full_path, get_file_name_from_url, overwrite


def save_image(url):
    file_name = get_file_name_from_url(url)
    file_name = get_full_path(file_name)

    # Don't overwrite the file
    if not overwrite(file_name):
        exit()

    # Save an image
    try:
        img = urlopen(url)
    except:
        print(f'Can not access to {url}')
        exit()
    try:
        fhand = open(file_name, 'wb')
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
    # url = input()
    url = 'http://data.pr4e.org/cover3.jpg'
    save_image(url)


if __name__ == '__main__':
    main()
