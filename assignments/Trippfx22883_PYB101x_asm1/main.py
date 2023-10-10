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
            lst = [float(i) for i in lst]
            # lst = [int(i) for i in lst]
        except ValueError:
            print(
                'Bạn phải nhập 6 số cho các tọa độ của các điểm. Vui lòng nhập lại.')
            # print(
            #     'Bạn phải nhập 6 số nguyên cho các tọa độ của các điểm. Vui lòng nhập lại.')
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
# Lưu ý: Vector AB có hướng đi từ A đến B.
def tao_vector(x1, y1, x2, y2):
    '''Tạo ra một vector dựa trên tọa độ của hai điểm'''
    return (x2-x1, y2-y1)


# Công thức tính góc giữa hai Vector trong mặt phẳng Oxy:
# Trong mặt phẳng với hệ trục tọa độ Đề-các vuông góc Oxy,
# cho hai Vector n1=(a1;b1), n2=(a2;b2).
# Cô-sin của góc giữa hai Vector này được tính theo công thức:
# cos(n1,n2) = (a1*a2 + b1*b2) / (math.sqrt(a1**2 + b1**2) * math.sqrt(a2**2 + b2**2))
# Từ đây, ta dùng hàm lượng giác ngược arccos (math.acos() trong Python) suy ra
# số đo góc giữa hai Vector n1, n2 .
def goc_tu_hai_vector(v1, v2):
    '''Tính số đo độ của góc tạo bởi hai vector'''
    a1 = v1[0]
    b1 = v1[1]
    a2 = v2[0]
    b2 = v2[1]
    tu_so = a1*a2 + b1*b2
    mau_so = math.sqrt(a1**2 + b1**2) * math.sqrt(a2**2 + b2**2)
    cos = tu_so / mau_so
    return round(math.degrees(math.acos(cos)), 2)


def goc(xA, yA, xB, yB, xC, yC):
    '''Tính số đo độ của góc từ tọa độ của ba điểm trong một tam giác'''
    v_ab = tao_vector(xA, yA, xB, yB)
    v_cb = tao_vector(xC, yC, xB, yB)
    return goc_tu_hai_vector(v_ab, v_cb)


def format_float(num):
    s = str(num)
    pos = s.find('.')
    if pos != -1:
        if s[pos+1] == '0' and len(s) == len(s[:pos+2]):
            return int(s[:pos])
    return num


# Tam giác vuông: Trong tam giác có 1 góc = 90 độ.
# Bạn cũng sẽ cần chỉ ra xem tam giác đó vuông ở đỉnh nào,
# ví dụ: "Tam giác vuông tại đỉnh A".
def tam_giac_vuong(xA, yA, xB, yB, xC, yC):
    # msg = 'Tam giác vuông tại đỉnh'
    goc_a = goc(xB, yB, xA, yA, xC, yC)
    goc_b = goc(xA, yA, xB, yB, xC, yC)
    goc_c = goc(xB, yB, xC, yC, xA, yA)
    if goc_a == 90:
        return (True, 'A')
    if goc_b == 90:
        return (True, 'B')
    if goc_c == 90:
        return (True, 'C')
    return (False,)


# Tam giác tù: Trong tam giác có 1 góc > 90 độ.
# Bạn cũng sẽ chỉ ra xem góc nào là góc tù,
# ví dụ: "Tam giác tù tại góc B".
def tam_giac_tu(xA, yA, xB, yB, xC, yC):
    # msg = 'Tam giác tù tại góc'
    goc_a = goc(xB, yB, xA, yA, xC, yC)
    goc_b = goc(xA, yA, xB, yB, xC, yC)
    goc_c = goc(xB, yB, xC, yC, xA, yA)
    if goc_a > 90:
        return (True, 'A')
    if goc_b > 90:
        return (True, 'B')
    if goc_c > 90:
        return (True, 'C')
    return (False,)


# Tam giác cân: Trong tam giác có 2 cạnh bằng nhau.
# Bạn cũng sẽ cần chỉ ra xem tam giác cân ở đỉnh nào,
# ví dụ: "Tam giác cân tại đỉnh C".
def tam_giac_can(xA, yA, xB, yB, xC, yC):
    # msg = 'Tam giác cân tại đỉnh'
    ab = khoangcach(xA, yA, xB, yB)
    ac = khoangcach(xA, yA, xC, yC)
    bc = khoangcach(xB, yB, xC, yC)
    if ab == ac:
        return (True, 'A')
    if ab == bc:
        return (True, 'B')
    if ac == bc:
        return (True, 'C')
    return (False,)


# Tam giác đều: Tam giác có 3 cạnh bằng nhau hoặc 3 góc bằng 60 độ.
# Bạn sẽ chỉ cần trả về như sau "Tam giác đều".
def tam_giac_deu(xA, yA, xB, yB, xC, yC):
    ab = khoangcach(xA, yA, xB, yB)
    ac = khoangcach(xA, yA, xC, yC)
    bc = khoangcach(xB, yB, xC, yC)
    if ab == ac == bc:
        return (True, 'đều')
    return (False,)


