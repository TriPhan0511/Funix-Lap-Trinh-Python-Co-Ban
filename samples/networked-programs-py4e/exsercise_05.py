# #
# Exercise 5: (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.
#

import socket
from utilities import validate_url, get_file_name_from_url, get_full_path, overwrite


def get_socket(url, port=80):
    if not validate_url(url):
        exit()

    # Get host from url
    words = url.split('/')
    host = words[2]

    try:
        my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_sock.connect((host, port))
        cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
        my_sock.send(cmd)
    except:
        print('Something went wrong when open connection.')
        return
    return my_sock


def count_and_save(url, limit):
    try:
        my_sock = get_socket(url)
    except:
        print(f'Can not open connection to {url}')
        exit()

    file_name = get_file_name_from_url(url)
    file_name = get_full_path(file_name)

    # Don't overwrite the file
    if not overwrite(file_name):
        exit()

    count = 0
    info = b''
    displayed = False
    found = False
    try:
        fout = open(file_name, 'wb')
    except:
        print('Something went wrong while writing to file.')
        exit()

    while True:
        try:
            # data = my_sock.recv(512)
            data = my_sock.recv(5120)
        except:
            print('Something went wrong when receiving data.')
            exit()
        if len(data) < 1:
            break

        count += len(data)
        info += data
        # Look for the end of the header (2CRLF)
        pos = info.find(b'\r\n\r\n')
        if pos != -1 and not found:
            info = info[pos+4:]
            found = True
        if found:
            fout.write(info)
            if len(info) >= limit and not displayed:
                print(
                    f'\n***** The first {limit} characters in the doument: *****\n')
                print(info[:limit].decode())
                displayed = True

    my_sock.close()
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

    # display_text(url, limit)

    count_and_save(url, limit)


if __name__ == '__main__':
    main()
