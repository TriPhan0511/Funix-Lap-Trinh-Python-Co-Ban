import os
import re
import urllib.request

# #
# Reading binary files using urllib

# Sometimes you want to retrieve a non-text (or binary) file such as an image or
# video file. The data in these files is generally not useful to print out, but you can
# easily make a copy of a URL to a local file on your hard disk using urllib.

# The pattern is to open the URL and use read to download the entire contents of
# the document into a string variable (img) then write that information to a local file as follows:
#


def get_full_path(file_name):
    return f'{os.path.dirname(__file__)}/{file_name}'


def get_image_name(url=''):
    lst = re.findall('http.*/([a-zA-Z0-9.]+jpg|jpeg|png$)', url)
    if len(lst) > 0:
        return lst[0]


# def save_image(url):
#     # Extract the image's name in the url string
#     file_name = get_image_name(url)
#     # Use the read() function to download the entire contents of the document
#     # into a string variable
#     try:
#         img = urllib.request.urlopen(url).read()
#     except urllib.error.URLError:
#         print(f'Can not access to {url}')
#         exit()
#     # Write the information which has just downloaded to a local file
#     try:
#         fhand = open(get_full_path(file_name), 'wb')
#     except:
#         print(f'Cannot write to file {file_name}')
#         exit()
#     fhand.write(img)

#     # Close the stream and notify result to the user
#     fhand.close()
#     print('An image was saved.')

# However if this is a large audio or video file, this program may crash or at least
# run extremely slowly when your computer runs out of memory. In order to avoid
# running out of memory, we retrieve the data in blocks (or buffers) and then write
# each block to your disk before retrieving the next block. This way the program can
# read any size file without using up all of the memory you have in your computer.


def save_image(url):
    # Extract the image's name
    file_name = get_image_name(url)
    # Access to the file on the server
    try:
        img = urllib.request.urlopen(url)
    except:
        print(f'Can not access to {url}')
        exit()
    # Retrieve the data in blocks and then write each block to the disk
    try:
        fhand = open(get_full_path(file_name), 'wb')
        # size = 0
        while True:
            info = img.read(100000)  # Read only 100,000 characters at a time
            if len(info) < 1:
                break
            # size += len(info)
            fhand.write(info)
        # print(f'{size} characters copied.')
        fhand.close()
        print('An image was saved.')
    except:
        print('Something went wrong when writing to file.')
        exit()


def main():
    url = 'http://data.pr4e.org/cover3.jpg'
    save_image(url)


if __name__ == '__main__':
    main()