# Xác định tam giác thuộc một trong các loại tam giác sau:
# Tam giác đều, tam giác vuông, tam giác tù, tam giác cân,
# tam giác vuông cân, tam giác tù và cân hoặc tam giác thường
def loai_tamgiac(xA, yA, xB, yB, xC, yC):
    '''Xác định loại tam giác từ tọa độ của ba điểm'''
    msg = 'Loại của tam giác ABC: Tam giác'

    # Tam giác đều
    tgd = tam_giac_deu(xA, yA, xB, yB, xC, yC)
    if tgd[0]:
        print(f'{msg} {tgd[1]}')
        return

    tgc = tam_giac_can(xA, yA, xB, yB, xC, yC)
    tgv = tam_giac_vuong(xA, yA, xB, yB, xC, yC)
    tgt = tam_giac_tu(xA, yA, xB, yB, xC, yC)

    # Tam giác vuông cân
    if tgc[0] and tgv[0]:
        print(f'{msg} vuông cân tại đỉnh {tgc[1]}')
        return

    # Tam giác tù và cân
    if tgc[0] and tgt[0]:
        print(f'{msg} tù và cân tại đỉnh {tgc[1]}')
        return

    # Tam giác vuông
    if tgv[0]:
        print(f'{msg} vuông tại đỉnh {tgv[1]}')
        return

    # Tam giác tù
    if tgt[0]:
        print(f'{msg} tù tại góc {tgt[1]}')
        return

    # Tam giác cân
    if tgc[0]:
        print(f'{msg} cân tại đỉnh {tgc[1]}')
        return

    # Tam giác thường
    print(f'{msg} thường')


# area = a * ha / 2
# Trong đó area là diện tích của tam giác cân tại đỉnh A,
# ha là chiều dài đường cao kẻ từ điểm A xuống cạnh a.
def dientich_tamgiac_can(xA, yA, xB, yB, xC, yC):
    '''Tính diện tích của tam giác cân'''
    d_ab = khoangcach(xA, yA, xB, yB)
    d_ac = khoangcach(xA, yA, xC, yC)
    d_bc = khoangcach(xB, yB, xC, yC)
    h_dict = duongcao_tamgiac(xA, yA, xB, yB, xC, yC)
    tgc = tam_giac_can(xA, yA, xB, yB, xC, yC)
    if tgc[1] == 'A':
        return round(d_bc * h_dict['A'] / 2, 2)
    if tgc[1] == 'B':
        return round(d_ac * h_dict['B'] / 2, 2)
    if tgc[1] == 'C':
        return round(d_ab * h_dict['C'] / 2, 2)


# area = a**2 * math.sqrt(3) / 4
# Trong đó area là diện tích của tam giác đều,
# có độ dài các cạnh là a.
def dientich_tamgiac_deu(xA, yA, xB, yB, xC, yC):
    '''Tính diện tích của tam giác đều'''
    d_ab = khoangcach(xA, yA, xB, yB)
    return round(d_ab**2 * math.sqrt(3) / 4, 2)


# area = a * b / 2
# Trong đó area là diện tích của tam giác vuống tại đỉnh A,
# có hai cạnh góc vuông (hay còn gọi là cạnh bên) là a và b.
def dientich_tamgiac_vuong(xA, yA, xB, yB, xC, yC):
    '''Tính diện tích của tam giác vuông'''
    d_ab = khoangcach(xA, yA, xB, yB)
    d_ac = khoangcach(xA, yA, xC, yC)
    d_bc = khoangcach(xB, yB, xC, yC)
    tgv = tam_giac_vuong(xA, yA, xB, yB, xC, yC)
    if tgv[1] == 'A':
        return round(d_ab * d_ac / 2, 2)
    if tgv[1] == 'B':
        return round(d_ab * d_bc / 2, 2)
    if tgv[1] == 'C':
        return round(d_ac * d_bc / 2, 2)


# Sử dụng công thức Heron:
# area = math.sqrt(p*(p-a)*(p-b)*(p-c))
# Trong đó a, b, c là chiều dài của ba cạnh tam giác
# và p là nửa chu vi của tam giác:
# p = (a + b + c) / 2
def dientich_tamgiac(xA, yA, xB, yB, xC, yC):
    '''Tính diện tích của tam giác'''
    # Độ dài các cạnh của tam giác
    d_ab = khoangcach(xA, yA, xB, yB)
    d_ac = khoangcach(xA, yA, xC, yC)
    d_bc = khoangcach(xB, yB, xC, yC)
    # Nửa chu vi p
    p = (d_ab + d_ac + d_bc) / 2
    # Diện tích tam giác
    return round(math.sqrt(p * (p-d_ab) * (p-d_ac) * (p-d_bc)), 2)


