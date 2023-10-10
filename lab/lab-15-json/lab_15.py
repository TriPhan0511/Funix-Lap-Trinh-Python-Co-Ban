# #
# lab 15

# Ở Lab này bạn sẽ được thực hành thao tác trích xuất và xử lý dữ liệu dưới dạng JSON.
# Chương trình sẽ sử dụng thư viện urllib để đọc HTML từ trang web
# và phân tích cú pháp dữ liệu, trích xuất các dữ liệu cần thiết.

# Hướng dẫn chi tiết

# Bạn sẽ cần trích xuất dữ liệu từ trang web:
# https://py4e-data.dr-chuck.net/comments_1430672.json
# Dữ liệu sẽ là một file ở định dạng JSON với các dữ liệu
# về thống kê số lượng comment của từng User, ví dụ như sau:

# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }

# Với dữ liệu như trên tức là User Matthias đã có 97 Comment.
# Nhiệm vụ của bạn là viết một chương trình Python sẽ trích xuất số lượng Comment của từng User,
# sau đó tính tổng số comment của toàn bộ User.
#


import ssl
from urllib.request import urlopen
from urllib.error import URLError
import json


def get_context():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


def compute(url):
    # Fetch data from a url
    try:
        ctx = get_context()
        data = urlopen(url, context=ctx).read().decode()
    except URLError:
        print(f'Can not connect to {url}')
        exit()

    # Parse data which has just fetched into a Python dictionary
    try:
        res = json.loads(data)
    except:
        res = None

    if res is None:
        print('===== Failure To Retrieve')
        exit()
    # print(json.dumps(res, indent=2))

    # Compute number of comments
    total = 0
    if 'comments' in res:
        comments = res['comments']
        for comment in comments:
            if 'count' in comment:
                try:
                    total += int(comment['count'])
                except ValueError:
                    pass

    return total


def main():
    url = 'https://py4e-data.dr-chuck.net/comments_1430672.json'
    print(f'There are {compute(url)} comments in total.')
    # There are 2776 comments in total.


if __name__ == '__main__':
    main()
