##
# Đề bài:
# Cho một dãy số gồm các số tự nhiên và một dòng các lệnh remove cần được thực thi.
# Hãy đưa dãy số tự nhiên này vào một set s, thực thi các lệnh remove ở dòng lệnh remove
# và in ra tổng các phần tử còn lại trong set s.
# Nếu giá trị cần remove không có trong set s, bỏ qua giá trị ấy.

# Ví dụ nếu bạn nhập
# 10 7 8 9 12 13 15 14
# remove 10 remove 7 remove 16 remove 8 remove 12

# Thì chương trình sẽ hiển thị ra:
# 51
#

def parse_line(line):
    numbers = line.strip().split(' ')
    result = set()
    for num in numbers:
        try:
            result.add(float(num))
        except Exception:
            continue
    return result


def sum_remaining_items(source_line, removed_numbers_line):
    source = parse_line(source_line)
    removed_numbers = parse_line(removed_numbers_line)
    source = filter(lambda x: x not in removed_numbers, source)
    return round(sum(source))


def main():
    # line1 = '10 7 8 9 12 13 15 14'
    # line2 = 'remove 10 remove 7 remove 16 remove 8 remove 12'
    # # -> 51

    # line1 = '5 10 15 20 25 30 35 40 40'
    # line2 = 'remove 3 remove 5 remove 7 remove 10 remove 15 remove 17 remove 25'
    # # -> 125

    # line1 = '1 7 21 6 1 9 1 7 6 22'
    # line2 = 'remove 3 remove 2 remove 22 remove 6 remove 1'
    # -> 37

    line1 = input()
    line2 = input()

    print(sum_remaining_items(line1, line2))


if __name__ == '__main__':
    main()
