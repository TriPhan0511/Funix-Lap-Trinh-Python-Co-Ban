import math


def nhap_toa_do_ba_diem():
    '''Nhập tọa độ 3 điểm từ bàn phím'''
    while True:
        inp = input('Nhập tọa độ Ax, Ay, Bx, By, Cx, Cy: ')
        lst = inp.split(',')
        if len(lst) != 6:
            print('Bạn đã nhập dữ liệu sai. Vui lòng nhập lại.')
            continue
        lst = [i.strip() for i in lst]
        try:
            lst = [int(i) for i in lst]
        except ValueError:
            print(
                'Bạn phải nhập 6 số nguyên cho các tọa độ của các điểm. Vui lòng nhập lại.')
            continue
        break
    return tuple(lst)


def khoangcach(x1, y1, x2, y2):
    '''Tính độ dài các cạnh của tam giác'''
    # print(f'(x1,y1): {x1,y1} - (x2,y2): {x2,y2}')
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)


def kiemtra_tam_giac(xA, yA, xB, yB, xC, yC):
    '''Kiểm tra xem ba điểm có tạo được một tam giác không'''
    # Tính độ dài các cạnh của tam giác
    ab = khoangcach(xA, yA, xB, yB)
    ac = khoangcach(xA, yA, xC, yC)
    bc = khoangcach(xB, yB, xC, yC)

    # Kiểm tra ba cạnh có thỏa bất đẳng thức tam giác hay không
    if ab+ac <= bc or ab+bc <= ac or ac+bc <= ab:
        return False
    return True


def tinh_so_do_goc():
    '''Tính số đo của một góc'''
    # Tiếp theo, bạn sẽ tính xem ba góc BAC, ABC và ACB có độ lớn như nào (ở đơn vị độ).

    # BAC là góc giữa 2 vector là BA và AC.
    # ABC là góc giữa 2 vector là AB và BC.
    # ACB là góc giữa 2 vector là AC và CB.
    


def main():
    # print("PYB101x - Assignment 01")
    # Nhập tọa độ 3 điểm từ bàn phím
    # (xA, yA, xB, yB, xC, yC) = nhap_toa_do_ba_diem()
    (xA, yA, xB, yB, xC, yC) = (1, 1, 2, 2, 3, 1)

    # Tính độ dài các cạnh của tam giác và in ra
    distance_ab = khoangcach(xA, yA, xB, yB)
    distance_ac = khoangcach(xA, yA, xC, yC)
    distance_bc = khoangcach(xB, yB, xC, yC)
    print(f'Độ dài cạnh AB  = {distance_ab} cm.')
    print(f'Độ dài cạnh AC  = {distance_ac} cm.')
    print(f'Độ dài cạnh BC  = {distance_bc} cm.')

    # Kiểm tra ba điểm đầu vào có phải tam giác hay không
    if not kiemtra_tam_giac(xA, yA, xB, yB, xC, yC):
        print('A,B, C không phải là một tam giác')
        exit()
    else:
        print('A,B, C là một tam giác')


if __name__ == '__main__':
    main()
