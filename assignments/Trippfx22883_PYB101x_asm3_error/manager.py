

from employee import Employee
from utilities import format_currency


class Manager(Employee):
    def __init__(self, id, name, salary_base, working_days, department, working_performance, bonus, late_comming_days):
        super().__init__(id, name, salary_base, working_days,
                         department, working_performance, bonus, late_comming_days)
        self.is_manager = True

    def __str__(self) -> str:
        out = f'Mã số: {self.id}'
        out += f'\nMã bộ phận: {self.department}'
        out += f'\nChức vụ: Quản lý'  # to_do
        out += f'\nHọ và tên: {self.name}'
        out += f'\nHệ số lương: {format_currency(self.salary_base)}'
        out += f'\nSố ngày làm việc: {self.working_days} (ngày)'
        out += f'\nHệ số hiệu quả: {self.working_performance}'
        out += f'\nThưởng: {format_currency(self.bonus)}'
        out += f'\nSố ngày đi muộn: {self.late_comming_days}'
        return out

    # Overwrite the "compute_bonus_salary" method
    # Các quản lý sẽ được thưởng thêm 10% thưởng bộ phận.
    def compute_bonus_salary(self, depts=[]):
        lst = [(dept.id, dept.bonus_salary) for dept in depts]
        dept_id = self.department
        for id, bonus_salary in lst:
            if id == dept_id:
                if isinstance(self, Manager):
                    return bonus_salary + bonus_salary * 0.1
                return bonus_salary
