from utilities_2 import fetch_departments_and_employees
from utilities_3 import get_string, display_ids
from utilities import display_list


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
    



def main():
    depts, emps = fetch_departments_and_employees('test.json')

    # test
    print('----------DEPT IDS IN EMPS:---------')
    dept_ids = [e.department.lower() for e in emps]
    for i in dept_ids:
        print(i)

    # test
    print('----------Before deleting:---------')
    display_ids(depts)

    delete_department(depts,emps)

    # test
    print('----------After deleting:---------')
    display_ids(depts)
    

if __name__ == '__main__':
    main()
    