"""lab 13"""

##
# Ở bài Lab này, bạn sẽ được thực hành các thao tác để trích xuất dữ liệu từ website,
# sau đó sử dụng các dữ liệu đã trích xuất được và thực hiện phần tích.
# Chương trình sẽ sử dụng thư viện urllib để đọc HTML từ trang web
# và phân tích cú pháp dữ liệu, trích xuất các dữ liệu cần thiết.

# Hướng dẫn chi tiết:

# Bạn sẽ cần trích xuất dữ liệu từ trang web:
# https://py4e-data.dr-chuck.net/comments_1430669.html
# Dữ liệu từ trang web được cấu tạo theo dạng bảng, bao gồm hai cột là Name và Comments
# với các dữ liệu về thống kê số lượng comment của từng User, nhiệm vụ của bạn là
# viết chương trình truy cập, trích xuất dữ liệu từ trang web, sau đó tính được hai chỉ số sau:

# Số lượng hàng trong bảng
# Tổng các giá trị của cột "Comments"

# Dữ liệu ở trên Website sẽ là một file HTML chứa bảng với format như sau:

# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

# Bạn phải tìm tất cả các thẻ <span> trong đoạn mã HTML và lấy ra các giá trị từ thẻ đó và tính tổng .
#

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Get context (Ignore SSL certificate errors)
def get_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


# Get all specific tags within an url
def get_tags(url, tag_str='a'):
    ctx = get_context()
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the tags
    return soup(tag_str)


# Compute number of rows which contain comments and how many comments in total.
# Solution 1:
def compute(url):
    rows = get_tags(url, 'tr')
    total = 0
    for row in rows[1:]:
        cells = row.contents
        if len(cells) >= 2:
            comment_cell = cells[1]
            if len(comment_cell.contents) >= 1:
                span_tag = comment_cell.contents[0]
            if len(span_tag.contents) == 1:
                try:
                    value = int(span_tag.contents[0].strip())
                except ValueError:
                    continue
                total += value
    return (len(rows)-1, total)


# Compute number of rows which contain comments and how many comments in total.
# Solution 2:
def compute2(url):
    span_tags = get_tags(url, 'span')
    total = 0
    for tag in span_tags:
        classes = tag.get('class', None)
        if 'comments' in classes:
            if len(tag.contents) == 1:
                try:
                    total += int(tag.contents[0].strip())
                except ValueError:
                    continue

    return (len(span_tags), total)


def main():
    url = 'https://py4e-data.dr-chuck.net/comments_1430669.html'
    # (rows, total) = compute(url)
    (rows, total) = compute2(url)
    print(f'There are {rows} rows in the table (table header is excluded)')
    print(f"There are {total} comments in total.")

    # Output:
    # There are 50 rows in the table (table header is excluded)
    # There are 2699 comments in total.


if __name__ == '__main__':
    main()
