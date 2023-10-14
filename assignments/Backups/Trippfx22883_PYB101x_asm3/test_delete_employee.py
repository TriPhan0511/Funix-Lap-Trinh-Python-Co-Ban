from utilities_2 import fetch_departments_and_employees
from utilities_3 import get_string, display_ids


def delete_employee(emps):
    ids = [e.id.lower() for e in emps]
    # # test
    # for i in ids:
    #     print(i)
    id = get_string('Nhập mã nhân viên muốn xóa: ')
    if id not in ids:
        print('Mã nhân viên không tồn tại')
        return False
    



def main():
    _, emps = fetch_departments_and_employees('test.json')
    delete_employee(emps)
    

if __name__ == '__main__':
    main()
    