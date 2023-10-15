from department import Department
from employee import Employee
from manager import Manager
from utilities_2 import fetch_departments_and_employees
from utilities import display_list


# def get_string(msg='Nhập dữ liệu: ', err_msg='Bạn không được bỏ trống thông tin này', allow_empty=False):
def get_string(msg='Enter: ', err_empty_msg='This part can not be empty.', allow_empty=False):
    '''Get a string from user input.'''
    while True:
        inp = input(msg)
        inp = inp.strip()
        if allow_empty:
            return inp
        if len(inp) == 0:
            print(err_empty_msg)
            continue
        return inp



# def get_float(msg='Nhập vào một số: ', err_not_a_number_msg='Bạn phải nhập một số.', err_less_than_zero_msg='Bạn phải nhập một số không âm', err_equal_to_zero__msg='Bạn phải nhập một số lớn hơn 0.', allow_empty=False, allow_zero=True):
def get_float(msg='Enter a number: ', err_not_a_number_msg='You must enter a number.', err_less_than_zero_msg='You must enter a number which is greater than or equal to zero.', err_equal_to_zero__msg='You must enter a number which is greater than zero.', allow_empty=False, allow_zero=True):
    '''Get a floating-point number from user input.'''
    while True:
        inp = get_string(msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            float_number = float(inp)
        except ValueError:
            print(err_not_a_number_msg)
            continue
        if float_number < 0:
            print(err_less_than_zero_msg)
            continue
        if not allow_zero and float_number == 0:
            print(err_equal_to_zero__msg)
            continue
        return float_number








def get_int(msg='Enter an integer number: ', err_not_an_integer_msg='You must enter an integer number.', err_less_than_zero_msg='You must enter a number which is greater than or equal to zero.', allow_empty=False, err_equal_to_zero__msg='You must enter a number which is greater than zero.', allow_zero=True):
    '''Get an integer number from user input.'''
    while True:
        inp = get_string(msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            int_number = int(inp)
        except ValueError:
            print(err_not_an_integer_msg)
            continue
        if int_number < 0:
            print(err_less_than_zero_msg)
            continue
        if not allow_zero and int_number == 0:
            print(err_equal_to_zero__msg)
            continue
        return int_number


def create_a_new_department(id):
    bonus_salary = get_int('Nhập thưởng bộ phận: ')
    return Department(id, bonus_salary)


# Get employee's id from user input
def get_employee_id(emps, msg='Enter an ID: ', err_msg = 'This ID was taken.\nPlease enter another.'):
    ids = [emp.id.lower() for emp in emps]
    while True:
        id = get_string(msg)
        if id.lower() in ids:
            print(err_msg)
            continue
        return id



# Get department's id from user input
def get_department_id(dept_ids, depts):
    depts_2 = depts[:]  # copy list
    while True:
        dept_id = get_string('Nhập mã bộ phận: ')
        if dept_id.lower() not in dept_ids:
            print('Mã bộ phận chưa tồn tại, tạo mới ...')
            dept = create_a_new_department(dept_id)
            if isinstance(dept, Department):
                depts_2.append(dept)
        return (dept_id, depts_2)


# Check if an id exists in a list of department ids.
# If not, create a new department with that id
# and append it to the list of existed departments.
def is_dept_id_exist(id, depts):
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
def get_position(allow_empty=False):
    while True:
        position = get_string('Nhập chức vụ (NV / QL): ',
                              allow_empty=allow_empty)
        if len(position) == 0:
            return 0
        position = position.upper()
        if position not in ['NV', 'QL']:
            print('Nhập sai.\nNhập "QL" nếu là Quản Lý hoặc nhập "NV" nếu là Nhân Viên.')
            continue
        if position == 'NV':
            return 1
        return 2


# Get employee's position from user input
def is_manager(msg='Enter a position (NV/QL): ', err_msg='You must enter "QL" if a manager or "NV" if an employee'):
    while True:
        position = get_string(msg)
        position = position.upper()
        if position not in ['NV', 'QL']:
            print(err_msg)
            continue
        if position == 'QL':
            return True
        return False





# NOTE:
# Function "get_name" is used in functions: "add_employee" and "edit_employee"
# Get employee's name from user input
def get_name(msg='Enter fullname: ', allow_empty=False):
    return get_string(msg=msg, allow_empty=allow_empty)



# Get number of days from user input
# def get_days(msg='Nhập số ngày: ', total_days_in_month=31, allow_empty=False, err_msg_1='Nhập sai. Vui lòng nhập vào một số nguyên.', err_msg_2='Có lỗi!'):
def get_days(msg='Enter number of days: ', total_days_in_month=31, allow_empty=False, err_not_an_integer_msg='You must enter an integer number.', err_less_than_zero_msg='You must enter a number which is greater than or equal to zero.'):
    while True:
        days = get_int(msg, err_not_an_integer_msg=err_not_an_integer_msg, err_less_than_zero_msg=err_less_than_zero_msg, allow_empty=allow_empty)
        # days = get_int(msg, err_msg_1=err_msg, allow_empty=allow_empty)
        if days == None:
            return None
        if days < 0 or days > total_days_in_month:
            print(
                f'Nhập sai. Vui lòng nhập một số nguyên từ 0 đến {total_days_in_month}.')
            continue
        return days



def display_ids(lst, msg='=========================='):
    ids = [item.id.lower() for item in lst]
    display_list(ids, msg)


# ----------------------------------------------------------------------------------------------
def get_int_10(msg='Enter an integer number: ', 
               err_not_an_integer_msg='You must enter an integer number.',
                err_less_than_zero_msg='You must enter a number which is greater than or equal to zero.',
                allow_empty=False, err_equal_to_zero__msg='You must enter a number which is greater than zero.', 
                allow_zero=True):
    '''Get an integer number from user input.'''
    while True:
        inp = get_string(msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            int_number = int(inp)
        except ValueError:
            print(err_not_an_integer_msg)
            continue
        if int_number < 0:
            print(err_less_than_zero_msg)
            continue
        if not allow_zero and int_number == 0:
            print(err_equal_to_zero__msg)
            continue
        return int_number


# Salary base should be an integer number and greater than zero.
def get_salary_base(msg='Enter a salary base: ', 
                    err_empty_msg = 'This part can not be empty.',
                    err_not_an_integer_msg='You must enter an integer number.', 
                    err_less_than_or_equal_to_zero_msg='You must enter a number which is greater than zero.',
                    allow_empty=False):
    while True:
        inp = get_string(msg, err_empty_msg=err_empty_msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            int_number = int(inp)
        except ValueError:
            print(err_not_an_integer_msg)
            continue
        if int_number <= 0:
            print(err_less_than_or_equal_to_zero_msg)
            continue
        return int_number



# Number of working days should be an integer and the value is between 0 and days in month(example: 31)
def get_working_days(msg='Enter a working days: ', 
                    err_empty_msg = 'This part can not be empty.',
                    err_not_an_integer_msg='You must enter an integer number.', 
                    err_less_than_zero_msg='You must enter a number which is greater than or equal to zero.',
                    err_greater_than_total_days_in_month_msg='You must enter a number which is greater than or equal to zero and less than total days in month.',
                    total_days_in_month=31, 
                    allow_empty=False):
    while True:
        inp = get_string(msg, err_empty_msg=err_empty_msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            int_number = int(inp)
        except ValueError:
            print(err_not_an_integer_msg)
            continue
        if int_number < 0:
            print(err_less_than_zero_msg)
            continue
        if int_number > total_days_in_month:
            print(err_greater_than_total_days_in_month_msg)
            continue
        return int_number


def add_employee(depts, emps):
    print('Thêm nhân viên mới ...')
    err_empty_msg = 'Bạn không được bỏ trống thông tin này'
    err_not_an_integer_msg = 'Bạn phải nhập vào một số nguyên.'
    err_less_than_or_equal_to_zero_msg = 'Bạn phải nhập một số không âm'
    id = get_employee_id(emps, msg='Nhập mã số: ', err_msg = 'Mã nhân viên đã tồn tại\nVui lòng nhập một mã số khác.')
    dept_id = get_string(msg='Nhập mã bộ phận: ', error_msg='Bạn không được bỏ trống thông tin này')
    manager = is_manager(msg='Nhập chức vụ (NV / QL): ', err_msg='Bạn phải nhập "QL" nếu là Quản Lý hoặc nhập "NV" nếu là Nhân Viên.')
    name = get_name(msg='Nhập họ và tên: ')    
    salary_base = get_salary_base(msg='Nhập hệ số lương: ', 
                                  err_empty_msg=err_empty_msg, 
                                  err_not_an_integer_msg=err_not_an_integer_msg, 
                                  err_less_than_or_equal_to_zero_msg=err_less_than_or_equal_to_zero_msg)
    working_days = get_days('Nhập số ngày làm việc: ', 
                            err_not_an_integer_msg=err_not_an_integer_msg, 
                            err_less_than_zero_msg=err_less_than_or_equal_to_zero_msg)
    # todo
    working_performance = get_float('Nhập hệ số hiệu quả: ', err_less_than_zero_msg=err_less_than_or_equal_to_zero_msg)
    bonus = get_int('Nhập thưởng: ')
    late_comming_days = get_days('Nhập số ngày đi muộn: ')

    if is_dept_id_exist(dept_id, depts):
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



def edit_employee(emps, msg='Edit Employee'):
    print(msg)
    print('Chỉnh sửa nhân viên')
    err_msg = 'Bạn cần nhập đúng định dạng'
    id, pos = get_emp_id_for_editing(
        emps, not_exist_id_msg='\nNhân viên không tồn tại')
    if id == None:
        return False
    emp = emps[pos]
    name = get_name(msg='\nNhập họ và tên: ', allow_empty=True)
    if len(name) == 0:
        name = emp.name
    # 0: No edit, 1: Employee, 2: Manager
    position = get_position(allow_empty=True)
    salary_base = get_int(msg='Nhập hệ số lương: ', err_not_an_integer_msg=err_msg, allow_empty=True)
    if salary_base == None:
        salary_base = emp.salary_base
    working_days = get_days(msg='Nhập số ngày làm việc: ',
                            allow_empty=True, err_less_than_zero_msg=err_msg)
    if working_days == None:
        working_days = emp.working_days
    working_performance = get_float(
        msg='Nhập hệ số hiệu quả: ', err_not_a_number_msg=err_msg, allow_empty=True)
    if working_performance == None:
        working_performance = emp.working_performance
    bonus = get_int(msg='Nhập thưởng: ', err_not_an_integer_msg=err_msg, allow_empty=True)
    if bonus == None:
        bonus = emp.bonus
    late_comming_days = get_days(
        msg='Nhập số ngày đi muộn: ', allow_empty=True, err_less_than_zero_msg=err_msg)
    if late_comming_days == None:
        late_comming_days = emp.late_comming_days

    is_manager = isinstance(emp, Manager)
    if position == 1 or (position == 0 and not is_manager):
        emps[pos] = Employee(id, name, salary_base, working_days,
                             emp.department, working_performance, bonus, late_comming_days)
    elif position == 2 or (position == 0 and is_manager):
        emps[pos] = Manager(id, name, salary_base, working_days,
                            emp.department, working_performance, bonus, late_comming_days)

    print('\nĐã hoàn tất chỉnh sửa')
    return True


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


def delete_department(depts, emps):
    dept_ids_in_emps = [e.department.lower() for e in emps]
    ids = [dept.id.lower() for dept in depts]
    id = get_string('Nhập mã bộ phận muốn xóa: ')
    id = id.lower()
    if id not in ids:
        print('\nMã bộ phận không tồn tại')
        return False
    if id in dept_ids_in_emps:
        print('\nBạn không thể xóa bộ phận đang có nhân viên')
        return False
    pos = ids.index(id)
    depts.pop(pos)
    print('\nĐã xóa thành công')
    return True


def get_emp_id_for_editing(emps, msg='Nhập mã nhân viên: ', not_exist_id_msg='ID này không tồn tại'):
    ids = [emp.id.lower() for emp in emps]
    while True:
        id = get_string(msg)
        if id.lower() not in ids:
            print(not_exist_id_msg)
            return (None, None)
        return (id, ids.index(id.lower()))





def main():
    # _, emps = fetch_departments_and_employees('test.json')
    # edit_employee(emps)
    pass


if __name__ == '__main__':
    main()
