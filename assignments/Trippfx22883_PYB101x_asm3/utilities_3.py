from department import Department
from employee import Employee
from manager import Manager
from utilities_2 import fetch_departments_and_employees
from utilities import display_list


def get_string(msg, error_msg='Bạn không được bỏ trống thông tin này'):
    '''Get a string from user input.'''
    while True:
        inp = input(msg)
        inp = inp.strip()
        if len(inp) == 0:
            print(error_msg)
            continue
        return inp


def get_float(msg='Nhập vào một số: ', err_msg_1='Nhập sai. Vui lòng nhập vào một số.', err_msg_2='Bạn phải nhập một số không âm'):
    '''Get a floating-point number from user input.'''
    while True:
        float_number = get_string(msg)
        try:
            float_number = float(float_number)
        except ValueError:
            print(err_msg_1)
            continue
        if float_number <= 0:
            print(err_msg_2)
            continue
        return float_number


def get_int(msg='Nhập vào một số nguyên: ', err_msg_1='Nhập sai. Vui lòng nhập vào một số nguyên.', err_msg_2='Bạn phải nhập một số không âm'):
    '''Get an integer number from user input.'''
    while True:
        int_number = get_string(msg)
        try:
            int_number = int(int_number)
        except ValueError:
            print(err_msg_1)
            continue
        if int_number < 0:
            print(err_msg_2)
            continue
        return int_number


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

# # Get employee's id from user input
# def get_employee_id(emp_ids):
#     while True:
#         id = get_string('Nhập mã số: ')
#         if id.lower() in emp_ids:
#             print('Mã nhân viên đã tồn tại')
#             continue
#         return id


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
def get_name():
    return get_string('Nhập họ và tên: ')


# Get number of days from user input
def get_days(msg='Nhập số ngày: ', total_days_in_month=31):
    while True:
        days = get_int(msg)
        if days < 0 or days > total_days_in_month:
            print(
                f'Nhập sai. Vui lòng nhập một số nguyên từ 0 đến {total_days_in_month}.')
            continue
        return days


# Display ids
def display_ids(lst, msg='=========================='):
    ids = [item.id.lower() for item in lst]
    display_list(ids, msg)


# Add a new employee
def add_employee(depts, emps):
    # # test
    # display_ids(depts, '====== DEPARTMENT IDS =====')
    # display_ids(emps, '====== EMPLOYEE IDS =====')

    print('Thêm nhân viên mới ...')
    id = get_employee_id(emps)
    dept_id = get_string('Nhập mã bộ phận: ')
    manager = is_manager()
    name = get_name()
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


def main():
    pass
    # depts, emps = fetch_departments_and_employees('test.json')
    # add_employee(depts, emps)

    # display_ids(depts, '====== DEPARTMENT IDS =====')
    # display_ids(emps, '====== EMPLOYEE IDS =====')


if __name__ == '__main__':
    main()
