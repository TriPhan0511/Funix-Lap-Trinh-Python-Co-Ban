from department import Department
from employee import Employee
from manager import Manager
from utilities_2 import fetch_departments_and_employees
from utilities import display_list


def get_string(msg, error_msg='Bạn không được bỏ trống thông tin này', allow_empty=False):
    '''Get a string from user input.'''
    while True:
        inp = input(msg)
        inp = inp.strip()
        if allow_empty:
            return inp
        if len(inp) == 0:
            print(error_msg)
            continue
        return inp



# def get_string(msg, error_msg='Bạn không được bỏ trống thông tin này'):
#     '''Get a string from user input.'''
#     while True:
#         inp = input(msg)
#         inp = inp.strip()
#         if len(inp) == 0:
#             print(error_msg)
#             continue
#         return inp


def get_float(msg='Nhập vào một số: ', err_msg_1='Nhập sai. Vui lòng nhập vào một số.', err_msg_2='Bạn phải nhập một số không âm', allow_empty=False):
    '''Get a floating-point number from user input.'''
    while True:
        inp = get_string(msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            float_number = float(inp)
        except ValueError:
            print(err_msg_1)
            continue
        if float_number <= 0:
            print(err_msg_2)
            continue
        return float_number


# def get_float(msg='Nhập vào một số: ', err_msg_1='Nhập sai. Vui lòng nhập vào một số.', err_msg_2='Bạn phải nhập một số không âm'):
#     '''Get a floating-point number from user input.'''
#     while True:
#         float_number = get_string(msg)
#         try:
#             float_number = float(float_number)
#         except ValueError:
#             print(err_msg_1)
#             continue
#         if float_number <= 0:
#             print(err_msg_2)
#             continue
#         return float_number

def get_int(msg='Nhập vào một số nguyên: ', err_msg_1='Nhập sai. Vui lòng nhập vào một số nguyên.', err_msg_2='Bạn phải nhập một số không âm', allow_empty=False):
    '''Get an integer number from user input.'''
    while True:
        inp = get_string(msg, allow_empty=allow_empty)
        if len(inp) == 0:
            return None
        try:
            int_number = int(inp)
        except ValueError:
            print(err_msg_1)
            continue
        if int_number < 0:
            print(err_msg_2)
            continue
        return int_number


# def get_int(msg='Nhập vào một số nguyên: ', err_msg_1='Nhập sai. Vui lòng nhập vào một số nguyên.', err_msg_2='Bạn phải nhập một số không âm'):
#     '''Get an integer number from user input.'''
#     while True:
#         int_number = get_string(msg)
#         try:
#             int_number = int(int_number)
#         except ValueError:
#             print(err_msg_1)
#             continue
#         if int_number < 0:
#             print(err_msg_2)
#             continue
#         return int_number


# todo
# Create a new department
def create_a_new_department(id):
    bonus_salary = get_int('Nhập thưởng bộ phận: ')
    return Department(id, bonus_salary)


# Get employee's id from user input
def get_employee_id(emps):
    ids = [emp.id.lower() for emp in emps]
    while True:
        id = get_string('Nhập mã số: ')
        if id.lower() in ids:
            print('Mã nhân viên đã tồn tại')
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
        position = get_string('Nhập chức vụ (NV / QL): ', allow_empty=allow_empty)
        if len(position) == 0:
            return 0
        position = position.upper()
        if position not in ['NV', 'QL']:
            print('Nhập sai.\nNhập "QL" nếu là Quản Lý hoặc nhập "NV" nếu là Nhân Viên.')
            continue
        if position == 'QL':
            return 2
        return 1


# Get employee's position from user input
def is_manager():
    while True:
        position = get_string('Nhập chức vụ (NV / QL): ')
        position = position.upper()
        if position not in ['NV', 'QL']:
            print('Nhập sai.\nNhập "QL" nếu là Quản Lý hoặc nhập "NV" nếu là Nhân Viên.')
            continue
        if position == 'QL':
            return True
        return False


# Get employee's name from user input
def get_name(allow_empty=False):
    return get_string(msg='Nhập họ và tên: ', allow_empty=allow_empty)



# # Get employee's name from user input
# def get_name():
#     return get_string('Nhập họ và tên: ')


# Get number of days from user input
def get_days(msg='Nhập số ngày: ', total_days_in_month=31, allow_empty=False, err_msg = 'Có lỗi!'):
    while True:
        days = get_int(msg, err_msg_1=err_msg, allow_empty=allow_empty)
        if days == None:
            return None
        if days < 0 or days > total_days_in_month:
            print(
                f'Nhập sai. Vui lòng nhập một số nguyên từ 0 đến {total_days_in_month}.')
            continue
        return days



# # Get number of days from user input
# def get_days(msg='Nhập số ngày: ', total_days_in_month=31):
#     while True:
#         days = get_int(msg)
#         if days < 0 or days > total_days_in_month:
#             print(
#                 f'Nhập sai. Vui lòng nhập một số nguyên từ 0 đến {total_days_in_month}.')
#             continue
#         return days


# Display ids
def display_ids(lst, msg='=========================='):
    ids = [item.id.lower() for item in lst]
    display_list(ids, msg)


# Add a new employee
def add_employee(depts, emps):
    print('Thêm nhân viên mới ...')
    id = get_employee_id(emps)
    dept_id = get_string('Nhập mã bộ phận: ')
    manager = is_manager()
    name = get_name()
    # todo
    # Change from get_float to get_int
    salary_base = get_float('Nhập hệ số lương: ') 
    working_days = get_days('Nhập số ngày làm việc: ')
    working_performance = get_float('Nhập hệ số hiệu quả: ')
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


# Delete employee
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

# Delete department
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



def get_emp_id_for_editing(emps):
    ids = [emp.id.lower() for emp in emps]
    while True:
        id = get_string('Nhập mã số: ')
        if id.lower() not in ids:
            print('Nhân viên không tồn tại')
            return (None,None)
        return (id, ids.index(id.lower()))



# def get_emp_id_for_editing(emps):
#     ids = [emp.id.lower() for emp in emps]
#     while True:
#         id = get_string('Nhập mã số: ', allow_empty=True)
#         if id.lower() not in ids:
#             print('Nhân viên không tồn tại')
#             return (None,None)
#         return (id, ids.index(id.lower()))


# Chỉnh sửa nhân viên
# Nhập mã nhân viên: 'NV002'

# Nhập họ và tên: ...
# Nhập chức vụ (NV / QL): ...
# Nhập hệ số lương: ...
# Nhập số ngày làm việc: ...
# Nhập hệ số hiệu quả: ...
# Nhập thưởng: ...
# Nhập số ngày đi muộn: ...

# Đã hoàn tất chỉnh sửa
# Edit employee
def edit_employee(emps):
     # test
    for e in emps:
        print(e)
    print('--------------------------')
    print('Chỉnh sửa nhân viên')
    err_msg = 'Bạn cần nhập đúng định dạng'
    id, pos = get_emp_id_for_editing(emps)
    if id == None:
        return False
    emp = emps[pos]
    # print(emp)
    name = get_name(allow_empty=True)
    if len(name) == 0:
        name = emp.name
    position = get_position(allow_empty=True) # 0: No edit, 1: Employee, 2: Manager
    salary_base = get_int(msg='Nhập hệ số lương: ', err_msg_1=err_msg, allow_empty=True)
    if salary_base == None:
        salary_base = emp.salary_base
    working_days = get_days(msg='Nhập số ngày làm việc: ', allow_empty=True, err_msg=err_msg)
    if working_days == None:
        working_days = emp.working_days
    working_performance = get_float(msg='Nhập hệ số hiệu quả: ', err_msg_1=err_msg, allow_empty=True)
    if working_performance == None:
        working_performance = emp.working_performance
    bonus = get_int(msg='Nhập thưởng: ', err_msg_1=err_msg, allow_empty=True)
    if bonus == None:
        bonus = emp.bonus
    late_comming_days = get_days(msg='Nhập số ngày đi muộn: ', allow_empty=True, err_msg=err_msg)
    if late_comming_days == None:
        late_comming_days = emp.late_comming_days

    emps[pos] = Employee(id, name, salary_base, working_days, emp.department, working_performance, bonus, late_comming_days)        

    # test
    print('--------------------------')
    for e in emps:
        print(e)

    # # test        
    # print(f'id:{id}')
    # print(f'name:{name}')
    # print(f'position:{position}')
    # print(f'salary_base:{salary_base}')
    # print(f'working_days:{working_days}')
    # print(f'working_performance:{working_performance}')
    # print(f'bonus:{bonus}')
    # print(f'late_comming_days:{late_comming_days}')

    

# def add_employee_0(depts, emps):
#     print('Thêm nhân viên mới ...')
#     id = get_employee_id(emps)
#     dept_id = get_string('Nhập mã bộ phận: ')
    # manager = is_manager()
#     name = get_name()
#     salary_base = get_float('Nhập hệ số lương: ')
#     working_days = get_days('Nhập số ngày làm việc: ')
#     working_performance = get_float('Nhập hệ số hiệu quả: ')
#     bonus = get_int('Nhập thưởng: ')
#     late_comming_days = get_days('Nhập số ngày đi muộn: ')

#     if is_dept_id_exist(dept_id, depts):
#         print('Đã tạo bộ phận mới ...')

#     if manager:
#         emp = Manager(id, name, salary_base, working_days, dept_id,
#                       working_performance, bonus, late_comming_days)
#     else:
#         emp = Employee(id, name, salary_base, working_days, dept_id,
#                        working_performance, bonus, late_comming_days)
#     emps.append(emp)

#     print('Đã thêm nhân viên mới ...')
#     return True    



def main():
    _, emps =  fetch_departments_and_employees('test.json')
    edit_employee(emps)


if __name__ == '__main__':
    main()
