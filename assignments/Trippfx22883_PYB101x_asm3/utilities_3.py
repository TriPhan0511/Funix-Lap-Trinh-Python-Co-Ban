from department import Department
from employee import Employee
from manager import Manager
from utilities_2 import fetch_departments_and_employees
from utilities import display_list

# # Messages
# ERR_EMPTY_MSG = 'Bạn không được bỏ trống thông tin này'
# ERR_NOT_AN_INTEGER_MSG = 'Bạn phải nhập vào một số nguyên.'
# ERR_NOT_A_NUMBER_MSG = 'Bạn phải nhập vào một số.'
# ERR_LESS_THAN_ZERO_MSG = 'Bạn phải nhập một số không âm'
# ERR_GREATER_THAN_TOTAL_DAYS_IN_MONTH_MSG='Bạn phải nhập một số nguyên nhỏ hơn hoặc bằng 31.' # Mặc định là một tháng có 31 ngày

# # ERR_EMPTY_MSG = 'This part can not be empty.',
# # ERR_NOT_AN_INTEGER_MSG='You must enter an integer number.'
# ERR_NOT_A_NUMBER_MSG = 'You must enter a number.'
# # ERR_LESS_THAN_OR_EQUAL_TO_ZERO_MSG='You must enter a number which is greater than zero.'
# # ERR_LESS_THAN_ZERO_MSG = 'You must enter a number which is greater than or equal to zero.'


def get_string(msg='Nhập dữ liệu: ', allow_empty=False):
    while True:
        inp = input(msg)
        inp = inp.strip()
        if allow_empty:
            return inp
        if len(inp) == 0:
            print('Bạn không được bỏ trống thông tin này')
            continue
        return inp
    
