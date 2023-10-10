"""lab 10.2: Phuong thuc (object) trong OOP"""

##
# Đề bài:
#  Hoàn thiện class NhanVien và 2 phương thức tinh_luong, hien_thi_luong
# để in ra kết quả lương của một nhân viên trong một tháng nhất định.

# Công thức tính lương thực nhận

# Lương tổng = Lương cơ bản x số ngày làm việc x hệ số lương - 1 triệu đồng.
# Nếu lương tổng > 9 triệu VNĐ/tháng: Lương thực nhận = 90% lương tổng.
# Các trường hợp khác: Lương thực nhận = lương tổng.

# Ví dụ nếu bạn nhập

# Nguyen Hai Phong
# 3, 500000, 20, 1.5

# Ý nghĩa của các con số trong input

# Tên nhân viên: 'Nguyen Hai Phong'
# Tháng: 3
# Lương cơ bản: 500000 VND/ngày
# Số ngày làm việc: 20
# Hệ số lương: 1.5

# Thì chương trình sẽ hiển thị ra:

# Luong cua nhan vien Nguyen Hai Phong nhan duoc trong thang 3 la: 12600000 VND.

# Chú ý: Kết quả lương sẽ được làm tròn về dạng int.
#


class NhanVien:
    limit = 9000000

    def __init__(self, name, month, basic_pay, work_days, coefficient):
        self.name = name
        self.month = month
        self.basic_pay = basic_pay
        self.work_days = work_days
        self.coefficient = coefficient

    def tinh_luong(self):
        total = self.basic_pay * self.work_days * self.coefficient - 1000000
        if total > self.limit:
            return int(total * 0.9)
        elif total > 0:
            return int(total)
        else:
            return 0

    def hien_thi_luong(self):
        print(
            f'Luong cua nhan vien {self.name} nhan duoc trong thang {self.month} la: {self.tinh_luong()} VND.')


# Sample input:
# Nguyen Hai Phong
# 3, 500000, 20, 1.5
def get_info():
    '''Get information from user input'''
    name = input().strip()
    other = input().strip()

    if len(name) == 0 or len(other) == 0:
        print('Name or another information can not be empty!')
        exit()

    lst = other.split(', ')
    if len(lst) != 4:
        print('You should enter month, basic pay, work days and pay rate.')
        exit()

    try:
        lst2 = [float(i) for i in lst]
        lst2[0] = int(lst2[0])
    except ValueError:
        print('You should enter numbers for month, basic pay, work days and pay rate.')
        exit()

    return (name, lst2[0], lst2[1], lst2[2], lst2[3])


def main():
    info = get_info()
    nhp = NhanVien(info[0], info[1], info[2], info[3], info[4], )
    nhp.hien_thi_luong()


if __name__ == '__main__':
    main()
