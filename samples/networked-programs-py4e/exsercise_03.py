# #
# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.
#

from urllib.request import urlopen
from utilities import overwrite, get_full_path, get_file_name_from_url


def count_and_save(url, limit):
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
    count = 0
    info = b''
    displayed = False
    for line in fhand:
        fout.write(line)
        count += len(line)
        if len(info) >= limit and not displayed:
            print(
                f'\n***** The first {limit} characters in the doument: *****\n')
            print(info[:limit].decode())
            displayed = True
        else:
            info += line

    fout.close()
    print(f'\n***** Received {count} characters in total. *****')
    print(f'\n***** A text file was saved. *****')


def main():
    # url = input('Enter a link (sample: http://data.pr4e.org/romeo.txt):\n')
    # url = 'http:/data.pr4e.org/romeo.txt'
    # url = 'http://data.pr4e.org'
    # url = 'http://data.pr4e.org/romeo.txt'
    url = 'http://data.pr4e.org/romeo-full.txt'
    # limit = 100
    limit = 3000

    count_and_save(url, limit)


if __name__ == '__main__':
    main()