# Bonus should be an integer and greater than or equal to zero
def get_bonus(msg='Nhập thưởng: ', allow_empty=False):
    while True:
        inp = get_string(msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            int_number = int(inp)
        except ValueError:
            print('Bạn phải nhập vào một số nguyên.')
            continue
        if int_number < 0:
            print('Bạn phải nhập một số không âm')
            continue
        return int_number     


def create_a_new_department(id):
    bonus = get_bonus(msg='Nhập thưởng bộ phận: ')                             
    return Department(id, bonus)


# Get employee's id from user input
# def get_employee_id(emps, msg='Enter an ID: ', err_msg = 'This ID was taken.\nPlease enter another.'):
def get_employee_id(emps, msg='Nhập mã số: '):
    ids = [emp.id.lower() for emp in emps]
    while True:
        id = get_string(msg=msg)
        if id.lower() in ids:
            print('Mã nhân viên đã tồn tại')
            continue
        return id


# # Get department's id from user input
# def get_department_id(dept_ids, depts, msg='Nhập mã bộ phận: '):
#     depts_2 = depts[:]  # copy list
#     while True:
#         dept_id = get_string(msg=msg)
#         if dept_id.lower() not in dept_ids:
#             print('Mã bộ phận chưa tồn tại, tạo mới ...')
#             dept = create_a_new_department(dept_id)
#             if isinstance(dept, Department):
#                 depts_2.append(dept)
#         return (dept_id, depts_2)


# Check if an id exists in a list of department ids.
# If not, create a new department with that id
# and append it to the list of existed departments.
def create_new_dept_if_id_is_new(id, depts):
    ids = [dept.id.lower() for dept in depts]
    while True:
        if id.lower() not in ids:
            print('Mã bộ phận chưa tồn tại, tạo mới ...')
            dept = create_a_new_department(id)
            if isinstance(dept, Department):
                depts.append(dept)
            return True
        return False


# Get employee's position from user input
def get_position(msg='Nhập chức vụ (NV / QL): ', allow_empty=False):
    while True:
        position = get_string(msg=msg, allow_empty=allow_empty)
        if len(position) == 0:
            return 0
        position = position.upper()
        if position not in ['NV', 'QL']:
            print('Nhập sai. Nhập "QL" nếu là Quản Lý hoặc nhập "NV" nếu là Nhân Viên.')
            continue
        if position == 'NV':
            return 1
        return 2


# Get employee's position from user input
def is_manager(msg='Nhập chức vụ (NV / QL): '):
    while True:
        position = get_string(msg=msg)
        position = position.upper()
        if position not in ['NV', 'QL']:
            print('Nhập sai. Nhập "QL" nếu là Quản Lý hoặc nhập "NV" nếu là Nhân Viên.')
            continue
        if position == 'QL':
            return True
        return False


# Get employee's name from user input
def get_name(msg='Nhập họ và tên: ', allow_empty=False):
    return get_string(msg=msg, allow_empty=allow_empty)


# Salary base should be an integer number and greater than zero.
def get_salary_base(msg='Nhập hệ số lương:  ', allow_empty=False):
    while True:
        inp = get_string(msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            int_number = int(inp)
        except ValueError:
            print('Bạn phải nhập vào một số nguyên')
            continue
        if int_number <= 0:
            print('Bạn phải nhập một số lớn hơn 0')
            continue
        return int_number



# Working days or late comming days should be an integer 
# and the value is between 0 and days in month(example: 31)
def get_days_2(msg= 'Nhập số ngày:', total_days_in_month=31, allow_empty=False):
    while True:
        inp = get_string(msg=msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            int_number = int(inp)
        except ValueError:
            print('Bạn phải nhập vào một số nguyên')
            continue
        if int_number < 0:
            print('Bạn phải nhập một số không âm')
            continue
        if int_number > total_days_in_month:
            print(f'Bạn phải nhập một số nguyên nhỏ hơn hoặc bằng {total_days_in_month}.')
            continue
        return int_number
    

# Working performance should be a number and greater than zero.
def get_working_performance(msg ='Nhập hệ số hiệu quả:', allow_empty=False):
    while True:
        inp = get_string(msg=msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            number = float(inp)
        except ValueError:
            print('Bạn phải nhập vào một số.')
            continue
        if number <= 0:
            print('Bạn phải nhập một số không âm')
            continue
        return number    
   


def add_employee(depts, emps):
    print('Thêm nhân viên mới ...')
    id = get_employee_id(emps)
    dept_id = get_string(msg='Nhập mã bộ phận: ')
    manager = is_manager()
    name = get_name()    
    salary_base = get_salary_base()                                  
    working_days = get_days_2(msg='Nhập số ngày làm việc: ')                                    
    working_performance = get_working_performance()
    bonus = get_bonus()
    late_comming_days = get_days_2(msg='Nhập số ngày đi muộn: ')                                     

    if create_new_dept_if_id_is_new(dept_id, depts):
        print('Đã tạo bộ phận mới ...')

    if manager:
        emp = Manager(id, name, salary_base, working_days, dept_id,
                      working_performance, bonus, late_comming_days)
    else:
        emp = Employee(id, name, salary_base, working_days, dept_id,
                       working_performance, bonus, late_comming_days)
    emps.append(emp)

    print('Đã thêm nhân viên mới ...')
    return True



# def edit_employee(emps, msg='Edit Employee'):
#     print(msg)
#     print('Chỉnh sửa nhân viên')
#     err_msg = 'Bạn cần nhập đúng định dạng'
#     id, pos = get_emp_id_for_editing(
#         emps, not_exist_id_msg='\nNhân viên không tồn tại')
#     if id == None:
#         return False
#     emp = emps[pos]
#     name = get_name(msg='\nNhập họ và tên: ', allow_empty=True)
#     if len(name) == 0:
#         name = emp.name
#     # 0: No edit, 1: Employee, 2: Manager
#     position = get_position(allow_empty=True)
#     salary_base = get_int(msg='Nhập hệ số lương: ', err_not_an_integer_msg=err_msg, allow_empty=True)
#     if salary_base == None:
#         salary_base = emp.salary_base
#     working_days = get_days(msg='Nhập số ngày làm việc: ',
#                             allow_empty=True, err_less_than_zero_msg=err_msg)
#     if working_days == None:
#         working_days = emp.working_days
#     working_performance = get_float(
#         msg='Nhập hệ số hiệu quả: ', err_not_a_number_msg=err_msg, allow_empty=True)
#     if working_performance == None:
#         working_performance = emp.working_performance
#     bonus = get_int(msg='Nhập thưởng: ', err_not_an_integer_msg=err_msg, allow_empty=True)
#     if bonus == None:
#         bonus = emp.bonus
#     late_comming_days = get_days(
#         msg='Nhập số ngày đi muộn: ', allow_empty=True, err_less_than_zero_msg=err_msg)
#     if late_comming_days == None:
#         late_comming_days = emp.late_comming_days

#     is_manager = isinstance(emp, Manager)
#     if position == 1 or (position == 0 and not is_manager):
#         emps[pos] = Employee(id, name, salary_base, working_days,
#                              emp.department, working_performance, bonus, late_comming_days)
#     elif position == 2 or (position == 0 and is_manager):
#         emps[pos] = Manager(id, name, salary_base, working_days,
#                             emp.department, working_performance, bonus, late_comming_days)

#     print('\nĐã hoàn tất chỉnh sửa')
#     return True


def delete_employee(emps):
    ids = [e.id.lower() for e in emps]
    id = get_string('Nhập mã nhân viên muốn xóa: ')
    id = id.lower()
    if id not in ids:
        print('\nMã nhân viên không tồn tại')
        return False
    pos = ids.index(id)
    emps.pop(pos)
    print('\nĐã xóa thành công')
    return True


# def delete_department(depts, emps):
#     dept_ids_in_emps = [e.department.lower() for e in emps]
#     ids = [dept.id.lower() for dept in depts]
#     id = get_string('Nhập mã bộ phận muốn xóa: ')
#     id = id.lower()
#     if id not in ids:
#         print('\nMã bộ phận không tồn tại')
#         return False
#     if id in dept_ids_in_emps:
#         print('\nBạn không thể xóa bộ phận đang có nhân viên')
#         return False
#     pos = ids.index(id)
#     depts.pop(pos)
#     print('\nĐã xóa thành công')
#     return True


# def get_emp_id_for_editing(emps, msg='Nhập mã nhân viên: ', not_exist_id_msg='ID này không tồn tại'):
#     ids = [emp.id.lower() for emp in emps]
#     while True:
#         id = get_string(msg)
#         if id.lower() not in ids:
#             print(not_exist_id_msg)
#             return (None, None)
#         return (id, ids.index(id.lower()))





def main():
    pass


if __name__ == '__main__':
    main()
