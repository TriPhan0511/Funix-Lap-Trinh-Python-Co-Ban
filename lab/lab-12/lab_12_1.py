##
# lab 12.1

# Đề bài:
# Tiếp tục với bài tập về phương thức ở task trước, ở bài này chúng ta sẽ tính lương cho một quản lý
# và in ra kết quả dựa theo lương nhận và hệ số hiệu quả. Hãy hoàn thiện các class NhanVien, QuanLy (kế thừa class NhanVien)
# và 3 phương thức tinh_luong, hien_thi_luong và tinh_luong_thuong.

# Công thức tính lương thực nhận cho quản lý:

# Lương tổng chưa thưởng = Lương cơ bản x số ngày làm việc x hệ số lương - 1 triệu đồng.
# Nếu lương tổng chưa thưởng > 9 triệu VNĐ/tháng: Lương nhận chưa thưởng = 90% lương tổng chưa thưởng.
# Các trường hợp khác: Lương nhận chưa thưởng = lương tổng chưa thưởng.
# Nếu hệ số hiệu quả < 1: Lương thực nhận = lương nhận chưa thưởng * hệ số hiệu quả.
# Các trường hợp khác: lương thưởng  = lương tổng chưa thưởng * (hệ số hiệu quả - 1) * 85%.
# Lương thực nhận = lương nhận chưa thưởng + lương thưởng

# Ví dụ nếu bạn nhập

# Nguyen Hai Dang
# 4 1000000 15 1.7 1.5

# Ý nghĩa của các con số trong input
# Tên quản lý: 'Nguyen Hai Dang'
# Tháng: 4
# Lương cơ bản: 1000000 VND/ngày
# Số ngày làm việc: 15
# Hệ số lương: 1.7
# Hệ số hiệu quả: 1.5

# Thì chương trình sẽ hiển thị ra

# Luong cua nhan vien Nguyen Hai Dang nhan duoc trong thang 4 la: 31.461.250 VND.

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


class QuanLy(NhanVien):
    def __init__(self, name, month, basic_pay, work_days, coefficient, performance):
        super().__init__(name, month, basic_pay, work_days, coefficient)
        self.performance = performance

    def tinh_luong_thuong(self):
        # Nếu hệ số hiệu quả < 1: Lương thực nhận = lương nhận chưa thưởng * hệ số hiệu quả.
        # Các trường hợp khác: lương thưởng  = lương tổng chưa thưởng * (hệ số hiệu quả - 1) * 85%.
        # Lương thực nhận = lương nhận chưa thưởng + lương thưởng
        if self.performance < 1:
            pay = self.tinh_luong() * self.performance
        else:
            bonus = self.tinh_luong() * (self.performance - 1) * 0.85
            pay = self.tinh_luong() + bonus
        return int(pay)

    # Overwrite method "hien_thi_luong"
    def hien_thi_luong(self):
        print(self.tinh_luong_thuong())
        pay = format_currency(self.tinh_luong_thuong())
        print(
            f'Luong cua nhan vien {self.name} nhan duoc trong thang {self.month} la: {pay} VND.')


# Sample input:
# Nguyen Hai Dang
# 4 1000000 15 1.7 1.5
def get_info():
    '''Get information from user input'''
    # # Testing
    # name = 'Nguyen Hai Dang'
    # other = '4 1000000 15 1.7 1.5'

    name = input().strip()
    other = input().strip()

    if len(name) == 0 or len(other) == 0:
        print('Name or another information can not be empty!')
        exit()

    lst = other.split()
    if len(lst) != 5:
        print('You should enter month, basic pay, work days, pay rate and performance.')
        exit()

    try:
        lst = [float(i) for i in lst]
        if lst[4] < 0:  # performance < 0
            print(
                'Performance rate should be greater than or equal to zero.')
            exit()
        lst[0] = int(lst[0])
    except ValueError:
        print('You should enter numbers for month, basic pay, work days, pay rate and performance.')
        exit()

    return (name, lst[0], lst[1], lst[2], lst[3], lst[4])


# Sample input:
# 31421250
# Sample ouput:
# 31.461.250
def format_currency(amount):
    return f'{amount:,}'.replace(',', '.')


# # Sample input:
# # 31421250.45
# # Sample ouput:
# # $31.421.250,45
# def format_currency_2(amount):
#     currency = f'{amount:,.2f}'
#     a, b = currency.split('.')
#     a = a.replace(',', '.')
#     return f'${a},{b}'


def main():
    info = get_info()
    nhd = QuanLy(info[0], info[1], info[2], info[3], info[4], info[5])
    nhd.hien_thi_luong()


if __name__ == '__main__':
    main()