# Ví dụ:
# Độ dài của đường cao kẻ từ điểm A xuống cạnh a:
# ha = 2 * area / a
def duongcao_tamgiac(xA, yA, xB, yB, xC, yC):
    '''Tính độ dài của các đường cao trong một tam giác'''
    # Độ dài các cạnh của tam giác
    d_ab = khoangcach(xA, yA, xB, yB)
    d_ac = khoangcach(xA, yA, xC, yC)
    d_bc = khoangcach(xB, yB, xC, yC)
    # Diện tích tam giác
    area = dientich_tamgiac(xA, yA, xB, yB, xC, yC)
    # Đường cao kẻ từ điểm A xuống cạnh BC
    ha = round(2 * area / d_bc, 2)
    # Đường cao kẻ từ điểm B xuống cạnh AC
    hb = round(2 * area / d_ac, 2)
    # Đường cao kẻ từ điểm C xuống cạnh AB
    hc = round(2 * area / d_ab, 2)

    return {'A': ha, 'B': hb, 'C': hc}


def main():
    # print("PYB101x - Assignment 01")

    # 2. Nhập tọa độ 3 điểm từ bàn phím
    # (xA, yA, xB, yB, xC, yC) = nhap_toa_do_ba_diem()

    # # Loại của tam giác ABC: Tam giác đều
    # (xA, yA, xB, yB, xC, yC) = (0, 0, math.sqrt(3), 3, -math.sqrt(3), 3)

    # # Loại của tam giác ABC: Tam giác vuông cân tại đỉnh B
    # (xA, yA, xB, yB, xC, yC) = (1, 1, 2, 2, 3, 1)

    # # Loại của tam giác ABC: Tam giác tù và cân tại đỉnh B
    # (xA, yA, xB, yB, xC, yC) = (4, 1, 6, 2, 8, 1)

    # # Loại của tam giác ABC: Tam giác vuông tại đỉnh A
    # (xA, yA, xB, yB, xC, yC) = (4, 1, 4, 3, 5, 1)

    # # Loại của tam giác ABC: Tam giác tù tại góc B
    # (xA, yA, xB, yB, xC, yC) = (4, 1, 6, 2, 7, 1)

    # # Loại của tam giác ABC: Tam giác cân tại đỉnh B
    # (xA, yA, xB, yB, xC, yC) = (4, 1, 5, 3, 6, 1)

    # # Loại của tam giác ABC: Tam giác cân thường
    (xA, yA, xB, yB, xC, yC) = (4, 1, 4, 2.5, 5, 2)

    # 3. Tính độ dài các cạnh của tam giác
    d_ab = khoangcach(xA, yA, xB, yB)
    d_ac = khoangcach(xA, yA, xC, yC)
    d_bc = khoangcach(xB, yB, xC, yC)
    print(f'Độ dài cạnh AB  = {d_ab} cm.')
    print(f'Độ dài cạnh AC  = {d_ac} cm.')
    print(f'Độ dài cạnh BC  = {d_bc} cm.')

    # 4. Kiểm tra xem ba điểm có tạo được một tam giác không
    if not kiemtra_tam_giac(xA, yA, xB, yB, xC, yC):
        print('A,B, C không phải là một tam giác')
        exit()
    else:
        print('A,B, C là một tam giác')

    # 5. Tính các góc của tam giác (ở đơn vị độ).
    # BAC là góc giữa 2 vector là BA và CA.
    # ABC là góc giữa 2 vector là AB và CB.
    # ACB là góc giữa 2 vector là AC và BC.
    print(f'Góc BAC = {format_float(goc(xB,yB,xA,yA,xC,yC))} (độ)')
    print(f'Góc ABC = {format_float(goc(xA,yA,xB,yB,xC,yC))} (độ)')
    print(f'Góc BCA = {format_float(goc(xB,yB,xC,yC,xA,yA))} (độ)')

    # 6. Xét loại của tam giác ABC
    loai_tamgiac(xA, yA, xB, yB, xC, yC)

    # 7. Tính diện tích tam giác
    area = dientich_tamgiac(xA, yA, xB, yB, xC, yC)
    print(f'Diện tích của tam giác = {area}')
    # if tam_giac_deu(xA, yA, xB, yB, xC, yC)[0]:
    #     area2 = dientich_tamgiac_deu(xA, yA, xB, yB, xC, yC)
    #     print(f'Diện tích của tam giác (tính theo tam giác đều) = {area2}')
    # if tam_giac_vuong(xA, yA, xB, yB, xC, yC)[0]:
    #     area3 = dientich_tamgiac_vuong(xA, yA, xB, yB, xC, yC)
    #     print(f'Diện tích của tam giác (tính theo tam giác vuông) = {area3}')
    # if tam_giac_can(xA, yA, xB, yB, xC, yC)[0]:
    #     area4 = dientich_tamgiac_can(xA, yA, xB, yB, xC, yC)
    #     print(f'Diện tích của tam giác (tính theo tam giác cân) = {area4}')

    # 8. Tính độ dài đường cao của tam giác
    h_dict = duongcao_tamgiac(xA, yA, xB, yB, xC, yC)
    msg = 'Độ dài đường cao từ điểm'
    msg2 = f'{msg} A = {h_dict["A"]}\n{msg} B = {h_dict["B"]}\n{msg} C = {h_dict["C"]}\n'
    print(msg2)


if __name__ == '__main__':
    main()
