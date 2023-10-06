import socket
import time

# ========== The world's simplest web browser ==========

# my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_sock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# my_sock.send(cmd)

# while True:
#     data = my_sock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')

# my_sock.close()

# ========== Retrieving an image over HTTP ==========

# HOST = 'data.pr4e.org'
# PORT = 80
# my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_sock.connect((HOST, PORT))
# my_sock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b""

# while True:
#     data = my_sock.recv(5120)
#     if len(data) < 1:
#         break
#     # time.sleep(0.25)
#     count += len(data)
#     print(len(data), count)
#     picture += data

# my_sock.close()

# # Look for the end of the header (2CRLF)
# pos = picture.find(b'\r\n\r\n')
# print(f'Header length {pos}')
# print(picture[:pos].decode())

# # Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open('stuff.jpg', 'wb')
# fhand.write(picture)
# fhand.close()
