from utilities import format_currency


# id: Mã số nhân viên
# name: Họ và tên nhân viên
# salary_base: Hệ số lương cơ bản
# working_days: Số ngày làm việc trong tháng
# department: Mã bộ phận
# working_performance: Hệ số hiệu quả
# bonus: Thưởng
# late_comming_days: Số ngày đi muộn
class Employee:
    def __init__(self, id, name, salary_base, working_days, department, working_performance, bonus, late_comming_days):
        self.id = id
        self.name = name
        self.salary_base = salary_base
        self.working_days = working_days
        self.department = department  # Mã bộ phận
        self.working_performance = working_performance
        self.bonus = bonus
        self.late_comming_days = late_comming_days

    # 3. Viết hàm tính lương cho nhân viên
    # tổng thu nhập chưa thưởng = (salary_base * working_days) * working_performance

    # def compute_salary(self):
    #     salary = self.salary_base * self.working_days * self.working_performance


class Manager(Employee):
    pass


# id: Mã bộ phận
# bonus_salary: Thưởng bộ phận
class Department:
    def __init__(self, id, bonus_salary):
        self.id = id
        self.bonus_salary = bonus_salary

    def __str__(self) -> str:
        out = f'Mã bộ phận: {str(self.id).upper()}'
        out += f'\nThưởng bộ phận: {format_currency(self.bonus_salary)}'
        # out += f'\nThưởng bộ phận: {self.bonus_salary} (VND)'
        return out
