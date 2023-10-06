'''Save a text file from a url'''

import os
from urllib.request import urlopen
from utilities import overwrite, get_full_path, get_file_name_from_url


def save_text_file(url):
    try:
        fhand = urlopen(url)
    except:
        print(f'Something went wrong when connecting to {url}')
        exit()

    file_name = get_file_name_from_url(url)
    file_name = get_full_path(file_name)

    # Don't overwrite the file
    if not overwrite(file_name):
        exit()

    fout = open(file_name, 'wb')
    for line in fhand:
        fout.write(line)

    fout.close()
    print('A text file was saved.')


def main():
    # url = input('Enter a link (sample: http://data.pr4e.org/romeo.txt):\n')
    url = 'http://data.pr4e.org/romeo-full.txt'

    save_text_file(url)


if __name__ == '__main__':
    main()
