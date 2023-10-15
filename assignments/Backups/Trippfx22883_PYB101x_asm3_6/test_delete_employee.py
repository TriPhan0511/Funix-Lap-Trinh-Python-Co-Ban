from utilities_2 import fetch_departments_and_employees
from utilities_3 import get_string, display_ids


def delete_employee(emps):
    ids = [e.id.lower() for e in emps]
    id = get_string('\nNhập mã nhân viên muốn xóa: ')
    id = id.lower()
    if id not in ids:
        print('\nMã nhân viên không tồn tại')
        return False
    pos = ids.index(id)
    emps.pop(pos)
    print('\nĐã xóa thành công')
    return True
    



def main():
    _, emps = fetch_departments_and_employees('test.json')
    print('----------Before deleting:---------')
    display_ids(emps)

    delete_employee(emps)

    print('----------After deleting:---------')
    display_ids(emps)
    

if __name__ == '__main__':
    main()
