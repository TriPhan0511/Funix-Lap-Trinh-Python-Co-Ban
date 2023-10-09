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


# Từ hai điểm A và B, bạn có thể tạo ra Vector AB đi qua hai điểm đó
# với toạ độ là (xB - xA, yB - yA).
def tao_vector(x1, y1, x2, y2):
    '''Tạo ra một vector dựa trên tọa độ của hai điểm'''
    # return (x1-x2, y1-y2)
    return (x2-x1, y2-y1)


# Công thức tính góc giữa hai vecto trong mặt phẳng Oxy:
# Trong mặt phẳng với hệ trục tọa độ Đề-các vuông góc Oxy,
# cho hai véc-tơ n1=(a1;b1), n2=(a2;b2).
# Cô-sin của góc giữa hai vec-tơ này được tính theo công thức:
# cos(n1,n2) = (a1*a2 + b1*b2) / (math.sqrt(a1**2 + b1**2) * math.sqrt(a2**2 + b2**2))
# Từ đây, ta dùng hàm lượng giác ngược arccos (math.acos() trong Python) suy ra
# số đo góc giữa hai vecto n1, n2 .
def goc(x1, y1, x2, y2, x3, y3):
    '''Tính số đo độ của góc tạo bởi hai vector'''
    v1 = tao_vector(x1, y1, x2, y2)
    v2 = tao_vector(x2, y2, x3, y3)

    a1 = v1[0]
    b1 = v1[1]
    a2 = v2[0]
    b2 = v2[1]
    tu_so = a1*a2 + b1*b2
    mau_so = math.sqrt(a1**2 + b1**2) * math.sqrt(a2**2 + b2**2)
    cos = tu_so / mau_so

    print(f'v1: {v1}, v2: {v2}')
    print(f'a1 = {a1}')
    print(f'a2 = {a2}')
    print(f'b1 = {b1}')
    print(f'b2 = {b2}')
    print(f'tu_so = {tu_so}')
    print(f'cos = {cos}')
    return round(math.degrees(math.acos(cos)))


# Tính số đo dộ của một góc dựa trên ba điểm
def getAngle(knee, hip, shoulder):
    ang = math.degrees(math.atan2(
        shoulder[1]-hip[1], shoulder[0]-hip[0]) - math.atan2(knee[1]-hip[1], knee[0]-hip[0]))
    return ang + 360 if ang < 0 else ang
# print(getAngle((5, 0), (0, 0), (0, 5)))


def main():
    # print("PYB101x - Assignment 01")

    # Nhập tọa độ 3 điểm từ bàn phím
    # (xA, yA, xB, yB, xC, yC) = nhap_toa_do_ba_diem()
    (xA, yA, xB, yB, xC, yC) = (1, 1, 2, 2, 3, 1)

    # # Tính độ dài các cạnh của tam giác và in ra
    # distance_ab = khoangcach(xA, yA, xB, yB)
    # distance_ac = khoangcach(xA, yA, xC, yC)
    # distance_bc = khoangcach(xB, yB, xC, yC)
    # print(f'Độ dài cạnh AB  = {distance_ab} cm.')
    # print(f'Độ dài cạnh AC  = {distance_ac} cm.')
    # print(f'Độ dài cạnh BC  = {distance_bc} cm.')

    # # Kiểm tra ba điểm đầu vào có phải tam giác hay không
    # if not kiemtra_tam_giac(xA, yA, xB, yB, xC, yC):
    #     print('A,B, C không phải là một tam giác')
    #     exit()
    # else:
    #     print('A,B, C là một tam giác')

    # print(f'Góc BAC = {goc(xB,yB,xA,yA,xC,yC)} (độ)')
    # print(f'Góc BAC = {goc(xC,yC,xA,yA,xB,yB)} (độ)')

    # print(f'Góc ABC = {goc(xA,yA,xB,yB,xC,yC)} (độ)')
    # print(f'Góc ACB = {goc(xA,yA,xC,yC,xB,yB)} (độ)')

    # BAC là góc giữa 2 vector là BA và AC.
    # ABC là góc giữa 2 vector là AB và BC.
    # ACB là góc giữa 2 vector là AC và CB.
    # --------------------------------------------------------

    pA = (xA, yA)
    pB = (xB, yB)
    pC = (xC, yC)
    print(f'Góc BAC = {getAngle(pB, pA, pC)}')
    print(f'Góc BAC = {getAngle(pC, pA, pB)}')
    # print(f'Góc ABC = {getAngle(pA, pB, pC)}')
    # print(f'Góc ACB = {getAngle(pA, pC, pB)}')
    # print(getAngle((5, 0), (0, 0), (0, 5)))


if __name__ == '__main__':
    main()
