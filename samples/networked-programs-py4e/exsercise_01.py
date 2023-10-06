import socket
import re

# #
# Exercise 1: Change the socket program socket1.py to prompt the user
# for the URL so it can read any web page. You can use split('/') to
# break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an improperly
# formatted or non-existent URL.
#


def display_text():
    # url = input('Enter a link (sample: http://data.pr4e.org/romeo.txt):\n')
    # url = 'http:/data.pr4e.org/romeo.txt'
    # url = 'http://data.pr4e.org'
    url = 'http://data.pr4e.org/romeo.txt '

    url = url.strip()
    if not re.search('^http[s]?://.+', url):
        print('The entered link is not an improperly formatted url.')
        exit()
    words = url.split('/')
    if len(words) < 4:
        print('Wrong input')
        exit()
    host = words[2]
    port = 80
    try:
        my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_sock.connect((host, port))
        cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
        my_sock.send(cmd)
    except:
        print('Something went wrong when open connection.')
        exit()

    while True:
        data = my_sock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    my_sock.close()


def main():
    display_text()


if __name__ == '__main__':
    main()
