# from manager import Manager


def compute_bonus_salary(emp, depts):
    lst = [(dept.id, dept.bonus_salary) for dept in depts]
    dept_id = emp.department
    for id, bonus_salary in lst:
        if id == dept_id:
            # if isinstance(emp, Manager):
            #     return bonus_salary + bonus_salary * 0.1
            return bonus_salary
