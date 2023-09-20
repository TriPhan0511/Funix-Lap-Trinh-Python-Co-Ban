##
# Đề bài: Mỗi tháng, giám đốc Yoon đi công tác qua 3-10 quốc gia,
# có những quốc gia Yoon bay qua bay lại nhiều lần.
# Anh ấy muốn đếm tổng số các quốc gia khác nhau mà anh ấy đã đi qua
# thông qua thông qua thông tin trên hộ chiếu.
# Áp dụng hàm set.add() để giúp Yoon thống kê số quốc gia mà anh ấy đã đi qua.

# Ví dụ nếu bạn nhập
# France France Vietnam Germany Germany Italy

# Thì chương trình sẽ hiển thị ra:
# 4
#

# Solution 1: Use the add method
def count_nations(line):
    line = line.strip().lower()
    if len(line) > 0:
        lst = line.split(' ')
        nations = set()
        for e in lst:
            nations.add(e)
        return len(nations)
    else:
        print('Wrong input!')

# # Solution 2: Use the constructor method
# def count_nations(line):
#     line = line.strip().lower()
#     if len(line) > 0:
#         nations = set(line.split(' '))
#         return len(nations)
#     else:
#         print('Wrong input!')


def main():
    # Testing
    # line = ''  # Wrong input!
    # line = '       '  # Wrong input!
    # line = '    France France Vietnam Germany Germany Italy     '  # 4
    # line = 'FRANCE France Vietnam Germany Germany Italy'  # 4
    # line = 'France France Vietnam Germany Germany Italy'  # 4
    # line = 'China USA Ukraina Russia China Holland Laos China Korea'  # 7
    # line = 'Vietnam China Vietnam China Laos Vietnam Campuchia Vietnam Vietnam Thailand'  # 5

    line = input()
    number_of_nations = count_nations(line)
    if number_of_nations != None:
        print(number_of_nations)


if __name__ == '__main__':
    main()
