from utilities import format_currency, compute_fine, compute_tax
# from utilities_2 import compute_bonus_salary


# id: Mã số nhân viên
# name: Họ và tên nhân viên
# salary_base: Hệ số lương cơ bản
# working_days: Số ngày làm việc trong tháng
# department: Mã bộ phận
# working_performance: Hệ số hiệu quả
# bonus: Thưởng
# late_comming_days: Số ngày đi muộn
class Employee:
    # Class variables
    url_fines = 'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de'
    url_tax_rates = 'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7'

    def __init__(self, id, name, salary_base, working_days, department, working_performance, bonus, late_comming_days):
        self.id = id
        self.name = name
        self.salary_base = salary_base
        self.working_days = working_days
        self.department = department  # Mã bộ phận
        self.working_performance = working_performance
        self.bonus = bonus
        self.late_comming_days = late_comming_days

    # Mã số: NV001
    # Mã bộ phận: SALE001
    # Chức vụ: Nhân viên
    # Họ và tên: Nguyễn Văn A
    # Hệ số lương: 200,000 (VND)
    # Số ngày làm việc: 26 (ngày)
    # Hệ số hiệu quả: 1
    # Thưởng: 500,000 (VND)
    # Số ngày đi muộn: 2
    def __str__(self):
        out = f'Mã số: {self.id.upper()}'
        out += f'\nMã bộ phận: {self.department.upper()}'
        out += f'\nChức vụ: Nhân viên'  # to_do
        out += f'\nHọ và tên: {self.name}'
        out += f'\nHệ số lương: {format_currency(self.salary_base)}'
        out += f'\nSố ngày làm việc: {self.working_days} (ngày)'
        out += f'\nHệ số hiệu quả: {self.working_performance}'
        out += f'\nThưởng: {format_currency(self.bonus)}'
        out += f'\nSố ngày đi muộn: {self.late_comming_days}'
        return out

    def compute_bonus_salary(self, depts=[]):
        lst = [(dept.id, dept.bonus_salary) for dept in depts]
        dept_id = self.department
        for id, bonus_salary in lst:
            if id == dept_id:
                return bonus_salary

    # 3. Viết hàm tính lương cho nhân viên
    # tổng thu nhập chưa thưởng = (salary_base * working_days) * working_performance

    # Một nhân viên sẽ có các khoản thưởng như sau:
    # Thưởng bộ phận, được lấy từ các Class Department.
    # Chú ý: các quản lý sẽ được thưởng thêm 10% thưởng bộ phận.
    # Thưởng riêng cho từng nhân viên, được lấy từ thuộc tính bonus của Class Employee.
    # tổng thu nhập  = tổng thu nhập chưa thưởng + bonus + thưởng bộ phận - phạt đi muộn

    # Nhân viên sẽ cần trích ra 10.5% thu nhập để đóng bảo hiểm:
    # tổng thu nhập chưa thuế = tổng thu nhập * 89.5 %

    # Sau khi tính được tổng thu nhập, nhân viên sẽ cần đóng các khoản thuế thu nhập cá nhân.
    # Bạn cần tính khoản thuế cần đóng theo công thức ở bước 2.
    # lương thực nhận = tổng thu nhập chưa thuế - khoản thuế cần nộp

    def compute_salary(self, depts=[]):
        tong_thu_nhap_chua_thuong = self.salary_base * \
            self.working_days * self.working_performance

        thuong_bo_phan = self.compute_bonus_salary(depts)
        phat_di_muon = compute_fine(self.url_fines, self.late_comming_days)
        tong_thu_nhap = tong_thu_nhap_chua_thuong + \
            self.bonus + thuong_bo_phan - phat_di_muon

        tong_thu_nhap_chua_thue = tong_thu_nhap * 89.5 / 100

        khoan_thue_can_nop = compute_tax(
            self.url_tax_rates, tong_thu_nhap_chua_thue)
        luong_thuc_nhan = tong_thu_nhap_chua_thue - khoan_thue_can_nop

        return round(luong_thuc_nhan)
