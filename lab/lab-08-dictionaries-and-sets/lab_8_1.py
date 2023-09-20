##
# Đề bài: Phòng làm việc của trưởng phòng Yoon có 10 bạn nam.
# Yoon muốn tính chiều cao trung bình của các số đo chiều cao khác nhau
# của các bạn trong phòng của mình. Bạn hãy viết chương trình giúp Yoon
# xác định chiều cao trung bình này biết số đo của 10 bạn được nhập từ bàn phím trên 1 dòng.

# Ví dụ nếu bạn nhập
# 1.74 1.74 1.80 1.67 1.59 1.59 1.80 1.73 1.73 1.80

# Thì chương trình sẽ hiển thị ra:
# 1.71

# Lưu ý: kết quả được làm tròn đến chữ số thập phân thứ 2.
#

from functools import reduce


def compute_average(line):
    try:
        heights = set(line.split(' '))
        heights = set(filter(lambda e: len(e) > 0, heights))
        total = reduce(lambda x, y: float(x) + float(y), heights, 0)
        return total / len(heights)
    except Exception:
        print('Something went error.')
        return


def main():
    # Testing
    # line = ''  # Something went error.
    # line = '       '  # Something went error.
    # line = '1.0'  # 1.0
    # line = '1.0 1.4'  # 1.2
    # line = '  1.0 1.4       '  # 1.2
    # line = '1.0         1.4'  # 1.2
    # line = '1.74 1.74 1.80 1.67 1.59 1.59 1.80 1.73 1.73 1.80      '  # 1.71
    # line = '       1.74 1.74 1.80 1.67 1.59 1.59 1.80 1.73 1.73 1.80'  # 1.71
    # line = '1.74 1.74 1.80 1.67 1.59 1.59 1.80 1.73 1.73 1.80'  # 1.71
    # line = '1.87 1.92 1.73 1.64 1.79 1.87 1.75 1.75 1.92 1.75'  # 1.78
    # line = '1.70 1.67 1.65 1.64 1.75 1.67 1.65 1.75 1.78 1.70'  # 1.7

    line = input()
    result = compute_average(line.strip())
    if result != None:
        print(round(result, 2))


if __name__ == '__main__':
    main()
