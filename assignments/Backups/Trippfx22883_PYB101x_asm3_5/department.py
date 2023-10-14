from utilities import format_currency


# id: Mã bộ phận
# bonus_salary: Thưởng bộ phận
class Department:
    def __init__(self, id, bonus_salary):
        self.id = id
        self.bonus_salary = bonus_salary

    def __str__(self) -> str:
        out = f'Mã bộ phận: {self.id}'
        out += f'\nThưởng bộ phận: {format_currency(self.bonus_salary)}'
        return out
