"""lab 14"""

# #
# Tổng quan bài tập

# Tương tự với bài Lab 13, ở bài Lab này bạn sẽ được thực hành thao tác
# trích xuất và xử lý dữ liệu dưới dạng XML. Chương trình sẽ sử dụng thư viện urllib
# để đọc HTML từ trang web và phân tích cú pháp dữ liệu, trích xuất các dữ liệu cần thiết.

# Hướng dẫn chi tiết

# Bạn sẽ cần trích xuất dữ liệu từ trang web:
# https://py4e-data.dr-chuck.net/comments_1430671.xml
# Dữ liệu sẽ là một file ở định dạng XML với các dữ liệu
# về thống kê số lượng comment của từng User, ví dụ như sau:

# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>

# Với dữ liệu như trên tức là User Matthias đã có 97 Comments.
# Nhiệm vụ của bạn là viết một chương trình Python sẽ trích xuất
# số lượng Comment của từng User, sau đó tính tổng số comment của toàn bộ User.
# Bạn phải tìm tất cả các thẻ <comment> và tìm các giá trị <count> trong thẻ đó.
#


import ssl
from urllib.request import urlopen
from urllib.error import URLError
import xml.etree.ElementTree as ET


def get_context():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


def compute(url):
    try:
        ctx = get_context()
        data = urlopen(url, context=ctx).read().decode()
    except URLError:
        print(f'Can not connect to {url}')
        exit()

    tree = ET.fromstring(data)
    comments = tree.findall('comments/comment')
    total = 0
    for comment in comments:
        try:
            count = int(comment.find('count').text)
            total += count
        except:
            pass

    return total


def main():
    url = 'https://py4e-data.dr-chuck.net/comments_1430671.xml'
    print(f'There are {compute(url)} comments in total.')
    # There are 2377 comments in total.


if __name__ == '__main__':
    main()
